---
title: Variants and configuration
lead: The configuration options of the AH-64D Block I in the mod — fire control radar, mission equipment, IAFS or 1,200-round magazine, livery, tail number and pylon loadout — and where each is set.
keywords: [variants, fcr, longbow, radar, british, uk, us, mission equipment, iafs, robbie, 1200, magazine, livery, skin, texture, tail number, garage, pylons, preset]
---

The mod adds one aircraft, the **AH-64D BLOCK I**, under **BLUFOR → AH-64D Official Project → Helicopters**. It seats a pilot (rear crew station) and a copilot/gunner (front crew station), plus two passengers. Its configuration is set in the editor, in the field, or in the [mission planner]({{ '/mission/planner/' | relative_url }}).

## Configuration options

| Option | Default | Effect |
|---|---|---|
| Fire control radar | Not installed | The radar on the mast. Without it there is no [FCR]({{ '/targeting/fcr/' | relative_url }}) sight, no FCR page and no radar-guided Hellfire targeting. Adds weight. |
| Mission equipment | US | **US**: IR jammer and chaff. **British**: flares, missile warning system and chaff; no IR jammer. See [Survivability]({{ '/weapons/ase/' | relative_url }}). |
| IAFS or 1,200-round magazine | IAFS | The IAFS installs a 663 lb fuel cell in the ammunition bay and limits the gun to 300 rounds. The 1,200-round magazine replaces it, with no auxiliary fuel. |
| Livery | Default | Fifteen schemes; see below. |
| Tail number | None | Up to five digits on the tail. |
| Pylons | Rockets outboard, Hellfires inboard | The load on each of the four wing stations. See [Rearm and refuel]({{ '/mission/rearm/' | relative_url }}). |

## In the editor

### Appearance

**Edit Vehicle Appearance** (right-click on the aircraft) sets components and livery.

![Arma's appearance editor with the Apache's liveries listed](/images/screenshots/garageSystem.jpg)

- **Components**: **Mount FCR (Fire Control Radar)**, **Mount British Mission Equipment** and **Swap IAFS for 1200rnd magazine**. Selecting British mission equipment also installs the radar.
- **Liveries**: Default, Default Weathered, 229th ARB (and weathered), 1/211th ARB "The Air Pirates" Utah National Guard (and weathered), United Kingdom Army Air Corps (and weathered), United Kingdom Army Air Corps Special Forces, RNLAF 301 Squadron Q-09, RNLAF 301 Squadron Demo Team, Indian Air Force, Israeli Air Force (IAF Saraf), Shield (Marvel) and Kane's Wrath.

### Attributes

| Attribute | Function |
|---|---|
| Tail number | Up to five digits. A space leaves a position blank; characters other than 0–9 are left blank. |
| Loadout Config | A complete loadout in JSON (radar, IAFS, fuel and pylons), applied at mission start. Left empty unless a loadout is supplied. |
| Pylons | The Arma pylon editor, with the presets **Combat Support**, **Combat Support (FCR)**, **Heavy Attack**, **Heavy Attack (FCR)**, **COIN** and **Empty**. |

![The pylon editor, showing which slot is which rocket zone or missile rail](/images/screenshots/pylonMenu.jpg)

Each wing station has four slots, which are filled in order. A station is drawn from its first slot; every rocket zone on a station must hold the same rocket type; rockets and Hellfires cannot be mixed on one station.

## In the field

With ACE loaded, ground crew can reconfigure the aircraft between sorties. Each task requires a **Toolkit** in the player's inventory and the part within 10 m, and takes five minutes.

| ACE action | Requires | Result |
|---|---|---|
| Attach Fire Control Radar | An **AH-64 Fire Control Radar** crate | The radar is installed and the crate is consumed. |
| Detach Fire Control Radar | | The radar is removed as a crate. |
| Attach 1200 30mm Magazine | An **AH-64 1200 Magazine** crate | The IAFS is removed (carried by the player) and the gun is loaded with 1,200 rounds. |
| Attach Internal Auxiliary Fuel System | An **AH-64 IAFS** crate | The magazine is removed and the IAFS installed, with 300 rounds. |

The crates are in the editor under **Props → AH-64 Parts**. They can be dragged, carried and loaded as ACE cargo.

**Set Tail Numbers**, at the tail, changes the five digits individually. **Open/Close Pilot Door** and **Open/Close Gunner Door** operate the canopy from outside.

> The [mission planner]({{ '/mission/planner/' | relative_url }}) sets the radar, mission equipment, IAFS, fuel, pylons and tail number from one screen, and displays the resulting weight and performance before the configuration is applied.
{: .note}
