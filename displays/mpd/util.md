---
title: UTIL page
lead: The aircraft UTIL page switches the flight management computer's channels.
keywords: [util, fmc, channels, pitch, roll, yaw, collective, trim, anti-ice]
seats: [PLT, CPG]
redirect_from:
  - /mpd-util.html
---

{% include fig.html id="mpd-util" %}

## Buttons

| Button | Label | Action |
|---|---|---|
| `L1`{: .vab} | `PITCH`{: .mpd} | FMC pitch channel on or off. |
| `L2`{: .vab} | `ROLL`{: .mpd} | FMC roll channel on or off. |
| `L3`{: .vab} | `YAW`{: .mpd} | FMC yaw channel on or off. |
| `L4`{: .vab} | `COLL`{: .mpd} | FMC collective channel on or off. |
| `L5`{: .vab} | `TRIM`{: .mpd} | Force trim on or off. |
| `T2`{: .vab}–`T4`{: .vab} | | FLT, FUEL, PERF. `T6`{: .vab} (the boxed UTIL tab) returns to ENG. |
| `B1`{: .vab} | | MENU. |

A filled circle next to a channel means it is on. Turning any of the four FMC channels off disables the [stability augmentation and hold modes]({{ '/flying/flight-control/' | relative_url }}) on that axis and raises the `FMC DISENG`{: .mpd} caution.

> Leave every channel on. Turning one off is for flying a degraded aircraft on purpose, or for testing.
{: .note}

**NOE/A**, the **ANTI ICE** switches, **BLEED AIR**, **ECS**, **TEMP** and **GND**, and the temperature readouts, are drawn but not simulated.
