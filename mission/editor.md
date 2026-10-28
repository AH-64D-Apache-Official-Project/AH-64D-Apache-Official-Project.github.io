---
title: For mission makers
lead: How to set up Apache missions in the editor. Navigation points, the aircraft's own options, crews and the server settings that matter.
keywords: [mission, editor, eden, zeus, logic entity, dms, waypoint, hazard, control measure, target, threat, point index, ident, free text, server, settings, crew]
redirect_from:
  - /logicentities.html
---

## Navigation points {#points}

The aircraft's DMS points (waypoints, hazards, control measures and targets) can be placed in the editor as logic entities. In Eden open **Systems** (<kbd>F5</kbd>) → **Logic Entities** → **AH-64D DMS**:

| Entity | Point type | Point Index |
|---|---|---|
| **DMS Waypoint / Hazard** | Waypoint or hazard, by ident | 1 to 50 |
| **DMS Control Measure** | Control measure | 51 to 99 |
| **DMS Target / Threat** | Target or threat | 1 to 50 |

Each has three attributes:

| Attribute | |
|---|---|
| **Point Index** | The point's number. A new entity takes the next free number of its type. Waypoints and hazards share the numbers 1 to 50. Two entities of the same type with the same number clash: only one is kept. A number outside its type's range is rejected with an `Invalid index` error. |
| **Point Ident** | The two-letter code that sets the icon, chosen from a list with each icon shown. The list holds only idents that suit the entity: see [Idents]({{ '/mission/points/' | relative_url }}#idents). |
| **Point Free Text** | Up to three characters drawn beside the icon, such as `HLD` or a callsign. |

The point takes the entity's position and height.

The points are mission data, not loaded into any aircraft automatically. Crews load them with **MASTER LOAD** on the [DTU page]({{ '/displays/mpd/dms/' | relative_url }}#dtu), which replaces whatever the aircraft held. Tell your players to do it, or brief them on the point numbers so they can build their routes.

> Number your waypoints in the order you want them flown. Players build routes by typing point numbers on the KU, so W01, W02, W03 is far quicker than a scattered list.
{: .tip}

## The aircraft

Place the **AH-64D BLOCK I** from **BLUFOR → AH-64D Official Project → Helicopters**. Its options are covered on [Variants and customisation]({{ '/aircraft/variants/' | relative_url }}):

- **Appearance**: livery, radar, British mission equipment, IAFS or 1,200-round magazine.
- **Attributes**: tail number, a loadout from the [mission planner]({{ '/mission/planner/' | relative_url }}) as JSON, and the pylons with their presets.

The aircraft always starts cold and dark: battery off, rotor stopped. Allow your crews time to [start up]({{ '/flying/startup/' | relative_url }}), a few minutes with practice.

## Crews

Use the **AH-64D Pilot** unit (**BLUFOR → AH-64D Official Project → Men**), or give your own pilots the **IHADSS** helmet. Without it the crew has no helmet display and no head-aimed sights. See [Crew stations]({{ '/aircraft/crew/' | relative_url }}).

The aircraft is built for two players. With an AI or empty CPG seat, the TADS is pointed by the pilot's acquisition source and the pilot fires the weapons.

## Rearming and refuelling

Set up a way for crews to change loadouts: an ACE ammo source, a fuel source, or the mission planner's settings. See [Rearm and refuel]({{ '/mission/rearm/' | relative_url }}).

## Server settings

Set these in **Addon Options → Server** (or the mission's settings) so every player gets the same:

| Setting | Effect |
|---|---|
| **Mission Planner → Rearm Mode** | How long applying a planner loadout takes: instant, 30 seconds, or ACE's rearm times. |
| **Mission Planner → No Ammo Source Required** / **No Fuel Source Required** | Whether the planner needs an ammo truck or fuel source nearby. Turn both off for a realistic FARP. |
| **Animations → Air Data Probe** and **Rotor Swashplate** | Cosmetic. Turn off on busy servers if needed. |

HeliSim's flight-model options are client settings; players choose their own. See [Addon settings]({{ '/getting-started/settings/' | relative_url }}).

## Zeus

With [Zeus Enhanced](https://steamcommunity.com/workshop/filedetails/?id=1779063631) a Zeus can change the Apache's pylons and loadout from the Zeus interface.

## Other mods

Units from RHS, CUP, Pook's SAM Pack and PRACS are recognised by the radar and the warning receivers. See [Compatibility]({{ '/mission/compatibility/' | relative_url }}).
