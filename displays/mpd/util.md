---
title: Aircraft utility (A/C UTIL) page
lead: The A/C UTIL page displays the controls for the flight management computer (FMC) axes and force trim.
keywords: [util, fmc, channels, pitch, roll, yaw, collective, trim, anti-ice]
seats: [PLT, CPG]
redirect_from:
  - /mpd-util.html
---

{% include fig.html id="mpd-util" %}

## Buttons

| Button | Label | Function |
|---|---|---|
| `L1`{: .vab} | `PITCH`{: .mpd} | FMC pitch axis on or off |
| `L2`{: .vab} | `ROLL`{: .mpd} | FMC roll axis on or off |
| `L3`{: .vab} | `YAW`{: .mpd} | FMC yaw axis on or off |
| `L4`{: .vab} | `COLL`{: .mpd} | FMC collective axis on or off |
| `L5`{: .vab} | `TRIM`{: .mpd} | Force trim on or off |
| `T2`{: .vab}–`T4`{: .vab} | | FLT, FUEL, PERF; `T6`{: .vab} (the boxed UTIL page button) returns to the ENG page |
| `B1`{: .vab} | | MENU page |

A filled dot beside an axis indicates it is on. Selecting any FMC axis off removes [stability augmentation and the hold modes]({{ '/flying/flight-control/' | relative_url }}) in that axis and raises the `FMC DISENG`{: .mpd} caution. All axes are normally on; an axis is selected off only for degraded-mode flight or testing.

NOE/A, the ANTI ICE selections, BLEED AIR, ECS, TEMP, GND and the temperature readouts are displayed but not simulated.
