---
title: Emergency procedures
lead: What to do when a warning or caution comes up. Short checklists, with the detail on the pages they link to.
keywords: [emergency, fire, engine failure, single engine, dual engine, autorotation, hydraulics, emer hyd, low rotor, high rotor, generator, chips, jettison]
seats: [PLT, CPG]
---

Warnings are red, cautions yellow. Every message, and what raises it, is listed on the [WCA page]({{ '/displays/mpd/wca/' | relative_url }}). Acknowledge **MASTER WARNING** or **MASTER CAUTION** to silence it, then deal with the cause.

For most warnings, the [ENG page]({{ '/displays/mpd/eng/' | relative_url }}#emergency-format) also shows the immediate action steps in its lower half. The checklists below go further.

> In every emergency: **fly the aircraft first.** Keep the rotor in the green, keep away from the ground, then work the checklist.
{: .warning}

## Engine fire {#fire}

`ENGINE 1 FIRE`{: .mpd}, `ENGINE 2 FIRE`{: .mpd} or `APU FIRE`{: .mpd}, with a voice warning and the fire handle lit red.

1. **Confirm which side.** Check the lit fire handle, or the WCA page.
2. **Fire handle** for that engine or the APU: press to **arm**. Fuel to it is shut off; that engine runs down.
3. **PRI**: press to discharge the primary bottle.
4. If the fire still burns, **RES**: discharge the reserve bottle.
5. Engine fire: continue as for a [single engine failure](#engine-failure). APU fire on the ground: shut down.
{: .steps}

Arm the handle **before** discharging: a bottle only reaches a fire whose handle is already armed. Each bottle can fail, one time in four, which is why there are two. A fire that is not put out usually burns itself out within half a minute or so once the engine is shut down, doing damage until it does. See [Fire protection]({{ '/aircraft/fire/' | relative_url }}).

## Single engine failure {#engine-failure}

`ENG1 OUT`{: .mpd} or `ENG2 OUT`{: .mpd}. The other engine picks up the load and the aircraft is now single-engine: its limits change. See [single-engine limits]({{ '/flying/flight-model/' | relative_url }}#limits).

1. **Collective**: lower it as needed to keep **Nr at 95% or more**. A heavy aircraft on a hot day may not hold a hover on one engine.
2. **Airspeed**: in a hover or low and slow, gain forward speed if you can. Forward flight needs less power than hovering. Aim for at least **VSSE**, velocity safe single engine, shown on the [PERF page]({{ '/displays/mpd/perf/' | relative_url }}).
3. **Torque**: keep the good engine at or below 110%. Up to 122% is allowed for 2.5 minutes, up to 125% for 6 seconds.
4. **Failed engine power lever**: **OFF**.
5. **Weight**: if you cannot hold height, jettison stores with {% include key.html id="fza_ah64_collectiveEmergJett" %}.
6. **Land** as soon as practical. Plan a running landing if you cannot hover.
{: .steps}

Do not try to restart an engine that failed from damage. A tripped or fire-damaged engine cannot be restarted until the aircraft is repaired.

## Chips or low oil pressure

`ENG1 CHIPS`{: .mpd}, `ENG1 OIL PSI`{: .mpd} (or engine 2): the engine is damaged and will get worse.

1. Reduce power on that engine as far as the flight allows.
2. Land as soon as practical, before it fails. An engine that fails from oil starvation may catch fire.
{: .steps}

`GRBX`, `XMSN` and `GRBX VIB` cautions mean the drivetrain is damaged. Land as soon as possible: a failed transmission takes the rotors, generators and hydraulic pumps with it, and a failed tail gearbox stops the tail rotor. See [Engines and rotor]({{ '/aircraft/engines/' | relative_url }}#drivetrain).

## Dual engine failure

Both engines out: the rotor is your only source of energy.

1. **Collective: down, immediately.** Every second of delay costs rotor speed you cannot get back.
2. **Nr**: hold it in the green, 95% to 105%, with the collective.
3. Fly at a moderate forward speed towards the best landing area in reach.
4. Near the ground, **flare** with aft cyclic to slow down and cushion the descent, then level the aircraft.
5. As the aircraft settles, **raise the collective** to cushion the touchdown.
{: .steps}

## Rotor speed

| Warning | Cause | Action |
|---|---|---|
| `LOW RTR`{: .mpd} | Nr below 95% in the air: too much collective for the power available. | Lower the collective. |
| `HIGH RTR`{: .mpd} | Nr 106% or more: too little load, often in a descent or flare. | Raise the collective, reduce the descent rate. |

## Hydraulics

| Message | Action |
|---|---|
| `PRI HYD PSI`{: .mpd} / `PRI HYD LVL`{: .mpd} | The utility system still powers the flight controls. If the primary pump has failed, `BUCS FAIL`{: .mpd} and `FMC DISENG`{: .mpd} follow: fly without the hold modes. Land as soon as practical. |
| `UTIL HYD PSI`{: .mpd} / `UTIL HYD LVL`{: .mpd} | Gun and rocket pylons are lost (`GUN FAIL`{: .mpd}, **PYLON ERROR**). The primary system keeps the flight controls. Land as soon as practical. |
| `HYD FAIL`{: .mpd} | Both pumps failed. Press **EMER HYD** for about a minute and a half of control from the accumulator, and land at once. |
| `TAIL RTR`{: .mpd} | Tail rotor control lost. Land as soon as possible. |

See [Hydraulics]({{ '/aircraft/electrical/' | relative_url }}#hydraulics) and [Emergency hydraulics]({{ '/aircraft/electrical/' | relative_url }}#emergency-hydraulics).

## Electrical

One generator or rectifier carries the whole load, so `GEN1 FAIL`{: .mpd} or `RECT1 FAIL`{: .mpd} on its own needs no action beyond landing when convenient. With both of a pair failed you lose AC or DC systems: the MPDs, IHADSS, radar, sights or countermeasures, depending on which. See [What needs what]({{ '/aircraft/electrical/' | relative_url }}#what-needs-what).

## Fuel

`FWD FUEL LO`{: .mpd} or `AFT FUEL LO`{: .mpd}: one cell is low. Check the [FUEL page]({{ '/displays/mpd/fuel/' | relative_url }}). If the other cell has fuel, crossfeed to feed both engines from it, or transfer fuel across. If both are low, land.

## Flight controls

| Caution | Action |
|---|---|
| `FMC DISENG`{: .mpd} | The hold modes and stability augmentation are lost. Check the [UTIL page]({{ '/displays/mpd/util/' | relative_url }}) for a channel switched off; otherwise fly by hand and land as soon as practical. |
| `STAB FAIL`{: .mpd} | The stabilator is damaged. Expect pitch changes with speed and power; slow down and land as soon as practical. |
