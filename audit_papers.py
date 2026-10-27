#!/usr/bin/env python3
"""
CUET audit metrics — mechanical checks only (no content generation).

Measures, per subject: difficulty mix vs the 8/32/10 target, question-format
mix (match-list, assertion-reason, statements, sequence, case, numerical),
topic distribution, metadata gaps, very short stems/explanations and
templated stem skeletons. Writes a JSON summary used by docs/audit/.

Usage: python3 audit_papers.py CUET [--json out.json]
"""
import json, os, re, sys, glob
from collections import Counter, defaultdict

TARGET = {"easy": 8, "medium": 32, "hard": 10}
FORMATS = ["match-list", "assertion-reason", "multi-statement", "sequence",
           "case/passage", "numerical", "direct"]


def question_format(text):
    t = text.lower()
    if re.search(r"match (the )?list|list[- ]?i\b.*list[- ]?ii|सूची", t, re.S):
        return "match-list"
    if re.search(r"assertion|\breason\s*\(r\)|statement[- ]?i\b.*statement[- ]?ii|अभिकथन", t, re.S):
        return "assertion-reason"
    if re.search(r"(correct|right|logical|proper) (sequence|order)|arrange|chronolog|क्रम", t):
        return "sequence"
    if len(text) > 350 and re.search(r"passage|case|read the following|study the following|"
                                     r"on the basis of|based on the (above|given)|गद्यांश|अनुच्छेद", t):
        return "case/passage"
    if (re.search(r"\(a\).*\(b\).*\(c\)|\n\s*(1|i)[.)].*\n\s*(2|ii)[.)]", t, re.S)
            and re.search(r"choose|statements?|correct answer from|how many of the|कथन", t)):
        return "multi-statement"
    if len(re.findall(r"\d[\d,.]{2,}", text)) >= 2 or re.search(
            r"calculate|compute|find the value|evaluate|ज्ञात कीजिए", t):
        return "numerical"
    return "direct"


def skeleton(text):
    """Stem shape with numbers, quoted words and capitalised names blanked."""
    s = re.sub(r"\d[\d,.]*", "#", text)
    s = re.sub(r"[\"'“‘][^\"'”’]{1,40}[\"'”’]", "Q", s)
    s = re.sub(r"\b[A-Z][a-z]+\b", "N", s)
    return re.sub(r"\s+", " ", s).strip().lower()[-120:]  # tail = the actual ask, not a shared passage


def explanation_checks(q, r):
    """Explanation depth/structure and option giveaways."""
    e = q.get("explanation", "").strip()
    ex = r.setdefault("explanation", Counter())
    ex["lengths"] = ex.get("lengths", 0) + len(e)
    if len(e) < 150:
        ex["under_150_chars"] += 1
    if "\n" in e:
        ex["structured_multiline"] += 1
    if re.search(r"(?i)\boption\b|incorrect|wrong|whereas|distractor|other choices", e):
        ex["addresses_wrong_options"] += 1
    if re.search(r"(?i)step\s*\d|\n\s*\d[.)]", e):
        ex["numbered_steps"] += 1
    if question_format(q["question"]) == "numerical":
        ex["numerical_questions"] += 1
        if len(e) < 150:
            ex["numerical_under_150_chars"] += 1
    lens = [len(o) for o in q["options"]]
    i = "ABCD".index(q["correct_option"])
    if lens[i] == max(lens) and lens.count(max(lens)) == 1 and max(lens) > 1.3 * sorted(lens)[-2]:
        r["correct_is_clearly_longest"] = r.get("correct_is_clearly_longest", 0) + 1
    body = [re.sub(r"^[A-D]\)\s*", "", o).strip().lower() for o in q["options"]]
    if len(set(body)) < 4:
        r["duplicate_options"] = r.get("duplicate_options", 0) + 1
    if any(re.search(r"all of the above|none of the above|both (a|\(a\)) and", o) for o in body):
        r["combo_options"] = r.get("combo_options", 0) + 1


