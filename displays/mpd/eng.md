---
title: ENG page
lead: Engines, rotor and hydraulics at a glance. The page you watch during start-up, and the one that tells you what is wrong when something is.
keywords: [eng, engine, torque, tgt, np, nr, ng, oil, hydraulics, start]
seats: [PLT, CPG]
redirect_from:
  - /mpd-eng.html
---

Open it with the **A/C** button, from MENU, or by pressing the boxed tab on any aircraft page.

{% include fig.html id="mpd-eng" %}

## Formats

The page changes with what you are doing:

| Format | When | Adds |
|---|---|---|
| **Ground** | On the ground | Engine oil pressure for both engines. |
| **Flight** | Airborne | Nothing; the figure above. |
| **WCA** | Any warning or caution active | A box listing up to five of them, in place of the hydraulic pressures. |

While a starter is turning, a **START** box shows **ON** beside the engine being started.

{% include fig.html id="mpd-eng-start" %}

## Buttons

| Button | Label | Action |
|---|---|---|
| `T2`{: .vab} | `FLT`{: .mpd} | Opens FLT. |
| `T3`{: .vab} | `FUEL`{: .mpd} | Opens FUEL. |
| `T4`{: .vab} | `PERF`{: .mpd} | Opens PERF. |
| `T6`{: .vab} | `UTIL`{: .mpd} | Opens UTIL. |
| `R6`{: .vab} | `ACQ`{: .mpd} | Opens the [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list. |
| `B1`{: .vab} | | MENU. |
| `B6`{: .vab} | `WCA`{: .mpd} | Opens the [WCA page]({{ '/displays/mpd/wca/' | relative_url }}). |

**SYS** and **ETF** are not simulated.

## Reading the tapes

Each tape has a green normal range and yellow and red bands above it. The red markers across the tops are the limits. Torque and TGT have one tape per engine; in the middle, the two Np tapes sit either side of the rotor speed chevron, which should rest at 101% in flight. The [flight model]({{ '/flying/flight-model/' | relative_url }}#limits) page explains what happens when you exceed a limit.

A digital value turns red when it is outside its limits.
