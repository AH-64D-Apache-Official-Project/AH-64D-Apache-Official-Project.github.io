---
title: ASE page
lead: Aircraft survivability equipment. Threats around you on a ring, and the switches for the warning receivers, chaff, and the IR jammer or missile warner.
keywords: [ase, rlwr, rwr, lwr, radar warning, laser warning, chaff, flares, ir jammer, mws, autopage, threats]
seats: [PLT, CPG]
redirect_from:
  - /mpd-ase.html
---

Open it from the TSD (`T2`{: .vab} **ASE**), the WPN page, or MENU. What the systems detect, and how to defeat it, is on the [Survivability (ASE)]({{ '/weapons/ase/' | relative_url }}) page.

{% include fig.html id="mpd-ase" %}

## The threat ring

Your aircraft is in the centre, nose up. Each threat the warning receivers detect is drawn on the ring at its bearing, with an icon for what it is and what it is doing:

| State | Shown |
|---|---|
| **Search** | The radar is sweeping, not looking at you in particular. |
| **Acquisition** | The radar has picked you out. |
| **Track** | The radar is tracking you, ready to fire. A line runs from the centre towards it. |
| **Launch** | A radar-guided missile is in the air. The icon flashes. |
| **Laser** | You are being lased: designated or ranged. |
| **Missile** | British equipment only: the missile warner has seen a missile or rocket coming. The icon flashes. |

The number beside **RLWR** counts the radar and laser threats being shown.

## Buttons

| Button | Label | Action |
|---|---|---|
| `T1`{: .vab} | `CHAFF`{: .mpd} (US) / `CMS`{: .mpd} (British) | Arms or safes the chaff dispenser. It must be **ARM** for chaff to fire. |
| `T2`{: .vab} | | Opens the TSD. |
| `L3`{: .vab}–`L6`{: .vab} | `SRH` `ACQ` `TRK` `OFF` | **Autopage**. When a threat reaches the chosen state, the right MPD switches to this page, unless one of your MPDs already shows it. |
| `R1`{: .vab} | `IRJAM`{: .mpd} (US) / `MWS`{: .mpd} (British) | Turns the IR jammer, or the missile warning system, on or off. The IR jammer shows **WARM** for two seconds, then **OPER**. |
| `R6`{: .vab} | `RLWR`{: .mpd} | Turns the radar and laser warning receivers on or off. You hear a tone when they come on. |
| `B1`{: .vab} | | MENU. |

The quantity under the aircraft is the chaff remaining, and with British equipment the flares as well (**CH/FL**).

**CHAFF MODE**, **CAQ**, **UTIL** and **360** are not simulated.

> The RLWR, chaff and the IR jammer or MWS all start **off** or **SAFE**. Turn them on after start-up. Without DC power they drop out again: the RLWR turns off and chaff goes to SAFE.
{: .caution}
