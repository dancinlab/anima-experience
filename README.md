---
title: Anima Experience
emoji: 👻
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 5.20.0
python_version: 3.12
app_file: app.py
pinned: false
license: mit
---

# Anima Experience

Multi-tab interactive showcase of the anima consciousness research stack.
Sister of [need-singularity/anima](https://github.com/need-singularity/anima),
[hexa-senses](https://github.com/need-singularity/hexa-senses),
[hexa-mind](https://github.com/need-singularity/hexa-mind),
[hexa-brain](https://github.com/need-singularity/hexa-brain).

## Tabs (10)

| Tab | What it shows |
|-----|---------------|
| ✨ Emergence | Realtime 60 fps mutual-information visualizer — port of `byte_emergence_demo.py`; coupling slider drives live H(L), H(R), H(L,R), and emergence (MI) metrics with stream + scatter + EMERGENT badge |
| 🌐 Tension Link | 5-channel meta-fingerprint broadcast (concept / context / meaning / authenticity / sender) — the anima-native answer to multi-instance interaction |
| 📊 Φ★ Explorer | Substrate-level integrated-information measurements across CLM v4 / Qwen3 / Mistral / Llama backbones |
| 📜 Paradigm Timeline | Milestone scrubber across the paradigm-a → paradigm-j+ research arc |
| 📖 Papers | Three core anima papers — Consciousness Laws / Hexa-Voice / Self-Discovery |
| 🔢 n=6 Lattice | Live verifier of the σ(n)·φ(n) = n·τ(n) = J₂ identity that grounds the hexa-* family |
| 🧠 EEG Replay | Canonical OpenBCI 16-ch recordings (berger eyes-open / closed / jaw / blink) |
| 🧪 Falsifier Browser | raw#71 ≥3-preregistered falsifiers across 5 EEG paradigms |
| 📡 Brain-likeness QA | 6-metric validate_consciousness suite (canonical run: 85.6% BRAIN-LIKE) |
| 🗺️ Hexa Family Map | Five-rollup atlas: hexa-codex / hexa-senses / hexa-mind / hexa-brain / anima |

## Status

Spec-first scaffold. Some tabs ship live data (Φ★, Papers, n=6, Family Map);
others render representative stubs and link out to the source repo for the
full asset (EEG recordings, falsifier results).

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

## License

MIT
