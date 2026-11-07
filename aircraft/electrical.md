---
title: Electrical, APU and hydraulics
lead: Where the aircraft's power comes from, what each system needs, and what you lose when part of it fails.
keywords: [electrical, battery, apu, generator, transformer rectifier, tru, rectifier, ac, dc, bus, hydraulics, primary, utility, accumulator, emer hyd, emergency hydraulics, pneumatic, bleed air, accessory section, transmission, power]
seats: [PLT]
---

## How power flows

The generators and hydraulic pumps are all mounted on the **accessory section of the main transmission**. Whatever turns the accessory section powers the aircraft.

- **During start**, the APU turns the accessory section through the **APU drive shaft** (the No. 7 drive shaft).
- **With one or both engines running**, the engines turn it through the nose gearboxes and the main transmission. As the power levers are advanced to FLY, the APU disengages at about **95% Nr** and the engines take over the accessory section.
- **With both engines out**, the rotor keeps turning the transmission in an autorotation, and the accessory section with it, for as long as Nr holds up.

In short:

- **APU** (start) or **main transmission** (engines, rotor) → **accessory section**
  - above 45% Nr → **hydraulic pumps** → primary and utility hydraulics
  - above 85% Nr → **AC generators** → **AC** → **transformer rectifier units (TRUs)** → **DC**
- **AC** → recharges the **battery** → battery bus
- **APU**, or an engine at FLY → **pneumatic air** → **engine starters**

### Low rotor speed

Because the pumps need much less shaft speed than the generators, a low rotor speed costs you the electrics before it costs you the flight controls.

| Nr | What is lost |
|---|---|
| Below about **85%** | The generators are no longer turning fast enough to make power. Primary AC and DC are lost. Battery bus systems keep working for about 12 minutes, then all electrical power is lost. |
| Below about **45%** | The hydraulic pumps are no longer turning fast enough to make pressure. The flight controls can no longer move the main and tail rotors: control of the aircraft is lost. |

## Battery

The **MSTR IGN** switch, on the pilot's power lever quadrant, puts the battery on its bus. On the battery alone you get the UFD, the fire panel, **ARM/SAFE**, **GND ORIDE**, the master warning and caution buttons, the floodlights and the searchlight. The MPDs stay dark until there is AC.

The battery lasts about **12 minutes** without a generator, and below a quarter of its charge it cannot hold the bus up. It recharges from AC. A damaged battery shows the `BATTERY`{: .mpd} advisory.

## APU

The APU starts the engines, and powers the aircraft on the ground through the accessory section. It is started by the **utility hydraulic accumulator**, and needs:

- the **APU** pushbutton, on the pilot's power lever quadrant, pressed;
- **battery** power;
- at least **2,600 psi** in the accumulator;
- fuel in the **aft** cell. The APU draws fuel from the aft cell only, at 175 lb/h.

### APU start

1. Press the **APU** pushbutton. The UFD shows `APU START`{: .mpd}, then `APU PWR ON`{: .mpd}.
2. `ACCUM PSI`{: .mpd} appears: the accumulator has discharged all its available pressure to turn the APU over.
3. `ACCUM PSI`{: .mpd} clears during the start: the APU is turning the hydraulic pumps, and they have recharged the accumulator to 3,000 psi.
4. `APU ON`{: .mpd} shows once the APU is up to speed, about five seconds after the button was pressed.
{: .steps}

### What the APU provides

Through the accessory section, the APU provides electrical and hydraulic power. It also provides all the aircraft's pneumatic air, which turns the engine starters. It keeps providing electrical and hydraulic power until about **95% Nr**, when the engines are turning the accessory section.

> The mod has one pneumatic supply: the APU, or any engine with its power lever at FLY. An engine at FLY can start the other with its bleed air. The separate high- and low-pressure air sources of the real aircraft, and the integrated pressurized air system (IPAS) they feed, are not simulated.
{: .note}

### APU shutdown

The APU stops when:

- the **APU** pushbutton is pressed again: `APU STOP`{: .mpd} shows on the UFD;
- the **APU FIRE pushbutton** on the fire panel is pressed, which shuts off its fuel;
- the aft cell runs dry (fuel starvation);
- it loses battery power.

If it stops for any reason but the APU pushbutton, the pushbutton pops out. Press it again to restart. Left running in flight, the APU raises the `APU ON`{: .mpd} caution.

## Generators and TRUs

The aircraft has two **AC generators** and two **transformer rectifier units (TRUs)**. The generators are on the accessory section and provide power once it is turning above **85% Nr**.

