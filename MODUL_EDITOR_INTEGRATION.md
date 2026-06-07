# Modul-Editor → Modulbrowser: Integrations-Anweisungen

Dieses Dokument beschreibt den vollständigen Ablauf, wenn Ole eine JSON-Datei aus dem **Modul-Editor** (`ModulEditor.html`) hochlädt und sie in den `UI_Modul_Browser_STANDALONE.html` integriert werden soll.

---

## 0. Kontext: Was ist eine Modul-Editor-Datei?

Der Modul-Editor erzeugt eine JSON-Datei mit genau einem Modul (manchmal mehrere) im Format:

```json
{
  "modules": [
    {
      "id": "AW-BALL-ENTWURF-6496",
      "title": "...",
      "area": "...",
      "subcategory": "...",
      ...
      "visualization": {
        "svg_inner": "...",
        "konstellation_raw": { ... }
      },
      "_cognitive_labels": [...],
      "_integration": {
        "preset": "optimal",
        "toggles": { ... },
        "hints": "..."
      }
    }
  ]
}
```

**Editor-spezifische Felder** (`_integration`, `_cognitive_labels`) werden beim Integrieren ausgewertet und dann **entfernt** — sie gehören nicht ins finale Schema.

---

## 1. Pflicht-Vorbereitung

**Vor jeder Integration zwingend anfordern:**

> „Bevor ich integriere: Bitte lade die **aktuelle Version** von `UI_Modul_Browser_STANDALONE.html` hoch. Die Version im Projekt-Ordner kann veraltet sein."

Erst nach Erhalt des frischen Uploads weitermachen.

---

## 2. Eingangsprüfung der Editor-Datei

Folgende Prüfungen **vor** der Integration durchführen und ggf. Rückfrage stellen:

| Prüfung | Aktion bei Problem |
|---|---|
| `title` vorhanden und sinnvoll | Rückfrage wenn leer oder Tippfehler auffällig |
| `area` und `subcategory` gesetzt | **Blocker** — ohne diese kann keine ID vergeben werden |
| `description` ≥ 50 Zeichen | Warnung; bei Toggle `beschreibung=true` ausbauen |
| `goals_primary` nicht leer | Warnung; bei Toggle `lernziele=true` ergänzen |
| `visualization.svg_inner` vorhanden | **Blocker** — ohne SVG kein Symbol im Browser |
| `_integration.hints` lesen | Alle Anweisungen daraus priorisiert befolgen |

---

## 3. ID vergeben

Die Entwurfs-ID (`ENTWURF-XXXX`) muss durch eine echte ID ersetzt werden.

**Schema:** `<SUBCATEGORY>-<NNN>` — dreistellig, fortlaufend pro Subkategorie.

**Aktuell höchste IDs (Stand: Upload vom 07.06.2026 — 306 Module):**

