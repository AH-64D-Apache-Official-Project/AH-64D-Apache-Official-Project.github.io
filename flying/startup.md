---
title: Start-up
lead: From cold and dark to rotors turning at 101%. Click a step to tick it off; your progress is remembered on this device.
keywords: [startup, start, apu, battery, engine, power lever, idle, fly, rotor brake, cold start, checklist]
seats: [PLT]
redirect_from:
  - /startup.html
---

The engines, APU and battery are worked from the **pilot's** left console. The CPG cannot start the aircraft. Panel locations are shown on the [cockpit tour]({{ '/aircraft/cockpit/' | relative_url }}).

## Before you start

- Wear the **IHADSS** helmet. The *AH-64D Pilot* unit has it. Without it the monocle cannot be fitted and the head-aimed sights fall back to the aircraft's nose.
- Close the canopy. An open door shows the `CANOPY`{: .mpd} advisory.
- Ground crew, chocks and covers are not modelled. Make sure nothing is parked under the rotor disc.

## Checklist

1. **Rotor brake** switch: **OFF**. It steps OFF → BRK → LOCK → OFF. With the brake set, the power levers will not go to FLY.
2. **MSTR IGN** switch: **BATT**. The UFD comes on. The MPDs stay dark until the APU is running.
3. **HDU**: fit the monocle from its stowage on the right side of the cockpit. See [IHADSS]({{ '/displays/ihadss/' | relative_url }}).
4. **APU** pushbutton: press. The UFD shows `APU START`{: .mpd}, then `APU PWR ON`{: .mpd}, then `APU ON`{: .mpd} when it is ready to start engines. The MPDs come on: ENG on the left, the DTU page on the right.
5. **ENG 1 START** switch: **START**. The switch springs back; the `ENG1 START`{: .mpd} advisory shows while the starter turns.
6. Watch **Ng** on the [ENG page]({{ '/displays/mpd/eng/' | relative_url }}). Above **23%**, move the **engine 1 power lever** to **IDLE**. Fuel is introduced and the engine lights off.
7. The starter drops out at 52% Ng. Let Ng settle at about **68%**, idle.
8. Repeat steps 5 to 7 for **engine 2**.
9. **Power levers**: **FLY**. With both engines at idle, moving either lever to FLY takes both. Nr comes up to **101%**.
10. **APU** pushbutton: press to shut the APU down once both engines are at FLY. Left running in flight, it raises the `APU ON`{: .mpd} caution.
11. Check the UFD and the [WCA page]({{ '/displays/mpd/wca/' | relative_url }}): no warnings, no cautions.
{: .steps}

> Fuel only reaches the engine once Ng passes 23%. A power lever moved to IDLE sooner does nothing until then: the starter alone turns the engine to about 25%, and it lights off at 23%. If a start goes wrong, set that engine's start switch to **IGN ORIDE** (or click it again while it is starting) to abort, and put the lever back to **OFF**. Leave the switch at IGN ORIDE for a while: the starter keeps turning the engine and cools it. A hot engine restarted too soon starts hot. See [Engines and rotor]({{ '/aircraft/engines/' | relative_url }}#hot-starts).
{: .caution}

## After start

- **Lights**: set the exterior and cockpit lights for the time of day. See [Lighting]({{ '/aircraft/lighting/' | relative_url }}).
- **NVS mode** switch, at night: **NORM** to put the night vision sensor's picture on your monocle. See [Night vision]({{ '/targeting/nvs/' | relative_url }}).
- **Displays**: set up your MPDs, typically TSD on one and FLT or WPN on the other.
- **ASE**: on the ASE page, RLWR on, chaff to ARM, and the IR jammer or MWS on. They all start off. See [Survivability]({{ '/weapons/ase/' | relative_url }}).
- **Weapons**: the armament panel's **ARM/SAFE** and **GND ORIDE** buttons. On the ground, weapons cannot be actioned until ground override is on. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}).

## Locked-rotor start

You may start the engines with the rotor brake at **LOCK**, for example to warm up with the rotor still. The engines run at IDLE and the rotor stays locked. The `RTR BRK ON/LK`{: .mpd} caution is held off for the whole start; release the brake before going to FLY.
