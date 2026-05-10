"""Paradigm Timeline tab — milestone scrubber across the anima research arc."""
import json
from pathlib import Path
import gradio as gr


DATA_FILE = Path(__file__).parent.parent / "data" / "paradigm.json"


def load_milestones():
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text())


def render_milestone(idx: int, milestones: list):
    if not milestones or idx >= len(milestones):
        return "no milestone"
    m = milestones[idx]
    flag = {"PASS": "✅", "FAIL": "❌", "PARTIAL": "🟡", "SPECULATIVE": "⚠️"}.get(
        m.get("status", ""), "•"
    )
    return (
        f"### {flag} **{m['id']}** — {m['headline']}\n\n"
        f"**Date:** {m['date']}  \n"
        f"**Status:** {m.get('status', 'n/a')}  \n"
        f"**Lane:** {m.get('lane', 'n/a')}\n\n"
        f"{m.get('note', '')}"
    )


def build():
    milestones = load_milestones()
    gr.Markdown(
        "## 📜 Paradigm Timeline — milestones across the arc\n"
        f"Scrub through {len(milestones)} curated checkpoints from "
        "`paradigm-a → paradigm-j+ PIV`. Source: `REBORN.md` headlines."
    )
    if not milestones:
        gr.Markdown("⚠️ `data/paradigm.json` empty — populate during scaffold.")
        return
    with gr.Row():
        idx = gr.Slider(0, len(milestones) - 1, value=0, step=1, label="milestone index")
    out = gr.Markdown()
    state = gr.State(milestones)
    idx.change(render_milestone, [idx, state], out)
    out.value = render_milestone(0, milestones)
