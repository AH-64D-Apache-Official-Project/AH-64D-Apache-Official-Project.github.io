---
title: Rearm and refuel
lead: The ways to change the Apache's loadout and fuel, in the editor and in the field, and the rules the pylons follow.
keywords: [rearm, refuel, pylons, loadout, ace, ammo truck, fuel truck, zeus, farp, countermeasures, chaff, flares, repair]
seats: [PLT, CPG]
---

## The ways to rearm

| Where | How |
|---|---|
| **Editor** | The aircraft's **Pylons** attribute, with its presets, and the **Loadout Config** attribute. See [Variants and customisation]({{ '/aircraft/variants/' | relative_url }}). |
| **In the field, with ACE** | Bring an ACE ammo source (an ammo truck or ammunition container) near the aircraft and ACE-interact with the aircraft to open ACE's pylon screen. |
| **Mission planner** | Plan the whole loadout and fuel and apply it in one go. See [Mission planner]({{ '/mission/planner/' | relative_url }}). |
| **Zeus** | With Zeus Enhanced, Zeus can edit the pylons. |

The radar, the IAFS and the 1,200-round magazine are fitted with ACE actions and parts crates, or in the planner. See [Variants and customisation]({{ '/aircraft/variants/' | relative_url }}#in-the-field).

## Pylon rules

Each of the four wing stations has four slots. The aircraft corrects a loadout that breaks these rules, with a message in system chat:

- The **first slot** of a station sets what it carries. With it empty, the station's other slots are cleared.
- A station carries **rockets or Hellfires, not both**. With Hellfires in the first slot, any rockets on that station are removed, and the other way round.
- The stores belong to the **CPG's** weapons. Stores loaded to the pilot's turret are moved to the CPG.

A rocket station's slots are the pod's zones; see [Hydra 70 rockets]({{ '/weapons/rockets/' | relative_url }}#pods-and-zones).

## Fuel

Refuel with any ACE fuel source. The [FUEL page]({{ '/displays/mpd/fuel/' | relative_url }}) shows what each cell holds. External tanks are hung on the wing stations like any other store.

## Countermeasures

Chaff, and flares on aircraft with UK mission equipment, are restocked when a loadout is applied with the mission planner. See [Survivability (ASE)]({{ '/weapons/ase/' | relative_url }}).

## Repairs

Repairing the aircraft (ACE repair, Zeus or a script) also refills the fire extinguisher bottles, the hydraulic reservoirs, the accumulator and the battery, and clears engine chip, oil and failure faults. See [Damage and failures]({{ '/aircraft/damage/' | relative_url }}).
