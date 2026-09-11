#!/usr/bin/env python3
"""Neofetch-style info card SVG for rh0kzy (animated, SMIL/CSS only).

Each line fades/slides in staggered so the panel prints next to the portrait.
STATIC=1 env var emits a frozen frame for local previews.
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "info-card.svg")

W, H = 560, 500
PAD = 22
TITLEBAR_H = 30
BG = "#0d1117"
BG2 = "#111722"
FRAME = "#30363d"
MUTED = "#7d8590"
TEXT = "#e6edf3"
GREEN = "#3fb950"
CYAN = "#22d3ee"
GOLD = "#f2cc60"
PURPLE = "#bc8cff"

STATIC = bool(os.environ.get("STATIC"))

lines = [
    ("Now", "Co-Founder @ Massar Agency", GREEN),
    ("", "AI Engineering @ USTHB (3rd yr)", MUTED),
    ("Focus", "PhoneMAG · EdenStore · HireAI", CYAN),
    ("Stack", "React / Next.js · Django / FastAPI", TEXT),
    ("", "Electron · Supabase · Docker", MUTED),
    ("Ship", "Web + mobile apps for DZ SMBs", GOLD),
    ("Contact", "aymen-belkadi.vercel.app", PURPLE),
]

css = """
@keyframes fade { 0% { opacity: 0; transform: translateX(-8px); } 100% { opacity: 1; transform: translateX(0); } }
.l { opacity: 0; animation: fade 0.45s ease-out both; }
""".strip()

p = []
p.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">')
p.append(f'<style>{css}</style>')
p.append(f'<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient></defs>')
p.append(f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>')
p.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}" stroke-width="1"/>')
p.append(f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>')
for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    p.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')
p.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" text-anchor="middle">rh0kzy@github: ~$ neofetch</text>')

y = TITLEBAR_H + 52
p.append(f'<text x="{PAD}" y="{y}" fill="{TEXT}" font-size="20" font-weight="700">Hi, I\'m Aymen 👋</text>')
y += 30
p.append(f'<text x="{PAD}" y="{y}" fill="{MUTED}" font-size="13">Full-Stack Developer · AI Engineering Student</text>')
y += 28
p.append(f'<line x1="{PAD}" y1="{y}" x2="{W-PAD}" y2="{y}" stroke="{FRAME}" stroke-opacity="0.6"/>')
y += 30

for i, (key, val, color) in enumerate(lines):
    delay = 0.25 + i * 0.22
    style = '' if STATIC else f' style="animation-delay:{delay:.2f}s"'
    cls = '' if STATIC else ' class="l"'
    if key:
        p.append(f'<g{cls}{style}><text x="{PAD}" y="{y}" fill="{color}" font-size="14" font-weight="700">{key}</text><text x="{PAD+78}" y="{y}" fill="{MUTED}" font-size="14">:</text><text x="{PAD+92}" y="{y}" fill="{TEXT}" font-size="14">{val}</text></g>')
    else:
        p.append(f'<g{cls}{style}><text x="{PAD+92}" y="{y}" fill="{color}" font-size="14">{val}</text></g>')
    y += 30

y += 6
p.append(f'<line x1="{PAD}" y1="{y}" x2="{W-PAD}" y2="{y}" stroke="{FRAME}" stroke-opacity="0.6"/>')
y += 28
if STATIC:
    p.append(f'<text x="{PAD}" y="{y}" fill="{MUTED}" font-size="13">rh0kzy@github:~$ cat ./links.sh</text>')
else:
    p.append(f'<g class="l" style="animation-delay:{0.25 + len(lines)*0.22:.2f}s"><text x="{PAD}" y="{y}" fill="{MUTED}" font-size="13">rh0kzy@github:~$ cat ./links.sh</text><rect x="{PAD+232}" y="{y-12}" width="8" height="14" fill="{TEXT}"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" dur="1s" repeatCount="indefinite"/></rect></g>')

p.append('</svg>')
svg = "".join(p)
with open(OUT, "w") as f:
    f.write(svg)
print(f"wrote {OUT} ({len(svg)} bytes)")
