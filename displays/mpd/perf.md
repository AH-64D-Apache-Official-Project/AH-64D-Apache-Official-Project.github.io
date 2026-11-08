---
title: Performance (PERF) page
lead: Real-time performance data for the helicopter — hover torque, maximum gross weight, maximum torque available, cruise and airspeed data.
keywords: [perf, performance, hover, torque, gross weight, ige, oge, go no go, vne, vsse, max range, max endurance, dual engine, single engine, cruise, cg]
seats: [PLT, CPG]
redirect_from:
  - /mpd-perf.html
---

{% include fig.html id="mpd-perf" %}

The performance page provides real-time performance data for the helicopter, accurate from −40 to +40 °C and from 0 to 8,000 ft pressure altitude.

- **PA**: the current pressure altitude, the altitude above mean sea level, from 0 to 8,000 ft.
- **FAT**: the current free air temperature around the helicopter, in degrees Celsius, from −40 to +40 °C.
- **GWT**: the current gross weight of the helicopter. It accounts for ALL fuel and ammunition loaded, and decreases dynamically as weapons and fuel are expended.

DE is dual engine and SE single engine. Torque (Q) is per engine.

## Hover Q box

The Hover Q (torque) box provides real-time information on the torque required to hover at 5 ft in ground effect (IGE) and at 80 ft out of ground effect (OGE).

The **REQUIRED** IGE and OGE values are driven by the combination of PA, FAT and GWT: the higher the PA, FAT and GWT, the higher these values. They are fixed to their respective hover heights and give the pilot the torque required to hover in the current conditions.

The **GO-NO/GO** IGE and OGE values are driven by PA, FAT and Max Q (using 100% when Max Q exceeds 100%), and are calculated at a 5 ft hover. They allow the crew to determine, before picking up to a hover, whether IGE and OGE hover power is available:

- When the required IGE torque is greater than GO-NO/GO OGE, the helicopter **DOES NOT** have OGE hover power and cannot perform OGE manoeuvres.
- When the required IGE torque is greater than GO-NO/GO IGE, the helicopter **DOES NOT** have IGE hover power, has likely exceeded the maximum gross weight for combat of 20,260 lb, and **DOES NOT** have OGE hover power.

These values allow the crew to determine IGE and OGE hover power from a 5 ft hover, without climbing to 80 ft.

The **INDICATED** value is the torque currently being pulled, and should be within 1 to 2% of the REQUIRED value.

## Max GWT box

The Max GWT box provides the maximum allowable gross weight for the current PA and FAT. The values are measured at 5 ft and correspond to the GO-NO/GO IGE and OGE torque values respectively.

- If GWT exceeds Max GWT OGE, the helicopter **DOES NOT** have OGE hover power and cannot perform OGE manoeuvres.
- If GWT exceeds Max GWT IGE, the helicopter **DOES NOT** have IGE or OGE hover power, and may have exceeded the maximum gross weight for combat of 20,260 lb.

The Max GWT OGE value is used to determine the fuel and ammunition load.

## Max Q box

The Max Q box provides the maximum torque the engines can provide dual engine (DE) and single engine (SE). Whenever the indicated torque (on the PERF, ENG or FLT page or the HDU) reaches this value, Nr begins to droop, because the value is tied to the TGT limiters: 867 °C dual engine and 896 °C single engine. See [Engines, drive train and rotor]({{ '/aircraft/engines/' | relative_url }}#tgt-limiter-and-engine-performance).

## Cruise box

The Cruise box provides the torque required and expected fuel flow for maximum range (RNG) and maximum endurance/rate-of-climb (END) airspeed. Maximum range airspeed provides the most distance per pound of fuel burned; maximum endurance/rate-of-climb airspeed provides the maximum station time.

## TAS box

The TAS box provides the true airspeeds for:

- **VNE**, velocity never exceed. VNE must never be exceeded; loss of aircraft control can and will result, from retreating blade stall or compressibility depending on conditions.
- **VSSE**, velocity safe single engine: the minimum airspeed for single engine operation. Below this airspeed, maximum single engine torque **WILL BE REQUIRED** to maintain level flight, and exceeding the maximum torque available single engine **WILL RESULT** in main rotor droop.
- **RNG**: the expected airspeed with maximum range torque applied.
- **END**: the expected airspeed with maximum endurance torque applied.

## CG

The centre of gravity is displayed against the forward and aft limits.

## Buttons

The top row operates as on the other aircraft pages (`T4`{: .vab}, the boxed PERF page button, returns to the ENG page). PA>, FAT>, GWT>, the MAX and PLAN modes, HIT and WT are displayed but not simulated; the page displays current conditions only. Planning for other weights and conditions is done in the [mission planner]({{ '/mission/planner/' | relative_url }}).
