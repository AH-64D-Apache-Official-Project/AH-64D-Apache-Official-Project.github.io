---
title: Mission editor
lead: Setting up AH-64D missions in the editor — navigation points, aircraft options, crews and server settings.
keywords: [mission, editor, eden, zeus, logic entity, dms, waypoint, hazard, control measure, target, threat, point index, ident, free text, server, settings, crew]
redirect_from:
  - /logicentities.html
---

## Navigation points {#points}

The aircraft's DMS points (waypoints, hazards, control measures and targets) are placed in the editor as logic entities, under **Systems** (<kbd>F5</kbd>) → **Logic Entities** → **AH-64D DMS**:

| Entity | Point type | Point Index |
|---|---|---|
| DMS Waypoint / Hazard | Waypoint or hazard, by ident | 1 to 50 |
| DMS Control Measure | Control measure | 51 to 99 |
| DMS Target / Threat | Target or threat | 1 to 50 |

Each entity has three attributes:

| Attribute | |
|---|---|
| Point Index | The point number. A new entity takes the next free number of its type. Waypoints and hazards share the numbers 1 to 50. Two entities of the same type with the same number conflict; only one is kept. A number outside the type's range is rejected with an `Invalid index` error. |
| Point Ident | The two-letter code that sets the symbol, selected from a list showing each symbol. The list contains only idents valid for the entity; see [Idents]({{ '/mission/points/' | relative_url }}#idents). |
| Point Free Text | Up to three characters displayed beside the symbol, such as `HLD` or a callsign. |

The point takes the entity's position and height.

The points are mission data and are not loaded into an aircraft automatically. The crew loads them with MASTER LOAD on the [DTU page]({{ '/displays/mpd/dms/' | relative_url }}#dtu), which replaces the points the aircraft holds.

Lines, engagement areas, zones and routes cannot be placed in the editor. They are built as a [DTC]({{ '/mission/planner/' | relative_url }}#dtc) in the mission planner, and MASTER LOAD loads the DTC over the mission points. A DTC pushed to the mission from the planner's DTC manager is available to every crew.

> Waypoints numbered in the order they are to be flown (W01, W02, W03) allow routes to be built quickly on the KU.
{: .note}

## Aircraft

The **AH-64D BLOCK I** is placed from **BLUFOR → AH-64D Official Project → Helicopters**. Its options are described in [Variants and configuration]({{ '/aircraft/variants/' | relative_url }}):

- **Appearance**: livery, radar, British mission equipment, IAFS or 1,200-round magazine.
- **Attributes**: tail number, a loadout from the [mission planner]({{ '/mission/planner/' | relative_url }}) in JSON, and the pylons with their presets.

The aircraft starts cold: battery off, rotor stopped. The mission allows time for [start-up]({{ '/flying/startup/' | relative_url }}).

## Crews

Crews use the **AH-64D Pilot** unit (**BLUFOR → AH-64D Official Project → Men**), or other units with the **IHADSS** helmet. Without it there is no HMD symbology and no HMD sight. See [Crew stations]({{ '/aircraft/crew/' | relative_url }}).

The aircraft is designed for two players. With the CPG crew station empty or AI, the pilot's acquisition source points the TADS and the pilot fires the weapons.

## Rearming and refueling

Loadout changes require an ACE ammunition source, a fuel source, or the mission planner settings. See [Rearm and refuel]({{ '/mission/rearm/' | relative_url }}).

## Server settings

Set in **Addon Options → Server** (or the mission settings) so that every player has the same values:

| Setting | Effect |
|---|---|
| Mission Planner → Rearm Mode | Time to apply a planner loadout: instant, 30 seconds, or ACE rearm times |
| Mission Planner → No Ammo Source Required / No Fuel Source Required | Whether the planner requires an ammunition or fuel source nearby. Both off requires a FARP. |
| Animations → Air Data Probe and Rotor Swashplate | Cosmetic; can be disabled on busy servers |

The HeliSim flight model options are client settings. See [Addon settings]({{ '/getting-started/settings/' | relative_url }}).

## Zeus

With [Zeus Enhanced](https://steamcommunity.com/workshop/filedetails/?id=1779063631), Zeus can change the aircraft's pylons and loadout from the Zeus interface.

## Other mods

Units from RHS, CUP, Pook's SAM Pack and PRACS are classified by the radar and the warning receivers. See [Compatibility]({{ '/mission/compatibility/' | relative_url }}).
