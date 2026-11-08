---
title: Crew stations
lead: The pilot's and copilot/gunner's crew stations, their functions, and which functions are aircraft common or crewstation independent.
keywords: [crew, pilot, cpg, copilot, gunner, seat, front seat, back seat, multiplayer, take controls, plt]
seats: [PLT, CPG]
---

## Crew station functions

| | Pilot `PLT`{: .seat .seat-plt} | Copilot/gunner `CPG`{: .seat .seat-cpg} |
|---|---|---|
| Crew station | Rear | Front |
| Arma role | Driver | Gunner (copilot) |
| Flight controls | Yes | When given control (Arma **Take Controls**) |
| Engine start and shutdown | Yes | No; the engine controls are in the pilot's crew station only |
| Sights | HMD, FCR | TADS, HMD, FCR |
| Night vision sensor (default) | PNVS | TADS |
| Weapons | Gun, rockets, Hellfires | Gun, rockets, Hellfires |

Both crew stations contain two [MPDs]({{ '/displays/mpd/' | relative_url }}), the [UFD]({{ '/displays/ufd/' | relative_url }}), a [keyboard unit]({{ '/displays/ku/' | relative_url }}), a fire detection and extinguishing panel, the A/S and GND ORIDE buttons, the MSTR WARN and MSTR CAUT lighted buttons, the EMER HYD button, an NVS MODE switch, a floodlight and the [IHADSS]({{ '/displays/ihadss/' | relative_url }}). Their locations are shown on the [Cockpit]({{ '/aircraft/cockpit/' | relative_url }}) page.

## Aircraft common and crewstation independent functions

**Aircraft common** functions: the engines, fuel and aircraft systems, warnings, cautions and advisories, the stored points and routes, FCR targets, the weapon inventory, A/S, GND ORIDE, and the IHADSS flight symbology mode (transition, cruise, hover or bob-up).

**Crewstation independent** functions: MPD pages, the selected sight, the [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq), the range source and the [weapon action switch]({{ '/weapons/was/' | relative_url }}).

Some aircraft common items are controlled by one crew station at a time:

| Item | Controlled by |
|---|---|
| Fire control radar | The crew station that last selected FCR as its sight. Only that crew station can scan, slew and slave the radar. |
| Night vision sensors | One crew station uses the PNVS and the other the TADS. **NVS Select PNVS/TADS** exchanges them. |
| Weapons | One weapon at a time, held by the crew station that last actioned it. Both crew stations can hold rockets together. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}). |

## Changing crew stations

Crew stations are changed with the Arma action menu while the other crew station is unoccupied. The CPG takes the flight controls with the Arma **Take Controls** action, and the pilot can take them back. The flight model state, including engines, rotor, trim and hold modes, is retained.

> In multiplayer, the introduction pop-up is displayed to each player on first entry. It is disabled in [Addon settings]({{ '/getting-started/settings/' | relative_url }}).
{: .note}
