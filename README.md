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

- Static HF Space (`sdk: static`) — first paint < 1 s, no cold start.
- `requestAnimationFrame` 60 fps loop.
- 16-bin histogram entropy, 256-sample window per frame.
- LCG seeded by frame index → reproducible noise per tick.

## Sister

- 👻 [need-singularity/anima](https://github.com/need-singularity/anima) — consciousness/soul cousin (working research code, source of `byte_emergence_demo.py`).
- 🧬 [need-singularity/hexa-brain](https://github.com/need-singularity/hexa-brain) — BCI hardware sister-repo.
- 👁️ [need-singularity/hexa-senses](https://github.com/need-singularity/hexa-senses) — 5-verb sensory substrate.
- 🧠 [need-singularity/hexa-mind](https://github.com/need-singularity/hexa-mind) — 7-verb mental substrate.

## License

MIT.
