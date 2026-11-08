---
title: Hydra 70 rockets
lead: The 2.75 inch Hydra 70 rocket system — warheads, launcher zones, engagement sequence, cooperative engagement and messages.
keywords: [rockets, hydra, 2.75, m151, m255, flechette, m261, mpsm, m257, m278, illumination, pod, zone, rkt tof, coop, steering cursor, quantity, swarm]
seats: [PLT, CPG]
redirect_from:
  - /weapons-rockets.html
  - /weapons-ammo-rockets.html
---

## Description

The rocket system fires unguided 2.75 inch Hydra 70 rockets from 19-tube M261 launchers on the wing stations. The pylons articulate in elevation to the ballistic solution for the selected range; azimuth is controlled by the heading of the aircraft.

| Rocket | Code | Warhead | Use |
|---|---|---|---|
| M151 HEDP | `6PD`{: .mpd} | 10 lb high explosive, pre-fragmented | Light vehicles, personnel |
| M255A1 FLEC | `6FL`{: .mpd} | Flechettes | Personnel in the open |
| M261 MPSM | `6MP`{: .mpd} | Nine parachute-retarded submunitions | Personnel and light armor over an area |
| M257 IL | `6IL`{: .mpd} | Parachute flare, visible light | Illuminates approximately 1 km² for approximately 100 s, deployed approximately 3.5 km from launch |
| M278 IR IL | `6IR`{: .mpd} | Parachute flare, infrared | As M257; visible through night vision and thermal sensors only |

## Launchers and zones

Each launcher holds 19 rockets in three zones, and each zone can be loaded with a different rocket type:

| Zone | Rockets |
|---|---|
| A / C | 12 |
| B / D | 4 |
| E (center) | 3 |

The pylon loadout sets the rocket type in each zone; see [Rearm and refuel]({{ '/mission/rearm/' | relative_url }}). The [WPN page]({{ '/displays/mpd/wpn/' | relative_url }}) lists up to five rocket types loaded, with the quantity of each.

The pylons articulate from 4° up to 15° down in the air, and to 5° down on the ground. Outside these limits PYLON LIMIT is displayed; in the air it is a warning only, and on the ground it inhibits launch. With utility hydraulics failed, the pylons cannot articulate and rockets are inhibited (PYLON ERROR). Rockets are inhibited below 0.5 g.

## Engagement sequence

A target is engaged with rockets using the following sequence, known as SWARM:

1. **Sight**: select HMD {% include key.html id="fza_ah64_v30_sightSelectHMD" %}, TADS {% include key.html id="fza_ah64_v30_sightSelectTADS" %} or FCR {% include key.html id="fza_ah64_v30_sightSelectFCR" %}.
2. **Weapon**: WAS the rockets {% include key.html id="fza_ah64_wasRkt" %}. On the WPN page rocket format, select the rocket type (`L1`{: .vab}–`L5`{: .vab}) and the quantity per trigger pull (`R1`{: .vab} QTY: 1, 2, 4, 8, 12, 24 or ALL).
3. **Armed**: arm the aircraft with the A/S button on the armament panel, and verify the ARMED indication on the WPN page.
4. **Range**: verify the desired Manual, Default, Auto or Navigation Range after WASing. If the desired range source is incorrect, reset the range source. The PLT will have to reselect the ACQ at `R6`{: .vab} and the CPG will have to press the SLAVE button {% include key.html id="fza_ah64_sightSlave" %} to restore a navigation range.

   If performing a COOP engagement, lase once for a stationary target, or lase continuously for a moving target, then call "Match and Shoot" to alert the pilot they need to align the rocket steering cursor. Verify the range is outside the minimum (500 m) and within the maximum (7,500 m).
5. **Messages**: verify the rocket type, mode and quantity in the HAD weapon status field, and that no inhibit is displayed.
{: .steps}

Turn the aircraft to place the rocket steering cursor on the reticle, then fire with the weapon trigger. Rockets in a volley are launched 0.09 s apart. After launch, the HAD displays the time of flight to the last volley's impact as `RKT TOF=nn`{: .mpd}. The ballistic solution includes lead for a moving target tracked by the FCR.

## Cooperative engagement

When both crew stations action the rockets, with the CPG's sight TADS and the pilot's sight HMD, the rockets are fired cooperatively (`COOP`{: .mpd}). The CPG acquires and lases the target with the TADS; the pilot flies the aircraft onto the steering cursor using the CPG's range.
