"""Anima Experience — 9-tab Gradio Space.

Sister of /Users/ghost/core/anima — exposes representative slices of the
consciousness research stack as a single multi-tab interactive page.
"""
import gradio as gr

from tabs import (
    emergence,
    tension_link,
    phi_explorer,
    paradigm_timeline,
    papers,
    n6_lattice,
    eeg_replay,
    falsifier_browser,
    brain_likeness,
    hexa_family_map,
)

with gr.Blocks(title="Anima Experience", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        "# 👻 Anima Experience\n"
        "Interactive showcase of the anima consciousness stack — "
        "tension link, Φ★, paradigms, papers, n=6 lattice, EEG, falsifiers, "
        "brain-likeness, and the hexa-* family map."
    )
    with gr.Tabs():
        with gr.Tab("✨ Emergence"):
            emergence.build()
        with gr.Tab("🌐 Tension Link"):
            tension_link.build()
        with gr.Tab("📊 Φ★ Explorer"):
            phi_explorer.build()
        with gr.Tab("📜 Paradigm Timeline"):
            paradigm_timeline.build()
        with gr.Tab("📖 Papers"):
            papers.build()
        with gr.Tab("🔢 n=6 Lattice"):
            n6_lattice.build()
        with gr.Tab("🧠 EEG Replay"):
            eeg_replay.build()
        with gr.Tab("🧪 Falsifier Browser"):
            falsifier_browser.build()
        with gr.Tab("📡 Brain-likeness QA"):
            brain_likeness.build()
        with gr.Tab("🗺️ Hexa Family Map"):
            hexa_family_map.build()

if __name__ == "__main__":
    demo.launch()