| Subkategorie | Höchste ID | Nächste frei |
|---|---|---|
| AT-AUS | AT-AUS-003 | AT-AUS-004 |
| AT-KOOR | AT-KOOR-006 | AT-KOOR-007 |
| AT-KRAFT | AT-KRAFT-003 | AT-KRAFT-004 |
| AT-SCHN | AT-SCHN-007 | AT-SCHN-008 |
| AT-SPRG | AT-SPRG-006 | AT-SPRG-007 |
| AT-STAB | AT-STAB-011 | AT-STAB-012 |
| AW-AKT | AW-AKT-012 | AW-AKT-013 |
| AW-BALL | AW-BALL-011 | AW-BALL-012 |
| AW-COOL | AW-COOL-004 | AW-COOL-005 |
| AW-MENT | AW-MENT-005 | AW-MENT-006 |
| AW-MOB | AW-MOB-007 | AW-MOB-008 |
| AW-PRAEV | AW-PRAEV-006 | AW-PRAEV-007 |
| KS-BALL | KS-BALL-004 | KS-BALL-005 |
| KS-FANG | KS-FANG-004 | KS-FANG-005 |
| KS-FUN | KS-FUN-005 | KS-FUN-006 |
| KS-KOOP | KS-KOOP-003 | KS-KOOP-004 |
| KS-WETT | KS-WETT-023 | KS-WETT-024 |
| TA-A-1V1 | TA-A-1V1-005 | TA-A-1V1-006 |
| TA-A-AUS | TA-A-AUS-003 | TA-A-AUS-004 |
| TA-A-FREI | TA-A-FREI-007 | TA-A-FREI-008 |
| TA-A-KREUZ | TA-A-KREUZ-003 | TA-A-KREUZ-004 |
| TA-A-STOSS | TA-A-STOSS-005 | TA-A-STOSS-006 |
| TA-D-MAN | TA-D-MAN-010 | TA-D-MAN-011 |
| TA-D-OFF | TA-D-OFF-005 | TA-D-OFF-006 |
| TA-X-TEMP | TA-X-TEMP-013 | TA-X-TEMP-014 |
| TE-A-PASS | TE-A-PASS-035 | TE-A-PASS-036 |
| TE-A-PRELL | TE-A-PRELL-006 | TE-A-PRELL-007 |
| TE-A-STOSS | TE-A-STOSS-012 | TE-A-STOSS-013 |
| TE-A-TAUSCH | TE-A-TAUSCH-003 | TE-A-TAUSCH-004 |
| TE-A-WURF | TE-A-WURF-012 | TE-A-WURF-013 |
| TE-D-1V1 | TE-D-1V1-008 | TE-D-1V1-009 |
| TE-D-BLOCK | TE-D-BLOCK-004 | TE-D-BLOCK-005 |
| TE-D-STELL | TE-D-STELL-005 | TE-D-STELL-006 |
| TE-X-BEID | TE-X-BEID-003 | TE-X-BEID-004 |
| TW-ABW | TW-ABW-003 | TW-ABW-004 |
| TW-ATHL | TW-ATHL-003 | TW-ATHL-004 |
| TW-AUF | TW-AUF-003 | TW-AUF-004 |
| TW-REAK | TW-REAK-003 | TW-REAK-004 |
| TW-STELL | TW-STELL-003 | TW-STELL-004 |
| US-2V2 | US-2V2-003 | US-2V2-004 |
| US-3V3 | US-3V3-003 | US-3V3-004 |
| US-4V4 | US-4V4-003 | US-4V4-004 |
| US-AUFGAB | US-AUFGAB-004 | US-AUFGAB-005 |
| US-MINI | US-MINI-015 | US-MINI-016 |
| US-REGEL | US-REGEL-009 | US-REGEL-010 |

**Wichtig:** Diese Tabelle ist nach jeder Integration zu aktualisieren (in diesem Dokument und in `BESTAND_AKTUELL.md`). Bei mehreren Modulen in derselben Subkategorie werden IDs sequenziell vergeben.

**Kollisionscheck:** Vor der Vergabe `EMBED_MODULES` in der hochgeladenen HTML-Datei prüfen ob die Ziel-ID bereits vorkommt — regex `<neue_id>` suchen.

---

## 4. Auto-Felder auflösen

Felder mit Wert `"auto"` müssen vor der Integration auf konkrete Werte gesetzt werden.

**Priorität:** `_integration.hints` → `description` → `subcategory` → Kontext

| Feld | Ableitung |
|---|---|
| `level` | 1 = Grundform/isoliert, 2 = Kombination/Laufen, 3 = Gegner/Entscheidung/Komplex. Hinweise aus `hints` priorisieren. |
| `intensity` | `niedrig` = Technik/Aufwärmen ohne Sprint, `mittel` = Standard, `hoch` = Sprint/Wettkampf/Gegner |
| `ek_konform` | `false` nur wenn hints es explizit sagen, Übung zu komplex für junge D-Jugend, oder subcategory = athletik mit Maximalkraft/Plyometrie |
| `transition_relevance` | `high` bei Umschalten/Gegenstoß/Tempo, `low` bei isolierter Technik, `medium` sonst |

