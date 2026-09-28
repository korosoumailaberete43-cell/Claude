#!/usr/bin/env bash
# Régénère toute l'identité Step by Step Academy : supports, charte, modèles, pack, zip.
set -euo pipefail
cd "$(dirname "$0")"
export NODE_PATH="${NODE_MODULES_EXTRA:-}:$(npm root -g)"
python3 logo.py
python3 pptx_assets.py
python3 supports.py
python3 build.py
mkdir -p ../out/office
node deck.js ../out/office/StepByStep_Modele_support_de_cours.pptx
node word.js ../out/office
python3 export.py
cd .. && rm -f StepByStep_Academy_Pack.zip \
  && python3 -c "import shutil; shutil.make_archive('StepByStep_Academy_Pack', 'zip', 'pack')"
echo "terminé"
