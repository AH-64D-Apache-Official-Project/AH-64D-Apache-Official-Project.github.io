---
title: PERF page
lead: How much power you need, how much you have, and how heavy you can be, worked out for your weight and today's conditions.
keywords: [perf, performance, hover, torque, gross weight, ige, oge, go no go, vne, vsse, max range, max endurance, dual engine, single engine, cruise, cg]
seats: [PLT, CPG]
redirect_from:
  - /mpd-perf.html
---

{% include fig.html id="mpd-perf" %}

The page works from the aircraft as it is: its current pressure altitude, temperature, gross weight and centre of gravity. Use it before you pick up into a hover at a heavy weight, and before you plan a long transit.

**IGE** is a hover in ground effect, low over the ground; **OGE** is out of ground effect, above about one rotor diameter. **DE** is dual engine, **SE** single engine. Torque (**Q**) is per engine.

| Box | Read it as |
|---|---|
| **Hover Q** | **REQUIRED**: the torque you need to hover IGE and OGE at your gross weight. **GO-NO/GO**: the torque a 5 ft hover takes at the maximum dual engine gross weight, for IGE and for OGE. Hover at 5 ft and compare: at or below the OGE figure, you can hover out of ground effect; at or below the IGE figure, in ground effect. **INDICATED**: the torque you are pulling now, from the higher of the two engines. |
| **Max GWT** | The maximum gross weight for the pressure altitude, temperature and torque available: DE and SE, for an IGE and an OGE hover. Compare it with your **GWT** at the left. |
| **Max Q** | Maximum torque available per engine: DE at the 30-minute limit, SE at the 2.5-minute limit. |
| **Cruise** | Torque (Q) and total fuel flow of both engines (FF), at the maximum range (RNG) and maximum endurance (END) airspeeds. |
| **TAS** | True airspeeds. **VNE**: velocity never exceed. **VSSE**: velocity safe single engine, the minimum airspeed for safe single engine flight. **RNG**: maximum range, the airspeed that covers the most distance per pound of fuel in still air. **END**: maximum endurance, the airspeed with the lowest fuel flow, which keeps you in the air longest; it also gives the best rate of climb. |
| **CG** | Your centre of gravity against the forward and aft limits. |

A **?** means you are above the altitude the performance tables cover.

## Buttons

The top row works as on the other aircraft pages (`T4`{: .vab}, the boxed PERF tab, returns to ENG). **PA>**, **FAT>**, **GWT>**, **MAX/PLAN** modes and **HIT**/**WT** are drawn but not simulated: the page always shows current conditions. To plan for other weights and conditions, use the [mission planner]({{ '/mission/planner/' | relative_url }}).