AC flows from the generators, through the high power switching modules (HPSMs, not simulated), into the TRUs, and returns to the HPSMs as DC. A single generator and a single TRU can power the whole aircraft.

The UFD tells you when one of these components fails:

| UFD | Cause | Result |
|---|---|---|
| `GEN1 FAIL`{: .mpd} / `GEN2 FAIL`{: .mpd} | That generator has failed. | The other generator carries the whole AC load. With **both** failed there is no AC, and so no DC either: only the battery bus is left, for about 12 minutes. |
| `RECT1 FAIL`{: .mpd} / `RECT2 FAIL`{: .mpd} | That TRU has failed. | The other TRU carries the whole DC load. With **both** failed there is no DC. AC systems keep working, and the battery keeps charging. |
| `BATTERY`{: .mpd} | The battery is damaged. | See [Damage and failures]({{ '/aircraft/damage/' | relative_url }}). |

### What needs what

| Needs | Systems |
|---|---|
| Battery bus | UFD, fire detection and extinguishing, armament and caution pushbuttons, emergency jettison, floodlights, searchlight. |
| AC | MPDs and the VIDEO page, the TADS as a sensor, the laser. |
| AC and DC | IHADSS symbology, PNVS, fire control radar, cannon, anti-collision lights. |
| DC | Chaff, flares, IR jammer, radar and laser warning receivers, and the FIRE pushbuttons' fuel shut-off. |

## Hydraulics

The aircraft has two independent hydraulic systems, **primary** and **utility**. Each has its own pump on the accessory section of the main transmission, at 3,000 psi.

| System | Powers |
|---|---|
| **Primary** | The primary side of the flight control servos, and with it the FMC, which can only move the controls on the primary side. BUCS is not simulated beyond its caution. |
| **Utility** | The utility side of the flight control servos, the area weapon system (AWS) turret and ammunition carrier drive, pylon articulation, and the accumulator. The tail wheel unlock is not simulated. |

The [ENG page]({{ '/displays/mpd/eng/' | relative_url }}) shows both pressures and the accumulator.

### Loss of one system

- **Primary**: the utility system keeps the flight controls. The FMC is lost: `BUCS FAIL`{: .mpd} and `FMC DISENG`{: .mpd}.
- **Utility**: the primary system keeps the flight controls. The AWS and pylon articulation are lost.
- A damaged **reservoir** leaks. A light hit weeps, a heavy one empties it in about two minutes. When the fluid goes, the pump loses its prime and the pressure follows: `PRI HYD LVL`{: .mpd} / `UTIL HYD LVL`{: .mpd}, then `PRI HYD PSI`{: .mpd} / `UTIL HYD PSI`{: .mpd}.
- Hits on the gun turret or the pylons also drain the utility system.

### Tail rotor hydraulic failure

With **primary hydraulic pressure low** and **utility hydraulic level low** at the same time, the crew gets the `TAIL RTR`{: .mpd} warning. The tail rotor stays fixed in its last commanded position, and does not respond to pedal input.

### Hydraulic failure

A loss of **both** primary and utility hydraulics is a loss of all control of the aircraft. The crew gets the hydraulic failure voice warning and `HYD FAIL`{: .mpd} on the UFD.

The crew **must immediately** press **EMER HYD** and land the aircraft without delay. See [Emergency hydraulics](#emergency-hydraulics).

## Accumulator

The utility hydraulic accumulator stores utility pressure, 3,000 psi when charged. It provides:

1. **APU start power.** A start needs at least 2,600 psi, and discharges the accumulator down to its 1,650 psi precharge. Once the APU is turning the pumps, they recharge it in a few seconds. At 1,650 psi or below the `ACCUM PSI`{: .mpd} advisory shows, and the APU will not start.
2. <span id="emergency-hydraulics"></span>**Emergency hydraulic power.** With primary and utility pressure both below 1,260 psi, pressing **EMER HYD** in either crew station routes the accumulator's pressure to the utility side of the flight control servos. It gives about **60 seconds** of control. When the accumulator reaches 1,650 psi, all hydraulic power is lost and the accumulator reads 0. Press **EMER HYD** again to turn it off.

> A failed APU start can leave the accumulator discharged with nothing to recharge it. Repairing the aircraft (ACE, Zeus or a script) recharges it.
{: .tip}

## Repairs

Any repair to the airframe tops up the stores: fluid in the reservoirs, the accumulator and the battery. It also clears engine chips, oil and failure faults on a repaired engine. See [Damage and failures]({{ '/aircraft/damage/' | relative_url }}).
