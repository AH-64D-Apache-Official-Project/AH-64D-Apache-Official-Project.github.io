---
title: Engines and rotor
lead: Two turboshaft engines drive the rotors through nose gearboxes and the main transmission. How they start, how they are governed, and how they fail.
keywords: [engine, turboshaft, t700, 701c, ng, np, nr, tgt, torque, oil, power lever, idle, fly, dec, governor, start, hot start, abort, overspeed, tgt limiter, droop, chips, transmission, gearbox, nose gearbox, rotor brake, drive train]
seats: [PLT]
---

## The engines

The AH-64D is powered by two General Electric **T700-GE-701C** turboshaft engines. Each engine has four sections:

| Section | Contains |
|---|---|
| **Cold** | The inlet and the compressor. |
| **Hot** | The combustion section. |
| **Power turbine** | The turbine that turns the energy from the hot section into shaft power, which turns the rotor. |
| **Accessory** | The engine's support components: oil and fuel pumps, air turbine starter, hydromechanical unit (HMU), alternator and others. |

## The numbers you watch

| Reading | What it is | Normal in flight |
|---|---|---|
| **Ng** | Gas generator speed: how hard the engine core is working. | Rises and falls with power. About 68% at idle. |
| **TGT** | Turbine gas temperature. | Below 810 °C. |
| **Np** | Power turbine speed: the shaft that drives the rotor. | 101% |
| **Nr** | Main rotor speed. | 101% |
| **TQ** | Torque from each engine, percent. | Matched between engines, below 100%. |
| **Oil** | Engine oil pressure, psi. | 23 to 120 psi. |

All are on the [ENG page]({{ '/displays/mpd/eng/' | relative_url }}), oil pressure only in its ground format. Torque is also on the FLT page and the IHADSS.

The torque, TGT, Np and Ng readings are colour coded:

- **Green**: within the normal operating range.
- **Yellow**: a cautionary, time-limited range. A timer counts down the time allowed; when it runs out, the engine or drive train starts taking damage.
- **Red**: past the maximum, or below the minimum needed to operate. Red above a maximum means damage is being done.

