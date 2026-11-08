---
title: Mission planner
lead: The ground planning screen — loadout, fuel, weight and performance, application, saved loadouts, and the data transfer cartridge (DTC).
keywords: [mission planner, loadout, planning, fuel, weight, performance, rearm, apply, save, pylons, fcr, iafs, dtc]
seats: [PLT, CPG]
---

## Access

The planner is opened with ACE interaction, with the aircraft on the ground and stationary:

- within 15 m of the aircraft: **Interact → Mission Planner**; or
- in the aircraft: **Self-interact → Mission Planner**.

## Configuration tab

The planner opens on **Configuration**, for the aircraft's loadout. The **Waypoint/Hazards**, **Control Measures**, **Target/Threats**, **Areas/Zones**, **Lines** and **Routes** tabs build a [DTC](#dtc). **Communications** is not yet implemented.

The Hatchet cockpit cursor is paused while the planner is open.

| Section | Selection |
|---|---|
| Mission equipment | **US Army** or **UK Army** equipment. See [Variants and configuration]({{ '/aircraft/variants/' | relative_url }}). |
| FCR | Radar installed or not |
| IAFS / Magazine | The IAFS with 300 gun rounds, or the 1,200-round magazine |
| Pylons 1–4 | For each wing station: empty, an **M-261** rocket launcher with a rocket type in each zone, an **M-299** Hellfire launcher with a missile type on each rail, or a 230-gallon external tank |
| Cannon | Rounds, up to 300 or 1,200 |
| Fuel | Gallons in the forward (155), aft (220), center (100, with the IAFS) and external tanks |
| Tail number | The number painted on the tail |

Changing the radar, or exchanging the IAFS and magazine, is marked with a warning: it requires approximately 300 seconds with ACE timings.

## Weight and performance

For the pressure altitude and temperature at the aircraft's location, the planner calculates:

- **Weights**: empty, ammunition, current and maximum gross weight, and the weight that can be jettisoned, with the corresponding torque saving of 1% per 200 lb.
- **Torque**: maximum torque available dual engine (DE) and single engine (SE), continuous DE torque, and the torque to hover in ground effect (IGE) and out of ground effect (OGE). The DE power margin is the continuous torque remaining in an OGE hover; the maximum rate of descent OGE is derived from it.
- **Airspeeds and fuel**: maximum endurance and maximum range true airspeeds, each with its fuel flow; endurance of the fuel loaded at the maximum range fuel flow; and VSSE, current and after a jettison.

These values use the same aircraft data as the [PERF page]({{ '/displays/mpd/perf/' | relative_url }}). A loadout with no power margin is reduced before flight.

## Applying a configuration

**Apply Config** loads the aircraft with the planned configuration. The time required depends on the server's **Rearm Mode** setting ([Addon settings]({{ '/getting-started/settings/' | relative_url }})):

| Mode | Time |
|---|---|
| Instant | None |
| 30 Seconds | 30 seconds for the complete change |
| ACE Settings | ACE rearm times per store; 300 seconds for the radar or the IAFS exchange |

Unless the server allows otherwise, supplies are required nearby:

- **Ammunition, pylons and gun**: an ACE ammunition source within the ACE pylon search distance (15 m by default); its supply is consumed.
- **Fuel**: an ACE fuel source within hose reach (12 m by default); the fuel added is taken from it.

**FARP Status** indicates whether a source is in reach. **Close Without Applying** discards the changes.

## Saved loadouts

A loadout is named and saved with **Save**. Saved loadouts are kept in the player's Arma profile and are available in any mission. **Load** restores one; **Delete** removes it.

**Push to Mission** saves the loadout to the mission instead of the profile, for every player in the mission. It remains until the mission ends, and only the player who pushed it can delete it.

## Data transfer cartridge (DTC) {#dtc}

The DTC carries mission data into the aircraft: points, routes, lines, engagement areas, and priority fire and no fire zones. It is built on the planner's DTC tabs, uploaded to the aircraft, and loaded in the cockpit with MASTER LOAD on the [DTU page]({{ '/displays/mpd/dms/' | relative_url }}#dtu).

### Tabs

| Tab | Contents |
|---|---|
| Waypoint/Hazards | `W01`–`W50` |
| Control Measures | `C51`–`C99` |
| Target/Threats | `T01`–`T50` |
| Areas/Zones | 12 engagement areas, 8 priority fire zones and 8 no fire zones. NF ACTIVE sets MULTI or SINGLE, as on the [ZN page]({{ '/displays/mpd/tsd/' | relative_url }}#zn). |
| Lines | 15 lines: phase (PL), boundary (BL), FLOT, FLET and FSCL |
| Routes | Routes 1 to 10 |

Each tab has its list on the left and an Arma map on the right. The list sets each point's ident, free text (three characters), height above ground and order, or deletes it. A line's ident is its type, up to five characters in total.

### Map

| Action | Result |
|---|---|
| Right-click on an empty position | Adds a waypoint, hazard, control measure, target or threat (with its ident), a line (with its type), or an area, PF zone or NF zone. A new line is 2 km long east–west; an area or zone is a 1 km square. |
| Right-click on a point | Changes its ident, adds it to a route (a route with points is marked with a star), or deletes it |
| Right-click on a line, area or zone | Changes a line's type, inserts a point into a line of fewer than four points, or deletes it |
| Drag a list row onto the map | Places that point or shape |
| Drag a point or a corner | Moves it; a point released next to another snaps to it |
| Drag a line's center handle | Adds a corner |
| Drag, wheel, <kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> | Pan and zoom |
| <kbd>Esc</kbd> | Closes a menu or cancels the current action |

A corner that would make an area's or zone's sides cross is rejected.

On the **Routes** tab, a route is selected, **Add Points** pressed, and points selected on the map, up to 50. **Remove Last** and **Clear** remove them.

> The aircraft flies route 1. The other routes are carried on the DTC but cannot yet be selected on the TSD.
{: .note}

### DTC controls

| Button | Function |
|---|---|
| Name | Up to eight letters or numbers |
| OPEN DTC / SAVE DTC | Opens a saved DTC, or saves the current DTC to the profile |
| Upload to Acft | Uploads the DTC to the aircraft, ready for MASTER LOAD |
| Download from Acft | Opens the data the aircraft holds, to edit or save |
| DTC MANAGER | Saved and mission DTCs. **Push to Mission** shares a DTC with the mission; **Delete** removes one; **Export** and **Import** transfer a DTC as text |
| Clear DTC | Starts a new, empty DTC |

DTCs are saved per map: a save under a name already used on the map replaces it, while the same name on another map is a separate DTC. A DTC loads only into an aircraft on the map it was made for.

### Loading

1. Build the DTC; **Upload to Acft**.
2. DTU page – MASTER LOAD.
{: .steps}

MASTER LOAD loads the mission points first, then the DTC over them. A DTC with no points of a type, or no routes, leaves the mission's data in place.
