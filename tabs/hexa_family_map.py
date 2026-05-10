"""Hexa Family Map tab — five-rollup atlas."""
import json
from pathlib import Path
import gradio as gr


DATA_FILE = Path(__file__).parent.parent / "data" / "family.json"


def load_family():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []


def render_table(family: list) -> str:
    head = "| Repo | Emoji | Verbs | Domain | Status |\n|---|---|---|---|---|\n"
    rows = []
    for f in family:
        rows.append(
            f"| **{f['name']}** | {f['emoji']} | {f['verbs']} | {f['domain']} | {f['status']} |"
        )
    return head + "\n".join(rows)


def render_detail(name: str, family: list) -> str:
    f = next((x for x in family if x["name"] == name), None)
    if not f:
        return "no entry"
    flag = "✅" if "WORKING" in f["status"] else ("⚠️" if "SPECULATIVE" in f["status"] else "📋")
    return (
        f"### {flag} {f['emoji']} **{f['name']}** — {f['domain']}\n\n"
        f"**Verbs:** {f['verbs']}  \n"
        f"**Status:** {f['status']}  \n"
        f"**Provenance:** {f.get('provenance', 'n/a')}  \n\n"
        f"{f.get('note', '')}"
    )


def build():
    family = load_family()
    gr.Markdown(
        "## 🗺️ Hexa Family Map — five-rollup atlas\n"
        "Sister repos under `/Users/ghost/core/`, sharing the n=6 lattice."
    )
    if not family:
        gr.Markdown("⚠️ `data/family.json` empty.")
        return

    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown(render_table(family))
        with gr.Column(scale=1):
            pick = gr.Dropdown(
                [f["name"] for f in family],
                value=family[0]["name"],
                label="select repo for detail",
            )
            detail = gr.Markdown()
            state = gr.State(family)
            pick.change(render_detail, [pick, state], detail)
            detail.value = render_detail(family[0]["name"], family)
