"""Falsifier Browser tab — raw#71 ≥3-preregistered falsifiers per paradigm (stub)."""
import gradio as gr


PARADIGMS = [
    {
        "id": "resting_baseline",
        "label": "Resting baseline",
        "falsifiers": [
            ("F_RB_01", "α-band power must rise on eye closure"),
            ("F_RB_02", "Inter-electrode coherence stable across eyes-open trials"),
            ("F_RB_03", "Hjorth mobility within reference distribution"),
        ],
    },
    {
        "id": "daily_life",
        "label": "Daily-life cognition",
        "falsifiers": [
            ("F_DL_01", "β/α ratio elevated under task load vs rest"),
            ("F_DL_02", "PE complexity rises during structured task"),
            ("F_DL_03", "Cross-trial reproducibility above chance"),
        ],
    },
    {
        "id": "p300_visual",
        "label": "P300 visual oddball",
        "falsifiers": [
            ("F_PV_01", "P300 latency 250–400 ms post-target"),
            ("F_PV_02", "Centroparietal scalp distribution"),
            ("F_PV_03", "Effect absent under random-onset control"),
        ],
    },
    {
        "id": "p300_auditory",
        "label": "P300 auditory oddball",
        "falsifiers": [
            ("F_PA_01", "Auditory P300 distinguishable from visual"),
            ("F_PA_02", "Effect scales with deviance probability"),
            ("F_PA_03", "Null under matched-pitch control"),
        ],
    },
    {
        "id": "integration_test",
        "label": "Integration test",
        "falsifiers": [
            ("F_IT_01", "Cross-paradigm pipeline produces byte-identical output"),
            ("F_IT_02", "Brain-likeness ≥ 80% on canonical replay"),
            ("F_IT_03", "Resolver routes verbs without darwin-host bypass leak"),
        ],
    },
]


def render(label: str) -> str:
    p = next((x for x in PARADIGMS if x["label"] == label), None)
    if not p:
        return "no paradigm"
    rows = "\n".join(f"- **{fid}** — {desc}" for fid, desc in p["falsifiers"])
    return (
        f"### {p['label']}  \n_paradigm id: `{p['id']}`_\n\n"
        f"**Preregistered falsifiers (raw#71, frozen 2026-04-28):**\n\n{rows}\n\n"
        f"_Source: `hexa-brain/tool/module/_paradigms/`._"
    )


def build():
    gr.Markdown(
        "## 🧪 Falsifier Browser — raw#71 preregistered falsifiers\n"
        "hexa-brain ships ≥3 falsifiers per paradigm, frozen 2026-04-28. "
        "Pick a paradigm to see the slot list."
    )
    pick = gr.Dropdown(
        [p["label"] for p in PARADIGMS],
        value=PARADIGMS[0]["label"],
        label="paradigm",
    )
    out = gr.Markdown()
    pick.change(render, pick, out)
    out.value = render(PARADIGMS[0]["label"])
