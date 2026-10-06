#!/usr/bin/env python3
"""
validate_papers.py
Mechanical validation script for CUET mock test papers.
Strictly non-content: only parses, counts, verifies distributions, checks duplicates, and reports metrics.
"""

import sys
import os
import json
import glob
import re
import argparse
from collections import Counter, defaultdict

# Difficulty targets from Questionsgenerationinstructions.md
# Format: (easy, medium, hard) for a 50-question paper
LEVEL_TARGETS = {
    '1': (35, 12, 3),   # 70% / 25% / 5%
    '2': (30, 15, 5),   # 60% / 30% / 10%
    '3': (25, 17, 8),   # 50% / 35% / 15%
    '4': (20, 20, 10),  # 40% / 40% / 20%
    '5': (15, 23, 12),  # 30% / 45% / 25%
    '6': (12, 23, 15),  # 25% / 45% / 30%
    '7': (10, 23, 17),  # 20% / 45% / 35%
    '8': (8, 22, 20),   # 15% / 45% / 40%
    '9': (5, 20, 25),   # 10% / 40% / 50%
    '10': (3, 15, 32),  # 5% / 30% / 65%
}

def validate_subject(cuet_dir, subject_name):
    # Resolve directory
    subj_dir = os.path.join(cuet_dir, subject_name)
    if not os.path.exists(subj_dir):
        # try matching case-insensitively
        found = False
        for d in os.listdir(cuet_dir):
            if d.lower() == subject_name.lower():
                subj_dir = os.path.join(cuet_dir, d)
                subject_name = d
                found = True
                break
        if not found:
            print(f"Error: Subject directory '{subj_dir}' not found.")
            sys.exit(1)

    all_json = sorted(glob.glob(os.path.join(subj_dir, "*.json")))
    papers = [f for f in all_json if not os.path.basename(f).startswith("series_index") and not os.path.basename(f).endswith("summary.json") and not os.path.basename(f).startswith("all_") and not os.path.basename(f).startswith("existing_") and not os.path.basename(f).startswith("gk_")]

    print(f"\n========================================================")
    print(f"  VALIDATION REPORT: {subject_name}")
    print(f"  Directory: {subj_dir}")
    print(f"  Total Papers Evaluated: {len(papers)} / 25")
    print(f"========================================================\n")

    total_questions = 0
    total_key_dist = Counter()
    json_errors = []
    q_count_errors = []
    option_count_errors = []
    correct_option_errors = []
    diff_mismatches = []
    within_paper_dups = []
    cross_paper_dups = []
    stem_tracker = {}
    expl_mismatches = []
    self_ref_issues = []
    missing_rc_passages = []

    for p in papers:
        p_name = os.path.basename(p)
        try:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            json_errors.append((p_name, str(e)))
            continue

        if not isinstance(data, dict):
            json_errors.append((p_name, "Root is not a JSON object"))
            continue

        questions = data.get("questions", [])
        q_count = len(questions)
        total_questions += q_count

        if q_count != 50:
            q_count_errors.append((p_name, q_count))

        # Difficulty check
        lvl_str = str(data.get("difficulty_level", ""))
        base_lvl = re.sub(r"[ABC]", "", lvl_str)
        paper_diffs = Counter(q.get("difficulty", "").lower() for q in questions)
        if base_lvl in LEVEL_TARGETS:
            exp_e, exp_m, exp_h = LEVEL_TARGETS[base_lvl]
            act_e = paper_diffs.get("easy", 0)
            act_m = paper_diffs.get("medium", 0)
            act_h = paper_diffs.get("hard", 0)
            if abs(act_e - exp_e) > 5 or abs(act_h - exp_h) > 5:
                diff_mismatches.append((p_name, f"Target ({exp_e}E/{exp_m}M/{exp_h}H) vs Actual ({act_e}E/{act_m}M/{act_h}H)"))

        p_stems = set()
        p_keys = Counter()

        for idx, q in enumerate(questions):
            q_id = str(q.get("id", f"idx_{idx+1}"))
            stem = q.get("question", "").strip()
            norm_stem = re.sub(r"\s+", " ", stem.lower())

            # Duplicates
            if norm_stem in p_stems:
                within_paper_dups.append((p_name, q_id, stem[:60]))
            else:
                p_stems.add(norm_stem)

            if norm_stem in stem_tracker:
                cross_paper_dups.append((p_name, q_id, stem_tracker[norm_stem], stem[:60]))
            else:
                stem_tracker[norm_stem] = (p_name, q_id)

            # Options count
            opts = q.get("options", [])
            if not isinstance(opts, list) or len(opts) != 4:
                option_count_errors.append((p_name, q_id, len(opts) if isinstance(opts, list) else "not_list"))

            # Correct option
            corr = q.get("correct_option", "")
            if corr not in ["A", "B", "C", "D"]:
                correct_option_errors.append((p_name, q_id, corr))
            else:
                p_keys[corr] += 1
                total_key_dist[corr] += 1

            # Explanation mismatch check
            expl = q.get("explanation", "")
            # Look for explicit conclusion in explanation
            m = re.findall(r"(?:option|answer is|correct option is|correct answer is)\s+([A-D])\b", expl, re.IGNORECASE)
            if m:
                last_m = m[-1].upper()
                if corr and last_m != corr:
                    expl_mismatches.append((p_name, q_id, f"correct_option='{corr}' but explanation concludes '{last_m}'"))

            # Self-reference and positional option issues
            for o_idx, opt in enumerate(opts):
                letter = chr(ord('A') + o_idx)
                # E.g. Option A says "Both A and C"
                if re.search(r"\bboth\b.*\b" + letter + r"\b", opt, re.IGNORECASE):
                    self_ref_issues.append((p_name, q_id, f"Option {letter} refers to itself: '{opt}'"))
                # "All of the above" or "None of the above" not at D
                if "all of the above" in opt.lower() and letter != "D":
                    self_ref_issues.append((p_name, q_id, f"'All of the above' at Option {letter}: '{opt}'"))
                if "none of the above" in opt.lower() and letter != "D":
                    self_ref_issues.append((p_name, q_id, f"'None of the above' at Option {letter}: '{opt}'"))

            # Reading Comprehension passage check
            top = q.get("topic", "").lower()
            sub = q.get("sub_topic", "").lower()
            if ("reading comprehension" in top or "passage" in sub) and len(stem) < 250:
                missing_rc_passages.append((p_name, q_id, stem[:60]))

    # Report results
    print("--- 1. STRUCTURAL & FILE INTEGRITY ---")
    print(f"JSON Parse Errors: {len(json_errors)}")
    for err in json_errors:
        print(f"   [!] {err[0]}: {err[1]}")
    print(f"Wrong Question Counts (Expected 50): {len(q_count_errors)}")
    for err in q_count_errors:
        print(f"   [!] {err[0]}: {err[1]} questions")
    print(f"Option Count Errors (Expected 4): {len(option_count_errors)}")
    for err in option_count_errors:
        print(f"   [!] {err[0]} Q {err[1]}: found {err[2]} options")

    print("\n--- 2. ANSWER KEY INTEGRITY & BALANCE ---")
    print(f"Invalid correct_option fields: {len(correct_option_errors)}")
    for err in correct_option_errors:
        print(f"   [!] {err[0]} Q {err[1]}: value='{err[2]}'")
    print(f"Total Key Distribution: A={total_key_dist['A']} ({total_key_dist['A']/max(1, total_questions)*100:.1f}%), B={total_key_dist['B']} ({total_key_dist['B']/max(1, total_questions)*100:.1f}%), C={total_key_dist['C']} ({total_key_dist['C']/max(1, total_questions)*100:.1f}%), D={total_key_dist['D']} ({total_key_dist['D']/max(1, total_questions)*100:.1f}%)")
    print(f"Explanation vs correct_option Mismatches: {len(expl_mismatches)}")
    for err in expl_mismatches[:15]:
        print(f"   [!] {err[0]} Q {err[1]}: {err[2]}")
    if len(expl_mismatches) > 15:
        print(f"   ... and {len(expl_mismatches) - 15} more")

    print("\n--- 3. OPTION LOGIC & POSITIONAL INTEGRITY ---")
    print(f"Self-referential / Misplaced Option Issues: {len(self_ref_issues)}")
    for err in self_ref_issues:
        print(f"   [!] {err[0]} Q {err[1]}: {err[2]}")

    print("\n--- 4. DUPLICATION CHECKS ---")
    print(f"Within-Paper Duplicate Stems: {len(within_paper_dups)}")
    for err in within_paper_dups:
        print(f"   [!] {err[0]} Q {err[1]}: '{err[2]}...'")
    print(f"Cross-Paper Duplicate Stems: {len(cross_paper_dups)}")
    for err in cross_paper_dups[:10]:
        print(f"   [!] {err[0]} Q {err[1]} duplicates {err[2][0]} Q {err[2][1]}: '{err[3]}...'")
    if len(cross_paper_dups) > 10:
        print(f"   ... and {len(cross_paper_dups) - 10} more")

    print("\n--- 5. PASSAGE COMPLETENESS ---")
    print(f"Reading Comprehension Questions Missing Inline Passage: {len(missing_rc_passages)}")
    for err in missing_rc_passages[:10]:
        print(f"   [!] {err[0]} Q {err[1]}: '{err[2]}...'")
    if len(missing_rc_passages) > 10:
        print(f"   ... and {len(missing_rc_passages) - 10} more")

    print("\n--- 6. DIFFICULTY DISTRIBUTION ---")
    print(f"Difficulty Deviation (>5 Qs from target): {len(diff_mismatches)}")
    for err in diff_mismatches:
        print(f"   [!] {err[0]}: {err[1]}")

    print(f"\n========================================================\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate CUET Mock Test Papers")
    parser.add_argument("cuet_dir", help="Path to CUET directory")
    parser.add_argument("--subject", required=True, help="Subject name (e.g. English, Mathematics, Physics)")
    args = parser.parse_args()

    validate_subject(args.cuet_dir, args.subject)