def audit_subject(sub_dir):
    files = sorted(glob.glob(os.path.join(sub_dir, "CUET_*Paper*.json")))
    r = {"papers": len(files), "questions": 0, "difficulty": Counter(),
         "formats": Counter(), "topics": Counter(), "papers_off_target": 0,
         "rewrites_needed": 0, "empty_sub_topic": 0, "short_stem": 0,
         "short_explanation": 0, "templated_groups": 0, "templated_questions": 0,
         "format_by_difficulty": defaultdict(Counter), "provenance": Counter()}
    skel = defaultdict(list)
    for f in files:
        data = json.load(open(f, encoding="utf-8"))
        r["provenance"][f"{data.get('syllabus_source')} | PYQ: {data.get('past_paper_reference')}"] += 1
        diff = Counter()
        for q in data["questions"]:
            r["questions"] += 1
            d = q.get("difficulty", "").lower()
            diff[d] += 1
            fmt = question_format(q["question"])
            r["formats"][fmt] += 1
            r["format_by_difficulty"][d][fmt] += 1
            r["topics"][q.get("topic") or "(blank)"] += 1
            if not q.get("sub_topic"):
                r["empty_sub_topic"] += 1
            if len(q["question"].strip()) < 40:
                r["short_stem"] += 1
            if len(q.get("explanation", "").strip()) < 40:
                r["short_explanation"] += 1
            skel[skeleton(q["question"])].append(q["id"])
            explanation_checks(q, r)
        r["difficulty"].update(diff)
        keys = "".join(q["correct_option"] for q in data["questions"])
        r["max_key_streak"] = max(r.get("max_key_streak", 0),
                                  max(len(m.group(0)) for m in re.finditer(r"(.)\1*", keys)))
        if any(abs(diff[k] - v) > 1 for k, v in TARGET.items()):
            r["papers_off_target"] += 1
        r["rewrites_needed"] += sum(max(0, diff[k] - v) for k, v in TARGET.items())
    groups = [ids for k, ids in skel.items() if len(ids) >= 3 and len(k) > 30]
    r["templated_groups"] = len(groups)
    r["templated_questions"] = sum(len(g) for g in groups)
    r["format_by_difficulty"] = {k: dict(v) for k, v in r["format_by_difficulty"].items()}
    ex = r.get("explanation", Counter())
    ex["avg_chars"] = round(ex.pop("lengths", 0) / max(1, r["questions"]))
    r["explanation"] = dict(ex)
    for k in ("difficulty", "formats", "topics", "provenance"):
        r[k] = dict(r[k])
    return r


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "CUET"
    out = sys.argv[sys.argv.index("--json") + 1] if "--json" in sys.argv else None
    results = {os.path.basename(d): audit_subject(d)
               for d in sorted(glob.glob(os.path.join(root, "*"))) if os.path.isdir(d)}
    print(f"{'Subject':19s} {'E/M/H':>15s} {'rewr':>5s} {'MTF':>4s} {'A-R':>4s} {'Stmt':>4s} "
          f"{'Seq':>4s} {'Case':>4s} {'Num':>4s} {'Dir':>4s} {'tmpl':>5s} {'noSub':>5s} {'short':>5s}")
    for s, r in results.items():
        f, d = r["formats"], r["difficulty"]
        pct = lambda k: round(100 * f.get(k, 0) / r["questions"])
        print(f"{s[:19]:19s} {d.get('easy',0):>5}/{d.get('medium',0)}/{d.get('hard',0):<4} "
              f"{r['rewrites_needed']:>5} {pct('match-list'):>3}% {pct('assertion-reason'):>3}% "
              f"{pct('multi-statement'):>3}% {pct('sequence'):>3}% {pct('case/passage'):>3}% "
              f"{pct('numerical'):>3}% {pct('direct'):>3}% {r['templated_questions']:>5} "
              f"{r['empty_sub_topic']:>5} {r['short_stem']:>5}")
    if out:
        json.dump(results, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