The limits themselves, and how long each range allows, are on the [HeliSim flight model]({{ '/flying/flight-model/' | relative_url }}#limits) page.

## Power levers

Each engine has its own power lever, on the pilot's power lever quadrant, with three detents: **OFF**, **IDLE** and **FLY**. At **FLY** the engine's digital electronic control (DEC) governs Np, and therefore the rotor, at 101%: raise the collective and it adds fuel to hold the speed, lower it and it takes fuel away. Moving a lever from IDLE to FLY takes about eight seconds of travel; the rotor follows.

With both engines at IDLE, moving either lever to **FLY** moves both. To bring one engine up on its own, the other must be OFF or already at FLY. The levers cannot go to FLY while the rotor brake is on.

## Starting

The starters are air turbines. They need pneumatic air from the APU, or bleed air from the other engine once its lever is at FLY.

1. Set the start switch to **START**. The `ENG1 START`{: .mpd} advisory shows and Ng begins to climb.
2. Above **23% Ng**, move the power lever to **IDLE**. Fuel is introduced and the engine lights off.
3. At **52% Ng** the starter drops out, and the engine accelerates on its own to idle, about 68%.
{: .steps}

The [start-up checklist]({{ '/flying/startup/' | relative_url }}) puts it all in order.

### Hot starts

Watch TGT during the start. Above **851 °C** while starting is a hot start, and it damages the engine for as long as it lasts. The usual cause is **restarting a hot engine**: heat left in the engine from its last run makes the next start peak hotter. Before moving the lever to IDLE, let TGT come down below about 80 °C. Holding the start switch at **IGN ORIDE** with the lever at OFF turns the engine on the starter without fuel, which cools it faster.

Moving the lever to IDLE before 23% Ng does no harm: fuel is only introduced at 23%, which the starter reaches on its own.

To **abort** a start, set the start switch to **IGN ORIDE**, or click it again while the engine is starting, and bring the power lever back to OFF. IGN ORIDE stays where you put it and keeps the starter turning the engine, cooling it. Return the switch to OFF before trying again.

## Limits and damage

Running outside a limit is counted, not just shown. The aircraft allows a set time in each range, then damages the engine, the nose gearboxes or the transmission. The ranges are on the [HeliSim flight model]({{ '/flying/flight-model/' | relative_url }}#limits) page.

| Exceeded | Damages |
|---|---|
| TGT, Ng, Np | That engine |
| Torque, dual engine | The main transmission |
| Torque, single engine | That engine's nose gearbox |

### Engine protection

- **TGT limiter.** The DEC stops feeding the engine more fuel at **867 °C** dual engine, or **896 °C** single engine. At the limit TGT stops rising, but no more power reaches the rotor either: pull more collective and the rotor slows down, or "droops".
- **Ng overspeed.** A mechanical overspeed protection shuts the engine down at **110% Ng**.
- **Np overspeed.** An electrical overspeed protection shuts the engine down at **119.6% Np**. `ENG1 OVSP`{: .mpd} / `ENG2 OVSP`{: .mpd} warns of Np at 115% or more, before it trips.

An engine shut down by its overspeed protection cannot be restarted until the aircraft is repaired.

### How an engine fails

Engine damage gets worse in steps, whether it comes from enemy fire or from exceeding limits:

| Engine damage | What you see |
|---|---|
| Light | Nothing yet. Past a quarter, the damage slowly worsens by itself while the engine runs. |
| Half | `ENG1 CHIPS`{: .mpd}: metal in the oil. |
| Heavier | Oil pressure starts to fall, then falls faster: `ENG1 OIL PSI`{: .mpd}. |
| Severe | No oil pressure. The engine starves, and wears out faster the harder you run it. |
| Destroyed | The engine fails: `ENG1 OUT`{: .mpd}. An engine that fails from oil starvation may catch fire. |

Once you see chips or low oil pressure, the engine is on borrowed time. Reduce power on it, plan to land, and see [Emergency procedures]({{ '/flying/emergency/' | relative_url }}).

## Drive train

| Part | Carries | When damaged |
|---|---|---|
| **Nose gearboxes** (one per engine) | Each engine's torque into the main transmission. | `GRBX1 OIL PSI`{: .mpd}, then `GRBX1 CHIPS`{: .mpd}. A damaged one slips, so its engine's torque jumps about. |
| **Main transmission** | Both engines to the main rotor, the tail rotor drive and the accessory section. | `XMSN1 OIL PSI`{: .mpd}, `XMSN2 OIL PSI`{: .mpd}, then `XMSN CHIPS`{: .mpd}. |
| **Intermediate** and **tail rotor gearboxes** | The tail rotor. | `GRBX VIB`{: .mpd}. |

Each message in these sequences means more severe damage than the one before it.

### Main transmission

Torque limits are exceeded on the main transmission when operating **dual engine**. As it is damaged, the transmission warns of its impending failure with `XMSN1 OIL PSI`{: .mpd}, then `XMSN2 OIL PSI`{: .mpd}, then `XMSN CHIPS`{: .mpd}. Once `XMSN CHIPS`{: .mpd} shows, land immediately, before the transmission fails.

A transmission failure is catastrophic: all hydraulic and electrical power, the main rotor and the tail rotor are lost.

### Nose gearboxes

Torque limits are exceeded on a nose gearbox when operating **single engine**. As it is damaged, the gearbox warns of its impending failure with `GRBX1 OIL PSI`{: .mpd}, then `GRBX1 CHIPS`{: .mpd} (or gearbox 2). Once `GRBX1 CHIPS`{: .mpd} shows, land immediately, before the gearbox fails.

When a nose gearbox fails, its engine loses its load. The engine accelerates to maximum power, trips its Np or Ng overspeed protection and shuts down. On one engine that leaves you with none: enter an [autorotation]({{ '/flying/emergency/' | relative_url }}#dual-engine-failure).

### Tail rotor gearboxes

The tail rotor has two gearboxes: the **intermediate** gearbox and the **tail rotor gearbox** itself. Critical damage to either shows the `GRBX VIB`{: .mpd} caution, warning of an impending failure. If either fails, the tail rotor stops turning and its thrust is lost. See [Gearbox vibration]({{ '/flying/emergency/' | relative_url }}#gearbox-vibration).

## Rotor brake

The rotor brake slows the rotor to a stop after shutdown, and locks it, for example in high winds. It starts in the OFF position. The rotor brake switch steps **OFF → BRK → LOCK → OFF**.

- **BRK** slows the rotor to a stop, in well under a minute, but only once Nr is below 50%.
- **LOCK** holds the stopped rotor.
- With the brake on, the power levers will not go to FLY, and moving one off OFF raises the `RTR BRK ON/LK`{: .mpd} caution. With both levers at OFF it is only the `RTR BRK ON`{: .mpd} advisory.

You can start the engines with the rotor locked, to warm them up without turning the rotor. Release the brake before going to FLY. See [Start-up]({{ '/flying/startup/' | relative_url }}#locked-rotor-start).
