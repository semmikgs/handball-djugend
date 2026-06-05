#!/usr/bin/env python3
"""
SVG-Build-Skript Charge 9 — Pass, Duell, Technik Wurf
17 Module: TE-A-PASS-021..027, TE-A-STOSS-009..012, TE-A-TAUSCH-001..002, TE-A-WURF-009..012
"""

import re
import xml.etree.ElementTree as ET
from pathlib import Path

CHARGE_NR = 9
OUTPUT_PATH = Path(f"/home/claude/charge{CHARGE_NR}_visuals.svg")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


def hf_bg():
    return '''<rect x="0" y="0" width="400" height="400" fill="#f4f1ea"/>
<rect x="10" y="10" width="380" height="380" fill="none" stroke="#c9bfa8" stroke-width="2.5"/>
<rect x="160" y="6" width="80" height="8" fill="#3a3a3a"/>
<path d="M 110 14 Q 200 140 290 14" fill="none" stroke="#7a6e54" stroke-width="2"/>
<path d="M 80 14 Q 200 180 320 14" fill="none" stroke="#7a6e54" stroke-width="1.5" stroke-dasharray="6 4"/>'''


def free_bg():
    return '''<rect x="0" y="0" width="400" height="400" fill="#f4f1ea"/>
<rect x="10" y="10" width="380" height="380" fill="none" stroke="#c9bfa8" stroke-width="2.5"/>'''


def att(x, y, label, r=12, fs=10):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ff8a00" '
            f'stroke="#7a3d00" stroke-width="2"/>'
            f'<text x="{x}" y="{y+4}" text-anchor="middle" '
            f'font-size="{fs}" fill="#fff" font-weight="bold">{label}</text>')


def def_(x, y, label, r=12, fs=10):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#3ec1ff" '
            f'stroke="#0a4d63" stroke-width="2"/>'
            f'<text x="{x}" y="{y+4}" text-anchor="middle" '
            f'font-size="{fs}" fill="#fff" font-weight="bold">{label}</text>')


def tw(x, y, label="TW", r=14):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#5dd39e" '
            f'stroke="#1a5a3a" stroke-width="2"/>'
            f'<text x="{x}" y="{y+4}" text-anchor="middle" '
            f'font-size="10" fill="#fff" font-weight="bold">{label}</text>')


def ball(x, y, r=6):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffd166" '
            f'stroke="#7a5d00" stroke-width="1.5"/>')


def cone(x, y, w=8):
    return f'<rect x="{x-w/2}" y="{y-w/2}" width="{w}" height="{w}" fill="#c9bfa8"/>'


def lt(text, color="#3a3a3a"):
    return (f'<text x="200" y="40" text-anchor="middle" font-size="11" '
            f'fill="{color}" font-weight="bold">{text}</text>')


symbols = {}

# TE-A-PASS-021: Peitschenwurf Grundform — Paare stehen sich gegenüber
symbols["TE-A-PASS-021"] = hf_bg() + \
    att(130, 300, "A1") + ball(120, 290) + \
    att(270, 160, "A2") + \
    '<path d="M 140 290 Q 200 220 260 168" fill="none" stroke="#2ea043" ' \
    'stroke-width="2" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Hohe Armposition — beide Seiten</text>' + \
    lt("Peitschenwurf Grundform")

# TE-A-PASS-022: Peitschenwurf mit Anlauf — Laufpfeil vor dem Pass
symbols["TE-A-PASS-022"] = hf_bg() + \
    att(130, 340, "A1") + ball(118, 328) + \
    att(270, 160, "A2") + \
    '<path d="M 130 325 L 130 270" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 140 268 Q 200 210 262 168" fill="none" stroke="#2ea043" ' \
    'stroke-width="2" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Anlauf → Peitschenwurf</text>' + \
    lt("Peitschenwurf mit Anlauf")

