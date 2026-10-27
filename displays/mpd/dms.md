---
title: DMS pages
lead: The data management pages. Load the mission's points into the aircraft, check the mod's files, and get to the WCA page and the games.
keywords: [dms, dtu, data transfer, load, mission points, ver, version, pbo, mismatch, software]
seats: [PLT, CPG]
redirect_from:
  - /mpd-dms.html
---

Open DMS from the MENU. Its pages share the top row: `T1`{: .vab} **DTU**, `T3`{: .vab} **IBIT** (the [MPD games]({{ '/displays/mpd/games/' | relative_url }})), `T5`{: .vab} **VERS**, and `B6`{: .vab} **WCA** for the [WCA page]({{ '/displays/mpd/wca/' | relative_url }}). `B1`{: .vab} returns to MENU.

The DMS page itself has nothing else on it yet: its **FAULTS** and **ADVISORIES** lists, and **FAULT** and **UTIL**, are not simulated.

## DTU {#dtu}

The data transfer unit page. The right MPD shows it when the aircraft powers up.

| Button | Label | Action |
|---|---|---|
| `L1`{: .vab} | `MASTER LOAD`{: .mpd} | Loads the mission's points into the aircraft. The page shows the load in progress, then complete, after about four seconds. Press `L1`{: .vab} again to return. |

**MASTER LOAD** copies every waypoint, hazard, control measure and target the mission maker placed in the editor ([For mission makers]({{ '/mission/editor/' | relative_url }}#points)) into this aircraft, replacing what it held. The points then appear on the TSD and can be used in routes.

> Load the mission data before you build your routes. A master load replaces the aircraft's points, including any you added yourself.
{: .caution}

The other DTU options (**DATA**, **WEAPONS/SIGHTS**, the right-hand list, **WP**, **SP** and **DP**) are not simulated.

## VER {#ver}

The software versions page lists every PBO of the mod, with the build each one comes from.

- A PBO from the same build as the rest is shown normally.
- A PBO from a different build, or one that is missing, is highlighted, and missing ones show `????????` in place of the build.

Any difference raises the `VERS MISM`{: .mpd} advisory when the aircraft spawns. Opening this page clears it. A mismatch means the mod did not install or update cleanly: verify the files in Steam, or reinstall the release. `B2`{: .vab} and `B3`{: .vab} page through the list.
