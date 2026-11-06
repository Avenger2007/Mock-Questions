"""Flag possible repeats across authored IAT papers for editorial review.

Usage: python tools/iat/check_series_overlap.py [--threshold 0.78]
This screens text, including number-swapped stems; it cannot certify semantic originality.
"""

import argparse
import difflib
import itertools
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def normalise(value, mask_numbers=False):
    value = value.lower().replace('−', '-').replace('×', 'x')
    if mask_numbers:
        value = re.sub(r'(?<!\w)\d+(?:\.\d+)?(?!\w)', '#', value)
    return re.sub(r'[^\w#]+', ' ', value).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--threshold', type=float, default=0.78)
    args = parser.parse_args()
    if not 0 < args.threshold <= 1:
        parser.error('threshold must be in (0, 1]')

    paths = sorted((ROOT / 'IISER').glob('IAT*TEST*.json'))
    papers = []
    for path in paths:
        data = json.loads(path.read_text(encoding='utf-8'))
        if isinstance(data.get('questions'), list):
            papers.append((path, data['questions']))
    cache = {(p.name, q['id']): (normalise(q['question']), normalise(q['question'], True)) for p, qs in papers for q in qs}
    issues = []
    for (left_path, left), (right_path, right) in itertools.combinations(papers, 2):
        for a, b in itertools.product(left, right):
            if a.get('subject') != b.get('subject'):
                continue
            first, masked_a = cache[(left_path.name, a['id'])]
            second, masked_b = cache[(right_path.name, b['id'])]
            plain = difflib.SequenceMatcher(None, first, second)
            masked = difflib.SequenceMatcher(None, masked_a, masked_b)
            # quick_ratio is an upper bound: pruning cannot remove a candidate.
            if plain.quick_ratio() < args.threshold and masked.quick_ratio() < args.threshold:
                continue
            score = plain.ratio()
            masked_score = masked.ratio()
            if first == second or masked_a == masked_b or max(score, masked_score) >= args.threshold:
                issues.append({
                    'left': f"{left_path.name}:{a['id']}",
                    'right': f"{right_path.name}:{b['id']}",
                    'similarity': round(score, 3),
                    'number_masked_similarity': round(masked_score, 3),
                    'exact': first == second,
                    'number_swapped': masked_a == masked_b,
                })
    print(json.dumps({'papers': [p.name for p, _ in papers], 'threshold': args.threshold,
                      'candidates': sorted(issues, key=lambda x: -max(x['similarity'], x['number_masked_similarity'])),
                      'note': 'Review flagged pairs and all shared reasoning angles manually; text similarity misses semantic repeats.'}, indent=2))
    if any(item['exact'] or item['number_swapped'] for item in issues):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
