#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_URL="${1:-http://localhost:5500/Carroseis/Carrossel%20IBS%20e%20CBS.dc.html}"
OUT_DIR="${2:-$SCRIPT_DIR/exports}"

if ! command -v google-chrome-stable >/dev/null 2>&1; then
  echo "Erro: google-chrome-stable nao encontrado no sistema." >&2
  exit 1
fi

if ! curl -fsS "${BASE_URL}?exportSlide=1" >/dev/null; then
  echo "Erro: nao consegui acessar ${BASE_URL}." >&2
  echo "Inicie o servidor local antes: python3 -m http.server 5500" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"

for i in 1 2 3; do
  google-chrome-stable \
    --headless \
    --disable-gpu \
    --hide-scrollbars \
    --force-device-scale-factor=2.5 \
    --window-size=432,540 \
    --virtual-time-budget=8000 \
    --screenshot="$OUT_DIR/slide-0${i}.png" \
    "${BASE_URL}?exportSlide=${i}" >/dev/null 2>&1

  echo "Gerado: $OUT_DIR/slide-0${i}.png"
done

echo "Concluido: 3 PNGs em $OUT_DIR"
