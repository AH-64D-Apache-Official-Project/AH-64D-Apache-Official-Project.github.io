---
title: PERF page
lead: How much power you need, how much you have, and how heavy you can be, worked out for your weight and today's conditions.
keywords: [perf, performance, hover, torque, gross weight, ige, oge, vne, cruise, cg]
seats: [PLT, CPG]
redirect_from:
  - /mpd-perf.html
---

{% include fig.html id="mpd-perf" %}

The page works from the aircraft as it is: its current pressure altitude, temperature, gross weight and centre of gravity. Use it before you pick up into a hover at a heavy weight, and before you plan a long transit.

**IGE** is a hover in ground effect, low over the ground; **OGE** is out of ground effect, above about one rotor diameter. **DE** is both engines, **SE** a single engine.

| Box | Read it as |
|---|---|
| **Hover Q** | *Required* is the torque you will need to hover. *Go/No-Go* is the torque that, if you can pull it without exceeding a limit, means you can hover. *Indicated* is the torque you are pulling now. |
| **Max GWT** | The heaviest you can be and still hover. Yellow values are below your current weight: you cannot hover in that condition. |
| **Max Q** | Torque available. Yellow boxes mark single-engine figures. |
| **Cruise** | Torque (Q) and fuel flow (FF) for best range and for best endurance. |
| **TAS** | Never-exceed speed, single-engine safe speed, best range and best endurance speeds. |
| **CG** | Your centre of gravity against the forward and aft limits. |

A **?** means you are above the altitude the performance tables cover.

## Buttons

The top row works as on the other aircraft pages (`T4`{: .vab}, the boxed PERF tab, returns to ENG). **PA>**, **FAT>**, **GWT>**, **MAX/PLAN** modes and **HIT**/**WT** are drawn but not simulated: the page always shows current conditions. To plan for other weights and conditions, use the [mission planner]({{ '/mission/planner/' | relative_url }}).
