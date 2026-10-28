---
title: Engines and rotor
lead: Two turboshaft engines drive the rotors through nose gearboxes and the main transmission. How they start, how they are governed, and how they fail.
keywords: [engine, turboshaft, ng, np, nr, tgt, torque, power lever, idle, fly, governor, start, hot start, abort, overspeed, chips, oil, transmission, gearbox, rotor brake, drivetrain]
seats: [PLT]
---

## The numbers you watch

| Reading | What it is | Normal in flight |
|---|---|---|
| **Ng** | Gas generator speed: how hard the engine core is working. | Rises and falls with power. About 68% at idle. |
| **TGT** | Turbine gas temperature. | Below 810 °C. |
| **Np** | Power turbine speed: the shaft that drives the rotor. | 101% |
| **Nr** | Main rotor speed. | 101% |
| **TQ** | Torque from each engine, percent. | Matched between engines, below 100%. |

All five are on the [ENG page]({{ '/displays/mpd/eng/' | relative_url }}). Torque is also on the FLT page and the IHADSS.

## Power levers

Each engine has its own power lever with three detents: **OFF**, **IDLE** and **FLY**. At **FLY** the engine control unit governs Np, and therefore the rotor, at 101%: raise the collective and it adds fuel to hold the speed, lower it and it takes fuel away. Moving a lever from IDLE to FLY takes about eight seconds of travel; the rotor follows.

With both engines at IDLE, moving either lever to **FLY** moves both. To bring one engine up on its own, the other must be OFF or already at FLY. The levers cannot go to FLY while the rotor brake is on.

## Starting

The starters are air turbines. They need bleed air from the APU, or from the other engine once its lever is at FLY.

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

Running outside a limit is counted, not just shown. The aircraft allows a set time in each band, then damages the engine, the nose gearboxes or the transmission. The bands are on the [HeliSim flight model]({{ '/flying/flight-model/' | relative_url }}#limits) page.

| Exceeded | Damages |
|---|---|
| TGT, Ng, Np | That engine |
| Torque, both engines | The main transmission |
| Torque, one engine | That engine's nose gearbox |

The engines also protect themselves. The governor holds TGT at 867 °C (896 °C on one engine). A mechanical limiter shuts the engine down at 110% Ng, and an electrical trip does the same at about 120% Np. A tripped engine cannot be restarted until the aircraft is repaired. `ENG1 OVSP`{: .mpd} / `ENG2 OVSP`{: .mpd} warns of Np at 115% or more.

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

## Drivetrain

| Part | Carries | When damaged |
|---|---|---|
| **Nose gearboxes** (one per engine) | Each engine's torque into the transmission. | `GRBX1 OIL PSI`{: .mpd}, then `GRBX1 CHIPS`{: .mpd}. A damaged one slips, so its engine's torque jumps about. If it comes apart, its engine overspeeds. |
| **Main transmission** | Both engines to the main rotor, the tail drive and the accessories. | `XMSN1 OIL PSI`{: .mpd}, `XMSN2 OIL PSI`{: .mpd}, then `XMSN CHIPS`{: .mpd}. If it fails, it takes the rotors, generators and hydraulic pumps with it. |
| **Intermediate** and **tail rotor gearboxes** | The tail rotor. | `GRBX VIB`{: .mpd}. If either fails, the tail rotor stops turning. |

## Rotor brake

The rotor brake switch steps **OFF → BRK → LOCK → OFF**.

- **BRK** slows the rotor to a stop, in well under a minute, but only once Nr is below 50%.
- **LOCK** holds the stopped rotor.
- With the brake on, the power levers will not go to FLY, and moving one off OFF raises the `RTR BRK ON/LK`{: .mpd} caution. With both levers at OFF it is only the `RTR BRK ON`{: .mpd} advisory.

You can start the engines with the rotor locked, to warm them up without turning the rotor. Release the brake before going to FLY. See [Start-up]({{ '/flying/startup/' | relative_url }}#locked-rotor-start).
