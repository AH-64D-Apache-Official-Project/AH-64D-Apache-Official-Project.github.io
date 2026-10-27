---
title: FLT page
lead: A head-down attitude indicator with airspeed, altitudes, heading and steering to the next point.
keywords: [flt, flight, attitude, horizon, airspeed, altitude, heading, fly-to, turn, slip]
seats: [PLT, CPG]
redirect_from:
  - /mpd-flt.html
---

Open it from the top row of any aircraft page, from MENU, or by pressing {% include key.html id="fza_ah64_symbologySelectPress" %}, which puts it on your left MPD.

{% include fig.html id="mpd-flt" %}

## Buttons

| Button | Label | Action |
|---|---|---|
| `T2`{: .vab} | `FLT`{: .mpd .box} | This page; pressed again, opens ENG. |
| `T3`{: .vab} | `FUEL`{: .mpd} | Opens FUEL. |
| `T4`{: .vab} | `PERF`{: .mpd} | Opens PERF. |
| `T6`{: .vab} | `UTIL`{: .mpd} | Opens UTIL. |
| `R6`{: .vab} | `ACQ`{: .mpd} | Opens the [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list. |
| `B1`{: .vab} | | MENU. |

The **-W- BIAS** and **SET** labels are not simulated.

## Navigation

When a route or a direct-to point is active, the box in the lower left shows the point's identifier, distance, ground speed and time to go, and the command heading caret and fly-to cue steer you to it. Points and routes are set up on the [TSD]({{ '/displays/mpd/tsd/' | relative_url }}).

## Sensor bearings

Small markers on the heading tape show where the radar's centreline and the other crew station's sight are pointing, when they are in use.
