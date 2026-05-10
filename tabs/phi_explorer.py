"""Φ★ Explorer tab — substrate-level integrated information across backbones."""
import json
from pathlib import Path
import gradio as gr


DATA_DIR = Path(__file__).parent.parent / "data" / "phi_star"

SUBSTRATES = {
    "CLM v4 (530M, anima-native)": "clm_v4_530m.json",
    "Qwen3 (baseline)": "qwen3.json",
    "Mistral (baseline)": "mistral.json",
    "Llama (4B/hid8)": "llama.json",
}


def load_substrate(label: str):
    f = DATA_DIR / SUBSTRATES[label]
    if not f.exists():
        return {"error": f"missing {f.name}"}, "n/a"
    data = json.loads(f.read_text())
    summary = (
        f"**Backbone:** {data.get('backbone', '?')}\n\n"
        f"**Substrate:** {data.get('substrate', '?')}\n\n"
        f"**Gates:** "
        f"positive {'✅' if data.get('gate_positive_PASS') else '❌'} | "
        f"substantial {'✅' if data.get('gate_substantial_PASS') else '❌'} | "
        f"magnitude {'✅' if data.get('gate_magnitude_PASS') else '❌'}\n\n"
        f"**Φ★ min / mean / max:** "
        f"{data.get('phi_star_min', 'n/a')} / "
        f"{data.get('phi_mean', 'n/a')} / "
        f"{data.get('phi_max', 'n/a')}\n\n"
        f"**Sign:** {data.get('phi_star_sign', 'n/a')}"
    )
    return data, summary


def build():
    gr.Markdown(
        "## 📊 Φ★ Explorer — substrate-level integrated information\n"
        "Pick a backbone. Each JSON is a real measurement run from "
        "`anima/state/` — gates, partition decomposition, signed magnitude."
    )
    with gr.Row():
        with gr.Column(scale=1):
            substrate = gr.Dropdown(
                list(SUBSTRATES.keys()),
                value=list(SUBSTRATES.keys())[0],
                label="substrate",
            )
        with gr.Column(scale=2):
            summary = gr.Markdown()
    raw = gr.JSON(label="full Φ★ measurement record")

    substrate.change(load_substrate, substrate, [raw, summary])
    init = list(SUBSTRATES.keys())[0]
    raw_val, sum_val = load_substrate(init)
    raw.value = raw_val
    summary.value = sum_val
