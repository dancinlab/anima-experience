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

- Static HF Space (`sdk: static`) — first paint < 1 s, no cold start, no Python runtime.
- Vanilla JS — `setInterval` 30 fps tick over a 250-sample rolling buffer.
- Engine: shared `sin(t)` + individual gaussian-ish noise per stream.
  `L = (1−c)·noiseL + c·sin(t)`, `R = (1−c)·noiseR + c·sin(t)`. High coupling
  collapses both streams onto the diagonal — the scatter aligns cleanly.
- 12-bin histogram entropy over `[−1.5, +1.5]`. EMERGENT badge shows only
  when MI > 0.30 (`opacity:0` + `visibility:hidden` otherwise — fully gone).

## Sister

- 👻 [need-singularity/anima](https://github.com/need-singularity/anima) — consciousness/soul cousin (working research code, source of `byte_emergence_demo.py`).
- 🧬 [need-singularity/hexa-brain](https://github.com/need-singularity/hexa-brain) — BCI hardware sister-repo.
- 👁️ [need-singularity/hexa-senses](https://github.com/need-singularity/hexa-senses) — 5-verb sensory substrate.
- 🧠 [need-singularity/hexa-mind](https://github.com/need-singularity/hexa-mind) — 7-verb mental substrate.

## License

MIT.
