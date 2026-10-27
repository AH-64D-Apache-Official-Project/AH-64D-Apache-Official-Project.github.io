---
title: Using the MPDs
lead: Each crew station has two multipurpose displays. Every page is driven by the buttons around its edge.
keywords: [mpd, multipurpose display, vab, fab, buttons, pages, menu, bezel, display]
seats: [PLT, CPG]
redirect_from:
  - /mpd.html
---

## The bezel

{% include fig.html id="mpd-menu" %}

**Variable action buttons (VABs)** are the 24 unlabelled buttons along the four edges. What each one does depends on the page, and the page labels its function next to it. They are named by edge and number, counting left to right and top to bottom: `T1`{: .vab}–`T6`{: .vab}, `B1`{: .vab}–`B6`{: .vab}, `L1`{: .vab}–`L6`{: .vab}, `R1`{: .vab}–`R6`{: .vab}. This manual uses those names throughout.

**Fixed action buttons (FABs)** have the same job on every page:

| Button | Opens |
|---|---|
| **M** | MENU. It sits in the `B1`{: .vab} position. |
| **FCR** | The FCR page. |
| **WPN** | The WPN page. |
| **TSD** | The TSD page. |
| **A/C** | The ENG page; pressed again on ENG, the FLT page. |
| **VID** | The VIDEO page. |
| **COM** | Not simulated. |

The **BRT** and **VID** knobs and the **DAY/NT/MONO** switch on the bezel are not simulated.

## Reading a page

- A label with an **arrow** above it opens another page.
- A **boxed** label is the current selection. On the top row of the aircraft pages, the boxed tab is the page you are on; pressing it again takes you back to ENG.
- A label with a **dark bar** under it is drawn but not simulated. Pressing it does nothing.
- **Green** is normal, **yellow** a caution, **red** a warning. **White** marks a value that needs your attention, such as an empty fuel cell.

## Pressing buttons

Click a button through the cockpit cursor ([Controls and bindings]({{ '/getting-started/controls/' | relative_url }})) or bind it directly: every button on both MPDs, in both seats, has a binding in **AH-64D Cockpit Controls** (`left mpd: t1`, `right mpd: fcr` and so on).

Each MPD remembers its page, and each page remembers its own settings. Both crew stations have their own pair of MPDs and can show any page independently, but they share the aircraft's data: a waypoint added on the pilot's TSD appears on the CPG's.

## The pages

<div class="cards">
  <a class="card" href="{{ '/displays/mpd/menu/' | relative_url }}"><span class="card-k">MENU</span><span class="card-t">MENU</span><span class="card-d">The index of every page.</span></a>
  <a class="card" href="{{ '/displays/mpd/flt/' | relative_url }}"><span class="card-k">FLT</span><span class="card-t">FLT</span><span class="card-d">Attitude, airspeed, altitudes and navigation.</span></a>
  <a class="card" href="{{ '/displays/mpd/eng/' | relative_url }}"><span class="card-k">ENG</span><span class="card-t">ENG</span><span class="card-d">Engines, rotor and hydraulics.</span></a>
  <a class="card" href="{{ '/displays/mpd/fuel/' | relative_url }}"><span class="card-k">FUEL</span><span class="card-t">FUEL</span><span class="card-d">Fuel cells, pumps, crossfeed and the fuel check.</span></a>
  <a class="card" href="{{ '/displays/mpd/perf/' | relative_url }}"><span class="card-k">PERF</span><span class="card-t">PERF</span><span class="card-d">What the aircraft can do at this weight today.</span></a>
  <a class="card" href="{{ '/displays/mpd/util/' | relative_url }}"><span class="card-k">UTIL</span><span class="card-t">UTIL</span><span class="card-d">Flight computer channels.</span></a>
  <a class="card" href="{{ '/displays/mpd/wca/' | relative_url }}"><span class="card-k">WCA</span><span class="card-t">WCA</span><span class="card-d">Every warning, caution and advisory.</span></a>
  <a class="card" href="{{ '/displays/mpd/tsd/' | relative_url }}"><span class="card-k">TSD</span><span class="card-t">TSD</span><span class="card-d">The moving map, points and routes.</span></a>
  <a class="card" href="{{ '/displays/mpd/wpn/' | relative_url }}"><span class="card-k">WPN</span><span class="card-t">WPN</span><span class="card-d">Weapon status and settings.</span></a>
  <a class="card" href="{{ '/displays/mpd/fcr/' | relative_url }}"><span class="card-k">FCR</span><span class="card-t">FCR</span><span class="card-d">The radar's targets, map and terrain profile.</span></a>
  <a class="card" href="{{ '/displays/mpd/ase/' | relative_url }}"><span class="card-k">ASE</span><span class="card-t">ASE</span><span class="card-d">Threats and countermeasures.</span></a>
  <a class="card" href="{{ '/displays/mpd/video/' | relative_url }}"><span class="card-k">VID</span><span class="card-t">VIDEO</span><span class="card-d">The TADS or PNVS picture on the MPD.</span></a>
  <a class="card" href="{{ '/displays/mpd/dms/' | relative_url }}"><span class="card-k">DMS</span><span class="card-t">DMS</span><span class="card-d">Data management, versions and coordinates.</span></a>
  <a class="card" href="{{ '/displays/mpd/com/' | relative_url }}"><span class="card-k">COM</span><span class="card-t">COM pages</span><span class="card-d">Laser codes, frequencies and channels.</span></a>
</div>
