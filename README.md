---
title: Anima Experience
emoji: ✨
colorFrom: blue
colorTo: green
sdk: static
pinned: false
license: mit
---

# Anima Experience — realtime mutual-information visualizer

60 fps client-side port of `byte_emergence_demo.py`. Two byte streams flow
through a coupled sine-wave engine; mutual information rises as the streams
bind. Pure HTML / Canvas / JS — server roundtrip 0, no Python runtime.

## Math

```
emergence = H(L) + H(R) − H(L, R)   (bits)
```

- **Independent random** → emergence ≈ 0 (no binding)
- **Engine-coupled** → emergence > 0 (integrated information)

## Tech

- Static HF Space (`sdk: static`) — no cold start.
- **Pyodide** — runs `byte_emergence_demo.py` 100% verbatim in the browser via WebAssembly. numpy included.
- First paint after Pyodide load (~5 s download, then cached): metrics tick at ~20-30 fps.
- 16-bin histogram entropy, 256-sample window per tick.
- Reproducible noise: `np.random.default_rng(t)` seeded by frame index — same as the Python original.

## Sister

- 👻 [need-singularity/anima](https://github.com/need-singularity/anima) — consciousness/soul cousin (working research code, source of `byte_emergence_demo.py`).
- 🧬 [need-singularity/hexa-brain](https://github.com/need-singularity/hexa-brain) — BCI hardware sister-repo.
- 👁️ [need-singularity/hexa-senses](https://github.com/need-singularity/hexa-senses) — 5-verb sensory substrate.
- 🧠 [need-singularity/hexa-mind](https://github.com/need-singularity/hexa-mind) — 7-verb mental substrate.

## License

MIT.
