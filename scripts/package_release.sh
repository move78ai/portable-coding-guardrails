#!/usr/bin/env bash
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${ROOT}/../portable-coding-guardrails-launch-kit.zip"
cd "$ROOT"
rm -f "$OUT"
zip -qr "$OUT" .
echo "$OUT"
