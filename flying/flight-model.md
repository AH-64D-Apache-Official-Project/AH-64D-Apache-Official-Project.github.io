---
title: HeliSim flight model
lead: The Apache does not use Arma's helicopter physics. HeliSim simulates the rotor, the engines and the aircraft's systems, and that changes how you fly and what you can break.
keywords: [helisim, flight model, physics, torque, limits, vrs, ground effect, etl, weight, performance, overtorque]
redirect_from:
  - /flight-model-helisim.html
---

HeliSim is a separate mod, [**HeliSim Core**](https://steamcommunity.com/workshop/filedetails/?id=3806917476), by BradMick. The Apache supplies its aircraft data: weights, rotor, engines, transmission, fuel, hydraulics and electrics.

## What it simulates

- **Rotor and airframe.** Lift, drag and power required come from the rotor and the fuselage, wings and stabilator. Weight, altitude and temperature change the power you need. Ground effect, translational lift and vortex ring state come from the rotor model.
- **Engines.** Two turboshaft engines with a gas generator (Ng), a free power turbine (Np) and a turbine temperature (TGT), governed to keep the rotor at 101%. They start, run and fail as engines do: see [Engines and rotor]({{ '/aircraft/engines/' | relative_url }}).
- **Transmission and gearboxes.** Engine torque passes through a nose gearbox on each side into the main transmission. Too much torque damages them.
- **Systems.** Battery, generators and rectifiers, the APU, primary and utility hydraulics with an accumulator, the fuel cells and pumps, and the flight management computer.
- **Weight and balance.** Fuel, ammunition, missiles, rockets, external tanks, the radar and the crew all add mass and move the centre of gravity. As you burn fuel and fire weapons the aircraft gets lighter.

## Limits

Exceeding a limit is not just a warning. HeliSim counts the time spent above each band and damages the engine or drivetrain when the allowance runs out.

### Torque

| Both engines | Allowed |
|---|---|
| Up to 100% | Continuous |
| 100% to 115% | 6 seconds |
| Above 115% | None: damage at once |

| One engine | Allowed |
|---|---|
| Up to 110% | Continuous |
| 110% to 122% | 2.5 minutes |
| 122% to 125% | 6 seconds |
| Above 125% | None: damage at once |

The aircraft counts as single-engine when one engine's torque falls below about half of the other's.

### Rotor speed

| Nr | |
|---|---|
| 95% to 105% | Normal |
| Below 95%, airborne | `LOW RTR`{: .mpd} warning |
| 106% and above | `HIGH RTR`{: .mpd} warning |
| 110% | Maximum |

### Temperature

The engines limit their own TGT to 867 °C, or 896 °C with one engine. TGT above 810 °C is time-limited; keep it there only as long as you need the power.

| TGT, both engines | Allowed |
|---|---|
| Up to 810 °C | Continuous |
| 810 to 870 °C | 30 minutes |
| 870 to 878 °C | 10 minutes |
| Above 878 °C | None: damage at once |

| TGT, one engine | Allowed |
|---|---|
| Up to 810 °C | Continuous |
| 810 to 870 °C | 30 minutes |
| 870 to 878 °C | 10 minutes |
| 878 to 896 °C | 2.5 minutes |
| 896 to 949 °C | 12 seconds |
| Above 949 °C | None: damage at once |

### Engine speeds

| Each engine | Allowed |
|---|---|
| Ng up to 102.2% | Continuous |
| Ng 102.2% to 105.1% | 12 seconds |
| Ng above 105.1% | None: damage at once |
| Np up to 105% | Continuous |
| Np 105% to 121% | 12 seconds |
| Np above 121% | None: damage at once |

Each band's allowance starts again from full whenever you enter it. The [ENG page]({{ '/displays/mpd/eng/' | relative_url }}#timers) shows the time left.

## Weight

| | |
|---|---|
| Empty | 13,920 lb (6,314 kg) |
| Maximum gross | 23,000 lb (10,433 kg) |

A full load of Hellfires, rockets, 1,200 rounds and full fuel is heavy. On a hot day or at altitude you may not be able to hover out of ground effect. The [PERF page]({{ '/displays/mpd/perf/' | relative_url }}) tells you what you can do at your weight in the conditions; the [mission planner]({{ '/mission/planner/' | relative_url }}) does the same before you load the aircraft.

> If you cannot get airborne, or can only hover in ground effect, take fuel or weapons off. The flight model is not broken: the aircraft is too heavy for the day.
{: .tip}

## Environment

The engines and rotor see the base altitude and temperature set in **Aircraft Environmental Settings** ([Addon settings]({{ '/getting-started/settings/' | relative_url }}#helisim)). The **Middle East** and **Central Asia - Summer** settings in particular cost a lot of power. Wind from the mission's weather is included unless a tester has turned it off.

## Vortex ring state

Descending slowly and nearly vertically under power lets the rotor settle into its own downwash. Lift falls away, and adding collective makes it worse. To avoid it, keep forward speed when you descend steeply, and keep the descent rate low below about 20 kt. To recover, move the aircraft out of the column of air: forward or sideways cyclic, then collective once the rotor bites again. Turn on **Enable VRS Warning** in the HeliSim settings for a warning as it develops.
