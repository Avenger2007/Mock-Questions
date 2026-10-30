"""Recompute descriptive counts from manually authored PYQ tags; never generates questions."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / 'docs/blueprints'
taxonomy = json.loads((BASE / 'iat_taxonomy.json').read_text())
ledger = json.loads((BASE / 'iat_pyq_ledger.json').read_text())
tags = {}
tiers = {'e': 'easy', 'm': 'medium', 'h': 'hard'}
tasks = {'R': 'recall', 'C': 'conceptual', 'N': 'numerical', 'T': 'table/match',
         'G': 'graph', 'D': 'diagram/structure', 'E': 'experiment'}
for line in (BASE / 'iat_pyq_manual_tags.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    year, subject, *items = line.split()
    for n, item in enumerate(items, 1):
        tags[int(year), subject, n] = item.split(':')
assert len(tags) == len(ledger) == 539
for row in ledger:
    code, tier, task = tags[row['year'], row['subject'], row['question_number']]
    row.update(chapter_code=code, chapter=taxonomy[row['subject']][code][0],
               primary_class=taxonomy[row['subject']][code][1],
               difficulty_estimate=tiers[tier], dominant_task=tasks[task],
               current_scope='historical_or_scope_review' if code.startswith('X') else 'listed_topic_family')
(BASE / 'iat_pyq_ledger.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + '\n')
metrics = {'n_questions': len(ledger), 'years': sorted({r['year'] for r in ledger}),
           'chapter_counts': {}, 'by_subject': {}, 'by_year': {}}
for subject in 'BCMP':
    all_rows = [r for r in ledger if r['subject'] == subject]
    recent = [r for r in all_rows if r['year'] >= 2023]
    current = [r for r in recent if not r['chapter_code'].startswith('X')]
    metrics['chapter_counts'][subject] = [
        {'code': code, 'chapter': label[0],
         'all_n': sum(r['chapter_code'] == code for r in all_rows),
         'recent_n': sum(r['chapter_code'] == code for r in recent),
         'recent_current_scope_percent': None if code.startswith('X') else
            round(100 * sum(r['chapter_code'] == code for r in current) / len(current), 1)}
        for code, label in taxonomy[subject].items()]
    metrics['by_subject'][subject] = {
        'all_n': len(all_rows), 'recent_n': len(recent), 'recent_current_n': len(current),
        'recent_tiers': dict(Counter(r['difficulty_estimate'] for r in recent)),
        'recent_tasks': dict(Counter(r['dominant_task'] for r in recent)),
        'recent_primary_classes': dict(Counter(str(r['primary_class']) for r in recent))}
for year in metrics['years']:
    rows = [r for r in ledger if r['year'] == year]
    metrics['by_year'][year] = {'n': len(rows),
        'tiers': dict(Counter(r['difficulty_estimate'] for r in rows)),
        'scope_review_n': sum(r['chapter_code'].startswith('X') for r in rows)}
(BASE / 'iat_pyq_metrics.json').write_text(json.dumps(metrics, ensure_ascii=False, indent=2) + '\n')
lines = ['# IAT PYQ chapter-count appendix', '',
         'Recomputed from the manual ledger. Recent = 2023–2026; counts are descriptive, not forecasts.', '',
         'One primary chapter per question. Scope-review rows have no current-scope percentage.', '']
for s, name in zip('BCMP', ['Biology', 'Chemistry', 'Mathematics', 'Physics']):
    stats = metrics['by_subject'][s]
    lines += [f'## {name}', '',
              f"All years n = {stats['all_n']}; recent n = {stats['recent_n']}; recent current-scope denominator = {stats['recent_current_n']}.", '',
              '| Primary chapter | All years | Recent | Recent current-scope share |',
              '|---|---:|---:|---:|']
    for row in metrics['chapter_counts'][s]:
        share = 'scope review' if row['recent_current_scope_percent'] is None else f"{row['recent_current_scope_percent']}%"
        lines.append(f"| {row['chapter']} | {row['all_n']} | {row['recent_n']} | {share} |")
    lines.append('')
(BASE / 'iat_pyq_chapter_counts.md').write_text('\n'.join(lines) + '\n')
print(f"Rebuilt {len(ledger)} ledger entries and descriptive metrics.")
