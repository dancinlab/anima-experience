"""Emergence tab — realtime byte-level mutual-information visualizer.

Loads a self-contained HTML/Canvas/JS page that runs at 60fps in the
browser. Port of `byte_emergence_demo.py`:

    emergence = H(L) + H(R) - H(L, R)   # bits

When two byte streams are coupled through a shared sine-wave engine,
mutual information rises above zero — "EMERGENT ✨" lights up.

Server-side cost: 0. The Python tab module just serves the static HTML.
"""
from pathlib import Path
import gradio as gr


HTML_FILE = Path(__file__).parent / "emergence.html"


def build():
    gr.Markdown(
        "## ✨ Emergence — realtime mutual-information visualizer\n"
        "Drag the **Coupling** slider. Two byte streams flow live; mutual "
        "information rises as they bind. Pure browser rendering at 60 fps — "
        "Python port of `byte_emergence_demo.py`."
    )
    if HTML_FILE.exists():
        gr.HTML(HTML_FILE.read_text(encoding="utf-8"))
    else:
        gr.Markdown("⚠️ `tabs/emergence.html` not found.")
