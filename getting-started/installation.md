---
title: Installation
lead: What you need, how to load it, and how to check it is working.
keywords: [install, workshop, dependencies, cba, ace, hatchet, helisim, launcher, requirements]
redirect_from:
  - /mod-Information.html
---

## Requirements {#requirements}

The Apache is one mod that leans on four others. All five must be loaded, on every client and on the server.

| Mod | Why it is needed |
|---|---|
| [CBA_A3](https://steamcommunity.com/workshop/filedetails/?id=450814997), version 3.16 or later | Addon settings, key bindings and the event system. |
| [ACE3](https://steamcommunity.com/workshop/filedetails/?id=463939057) | Laser codes, Hellfire guidance and the rearm framework. |
| [Hatchet Interaction Framework](https://steamcommunity.com/workshop/filedetails/?id=2941986336) | The cockpit cursor: it is what lets you click switches and buttons. |
| [HeliSim Core](https://steamcommunity.com/workshop/filedetails/?id=3806917476), version 1.4.2 or later | The flight model and the aircraft systems: engines, electrics, hydraulics, fuel, rotor. |
| **AH-64D Apache Longbow** | This mod. |

### Optional

| Mod | What it adds |
|---|---|
| [A3 Thermal Improvement](https://steamcommunity.com/workshop/filedetails/?id=2041057379) | Better thermal imagery. The TADS FLIR uses its picture when it is loaded. |
| [Zeus Enhanced](https://steamcommunity.com/workshop/filedetails/?id=1779063631) | Lets a Zeus edit the Apache's loadout and pylons. |
| RHS, CUP, Pook's SAM Pack, PRACS | Compatibility patches are built in: their vehicles are classified correctly on the radar and the threat warning receivers. See [Compatibility]({{ '/mission/compatibility/' | relative_url }}). |

## Steam Workshop

1. Subscribe to the [AH-64D Apache Longbow]({{ site.links.steam }}) on the Workshop. Steam offers to subscribe to the required mods as well; accept.
2. Open the Arma 3 launcher. Under **Mods**, make sure all five mods are ticked.
3. Start the game.
{: .steps}

## GitHub releases

Each release on [GitHub]({{ site.links.github }}/releases) is a zip containing `@AH-64D Apache Longbow`.

1. Unzip it anywhere outside the Arma install folder.
2. In the launcher, **Mods → … → Add watched folder** (or **Add local mod**) and point it at the unzipped folder.
3. Subscribe to or install the four required mods yourself. The launcher cannot fetch dependencies for a local mod.
{: .steps}

> Building from the source repository is for developers. Development builds can be incomplete or broken; play on a Workshop or GitHub release.
{: .note}

## Check it is working

1. Open the editor (**Eden**) on any map.
2. Place the **AH-64D BLOCK I** from **BLUFOR → AH-64D Official Project → Helicopters**.
3. Set yourself as the pilot and press **Play Scenario**.
4. A welcome pop-up appears the first time you get in. The cockpit should be dark with the battery off: that is correct, the aircraft starts cold.
{: .steps}

If the aircraft is missing from the editor, a required mod is not loaded. If you get in and nothing in the cockpit responds to clicks, the Hatchet Interaction Framework is missing or its **Interact** key is not bound; see [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}).

## Multiplayer

Every player and the server need the same versions of all five mods.

The aircraft also checks its own files when it spawns. If its PBOs do not all come from the same build (an update that did not finish, files mixed from two versions, a PBO missing), you get a `VERS MISM`{: .mpd} advisory, and the [VER page]({{ '/displays/mpd/dms/' | relative_url }}#ver) lists which ones. Verify the files in Steam or reinstall the release.