---

## 5. Toggle-gesteuerte Optimierungen

Den `_integration.toggles`-Block auslesen. Für jeden aktiven Toggle gilt:

### `rechtschreibung: true`
Titel und description auf offensichtliche Tipp-/Grammatikfehler prüfen und korrigieren. Inhaltliche Änderungen nur wenn eindeutig falsch.

### `beschreibung: true`
Wenn description < 150 Zeichen: auf Qualitätsniveau der anderen Module ausbauen. Aufbau, Ablauf, Coaching-Punkte ergänzen. Stil der vorhandenen Beschreibungen im Browser orientieren.

### `lernziele: true`
- `goals_primary` leer → mind. 2 aus Kontext/subcategory/description ableiten
- `goals_secondary` leer → mind. 2 ergänzen (koordinative, kognitive oder taktische Aspekte der Übung)
- Vorhandene Ziele nur ergänzen, nie ersetzen

### `tags: true`
Fehlende Tags aus folgenden Quellen ergänzen:
- subcategory → Standard-Tags (z.B. AW-BALL → `ball`, `aufwaermen`)
- description → Schlagwörter extrahieren
- goals → thematische Tags
- Ziel: mind. 5 Tags gesamt

### `verlinkungen: true`
Aktiv im Bestand passende Module suchen:
- **prerequisites**: Einfachere Übung der gleichen Subcategory oder verwandter Technik
- **progressions**: Komplexere Folgeübung (Gegner, Entscheidung, mehr Spieler)
- **related**: Übungen mit gleichen Zielen oder Tags, andere Subcategory

Verlinkungen immer **bidirektional** nachziehen: wenn Modul X als Progression von Y eingetragen wird, Y auch in X.prerequisites eintragen (und Y im Browser entsprechend aktualisieren).

### `kognitive: true`
`cognitive_addons_compatible` prüfen und ggf. ergänzen:
- Entscheidungssituationen → COG-ENTS-*
- Reaktion auf Signal → COG-REAK-*
- Zwei Aufgaben gleichzeitig → COG-AUF-04
- Gegner lesen → COG-ANTI-*
- Regeleinhalten/schwache Hand → COG-INH-*

### `level: true`
Auto-Felder (level, intensity) eigenständig ableiten (siehe Abschnitt 4).

### `verzahnung: true`
Sicherstellen dass das neue Modul nicht isoliert eingefügt wird:
- Mind. 1 bestehende Verlinkung gesetzt
- Tags überschneiden sich mit mindestens 2 anderen Modulen im Bestand
- Subcategory-Nachbarn auf bidirektionale Verweise prüfen

---

## 6. SVG-Symbol aufbereiten

Das `visualization.svg_inner` aus dem Editor enthält den vollständigen SVG-Inhalt im Taktikboard-Format (viewBox 1000×700 oder 1400×700).

**Für den Modulbrowser** wird ein kompaktes Symbol benötigt (viewBox 400×400 für Halbfeld, 400×600 für Ganzfeld).

**Vorgehensweise:**
1. `konstellation_raw` aus dem Editor-Export auslesen (Tokens + Lines + Schnitt)
2. Koordinaten vom Taktikboard-Raum (1000×700) auf Symbol-Raum (400×400) skalieren:
   - Faktor X: `400/1000 = 0.4`
   - Faktor Y: `400/700 = 0.571`
3. Spielfeld-Hintergrund aus `SVG_BAUSTEINE.md` verwenden (`hf_bg()` oder `full_bg()`)
4. Token-SVG mit Modulbrowser-Stilen rendern (att=orange, def=blau, tw=grün, ball=rot)
5. Linien mit korrekten Marker-Referenzen (`arrowOrange`, `arrowGreen`, `arrowBlue`, `arrowRed`)

