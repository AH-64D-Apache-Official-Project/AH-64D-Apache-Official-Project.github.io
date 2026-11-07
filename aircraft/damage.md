---
title: Damage and failures
lead: The Apache is not one health bar. Each system has its own hitpoint, and losing one takes away what it does, often before anything shows on the outside.
keywords: [damage, hitpoints, failure, repair, battle damage, systems, engine, rotor, hydraulics, sensors, ace, zeus, g, g-stress, overstress, fatigue, blade, tail boom, stabilator, vertical fin]
seats: [PLT, CPG]
---

Most components fail outright at heavy damage. Some, the engines, gearboxes, transmission and hydraulic reservoirs, warn you first and get worse in steps. The [WCA page]({{ '/displays/mpd/wca/' | relative_url }}) and the UFD tell you what has been hit.

## What each hit costs you

### Powerplant and drive train

| Component | When damaged | Shows as |
|---|---|---|
| **Engines** (2) | Worsen in steps to chips, low oil pressure, oil starvation and failure. A heavy hit on a running engine can start a fire. See [Engines and rotor]({{ '/aircraft/engines/' | relative_url }}#how-an-engine-fails). | `ENG1 CHIPS`{: .mpd}, `ENG1 OIL PSI`{: .mpd}, `ENG1 OUT`{: .mpd} |
| **Nose gearboxes** (2) | Low oil pressure, then chips; a damaged one slips. If one fails, its engine overspeeds and its overspeed protection shuts it down. | `GRBX1 OIL PSI`{: .mpd}, `GRBX1 CHIPS`{: .mpd} |
| **Main transmission** | Low oil pressure, then chips. If it fails it takes all hydraulic and electrical power, and the main and tail rotors, with it. | `XMSN1 OIL PSI`{: .mpd}, `XMSN2 OIL PSI`{: .mpd}, `XMSN CHIPS`{: .mpd} |
| **Intermediate** and **tail rotor gearboxes** | Vibration, then the tail rotor stops. | `GRBX VIB`{: .mpd} |
| **Main rotor** | Destroyed, it makes no lift. | |
| **Tail rotor** | Destroyed, it makes no anti-torque. | |
| **APU** | Fails. A heavy hit while it runs can start a fire. | `APU FIRE`{: .mpd} |

### Electrical and hydraulic

| Component | When damaged | Shows as |
|---|---|---|
| **Battery** | Stops holding its charge. | `BATTERY`{: .mpd} |
| **Generators** (2) | No AC from that generator. | `GEN1 FAIL`{: .mpd}, `GEN2 FAIL`{: .mpd} |
| **Transformer rectifier units** (TRUs, 2) | No DC from that TRU. | `RECT1 FAIL`{: .mpd}, `RECT2 FAIL`{: .mpd} |
| **Hydraulic pumps** (primary, utility) | No pressure from that pump. Primary also takes BUCS and the FMC. | `PRI HYD PSI`{: .mpd}, `BUCS FAIL`{: .mpd}, `FMC DISENG`{: .mpd}, `UTIL HYD PSI`{: .mpd} |
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
| **Pylons** | Hits drain the utility hydraulics, which power pylon articulation. |
| **IR jammer** | No jamming: `IRJAM FAIL`{: .mpd} (US equipment). |

## Overstress {#overstress}

Pulling more than **3.5 g** fatigues the airframe. The more g, the faster: there are steps at 3.5, 4, 4.5, 5 and 6 g, and the fatigue builds faster as it grows. It never goes away in flight; only a full repair resets it. Fatigue builds only in the air.

| Fatigue | Lost |
|---|---|
| 60% | The **stabilator**. |
| 75% | The **vertical fin**, and the tail rotor with it. |
| 90% | The **tail boom**, with the fin, the stabilator and the tail rotor. The centre of gravity moves well forward. |

Held at 4 g, the stabilator goes in about 40 seconds; at 5 g, in about 5. Lost parts disappear from the aircraft.

Fatigue also damages the **main rotor blades**. As it builds, each pull risks a blade going out of track, losing its tip cap, snapping its pitch change link, or coming off altogether; the worse the fatigue, the worse the failure. A blade that comes off leaves the rotor out of balance: it shakes the transmission on its mounts, damaging it and throwing more blades, until the transmission fails and takes the rotor with it.

## Repairs

Repairing the aircraft, with ACE, Zeus or a script, restores the systems along with the hitpoints:

- hydraulic fluid, the accumulator and the battery come back full;
- a repaired engine loses its chips, oil pressure, failure and overspeed faults, and can be started again;
- the fire bottles are refilled;
- a full repair also resets the [overstress](#overstress) fatigue and puts lost tail parts and rotor blades back.

