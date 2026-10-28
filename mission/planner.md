---
title: Mission planner
lead: A planning screen for the aircraft on the ground. Build a loadout, set the fuel, see what the aircraft will weigh and how it will perform, then apply it.
keywords: [mission planner, loadout, planning, fuel, weight, performance, rearm, apply, save, pylons, fcr, iafs]
seats: [PLT, CPG]
---

## Opening it

Use ACE interaction:

- standing within 15 m of the aircraft: **Interact → Mission Planner**, or
- sitting in the aircraft: **Self-interact → Mission Planner**.

The aircraft must be on the ground and stopped.

## The configuration tab

The planner opens on **Configuration**, the working part of the tool. The other tabs (Waypoint/Hazards, Control Measures, Target/Threats, Areas/Zones, Lines, Communications) are placeholders for later.

| Section | What you set |
|---|---|
| **Mission equipment** | **US Army** or **UK Army** equipment. See [Variants and customisation]({{ '/aircraft/variants/' | relative_url }}). |
| **FCR** | Radar fitted or not. |
| **IAFS / Magazine** | The internal auxiliary fuel tank with 300 cannon rounds, or the 1,200-round magazine. |
| **Pylons 1–4** | For each wing station: nothing, an **M-261** rocket pod with a rocket type in each zone, an **M-299** Hellfire launcher with a missile type on each rail, or a 230-gallon external tank. |
| **Cannon** | Rounds, up to 300 or 1,200. |
| **Fuel** | Gallons in the forward (155), aft (220), centre (100, with the IAFS) and external tanks. |
| **Tail number** | The number painted on the tail. |

Changing the radar or swapping the IAFS and magazine is marked with a warning: it is a long job, about 300 seconds with ACE timings.

## Weight and performance

As you build the loadout the planner works out, for the pressure altitude and temperature where you are:

- **Weights**: empty, ammunition, fuel, the gross weight and the maximum, and how much you could jettison.
- **Hover torque** in and out of ground effect, maximum continuous torque, and maximum torque on both engines and one.
- **Power margin**, **maximum gross weight**, **maximum range** and **endurance**, and the maximum rate of descent out of ground effect.

These come from the same aircraft data as the [PERF page]({{ '/displays/mpd/perf/' | relative_url }}). If the loadout leaves no power margin, take something off before you fly.

## Applying it

**Apply Config** loads the aircraft with what you planned. How long it takes depends on the server's **Rearm Mode** setting ([Addon settings]({{ '/getting-started/settings/' | relative_url }})):

| Mode | Time |
|---|---|
| **Instant** | None. |
| **30 Seconds** | 30 seconds for the whole change. |
| **ACE Settings** | ACE's rearm times for each store; 300 seconds for the radar or the IAFS swap. |

Unless the server allows otherwise, you need supplies close by:

- **Ammunition, pylons and the cannon**: an ACE ammo source within ACE's pylon search distance (15 m by default). Its supply is used up as you load.
- **Fuel**: an ACE fuel source within hose reach (12 m by default). Fuel added is taken from it.

**FARP Status** on the screen shows whether a source is in reach. **Close Without Applying** discards your changes.

## Saving loadouts

Give a loadout a name and **Save** it. Saved loadouts are kept in your Arma profile, so they are there next time, on any mission. **Load** puts one back on the screen; **Delete** removes it.

**Push to Mission** saves the loadout under the mission instead of your profile, for everyone in the mission to load. It lasts until the mission ends, and only the player who pushed it can delete it.

The **DTC** box is a work in progress: its buttons are disabled.
