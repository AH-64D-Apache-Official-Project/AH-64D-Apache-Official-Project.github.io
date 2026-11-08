---
title: Rearm and refuel
lead: Changing the aircraft's loadout and fuel in the editor and in the field, and the pylon loading rules.
keywords: [rearm, refuel, pylons, loadout, ace, ammo truck, fuel truck, zeus, farp, countermeasures, chaff, flares, repair]
seats: [PLT, CPG]
---

## Rearm methods

| Location | Method |
|---|---|
| Editor | The aircraft's **Pylons** attribute, with its presets, and the **Loadout Config** attribute. See [Variants and configuration]({{ '/aircraft/variants/' | relative_url }}). |
| Field, with ACE | An ACE ammunition source (ammunition vehicle or container) near the aircraft; ACE interaction with the aircraft opens the ACE pylon screen. |
| Mission planner | The complete loadout and fuel, applied in one action. See [Mission planner]({{ '/mission/planner/' | relative_url }}). |
| Zeus | With Zeus Enhanced, Zeus can edit the pylons. |

The radar, the IAFS and the 1,200-round magazine are installed with ACE actions and parts crates, or in the planner. See [Variants and configuration]({{ '/aircraft/variants/' | relative_url }}#in-the-field).

## Pylon rules {#pylon-rules}

Each of the four wing stations has four slots. A loadout that breaks the following rules is corrected automatically, with a message in system chat:

- The first slot of a station sets its load. With the first slot empty, the station's other slots are cleared.
- A station carries rockets or Hellfires, not both. With Hellfires in the first slot, rockets on that station are removed, and the reverse.
- Wing stores belong to the CPG's weapons. Stores loaded to the pilot's turret are moved to the CPG.

The slots of a rocket station are the launcher zones; see [Hydra 70 rockets]({{ '/weapons/rockets/' | relative_url }}#launchers-and-zones).

## Fuel

The aircraft is refuelled from any ACE fuel source. The [FUEL page]({{ '/displays/mpd/fuel/' | relative_url }}) displays the quantity in each cell. External tanks are loaded on the wing stations as stores.

## Countermeasures

Chaff, and flares on aircraft with British mission equipment, are restocked when a loadout is applied with the mission planner. See [Survivability (ASE)]({{ '/weapons/ase/' | relative_url }}).

## Repairs

Repairing the aircraft (ACE repair, Zeus or a script) also refills the fire extinguisher bottles, the hydraulic reservoirs, the accumulator and the battery, and clears engine chip, oil pressure and failure faults. See [Damage and failures]({{ '/aircraft/damage/' | relative_url }}).
