"""EEG Replay tab — canonical OpenBCI recordings from hexa-brain (stub).

Real recordings live in /Users/ghost/core/hexa-brain/eeg/recordings/sessions/.
This tab lists the four canonical sessions; live waveform render lands in v1.1.
"""
import gradio as gr


SESSIONS = [
    {
        "name": "berger_eo_60s",
        "label": "Berger eyes-open (60 s)",
        "date": "2026-05-03",
        "channels": 16,
        "fs_hz": 250,
        "note": "Baseline α-suppression reference. Eyes open, relaxed gaze.",
    },
    {
        "name": "berger_ec_60s_v6",
        "label": "Berger eyes-closed v6 (60 s)",
        "date": "2026-05-03",
        "channels": 16,
        "fs_hz": 250,
        "note": "α-band rebound on eye closure. v6 of the canonical series.",
    },
    {
        "name": "jaw_session_90s",
        "label": "Jaw artifact (90 s)",
        "date": "2026-05-03",
        "channels": 16,
        "fs_hz": 250,
        "note": "EMG contamination probe — repeated jaw clenches.",
    },
    {
        "name": "blink_session_90s",
        "label": "Blink artifact (90 s)",
        "date": "2026-05-03",
        "channels": 16,
        "fs_hz": 250,
        "note": "EOG contamination probe — paced blinks.",
    },
]


def render_session(label: str) -> str:
    s = next((x for x in SESSIONS if x["label"] == label), None)
    if not s:
        return "no session"
    return (
        f"### {s['label']}\n\n"
        f"**Name:** `{s['name']}`  \n"
        f"**Date:** {s['date']}  \n"
        f"**Channels:** {s['channels']}  \n"
        f"**Sampling rate:** {s['fs_hz']} Hz  \n\n"
        f"{s['note']}\n\n"
        f"_Source: `hexa-brain/eeg/recordings/sessions/{s['name']}` — "
        f"live 16-ch waveform render lands in v1.1 once data is bundled._"
    )


def build():
    gr.Markdown(
        "## 🧠 EEG Replay — canonical OpenBCI recordings\n"
        "Four reference sessions from hexa-brain's production cycle "
        "(2026-05-03). Live waveform replay deferred to v1.1."
    )
    pick = gr.Dropdown(
        [s["label"] for s in SESSIONS],
        value=SESSIONS[0]["label"],
        label="session",
    )
    out = gr.Markdown()
    pick.change(render_session, pick, out)
    out.value = render_session(SESSIONS[0]["label"])
