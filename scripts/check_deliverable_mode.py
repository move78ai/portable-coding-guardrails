#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTS = {'.md', '.txt', '.yml', '.yaml'}
IGNORE_DIRS = {'dist', '.git', '__pycache__'}
IGNORE_FILES = {'docs/launch/GITHUB_REPO_SETTINGS.md', 'docs/review/DELIVERABLE_MODE_PHRASE_AUDIT.md'}
PATTERNS = [
    r'\bhere is\b',
    r'\bbelow is\b',
    r'\bI wrote\b',
    r'\byou can use this\b',
    r'\bI can\b',
    r'\bI will\b',
    r'\bAs an AI\b',
    r'\bassistant\b',
    r'\bgeneration process\b',
    r'\bmeta-commentary\b'
]

compiled = [re.compile(p, re.IGNORECASE) for p in PATTERNS]
issues = []

for path in ROOT.rglob('*'):
    if not path.is_file():
        continue
    if any(part in IGNORE_DIRS for part in path.parts):
        continue
    if path.suffix.lower() not in TEXT_EXTS:
        continue
    rel = str(path.relative_to(ROOT))
    if rel in IGNORE_FILES:
        continue
    try:
        text = path.read_text(encoding='utf-8')
    except Exception:
        continue
    for idx, line in enumerate(text.splitlines(), start=1):
        for rgx in compiled:
            if rgx.search(line):
                issues.append((rel, idx, line.strip()))
                break

report = []
report.append('# Deliverable-mode phrase audit')
report.append('')
report.append('Scanned text files for common chat-style or client-facing filler phrases.')
report.append('')
if not issues:
    report.append('No matches found.')
else:
    report.append('## Matches')
    report.append('')
    for file_path, line_no, line in issues:
        report.append('- ' + file_path + ':' + str(line_no) + ' — ' + line)

out = ROOT / 'docs' / 'review' / 'DELIVERABLE_MODE_PHRASE_AUDIT.md'
out.write_text('\n'.join(report) + '\n', encoding='utf-8')
print('Wrote ' + str(out))
print('Matches: ' + str(len(issues)))
