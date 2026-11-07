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

The planner opens on **Configuration**, for the aircraft's loadout. The **Waypoint/Hazards**, **Control Measures**, **Target/Threats**, **Areas/Zones**, **Lines** and **Routes** tabs build a [DTC](#dtc). **Communications** is a placeholder for later.

While the planner is open, the Hatchet cockpit cursor is paused.

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

- **Weights**: empty, ammunition, the current and maximum gross weight, and how much you could jettison, with the torque that would save: 1% for every 200 lb.
- **Torque**: maximum torque available dual engine (DE) and single engine (SE), continuous DE torque, and the torque to hover in ground effect (IGE) and out of it (OGE). The DE power margin is the continuous torque left over in an OGE hover; the maximum rate of descent OGE is worked out from it.
- **Airspeeds and fuel**: the maximum endurance and maximum range airspeeds, in knots true airspeed, each with its fuel flow; how long the fuel loaded lasts at the maximum range fuel flow; and VSSE, velocity safe single engine, now and after a jettison.

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

## The DTC {#dtc}

A **DTC**, data transfer cartridge, carries your mission data into the aircraft: points, routes, lines, engagement areas and priority fire and no fire zones. You build it on the planner's DTC tabs, upload it to the aircraft, and load it in the cockpit with **MASTER LOAD** on the [DTU page]({{ '/displays/mpd/dms/' | relative_url }}#dtu).

### The tabs

| Tab | Holds |
|---|---|
| **Waypoint/Hazards** | `W01`–`W50`. |
| **Control Measures** | `C51`–`C99`. |
| **Target/Threats** | `T01`–`T50`. |
| **Areas/Zones** | 12 engagement areas, 8 priority fire zones and 8 no fire zones. **NF ACTIVE** sets MULTI or SINGLE, as on the [ZN page]({{ '/displays/mpd/tsd/' | relative_url }}#zn). |
| **Lines** | 15 lines: phase (PL), boundary (BL), FLOT, FLET and FSCL. |
| **Routes** | Routes 1 to 10. |

Each tab has its list on the left and an Arma map on the right. In the lists you set each point's ident, free text (three characters) and height above the ground, move it up or down, or delete it. A line's ident is its kind and up to five characters in all.

### The map

| Do | To |
|---|---|
| Right-click an empty spot | Add a waypoint, hazard, control measure, target or threat there (choosing its ident), a line (choosing its kind), or an area, PF zone or NF zone. A new line is 2 km long east to west, an area or zone a box 1 km square. |
| Right-click a point | Change its ident, add it to a route (a route with points is starred), or delete it. |
| Right-click a line, area or zone | Change a line's kind, insert a point into a line of fewer than four, or delete it. |
| Drag a list row onto the map | Place that point or shape there. |
| Drag a point or a corner | Move it. A point let go next to another snaps onto it. |
| Drag a line's middle handle | Add a corner there. |
| Drag the map, wheel, <kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> | Pan and zoom. |
| <kbd>Esc</kbd> | Close a menu, or stop what you are doing. |

A corner that would make an area's or zone's sides cross is refused.

On the **Routes** tab, pick a route, press **Add Points** and click points on the map to add them, up to 50. **Remove Last** and **Clear** take them off again.

> The aircraft flies **route 1**. The other routes are carried on the DTC, but the TSD cannot select them yet.
{: .note}

### The DTC box

| Button | Does |
|---|---|
| **Name** | Up to eight letters or numbers. |
| **OPEN DTC** / **SAVE DTC** | Opens a saved DTC, or saves this one to your profile. |
| **Upload to Acft** | Puts the DTC in the aircraft, ready for MASTER LOAD. |
| **Download from Acft** | Opens what the aircraft holds now, to edit or save. |
| **DTC MANAGER** | Your saved DTCs and the mission's. **Push to Mission** shares one with everyone in the mission; **Delete** removes one; **Export** and **Import** copy a DTC as text, to pass on outside the game. |
| **Clear DTC** | Starts a new, empty DTC. |

DTCs are saved per map: saving under a name already used on this map replaces that save, while the same name on another map is a separate DTC. A DTC only loads into an aircraft on the map it was made for.

### Loading it

1. Build the DTC and press **Upload to Acft**.
2. In the cockpit, press **MASTER LOAD** on the DTU page.
{: .steps}

MASTER LOAD loads the mission's points first, then the DTC over them. A DTC with no points of a type, or no routes, leaves the mission's in place.
