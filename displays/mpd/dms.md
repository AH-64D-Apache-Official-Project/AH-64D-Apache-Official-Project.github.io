---
title: Data management (DMS) pages
lead: The DTU page, which loads mission data into the aircraft, and the VERS page, which verifies the mod's software versions.
keywords: [dms, dtu, data transfer, load, mission points, ver, version, pbo, mismatch, software]
seats: [PLT, CPG]
redirect_from:
  - /mpd-dms.html
---

DMS is selected from the MENU page. The DMS pages have the same page buttons: `T1`{: .vab} DTU, `T3`{: .vab} IBIT (the [MPD games]({{ '/displays/mpd/games/' | relative_url }}), a mod feature), `T5`{: .vab} VERS, and `B6`{: .vab} WCA for the [WCA page]({{ '/displays/mpd/wca/' | relative_url }}). `B1`{: .vab} returns to the MENU page.

The DMS FAULTS and ADVISORIES lists, FAULT and UTIL are not simulated.

## DTU {#dtu}

The data transfer unit page. The right MPD displays it at power-up.

| Button | Label | Function |
|---|---|---|
| `L1`{: .vab} | `MASTER LOAD`{: .mpd} | Loads the mission data, and any DTC, into the aircraft. The page displays the load in progress, then complete after approximately four seconds. `L1`{: .vab} again returns. |

MASTER LOAD performs the following, in order:

1. Copies every waypoint, hazard, control measure and target placed in the editor ([Mission editor]({{ '/mission/editor/' | relative_url }}#points)) into the aircraft, replacing the points held.
2. If a DTC has been uploaded to the aircraft from the [mission planner]({{ '/mission/planner/' | relative_url }}#dtc) for the current map, loads it over the mission data: its lines, areas and zones, and its points and routes. A DTC with no points of a type, or no routes, leaves the mission's data in place.
{: .steps}

The points are then displayed on the TSD and available for routes.

> MASTER LOAD replaces the aircraft's points, including points added in the cockpit. Mission data is loaded before routes are built.
{: .note}

DATA, WEAPONS/SIGHTS, the right-hand list, WP, SP and DP are not simulated.

## VERS {#ver}

The version page (mod feature) lists every PBO of the mod with its build.

- A PBO from the same build as the rest is displayed normally.
- A PBO from a different build, or a missing PBO, is highlighted; a missing PBO displays `????????` in place of the build.

Any difference raises the `VERS MISM`{: .mpd} advisory when the aircraft is spawned; selecting this page clears it. A mismatch indicates the mod is not installed or updated correctly: the files are verified in Steam, or the release is reinstalled. `B2`{: .vab} and `B3`{: .vab} page through the list.
