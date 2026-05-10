"""Tension Link tab — 5-channel meta-fingerprint generator (mock Phase 1).

Mirrors the structure documented in docs/modules/tension_link.md:
  concept (16f) | context (8f) | meaning (16f) | authenticity (scalar) | sender (4f)

This is a Phase-1 demo: the fingerprint is generated deterministically from
the user's sliders, not from a PureField encoder. Multi-user broadcast via a
TensionHub-style WebSocket queue is left for Phase 2.
"""
import math
import time
import gradio as gr


MOOD_THRESHOLDS = [
    (lambda t, c: c > 0.5, "surprised"),
    (lambda t, c: t > 1.0, "excited"),
    (lambda t, c: t > 0.3, "thoughtful"),
    (lambda t, c: t > 0.05, "calm"),
    (lambda t, c: True, "quiet"),
]


def classify_mood(tension: float, curiosity: float) -> str:
    for predicate, label in MOOD_THRESHOLDS:
        if predicate(tension, curiosity):
            return label
    return "quiet"


def generate_fingerprint(tension: float, curiosity: float, sender: str, topic_seed: int):
    rng_phase = topic_seed * 0.137 + tension
    concept = [math.sin(rng_phase + i * 0.4) * (0.5 + tension) for i in range(16)]
    norm = math.sqrt(sum(c * c for c in concept)) or 1.0
    concept = [c / norm for c in concept]

    now = time.time()
    context = [
        math.sin(2 * math.pi * (now % 86400) / 86400),
        curiosity / max(tension, 0.01),
        tension,
        curiosity,
        0.0, 0.0, 0.0, 0.0,
    ]

    meaning = [concept[i] * (0.3 + curiosity) for i in range(16)]
    auth = max(0.0, min(1.0, 1.0 - abs(0.5 - curiosity) * 0.4))
    sender_sig = [(hash(sender) % 1000) / 1000, tension % 1, (tension * curiosity) % 1, curiosity % 1]

    topic_hash = max(range(16), key=lambda i: concept[i])
    mood = classify_mood(tension, curiosity)

    return {
        "sender_id": sender,
        "timestamp": now,
        "tension": tension,
        "curiosity": curiosity,
        "mood": mood,
        "topic_hash": topic_hash,
        "authenticity": round(auth, 3),
        "concept": [round(c, 3) for c in concept],
        "context": [round(c, 3) for c in context],
        "meaning": [round(m, 3) for m in meaning],
        "sender_signature": [round(s, 3) for s in sender_sig],
    }


def build():
    gr.Markdown(
        "## 🌐 Tension Link — 5-channel meta-fingerprint\n"
        "Drag the sliders. The 5 channels (concept / context / meaning / "
        "authenticity / sender) are generated as in `docs/modules/tension_link.md`.\n"
        "*Phase 1 mock — fingerprint is deterministic from inputs, not a PureField encode.*"
    )
    with gr.Row():
        with gr.Column(scale=1):
            tension = gr.Slider(0.0, 2.0, value=0.4, step=0.01, label="tension")
            curiosity = gr.Slider(0.0, 1.0, value=0.3, step=0.01, label="curiosity")
            sender = gr.Textbox(value="anima_a", label="sender_id")
            topic = gr.Slider(0, 100, value=7, step=1, label="topic_seed (= argmax target)")
            btn = gr.Button("📡 Broadcast fingerprint", variant="primary")
        with gr.Column(scale=2):
            packet = gr.JSON(label="TensionPacket (5 channels)")
            mood_view = gr.Textbox(label="mood class (5-class rule from spec)", interactive=False)

    def emit(t, c, s, k):
        fp = generate_fingerprint(t, c, s, int(k))
        return fp, fp["mood"]

    btn.click(emit, [tension, curiosity, sender, topic], [packet, mood_view])