# TE-A-PASS-023: Peitschenwurf aus der Luft — Spieler in Sprunghöhe angedeutet
symbols["TE-A-PASS-023"] = hf_bg() + \
    att(150, 260, "A1") + ball(138, 248) + \
    att(280, 160, "A2") + \
    '<path d="M 150 245 L 150 200" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<circle cx="150" cy="190" r="12" fill="#ff8a00" stroke="#7a3d00" stroke-width="2" opacity="0.4"/>' + \
    '<text x="150" y="194" text-anchor="middle" font-size="10" fill="#fff" font-weight="bold">A1</text>' + \
    '<path d="M 162 188 Q 215 168 272 162" fill="none" stroke="#2ea043" ' \
    'stroke-width="2" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>' + \
    '<text x="90" y="185" font-size="8" fill="#c8102e">Sprung</text>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Pass im Scheitelpunkt des Sprungs</text>' + \
    lt("Peitschenwurf aus der Luft")

# TE-A-PASS-024: Pass im Kreuzungsspiel — zwei Spieler kreuzen
symbols["TE-A-PASS-024"] = hf_bg() + \
    att(130, 280, "A1") + ball(118, 268) + \
    att(270, 280, "A2") + \
    '<path d="M 145 272 L 255 272" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 255 275 L 145 275" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 140 268 Q 200 260 258 270" fill="none" stroke="#2ea043" ' \
    'stroke-width="2" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>' + \
    '<text x="200" y="240" text-anchor="middle" font-size="9" fill="#c8102e">Nahhand übergeben</text>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Ball mit Körper schützen</text>' + \
    lt("Pass im Kreuzungsspiel")

# TE-A-PASS-025: Pass über Zone — Verteidiger in der Mitte
symbols["TE-A-PASS-025"] = hf_bg() + \
    att(130, 300, "A1") + ball(118, 288) + \
    def_(200, 220, "V") + \
    att(300, 200, "A2") + \
    '<path d="M 142 286 Q 200 180 292 202" fill="none" stroke="#2ea043" ' \
    'stroke-width="2" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>' + \
    '<text x="185" y="175" font-size="8" fill="#3a3a3a">über</text>' + \
    '<line x1="180" y1="215" x2="220" y2="215" stroke="#3ec1ff" stroke-width="2"/>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Hohe Armpos. → Pass über Zone</text>' + \
    lt("Pass ueber die Zone")

# TE-A-PASS-026: Pass in Gegenrichtung — Lauf links, Pass rechts
symbols["TE-A-PASS-026"] = hf_bg() + \
    att(200, 280, "A1") + ball(188, 268) + \
    att(310, 200, "A2") + \
    att(90, 200, "A3") + \
    '<path d="M 188 275 L 120 275" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 210 270 Q 260 240 302 204" fill="none" stroke="#2ea043" ' \
    'stroke-width="2" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>' + \
    '<text x="145" y="260" font-size="8" fill="#ff8a00">Lauf</text>' + \
    '<text x="255" y="248" font-size="8" fill="#2ea043">Pass</text>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Bewegung andeuten — Pass in Gegenseite</text>' + \
    lt("Pass in Gegenrichtung")

# TE-A-PASS-027: Timing — Läufer startet, Passgeber wählt Moment
symbols["TE-A-PASS-027"] = hf_bg() + \
    att(130, 320, "A1") + ball(118, 308) + \
    att(260, 320, "A2") + \
    att(260, 200, "A2", r=10) + \
    '<path d="M 260 308 L 260 215" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 143 312 Q 200 270 252 205" fill="none" stroke="#2ea043" ' \
    'stroke-width="2" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>' + \
    '<text x="155" y="260" font-size="8" fill="#2ea043">Richtiger Moment</text>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Läufer in Bewegung versorgen</text>' + \
    lt("Timing: Pass zum richtigen Moment")

