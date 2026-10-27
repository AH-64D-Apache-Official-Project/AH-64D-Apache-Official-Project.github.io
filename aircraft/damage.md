---
title: Damage and failures
lead: The Apache is not one health bar. Each system has its own hitpoint, and losing one takes away what it does, often before anything shows on the outside.
keywords: [damage, hitpoints, failure, repair, battle damage, systems, engine, rotor, hydraulics, sensors, ace, zeus]
seats: [PLT, CPG]
---

Most components fail outright at heavy damage. Some, the engines, gearboxes, transmission and hydraulic reservoirs, warn you first and get worse in steps. The [WCA page]({{ '/displays/mpd/wca/' | relative_url }}) and the UFD tell you what has been hit.

## What each hit costs you

### Powerplant and drivetrain

| Component | When damaged | Shows as |
|---|---|---|
| **Engines** (2) | Worsen in steps to chips, low oil pressure, oil starvation and failure. A heavy hit on a running engine can start a fire. See [Engines and rotor]({{ '/aircraft/engines/' | relative_url }}#how-an-engine-fails). | `ENG1 CHIPS`{: .mpd}, `ENG1 OIL PSI`{: .mpd}, `ENG1 OUT`{: .mpd} |
| **Nose gearboxes** (2) | Low oil pressure, then chips; a damaged one slips. If one comes apart, its engine overspeeds. | `GRBX1 OIL PSI`{: .mpd}, `GRBX1 CHIPS`{: .mpd} |
| **Main transmission** | Low oil pressure, then chips. If it fails it takes the rotors, generators and hydraulic pumps with it. | `XMSN1 OIL PSI`{: .mpd}, `XMSN2 OIL PSI`{: .mpd}, `XMSN CHIPS`{: .mpd} |
| **Intermediate** and **tail rotor gearboxes** | Vibration, then the tail rotor stops. | `GRBX VIB`{: .mpd} |
| **Main rotor** | Destroyed, it makes no lift. | |
| **Tail rotor** | Destroyed, it makes no anti-torque. | |
| **APU** | Fails. A heavy hit while it runs can start a fire. | `APU FIRE`{: .mpd} |

### Electrical and hydraulic

| Component | When damaged | Shows as |
|---|---|---|
| **Battery** | Stops holding its charge. | `BATTERY`{: .mpd} |
| **Generators** (2) | No AC from that generator. | `GEN1 FAIL`{: .mpd}, `GEN2 FAIL`{: .mpd} |
| **Rectifiers** (2) | No DC from that rectifier. | `RECT1 FAIL`{: .mpd}, `RECT2 FAIL`{: .mpd} |
| **Hydraulic pumps** (primary, utility) | No pressure from that pump. Primary also takes the backup flight control system and the FMC. | `PRI HYD PSI`{: .mpd}, `BUCS FAIL`{: .mpd}, `FMC DISENG`{: .mpd}, `UTIL HYD PSI`{: .mpd} |
| **Hydraulic reservoirs** | Leak, from a weep to empty in about two minutes. | `PRI HYD LVL`{: .mpd}, `UTIL HYD LVL`{: .mpd} |

See [Electrical, APU and hydraulics]({{ '/aircraft/electrical/' | relative_url }}) for what each one feeds.

### Fuel and airframe

| Component | When damaged | Shows as |
|---|---|---|
| **Forward** and **aft cells**, **IAFS** | Leak, up to about 130 lb/h each. | The cell's quantity falling on the FUEL page |
| **External tanks** | Explode when their pylon is hit hard, if they hold more than about 200 lb. | |
| **Stabilator** | Freezes at its current angle instead of following airspeed. The same happens without DC power. | `STAB FAIL`{: .mpd} |

### Mission equipment

| Component | When damaged |
|---|---|
| **TADS DTV**, **TADS FLIR** | That sensor is lost. The sight status shows `TV FAIL`{: .mpd}, or `TADS FAIL`{: .mpd} with both gone. |
| **TADS turret** | The TADS stops moving. |
| **PNVS FLIR**, **PNVS turret** | No night vision picture from the PNVS: `NVS FAIL`{: .mpd}. |
| **Fire control radar** | The radar faults: `FCR FAULT`{: .mpd}. |
| **Gun turret** | The cannon fails. Cooked-off ammunition from an overheated gun does the same. |
| **Pylons** | Hits drain the utility hydraulics, which articulate the pylons. |
| **IR jammer** | No jamming: `IRJAM FAIL`{: .mpd} (US equipment). |

## Repairs

Repairing the aircraft, with ACE, Zeus or a script, restores the systems along with the hitpoints:

- hydraulic fluid, the accumulator and the battery come back full;
- a repaired engine loses its chips, oil pressure, failure and overspeed faults, and can be started again;
- the fire bottles are refilled.

