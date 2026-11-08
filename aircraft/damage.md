---
title: Damage and failures
lead: The component damage model, the indications for each damaged component, airframe overstress, and repair.
keywords: [damage, failure, repair, battle damage, systems, engine, rotor, hydraulics, sensors, ace, zeus, overstress, over-g, stress damage]
seats: [PLT, CPG]
---

## Description

Each aircraft system is modelled as a separate component with its own damage state. Most components fail completely at heavy damage. The engines, gearboxes, main transmission and hydraulic reservoirs degrade in stages and present cautions before they fail. Damage is indicated on the UFD and the [WCA page]({{ '/displays/mpd/wca/' | relative_url }}). Corrective actions are given on each system's page.

## Powerplant and drive train

| Component | Effect of damage | UFD |
|---|---|---|
| Engines (2) | Degrade in stages: chips, low oil pressure, oil starvation, failure. Heavy damage to a running engine can start a fire. See [Engines, drive train and rotor]({{ '/aircraft/engines/' | relative_url }}). | `ENG1 CHIPS`{: .mpd}, `ENG1 OIL PSI`{: .mpd}, `ENG1 OUT`{: .mpd} |
| Nose gearboxes (2) | Low oil pressure, then chips. A failed nose gearbox unloads its engine, which overspeeds and is shut down by its overspeed protection. | `GRBX1 OIL PSI`{: .mpd}, `GRBX1 CHIPS`{: .mpd} |
| Main transmission | Low oil pressure, then chips. Transmission failure removes all hydraulic and electrical power and the main and tail rotors. | `XMSN1 OIL PSI`{: .mpd}, `XMSN2 OIL PSI`{: .mpd}, `XMSN CHIPS`{: .mpd} |
| Intermediate and tail rotor gearboxes | Vibration, then loss of tail rotor drive. | `GRBX VIB`{: .mpd} |
| Main rotor | Destroyed: no lift. | |
| Tail rotor | Destroyed: no anti-torque thrust. | |
| APU | Fails. Heavy damage to a running APU can start a fire. | APU FIRE (MPD) |

## Electrical and hydraulic

| Component | Effect of damage | UFD |
|---|---|---|
| Battery | Battery no longer holds a charge. | `BATTERY`{: .mpd} |
| Generators (2) | No AC from that generator. | `GEN1 FAIL`{: .mpd}, `GEN2 FAIL`{: .mpd} |
| Transformer rectifier units (2) | No DC from that TRU. | `RECT1 FAIL`{: .mpd}, `RECT2 FAIL`{: .mpd} |
| Hydraulic pumps (primary, utility) | No pressure from that pump. Primary pump failure also removes the BUCS and the FMC. | `PRI HYD PSI`{: .mpd}, `BUCS FAIL`{: .mpd}, `FMC DISENG`{: .mpd}, `UTIL HYD PSI`{: .mpd} |
| Hydraulic reservoirs | Leak; the rate depends on the severity of the damage, up to empty in approximately two minutes. | `PRI HYD LVL`{: .mpd}, `UTIL HYD LVL`{: .mpd} |

See [Electrical, APU and hydraulics]({{ '/aircraft/electrical/' | relative_url }}).

## Fuel and airframe

| Component | Effect of damage | Indication |
|---|---|---|
| Forward and aft fuel cells, IAFS | Leak, at up to approximately 130 lb per hour per cell. | Cell quantity decreasing on the FUEL page |
| External tanks | Explode when their pylon is heavily damaged, if they contain more than approximately 200 lb. | |
| Stabilator | Remains at its current position and no longer schedules with airspeed. The same occurs without DC power. | `STAB FAIL`{: .mpd} |

## Mission equipment

| Component | Effect of damage |
|---|---|
| TADS DTV, TADS FLIR | That sensor is lost. The sight status displays `TADS FAIL`{: .mpd} with both lost. |
| TADS turret | The TADS no longer moves. |
| PNVS FLIR, PNVS turret | No PNVS image: `NVS FAIL`{: .mpd}. |
| Fire control radar | Radar fault: `FCR FAULT`{: .mpd}. |
| Gun turret | The gun fails. A round cooked off by an overheated barrel has the same effect. |
| Pylons | Damage drains the utility hydraulic system, which powers pylon articulation. |
| IR jammer | No jamming: `IRJAM FAIL`{: .mpd} (US equipment). |

## Overstress {#overstress}

HeliSim provides stress damage. Overstressing the aircraft (over-g) results in component loss. Stress damage accumulates and is not recovered in flight.

The components lost to overstress are the stabilator, the vertical fin, the tail rotor, the tail boom and the main rotor blades. Loss of the tail boom removes the vertical fin, stabilator and tail rotor with it, and moves the centre of gravity forward.

Main rotor blade damage presents as a blade out of track, loss of a blade tip cap, a failed pitch change link, or blade separation. A separated blade leaves the main rotor out of balance; the resulting vibration damages the main transmission and leads to further blade loss and transmission failure.

## Repair

Repairing the aircraft with ACE, Zeus or a script restores the systems along with the component damage:

- hydraulic fluid, the accumulator and the battery are restored;
- a repaired engine's chips, oil pressure, failure and overspeed faults are cleared, and it can be restarted;
- the fire bottles are refilled;
- a full repair restores components lost to overstress.
