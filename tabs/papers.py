"""Papers tab — three core anima papers as sub-tabs."""
from pathlib import Path
import gradio as gr


PAPERS_DIR = Path(__file__).parent.parent / "data" / "papers"

PAPERS = [
    ("Consciousness Laws", "consciousness_laws.md"),
    ("Hexa-Voice", "hexa_voice.md"),
    ("Self-Discovery", "self_discovery.md"),
]


def load_paper(filename: str) -> str:
    f = PAPERS_DIR / filename
    if not f.exists():
        return f"⚠️ `{filename}` not found in `data/papers/`."
    return f.read_text(encoding="utf-8")


def build():
    gr.Markdown(
        "## 📖 Papers — three core anima papers\n"
        "Source files live under `data/papers/`. Originally extracted "
        "from `anima/docs/anima/paper_*.hexa`."
    )
    with gr.Tabs():
        for label, filename in PAPERS:
            with gr.Tab(label):
                gr.Markdown(load_paper(filename))