# TE-A-STOSS-009: Positionskorrektur ohne Ball — kleiner Laufpfeil
symbols["TE-A-STOSS-009"] = hf_bg() + \
    def_(200, 260, "V") + \
    att(180, 300, "A") + \
    '<path d="M 178 287 L 148 247" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    att(148, 235, "A", r=10) + \
    '<text x="110" y="232" font-size="8" fill="#2ea043">bessere Pos.</text>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Kleiner Schritt → Vorteil vor Ballempfang</text>' + \
    lt("Positionskorrektur ohne Ball")

# TE-A-STOSS-010: Finte Grundform — Spieler vor Hütchen, zwei Richtungspfeile
symbols["TE-A-STOSS-010"] = hf_bg() + \
    cone(200, 220, w=14) + \
    att(200, 310, "A") + ball(188, 298) + \
    '<path d="M 192 298 L 145 230" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 200 295 L 200 235" fill="none" stroke="#c8102e" ' \
    'stroke-width="2" stroke-dasharray="4 3" opacity="0.5"/>' + \
    '<text x="145" y="220" font-size="8" fill="#ff8a00">echte Richtg.</text>' + \
    '<text x="205" y="255" font-size="8" fill="#c8102e" opacity="0.7">Täuschg.</text>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Finte: Täuschen — dann explosiv vorbei</text>' + \
    lt("Finte Grundform beidseits")

# TE-A-STOSS-011: Finte mit Körperkontakt — 1:1 mit aktiver Abwehr
symbols["TE-A-STOSS-011"] = hf_bg() + \
    def_(200, 220, "V") + \
    att(200, 310, "A") + ball(188, 298) + \
    '<path d="M 200 296 L 200 237" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 200 234 L 150 180" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<text x="175" y="215" font-size="8" fill="#c8102e">Kontakt</text>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Kontakt annehmen — Arm frei halten</text>' + \
    lt("Finte mit Koerperkontakt")

# TE-A-STOSS-012: Rhythmuswechsel — langsam dann explosiv
symbols["TE-A-STOSS-012"] = hf_bg() + \
    def_(200, 200, "V") + \
    att(200, 340, "A") + ball(188, 328) + \
    '<path d="M 200 325 L 200 260" fill="none" stroke="#ff8a00" ' \
    'stroke-width="1.5" stroke-dasharray="4 6" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 200 257 L 155 195" fill="none" stroke="#ff8a00" ' \
    'stroke-width="3" stroke-dasharray="6 3" marker-end="url(#arrowOrange)"/>' + \
    '<text x="145" y="265" font-size="8" fill="#3a3a3a">langsam</text>' + \
    '<text x="148" y="222" font-size="8" fill="#c8102e">explosiv!</text>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Verzögern — dann Tempowechsel</text>' + \
    lt("Rhythmuswechsel im Paedrag")

# TE-A-TAUSCH-001: Kreuzungsspiel Nahhand — zwei Spieler mit Kreuzpfaden
symbols["TE-A-TAUSCH-001"] = hf_bg() + \
    att(130, 300, "A1") + ball(118, 288) + \
    att(270, 300, "A2") + \
    '<path d="M 144 293 L 256 207" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 256 293 L 144 207" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 130 286 Q 200 248 268 207" fill="none" stroke="#2ea043" ' \
    'stroke-width="2" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>' + \
    '<text x="200" y="245" text-anchor="middle" font-size="8" fill="#c8102e">Nahhand</text>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Ball durch Körper schützen</text>' + \
    lt("Kreuzungsspiel: Nahhand")

# TE-A-TAUSCH-002: Kreuzung mit aktivem Abwehrspieler
symbols["TE-A-TAUSCH-002"] = hf_bg() + \
    att(130, 300, "A1") + ball(118, 288) + \
    att(270, 300, "A2") + \
    def_(200, 255, "V") + \
    '<path d="M 144 293 L 256 207" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 256 293 L 144 207" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 130 286 Q 200 248 268 207" fill="none" stroke="#2ea043" ' \
    'stroke-width="2" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Kreuzung gegen aktive Abwehr</text>' + \
    lt("Kreuzung mit Abwehrspieler")

