---
title: Installation
lead: Required and optional mods, installation from the Steam Workshop or a GitHub release, and verification.
keywords: [install, workshop, dependencies, cba, ace, hatchet, helisim, launcher, requirements]
redirect_from:
  - /mod-Information.html
---

## Requirements {#requirements}

The AH-64D mod requires four other mods. All five must be loaded on every client and on the server.

| Mod | Function |
|---|---|
| [CBA_A3](https://steamcommunity.com/workshop/filedetails/?id=450814997), version 3.16 or later | Addon settings, key bindings and the event system |
| [ACE3](https://steamcommunity.com/workshop/filedetails/?id=463939057) | Laser codes, Hellfire guidance and the rearm framework |
| [Hatchet Interaction Framework](https://steamcommunity.com/workshop/filedetails/?id=2941986336) | The cockpit cursor, for operating switches and buttons |
| [HeliSim Core](https://steamcommunity.com/workshop/filedetails/?id=3806917476), version 1.5.0 or later | The flight model and aircraft systems: engines, electrical, hydraulics, fuel, rotor |
| **AH-64D Apache Longbow** | This mod |

### Optional

| Mod | Function |
|---|---|
| [A3 Thermal Improvement](https://steamcommunity.com/workshop/filedetails/?id=2041057379) | Improved thermal imagery; the TADS FLIR uses its image when loaded |
| [Zeus Enhanced](https://steamcommunity.com/workshop/filedetails/?id=1779063631) | Zeus editing of the aircraft's loadout and pylons |
| RHS, CUP, Pook's SAM Pack, PRACS | Built-in compatibility: their vehicles are classified by the radar and the threat warning receivers. See [Compatibility]({{ '/mission/compatibility/' | relative_url }}) |

## Steam Workshop

1. Subscribe to the [AH-64D Apache Longbow]({{ site.links.steam }}) on the Workshop, and accept the required mods when Steam offers them.
2. Arma 3 launcher – Under **Mods**, select all five mods.
3. Start the game.
{: .steps}

## GitHub releases

Each release on [GitHub]({{ site.links.github }}/releases) is a zip containing `@AH-64D Apache Longbow`.

1. Unzip the release outside the Arma installation folder.
2. Launcher – **Mods → … → Add watched folder** (or **Add local mod**), and select the unzipped folder.
3. Install the four required mods separately; the launcher does not resolve dependencies for a local mod.
{: .steps}

> Development builds from the source repository can be incomplete; Workshop or GitHub releases are used for normal operation.
{: .note}

## Verification

1. Eden editor – Open on any map.
2. Place the **AH-64D BLOCK I** from **BLUFOR → AH-64D Official Project → Helicopters**.
3. Set the player as pilot; **Play Scenario**.
4. The introduction pop-up is displayed on first entry. The cockpit is dark with the battery off; the aircraft starts cold.
{: .steps}

If the aircraft is not listed in the editor, a required mod is not loaded. If cockpit controls do not respond, the Hatchet Interaction Framework is not loaded or its **Interact** binding is not set; see [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}).

## Multiplayer

Every client and the server require the same versions of all five mods.

The aircraft verifies its own files when spawned. If its PBOs are not all from the same build (an incomplete update, files from two versions, a missing PBO), the `VERS MISM`{: .mpd} advisory is displayed and the [VERS page]({{ '/displays/mpd/dms/' | relative_url }}#ver) lists the affected PBOs. The files are verified in Steam, or the release is reinstalled.
