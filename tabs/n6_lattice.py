"""n=6 Lattice tab — interactive verifier of σ(n)·φ(n) = n·τ(n) = J₂."""
from math import gcd
import gradio as gr


def divisors(n: int) -> list:
    return [d for d in range(1, n + 1) if n % d == 0]


def sigma(n: int) -> int:
    return sum(divisors(n))


def tau(n: int) -> int:
    return len(divisors(n))


def euler_phi(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def render(n: int) -> str:
    s, t, p = sigma(n), tau(n), euler_phi(n)
    sp, nt = s * p, n * t
    is_perfect = (sp == nt) and (s == 2 * n)
    j2 = sp if sp == nt else None

    rows = [f"| {nn} | {sigma(nn)} | {tau(nn)} | {euler_phi(nn)} | "
            f"{sigma(nn)*euler_phi(nn)} | {nn*tau(nn)} | "
            f"{'✅' if (sigma(nn)*euler_phi(nn) == nn*tau(nn)) and (sigma(nn) == 2*nn) else ('🟡' if sigma(nn)*euler_phi(nn) == nn*tau(nn) else '❌')} |"
            for nn in range(2, 13)]
    table = (
        "| n | σ(n) | τ(n) | φ(n) | σ·φ | n·τ | identity |\n"
        "|---|------|------|------|-----|-----|----------|\n"
        + "\n".join(rows)
    )
    head = (
        f"### n = {n}\n"
        f"- σ({n}) = {s}, τ({n}) = {t}, φ({n}) = {p}\n"
        f"- σ·φ = **{sp}**, n·τ = **{nt}**\n"
        f"- identity holds: **{'YES' if sp == nt else 'no'}**\n"
        f"- n is perfect: **{'YES (σ = 2n)' if s == 2 * n else 'no'}**\n"
        f"- J₂ value (if identity holds): **{j2 if j2 is not None else '—'}**\n\n"
    )
    if is_perfect:
        head += f"🎯 **n = {n} satisfies σ·φ = n·τ = J₂ = {j2} — the master identity used across the hexa-* family.**\n\n"
    return head + table


def build():
    gr.Markdown(
        "## 🔢 n=6 Lattice — master identity verifier\n"
        "The hexa-* family pins every parameter on `σ(n)·φ(n) = n·τ(n) = J₂`. "
        "Try other n: only **n=6** satisfies it as a perfect number."
    )
    n = gr.Slider(2, 12, value=6, step=1, label="n")
    out = gr.Markdown()
    n.change(render, n, out)
    out.value = render(6)
