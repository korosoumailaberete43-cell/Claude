# -*- coding: utf-8 -*-
"""Alignement forcé (CTC Viterbi) des paroles sur l'audio.
Modèle: NeMo FastConformer CTC multilingue (fr) exporté ONNX par sherpa-onnx.
Sortie: JSON {lines:[{section,text,start,end,words:[{w,start,end}]}]}
"""
import numpy as np, onnxruntime as ort, json, sys, re, unicodedata, subprocess, os

SR = 16000
FRAME = 0.08  # 10 ms * subsampling 8
HERE = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = sys.argv[1]
AUDIO = sys.argv[2]
LYRICS = sys.argv[3]
OUT = sys.argv[4]

# ---------- features (NeMo AudioToMelSpectrogram, per_feature norm) ----------
import librosa
_MEL = librosa.filters.mel(sr=SR, n_fft=512, n_mels=80, fmin=0, fmax=SR/2, htk=False, norm='slaney')

def load_audio(path):
    raw = subprocess.run(["ffmpeg","-v","error","-i",path,"-ac","1","-ar",str(SR),"-f","f32le","-"],
                         capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).astype(np.float64)

def nemo_feats(x):
    y = np.concatenate([[x[0]], x[1:] - 0.97*x[:-1]])
    S = librosa.stft(y, n_fft=512, hop_length=160, win_length=400, window='hann',
                     center=True, pad_mode='reflect')
    mel = _MEL @ (np.abs(S)**2)
    lm = np.log(mel + 2**-24)
    return ((lm - lm.mean(1, keepdims=True)) / (lm.std(1, ddof=1, keepdims=True) + 1e-5)).astype(np.float32)

# ---------- vocabulaire sentencepiece ----------
def load_tokens(p):
    d = {}
    for line in open(p, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line: continue
        piece, idx = line.rsplit(" ", 1)
        d[piece] = int(idx)
    return d

def norm_for_align(s):
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("E-N-E-T-P", "ENETP").replace("R-D-M", "RDM")
    s = re.sub(r"[«»\"…!?:;,\.\(\)]", " ", s)
    s = s.replace("-", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s

def encode_word(word, vocab, first_in_line=False):
    """Greedy longest-match sentencepiece encoding of one word."""
    s = "▁" + word
    ids, i = [], 0
    while i < len(s):
        for j in range(len(s), i, -1):
            piece = s[i:j]
            if piece in vocab:
                ids.append(vocab[piece]); i = j; break
        else:
            # caractère inconnu: on le saute
            i += 1
    return ids

# ---------- CTC forced alignment ----------
def ctc_align(logp, tokens, blank):
    """logp: (T,V) log-softmax. tokens: list of ids. Retourne frame de début par token."""
    T = logp.shape[0]
    ext = [blank]
    for t in tokens:
        ext.append(t); ext.append(blank)
    S = len(ext)
    NEG = -1e30
    dp = np.full((S,), NEG, dtype=np.float64)
    bp = np.zeros((T, S), dtype=np.int8)   # 0: stay, 1: from s-1, 2: from s-2
    dp[0] = logp[0, ext[0]]
    if S > 1: dp[1] = logp[0, ext[1]]
    for t in range(1, T):
        prev = dp
        cand0 = prev
        cand1 = np.concatenate(([NEG], prev[:-1]))
        cand2 = np.concatenate(([NEG, NEG], prev[:-2]))
        # saut de 2 interdit si token identique séparé par blank, ou si ext[s] est blank
        mask2 = np.ones(S, dtype=bool)
        mask2[0] = mask2[1] = False
        for s in range(2, S):
            if ext[s] == blank or ext[s] == ext[s-2]:
                mask2[s] = False
        cand2 = np.where(mask2, cand2, NEG)
        stack = np.vstack([cand0, cand1, cand2])
        arg = stack.argmax(0)
        best = stack.max(0)
        dp = best + logp[t, ext]
        bp[t] = arg
    # backtrack depuis le meilleur état final
    s = S-1 if dp[S-1] >= dp[S-2] else S-2
    path = np.zeros(T, dtype=np.int32)
    for t in range(T-1, -1, -1):
        path[t] = s
        s -= int(bp[t, s])
    starts = {}
    for t in range(T):
        s = path[t]
        if s % 2 == 1:                 # état "token" (indices impairs)
            k = (s-1)//2
            if k not in starts: starts[k] = t
    ends = {}
    for t in range(T-1, -1, -1):
        s = path[t]
        if s % 2 == 1:
            k = (s-1)//2
            if k not in ends: ends[k] = t
    return starts, ends

def main():
    vocab = load_tokens(os.path.join(MODEL_DIR, "tokens.txt"))
    blank = vocab["<blk>"]
    x = load_audio(AUDIO)
    dur = len(x)/SR
    F = nemo_feats(x)
    so = ort.SessionOptions(); so.intra_op_num_threads = 4
    sess = ort.InferenceSession(os.path.join(MODEL_DIR, "model.onnx"), so,
                                providers=["CPUExecutionProvider"])
    logp = sess.run(None, {"audio_signal": F[None], "length": np.array([F.shape[1]], dtype=np.int64)})[0][0]
    print("logprobs", logp.shape, "~frame", FRAME, "s  (couverture %.1fs)" % (logp.shape[0]*FRAME))

    # --- lecture des paroles ---
    sections, lines = [], []
    cur = ""
    for raw in open(LYRICS, encoding="utf-8"):
        raw = raw.rstrip("\n")
        if not raw.strip(): continue
        if raw.startswith("#"):
            cur = raw[1:].strip(); continue
        lines.append({"section": cur, "text": raw.strip()})

    tokens, meta = [], []   # meta: (line_idx, word_idx)
    for li, ln in enumerate(lines):
        words = norm_for_align(ln["text"]).split(" ")
        ln["align_words"] = words
        for wi, w in enumerate(words):
            ids = encode_word(w, vocab)
            if not ids: ids = [vocab.get("▁", 1)]
            for tid in ids:
                tokens.append(tid); meta.append((li, wi))
    print("tokens à aligner:", len(tokens), "frames:", logp.shape[0])

    starts, ends = ctc_align(logp.astype(np.float64), tokens, blank)
    # timings par mot
    words_t = {}
    for k, (li, wi) in enumerate(meta):
        if k not in starts: continue
        s, e = starts[k]*FRAME, (ends[k]+1)*FRAME
        key = (li, wi)
        if key in words_t:
            words_t[key] = (min(words_t[key][0], s), max(words_t[key][1], e))
        else:
            words_t[key] = (s, e)

    out = {"duration": dur, "lines": []}
    for li, ln in enumerate(lines):
        ws = []
        for wi, w in enumerate(ln["align_words"]):
            if (li, wi) in words_t:
                s, e = words_t[(li, wi)]
                ws.append({"w": w, "start": round(s, 3), "end": round(e, 3)})
        if not ws: continue
        out["lines"].append({
            "section": ln["section"], "text": ln["text"],
            "start": ws[0]["start"], "end": ws[-1]["end"], "words": ws})
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for l in out["lines"]:
        print(f'{l["start"]:7.2f} -> {l["end"]:7.2f}  [{l["section"]}] {l["text"][:60]}')

main()