# TE-A-WURF-009: Abschluss nach Pädrag Rückraum
symbols["TE-A-WURF-009"] = hf_bg() + \
    tw(200, 25) + \
    def_(200, 180, "V") + \
    att(200, 310, "A") + ball(188, 298) + \
    '<path d="M 200 296 L 160 185" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 155 178 L 195 42" fill="none" stroke="#c8102e" ' \
    'stroke-width="3" marker-end="url(#arrowRed)"/>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Pädrag — Finte — Abschluss</text>' + \
    lt("Abschluss nach Paedrag (Rueckraum)")

# TE-A-WURF-010: Abschluss Außen — Spieler von Außenposition
symbols["TE-A-WURF-010"] = hf_bg() + \
    tw(200, 25) + \
    att(60, 200, "A") + ball(48, 188) + \
    '<path d="M 68 190 Q 110 140 155 80" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 162 75 L 200 32" fill="none" stroke="#c8102e" ' \
    'stroke-width="3" marker-end="url(#arrowRed)"/>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Anlauf — Absprung — spitzer Winkel</text>' + \
    lt("Abschluss Aussen: Anlauf + Absprung")

# TE-A-WURF-011: 2:1 mit Entscheidung
symbols["TE-A-WURF-011"] = hf_bg() + \
    tw(200, 25) + \
    att(160, 250, "A1") + ball(148, 238) + \
    att(280, 200, "A2") + \
    '<path d="M 160 236 L 180 100" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 163 238 Q 220 215 272 202" fill="none" stroke="#2ea043" ' \
    'stroke-width="2" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">TW binden — dann Pass oder Abschluss</text>' + \
    lt("Abschluss 2:1 mit Entscheidung")

# TE-A-WURF-012: Abschluss nach Kreuzung mit Abwehr
symbols["TE-A-WURF-012"] = hf_bg() + \
    tw(200, 25) + \
    def_(200, 200, "V") + \
    att(130, 300, "A1") + ball(118, 288) + \
    att(270, 300, "A2") + \
    '<path d="M 144 293 L 256 207" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 256 293 L 144 207" fill="none" stroke="#ff8a00" ' \
    'stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>' + \
    '<path d="M 148 200 L 195 42" fill="none" stroke="#c8102e" ' \
    'stroke-width="3" marker-end="url(#arrowRed)"/>' + \
    '<text x="200" y="380" text-anchor="middle" font-size="9" fill="#3a3a3a">Kreuzung schafft Wurfraum</text>' + \
    lt("Abschluss nach Kreuzung + Abwehr")


# ============================================================================
# SVG ZUSAMMENBAUEN
# ============================================================================
HEADER = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <defs>
    <marker id="arrowOrange" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#ff8a00"/>
    </marker>
    <marker id="arrowBlue" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#3ec1ff"/>
    </marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2ea043"/>
    </marker>
    <marker id="arrowRed" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#c8102e"/>
    </marker>
  </defs>
'''
FOOTER = '</svg>\n'

body = ""
for mid, content in symbols.items():
    is_full = 'height="600"' in content
    viewbox = "0 0 400 600" if is_full else "0 0 400 400"
    body += f'  <symbol id="VIS-{mid}" viewBox="{viewbox}">\n    {content}\n  </symbol>\n\n'

raw = HEADER + body + FOOTER
raw = re.sub(r'&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', raw)
OUTPUT_PATH.write_text(raw, encoding="utf-8")
print(f"OK: {len(symbols)} SVG-Symbole nach {OUTPUT_PATH}")

try:
    tree = ET.parse(OUTPUT_PATH)
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    found = tree.getroot().findall('.//svg:symbol', ns)
    print(f"VALIDE XML: {len(found)} Symbole")
    for s in found:
        print(f"  {s.get('id')}")
except ET.ParseError as e:
    print(f"FEHLER: {e}")
    raise
