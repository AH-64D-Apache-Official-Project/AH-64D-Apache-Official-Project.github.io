---
title: Emergency procedures
lead: What to do when a warning or caution comes up. Short checklists, with the detail on the pages they link to.
keywords: [emergency, fire, engine failure, single engine, dual engine, autorotation, hydraulics, emer hyd, tail rotor, low rotor, high rotor, generator, tru, chips, transmission, gearbox, grbx vib, jettison]
seats: [PLT, CPG]
---

Warnings are red, cautions yellow. Every message, and what raises it, is listed on the [WCA page]({{ '/displays/mpd/wca/' | relative_url }}). Acknowledge **MASTER WARNING** or **MASTER CAUTION** to silence it, then deal with the cause.

For most warnings, the [ENG page]({{ '/displays/mpd/eng/' | relative_url }}#emergency-format) also shows the immediate action steps in its lower half. The checklists below go further.

> In every emergency: **fly the aircraft first.** Keep the rotor in the green, keep away from the ground, then work the checklist.
{: .warning}

## Engine fire {#fire}

`ENGINE 1 FIRE`{: .mpd}, `ENGINE 2 FIRE`{: .mpd} or `APU FIRE`{: .mpd}, with a voice warning and the FIRE pushbutton lit red.

1. **Confirm which side.** Check the lit FIRE pushbutton, or the WCA page.
2. **FIRE pushbutton** for that engine or the APU: press to **arm**. Fuel to it is shut off; that engine runs down.
3. **PRI**: press to discharge the primary bottle.
4. If the fire still burns, **RES**: discharge the reserve bottle.
5. Engine fire: continue as for a [single engine failure](#engine-failure). APU fire on the ground: shut down.
{: .steps}

Arm the FIRE pushbutton **before** discharging: a bottle only reaches a fire whose pushbutton is already armed. Each bottle can fail, one time in four, which is why there are two. A fire that is not put out usually burns itself out within half a minute or so once the engine is shut down, doing damage until it does. See [Fire protection]({{ '/aircraft/fire/' | relative_url }}).

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

## Transmission and nose gearboxes

`XMSN1 OIL PSI`{: .mpd}, `XMSN2 OIL PSI`{: .mpd} and `XMSN CHIPS`{: .mpd} mean the main transmission is damaged, usually from exceeding the dual engine torque limits. `GRBX1 OIL PSI`{: .mpd} and `GRBX1 CHIPS`{: .mpd} (or gearbox 2) mean a nose gearbox is damaged, usually from exceeding the single engine torque limits. Each message is more severe than the one before it.

1. **Torque**: reduce it, back inside its limits.
2. **Land as soon as possible.** Once `XMSN CHIPS`{: .mpd} or a `GRBX CHIPS`{: .mpd} shows, land **immediately**, before it fails.
{: .steps}

A transmission failure is catastrophic: all hydraulic and electrical power, the main rotor and the tail rotor are lost. A nose gearbox failure overspeeds its engine until the engine's overspeed protection shuts it down; on one engine, that means an [autorotation](#dual-engine-failure). See [Drive train]({{ '/aircraft/engines/' | relative_url }}#drive-train).

## Gearbox vibration

`GRBX VIB`{: .mpd}: the intermediate or tail rotor gearbox is critically damaged, and the tail rotor may stop turning.

1. **Airspeed**: accelerate above **100 kt**, and be prepared for a loss of tail rotor thrust.
2. **Land**, staying above 100 kt all the way to touchdown, so the aircraft does not spin about its yaw axis if the tail rotor fails.
{: .steps}

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
| `UTIL HYD PSI`{: .mpd} / `UTIL HYD LVL`{: .mpd} | The AWS and pylon articulation are lost (`GUN FAIL`{: .mpd}, **PYLON ERROR**). The primary system keeps the flight controls. Land as soon as practical. |
| `HYD FAIL`{: .mpd} | Primary and utility hydraulics both lost: all control of the aircraft is lost. **Immediately** press **EMER HYD**, in either crew station, and land without delay. The accumulator gives about 60 seconds of control. |
| `TAIL RTR`{: .mpd} | Primary pressure and utility fluid both lost. The tail rotor stays fixed in its last commanded position and does not answer the pedals. Land as soon as possible. |

See [Hydraulics]({{ '/aircraft/electrical/' | relative_url }}#hydraulics) and [Emergency hydraulics]({{ '/aircraft/electrical/' | relative_url }}#emergency-hydraulics).

## Electrical

A single generator and a single TRU carry the whole load, so `GEN1 FAIL`{: .mpd} or `RECT1 FAIL`{: .mpd} on its own needs no action beyond landing when convenient. With both of a pair failed you lose AC or DC systems: the MPDs, IHADSS, radar, sights or countermeasures, depending on which. With both generators failed, the battery bus lasts about 12 minutes. See [What needs what]({{ '/aircraft/electrical/' | relative_url }}#what-needs-what).

## Fuel

`FWD FUEL LO`{: .mpd} or `AFT FUEL LO`{: .mpd}: one cell is low. Check the [FUEL page]({{ '/displays/mpd/fuel/' | relative_url }}). If the other cell has fuel, crossfeed to feed both engines from it, or transfer fuel across. If both are low, land.

## Flight controls

| Caution | Action |
|---|---|
| `FMC DISENG`{: .mpd} | The hold modes and stability augmentation are lost. Check the [UTIL page]({{ '/displays/mpd/util/' | relative_url }}) for a channel switched off; otherwise fly by hand and land as soon as practical. |
| `STAB FAIL`{: .mpd} | The stabilator is damaged. Expect pitch changes with speed and power; slow down and land as soon as practical. |