**Alternativ:** `svg_inner` direkt als Symbol einbetten mit angepasstem `viewBox` — nur wenn Skalierung das Ergebnis verzerrt.

**asset_id:** `VIS-<neue_id>` (mit Bindestrich, nicht Underscore)

---

## 7. Schema-Mapping

Folgende Felder müssen vor der Integration geprüft/angepasst werden:

| Editor-Wert | Modulbrowser-Wert |
|---|---|
| `court_space: "halbes_feld"` | bleibt `"halbes_feld"` ✓ |
| `court_space: "ganzfeld"` | bleibt `"ganzfeld"` ✓ |
| `court_space: "viertel"` | bleibt `"viertel"` ✓ |
| `ek_konform: "auto"` | → auflösen (Abschnitt 4) |
| `level: "auto"` | → auflösen (Abschnitt 4) |
| `"auto"` (alle Felder) | → auflösen vor Integration |

**`phase`-Feld** wird aus `subcategory` abgeleitet wenn nicht gesetzt:
- `TA-*`, `TE-A-*` → `"angriff"`
- `TA-D-*`, `TE-D-*`, `TW-*` → `"abwehr"`
- `AW-*` → `"aufwaermen"`
- `AT-*` → `"athletik"`
- `KS-*`, `US-*` → `"spiel"`
- `TA-X-*`, `TE-X-*` → `"uebergang"`

---

## 8. Felder entfernen vor Integration

Diese Editor-Felder **nicht** ins finale Modul übernehmen:

- `_integration` (kompletter Block)
- `_cognitive_labels` (nur für Lesbarkeit im Editor)
- `visualization.konstellation_raw` (optional: kann drin bleiben als Archiv, ist aber groß)

---

## 9. Einfügen in den Modulbrowser

```python
# In UI_Modul_Browser_STANDALONE.html:
# EMBED_MODULES.modules → neues Modul am Ende einfügen
# vizDefs → neues SVG-Symbol als <symbol id="VIS-<ID>" viewBox="0 0 400 400">...</symbol> ergänzen
# _meta.total_modules → um 1 erhöhen
# _meta.verteilung[subcategory] → um 1 erhöhen
# _meta.chargen → neuen Eintrag ergänzen (typ: "eigene", datum: heute)
```

---

## 10. Qualitätskontrolle vor Lieferung

Checkliste:

- [ ] Entwurfs-ID ersetzt durch echte ID
- [ ] asset_id passt zur neuen ID
- [ ] Alle `"auto"`-Werte aufgelöst
- [ ] Editor-Felder entfernt (`_integration`, `_cognitive_labels`)
- [ ] SVG-Symbol valide und im Browser dargestellt
- [ ] `_meta` aktualisiert
- [ ] Bidirektionale Verlinkungen gesetzt (wenn `verlinkungen=true`)
- [ ] Geänderte Bestandsmodule (neue Verlinkungen) ebenfalls aktualisiert
- [ ] ID-Tabelle in diesem Dokument aktualisiert

---

## 11. Lieferung

Per `present_files`:
- `UI_Modul_Browser_STANDALONE.html` (mit integriertem Modul)

Kurze Zusammenfassung:
- Vergebene ID
- Aufgelöste Auto-Felder mit Begründung
- Durchgeführte Toggle-Optimierungen
- Gesetzte Verlinkungen (neu + bidirektional)
- Etwaige Rückfragen (z.B. Beschreibung zu kurz, kein SVG vorhanden)

---

## 12. Mehrere Module auf einmal

Wenn mehrere Modul-Editor-JSONs gleichzeitig hochgeladen werden:
1. Alle Eingangsprüfungen (Abschnitt 2) für alle Module zuerst
2. Alle IDs vergeben (sequenziell, keine Konflikte)
3. Kurze Übersicht präsentieren → Freigabe abwarten
4. Dann alle Module in einem Durchgang integrieren
5. Bidirektionale Verlinkungen über alle neuen Module hinweg prüfen (neue Module können sich auch gegenseitig verlinken)
