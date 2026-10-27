---
title: Electrical, APU and hydraulics
lead: Where the aircraft's power comes from, what each system needs, and what you lose when part of it fails.
keywords: [electrical, battery, apu, generator, rectifier, ac, dc, bus, hydraulics, primary, utility, accumulator, emer hyd, emergency hydraulics, bleed air, accessory drive, power]
seats: [PLT]
---

## How power flows

Everything turns off one shaft, the **accessory drive** on the main transmission. Before start-up the APU turns it. Once the rotor is turning, the transmission takes over, and it keeps the accessories turning with the engines dead, in an autorotation.

- **APU** or **rotor** → **accessory drive**
  - from 45% drive → **hydraulic pumps** → primary and utility hydraulics
  - from 85% drive → **generators** → **AC** → **rectifiers** → **DC**
- **AC** → recharges the **battery** → battery bus
- **APU bleed air** → **engine starters** (once one engine is at FLY, its bleed air can start the other)

Because the pumps need much less shaft speed than the generators, a low rotor speed costs you the electrics before it costs you the flight controls.

## Battery

The **MSTR IGN** switch puts the battery on its bus. On the battery alone you get the UFD, the fire panel, **ARM/SAFE**, **GND ORIDE**, the master warning and caution buttons, the floodlights and the searchlight. The MPDs stay dark until there is AC.

The battery runs flat in about 12 minutes without a generator, and below a quarter of its charge it cannot hold the bus up. It recharges from AC. A damaged battery shows the `BATTERY`{: .mpd} advisory.

## APU

The APU starts the engines and powers the aircraft on the ground. To start it needs all four of:

- the **APU** pushbutton pressed,
- battery power,
- fuel in the **aft** cell, which it burns at 175 lb/h,
- pressure in the hydraulic **accumulator**, which turns it over.

The UFD shows `APU START`{: .mpd}, then `APU PWR ON`{: .mpd}, then `APU ON`{: .mpd} once it is up to speed, about five seconds later. It then drives the generators and hydraulic pumps and supplies bleed air for the engine starters. When the rotor reaches 95% it lets go of the drive. Press the button again to stop it (`APU STOP`{: .mpd}).

If the APU runs out of fuel, loses battery power or is shut down by its fire handle, it stops and the pushbutton pops out. Press it again to restart. Left running in the air it raises the `APU ON`{: .mpd} caution.

## Generators and rectifiers

Two generators make AC once the accessory drive is at 85% or more. Two rectifiers turn it into DC. Either generator, and either rectifier, can carry the whole load on its own. A damaged unit shows `GEN1 FAIL`{: .mpd}, `GEN2 FAIL`{: .mpd}, `RECT1 FAIL`{: .mpd} or `RECT2 FAIL`{: .mpd}.

### What needs what

| Needs | Systems |
|---|---|
| Battery bus | UFD, fire detection and extinguishing, armament and caution pushbuttons, emergency jettison, floodlights, searchlight. |
| AC | MPDs and the VIDEO page, the TADS as a sensor, the laser. |
| AC and DC | IHADSS symbology, PNVS, fire control radar, cannon, anti-collision lights. |
| DC | Chaff, flares, IR jammer, radar and laser warning receivers, and the fire handles' fuel shut-off. |

## Hydraulics

Two independent systems, **primary** and **utility**, each at 3,000 psi from its own pump on the accessory drive.

| | Primary | Utility |
|---|---|---|
| Flight controls | Yes | Yes |
| Tail rotor | Pressure | Fluid |
| Gun turret and pylon articulation | | Yes |

- The **flight controls** work while either system has at least 1,260 psi.
- The **tail rotor** is lost only when primary pressure *and* utility fluid are both gone: `TAIL RTR`{: .mpd}.
- A damaged **reservoir** leaks. A light hit weeps, a heavy one empties it in about two minutes. When the fluid goes the pump loses its prime and the pressure follows: `PRI HYD LVL`{: .mpd} / `UTIL HYD LVL`{: .mpd}, then `PRI HYD PSI`{: .mpd} / `UTIL HYD PSI`{: .mpd}.
- Hits on the gun turret or the pylons also drain the utility system.
- With both pumps failed, `HYD FAIL`{: .mpd} is a warning: land as soon as possible.

The [ENG page]({{ '/displays/mpd/eng/' | relative_url }}) shows both pressures and the accumulator.

### Accumulator

The accumulator stores utility pressure, 3,000 psi when charged. It does two jobs:

1. **Starting the APU.** A start needs at least 2,600 psi and spends the charge down to 1,650 psi. As soon as the APU has the pumps turning, they refill it in a few seconds. Below 1,650 psi you get the `ACCUM PSI`{: .mpd} advisory and the APU will not turn over.
2. <span id="emergency-hydraulics"></span>**Emergency hydraulics.** **EMER HYD** puts the accumulator's pressure on the flight controls through the utility system, for about a minute and a half. It is your last chance to get the aircraft down after losing both pumps. Press it again to turn it off.

> A failed APU start can leave the accumulator empty with nothing to recharge it. Repairing the aircraft (ACE, Zeus or a script) refills it.
{: .tip}

## Repairs

Any repair to the airframe tops up the stores: fluid in the reservoirs, the accumulator and the battery. It also clears engine chips, oil and failure faults on a repaired engine. See [Damage and failures]({{ '/aircraft/damage/' | relative_url }}).
