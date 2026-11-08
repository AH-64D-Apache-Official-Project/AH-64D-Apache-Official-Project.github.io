---
title: Multipurpose displays (MPD)
lead: The MPDs are the primary means of interacting with and configuring aircraft systems. Bezel pushbuttons, pushbutton types, the MPD cursor and the page index.
keywords: [mpd, multipurpose display, vab, fab, buttons, pages, menu, bezel, display, cursor, barrier]
seats: [PLT, CPG]
redirect_from:
  - /mpd.html
---

## Bezel

{% include fig.html id="mpd-menu" %}

The MPDs are the primary means of interacting with and configuring aircraft systems. Each display has 24 variable action buttons (VABs) arranged around the bezel in groups of six. Buttons are referenced by their location around the MPD as top (T), right (R), bottom (B) and left (L), numbered left to right and top to bottom: `T1`{: .vab}–`T6`{: .vab}, `R1`{: .vab}–`R6`{: .vab}, `B1`{: .vab}–`B6`{: .vab}, `L1`{: .vab}–`L6`{: .vab}. The function of each VAB is set by the page and specified by the adjacent display text label.

The fixed action buttons (FABs), or subsystem buttons, and the Menu (M) button perform the same function on every page:

| Button | Function |
|---|---|
| M | MENU page (in the `B1`{: .vab} position) |
| FCR | FCR page |
| WPN | WPN page |
| TSD | TSD page |
| A/C | ENG page; pressed again on the ENG page, the FLT page |
| VID | VIDEO page |
| COM | COM page (not simulated) |

The BRT and VID controls and the DAY/NIGHT/MONO knob are not simulated.

## Pushbutton types

| Marking | Pushbutton |
|---|---|
| Arrow above the label | Page pushbutton: selects a page |
| Partial intensity barrier beside the label | Not selectable in the current operating mode |
| Right-facing chevron (`>`) | Data entry pushbutton: enters data with the KU |
| Filled or open dot beside the label | On/Off pushbutton: filled is on, open is off |
| Box around the label | Selected option. On the aircraft pages, the boxed page pushbutton is the page presented, and pressing it returns to the ENG page. |

Green indicates normal and advisory conditions; yellow, cautions and hazards; red, warnings and enemy threats; white, attention, such as an empty fuel cell; cyan, friendlies and the sky of the attitude indicator; brown, the ground of the attitude indicator. Partial intensity de-emphasizes normal conditions.

## MPD cursor {#cursor}

Each crew station has its own MPD cursor, a green ring with four spokes, which moves over that crew station's two MPDs. It selects buttons and selects symbols on the TSD and FCR pages. Its bindings are in **AH-64D Official Project**:

| Binding | Function |
|---|---|
| MPD Cursor: Up / Down / Left / Right | Moves the cursor; speed increases with stick deflection and with time held. |
| MPD Cursor: Enter | Presses the button whose label is under the cursor, or acts on the symbol under it. |
| MPD Cursor: Display Select | Moves the cursor to the center of the other MPD. |

- **Buttons**: with the cursor on a label, the label is displayed bold; Enter presses the button, and holding Enter holds it. A button without a label can be pressed at its position on the MPD edge.
- **Pages**: over the TSD map or the FCR scan area the cursor is displayed as a white X. The function of Enter there is described on the [TSD]({{ '/displays/mpd/tsd/' | relative_url }}#cursor) and [FCR]({{ '/displays/mpd/fcr/' | relative_url }}#cursor) pages.
- **Changing MPD**: the cursor moves to the other MPD when it is pushed against the inner edge, released and pushed again. On an MPD that is off, it moves to the other MPD.
- **Stowing**: three minutes after last use, the cursor moves to the lower left corner, unless it rests on a label or a TSD or FCR symbol.

The cockpit mouse cursor does not move the MPD cursor.

## Pressing buttons

Buttons are pressed with the cockpit cursor ([Controls and bindings]({{ '/getting-started/controls/' | relative_url }})) or a direct binding: every button on both MPDs in both crew stations has a binding in **AH-64D Official Project: Cockpit Controls** (`left mpd: left mpd t1`, `right mpd: right mpd fcr` and so on).

Each MPD retains its page, and each page retains its settings. MPD page selection is crewstation independent; aircraft data is aircraft common, so a waypoint added on the pilot's TSD is displayed on the CPG's.

## Pages

<div class="cards">
  <a class="card" href="{{ '/displays/mpd/menu/' | relative_url }}"><span class="card-k">MENU</span><span class="card-t">MENU</span><span class="card-d">Index of all pages.</span></a>
  <a class="card" href="{{ '/displays/mpd/flt/' | relative_url }}"><span class="card-k">FLT</span><span class="card-t">FLT</span><span class="card-d">Attitude, airspeed, altitude and navigation.</span></a>
  <a class="card" href="{{ '/displays/mpd/eng/' | relative_url }}"><span class="card-k">ENG</span><span class="card-t">ENG</span><span class="card-d">Engines, rotor and hydraulics.</span></a>
  <a class="card" href="{{ '/displays/mpd/fuel/' | relative_url }}"><span class="card-k">FUEL</span><span class="card-t">FUEL</span><span class="card-d">Fuel cells, pumps, crossfeed and fuel check.</span></a>
  <a class="card" href="{{ '/displays/mpd/perf/' | relative_url }}"><span class="card-k">PERF</span><span class="card-t">PERF</span><span class="card-d">Real-time performance data.</span></a>
  <a class="card" href="{{ '/displays/mpd/util/' | relative_url }}"><span class="card-k">UTIL</span><span class="card-t">UTIL</span><span class="card-d">FMC axes and force trim.</span></a>
  <a class="card" href="{{ '/displays/mpd/wca/' | relative_url }}"><span class="card-k">WCA</span><span class="card-t">WCA</span><span class="card-d">Warnings, cautions and advisories.</span></a>
  <a class="card" href="{{ '/displays/mpd/tsd/' | relative_url }}"><span class="card-k">TSD</span><span class="card-t">TSD</span><span class="card-d">Tactical situation display: map, points and routes.</span></a>
  <a class="card" href="{{ '/displays/mpd/wpn/' | relative_url }}"><span class="card-k">WPN</span><span class="card-t">WPN</span><span class="card-d">Weapon status and settings.</span></a>
  <a class="card" href="{{ '/displays/mpd/fcr/' | relative_url }}"><span class="card-k">FCR</span><span class="card-t">FCR</span><span class="card-d">Radar targets, map and terrain profile.</span></a>
  <a class="card" href="{{ '/displays/mpd/ase/' | relative_url }}"><span class="card-k">ASE</span><span class="card-t">ASE</span><span class="card-d">Threats and countermeasures.</span></a>
  <a class="card" href="{{ '/displays/mpd/video/' | relative_url }}"><span class="card-k">VID</span><span class="card-t">VIDEO</span><span class="card-d">TADS or night vision video.</span></a>
  <a class="card" href="{{ '/displays/mpd/dms/' | relative_url }}"><span class="card-k">DMS</span><span class="card-t">DMS</span><span class="card-d">Data management and software versions.</span></a>
  <a class="card" href="{{ '/displays/mpd/code/' | relative_url }}"><span class="card-k">CODE</span><span class="card-t">Laser codes</span><span class="card-d">Laser codes, frequencies and missile channels.</span></a>
</div>
