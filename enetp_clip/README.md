# ENETP Kabala — Clip paroles « Pitié, Monsieur le Directeur »

Clip vidéo de type *lyric video* fabriqué à partir de l'audio fourni :
pochette animée avec le logo de l'école au démarrage, puis les paroles qui
s'écrivent **mot à mot, en synchronisation réelle avec la voix**.

## Ce qui est livré (`out/`)

| Fichier | Description |
|---|---|
| `ENETP_Kabala_clip_paroles.mp4` | Le clip final (1920×1080, 30 i/s, H.264 + AAC) |
| `cover_ENETP_1920x1080.png` | La pochette seule, format 16/9 |
| `cover_ENETP_1080x1080.png` | La pochette seule, format carré (réseaux sociaux) |
| `enetp_karaoke.ass` | Sous-titres karaoké mot à mot (format ASS) |
| `enetp_paroles_video.srt` | Sous-titres classiques, calés sur la **vidéo** |
| `enetp_paroles_audio.srt` | Sous-titres classiques, calés sur le **mp3 d'origine** |
| `enetp_paroles.lrc` | Paroles synchronisées pour lecteurs audio |
| `paroles_minutees.txt` | Retranscription minutée, lisible |
| `align.json` | Minutage brut, **mot par mot** (début/fin en secondes) |

## Comment la synchronisation est obtenue

Ce n'est pas une répartition « à la louche » : c'est un **alignement forcé**
(forced alignment) des paroles sur l'audio.

1. `src/align.py` calcule les descripteurs acoustiques (log-mel 80 bandes,
   normalisation *per-feature*) exactement comme le préprocesseur NeMo.
2. Un modèle acoustique **CTC FastConformer multilingue NVIDIA NeMo**
   (français inclus, exporté en ONNX par le projet sherpa-onnx) produit les
   log-probabilités image par image (1 image = 80 ms).
3. Les paroles sont découpées en jetons SentencePiece, puis un **Viterbi CTC**
   cherche le chemin le plus probable qui lit exactement ces paroles →
   on obtient le début et la fin de **chaque mot**.
4. `src/build_subs.py` transforme ce minutage en karaoké ASS (`\kf`, remplissage
   progressif), en SRT, en LRC et en texte minuté.

Vérification : une reconnaissance libre (sans les paroles) sur des fenêtres de
contrôle (8‑20 s, 26‑34 s, 86‑92 s, 145‑152 s) retrouve bien les mêmes phrases
aux mêmes instants que l'alignement.

## Structure du clip

| Temps vidéo | Contenu |
|---|---|
| 0 → 3,5 s | Pochette : apparition du logo, nom de l'école, devise, titre |
| 3,5 s | Démarrage de l'audio (intro musicale) ; la pochette reste affichée |
| ≈ 12,4 s | Fondu : le logo passe en filigrane en haut à gauche |
| 12,4 s → fin | Paroles karaoké + ligne suivante en aperçu + nom de la section |

Décalage : **tout ce qui se passe dans la vidéo = temps du mp3 + 3,5 s**.

## Refabriquer / modifier

```bash
# 1. alignement (nécessite le modèle ONNX, voir plus bas)
python3 src/align.py <dossier_modele> <audio.mp3> src/lyrics.txt out/align.json

# 2. sous-titres (le 3.5 = durée de la pochette avant le son)
python3 src/build_subs.py 3.5

# 3. clip + pochette
./src/render.sh <audio.mp3> out/_master.mp4
./src/compress.sh out/_master.mp4 out/ENETP_Kabala_clip_paroles.mp4
./src/make_cover.sh
```

- **Changer le titre, la devise, le sous-titre** : en haut de `src/build_subs.py`
  (`TITRE`, `SOUS_TITRE`, `ECOLE`, `DEVISE`).
- **Corriger une parole** : modifier `src/lyrics.txt` (les lignes `#...` sont les
  noms de sections affichés en haut à droite) puis relancer les 3 étapes.
- **Couleurs / tailles du texte** : section `[V4+ Styles]` générée dans
  `src/build_subs.py` (`Karaoke` = ligne en cours, `Next` = aperçu).

Modèle acoustique utilisé (téléchargement ~435 Mo) :
`sherpa-onnx-nemo-fast-conformer-ctc-be-de-en-es-fr-hr-it-pl-ru-uk-20k`
(dépôt GitHub `k2-fsa/sherpa-onnx`, tag `asr-models`).

Dépendances Python : `numpy`, `scipy`, `librosa`, `onnxruntime`. Plus `ffmpeg`
(avec libass) pour le rendu.
