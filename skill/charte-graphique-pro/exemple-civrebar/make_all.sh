#!/usr/bin/env bash
# Régénère toute l'identité CivRebar AI : supports, charte, modèles, pack et zip.
# Prérequis : python3 (fonttools, brotli, cairosvg, pymupdf, pypdf, pillow, python-pptx)
#             node + playwright (global), pptxgenjs et docx (NODE_MODULES_EXTRA ou global).
set -euo pipefail
cd "$(dirname "$0")"
export NODE_PATH="${NODE_MODULES_EXTRA:-}:$(npm root -g)"

python3 pptx_assets.py           # fonds et logos PNG pour PowerPoint / Word
python3 supports.py              # 05_Supports_numeriques (lus par la charte)
python3 build.py                 # pages de la charte -> out/pages/*.pdf
mkdir -p ../out/deck ../out/word
node deck.js ../out/deck/CivRebar_AI_Modele_presentation.pptx
node word.js ../out/word
python3 export.py                # pack 01 à 06 + charte fusionnée
cd .. && rm -f CivRebar_AI_Pack_Logo.zip \
  && python3 -c "import shutil; shutil.make_archive('CivRebar_AI_Pack_Logo', 'zip', '.', 'CivRebar_AI_Pack_Logo')"
echo "terminé"
