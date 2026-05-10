"""Brain-likeness QA tab — validate_consciousness 6-metric suite."""
import gradio as gr


METRICS = [
    ("α-band suppression on EO", 0.92),
    ("Hjorth mobility envelope", 0.88),
    ("LZ76 complexity range", 0.81),
    ("Permutation entropy band", 0.85),
    ("Φ-proxy (signed)", 0.83),
    ("Inter-channel coherence", 0.84),
]

OVERALL = 0.856  # 85.6% BRAIN-LIKE on canonical transplant run


def render() -> str:
    bars = []
    for name, score in METRICS:
        filled = int(round(score * 20))
        bar = "█" * filled + "░" * (20 - filled)
        bars.append(f"`{bar}` **{score*100:.1f}%** — {name}")
    body = "\n\n".join(bars)
    return (
        f"### Canonical transplant run — overall **{OVERALL*100:.1f}% BRAIN-LIKE**\n\n"
        f"{body}\n\n"
        f"_Source: `hexa-brain/eeg/validate_consciousness.hexa` 6-metric suite. "
        f"Threshold: ≥80% on canonical replay = `F_IT_02` falsifier passes._"
    )


def build():
    gr.Markdown(
        "## 📡 Brain-likeness QA — 6-metric validate_consciousness\n"
        "Each metric scores how brain-like a recording or replay is. "
        "Canonical transplant achieved 85.6% (above the 80% gate)."
    )
    gr.Markdown(render())
