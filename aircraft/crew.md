---
title: Crew stations
lead: The pilot sits in the back and flies. The copilot/gunner sits in front and works the TADS. Each has a full set of displays and can do most jobs, and the aircraft shares its data between them.
keywords: [crew, pilot, cpg, copilot, gunner, seat, front seat, back seat, multiplayer, take controls, plt]
seats: [PLT, CPG]
---

## Who does what

| | Pilot `PLT`{: .seat .seat-plt} | Copilot/gunner `CPG`{: .seat .seat-cpg} |
|---|---|---|
| **Seat** | Rear | Front |
| **In Arma** | Driver | Gunner (copilot) |
| **Flies** | Yes | When given the controls (Arma's **Take Controls**) |
| **Starts and stops the engines** | Yes | No: the engine controls only work from the pilot's seat |
| **Sights** | HMD, FCR | TADS, HMD, FCR |
| **Night vision sensor** | PNVS, by default | TADS, by default |
| **Weapons** | Cannon, rockets, Hellfires | Cannon, rockets, Hellfires |

The rest of the cockpit is the same in both seats: two [MPDs]({{ '/displays/mpd/' | relative_url }}), the [UFD]({{ '/displays/ufd/' | relative_url }}), a [keyboard unit]({{ '/displays/ku/' | relative_url }}), a fire panel, **ARM/SAFE** and **GND ORIDE**, **MASTER WARNING** and **MASTER CAUTION**, **EMER HYD**, an NVS mode switch, a floodlight and an [IHADSS]({{ '/displays/ihadss/' | relative_url }}) helmet display. The [cockpit tour]({{ '/aircraft/cockpit/' | relative_url }}) shows where each one is.

## What you share and what is your own

**Shared**: everything about the aircraft itself. That means the engines, fuel, systems and warnings, the stored points and routes, radar targets, the weapon inventory, **ARM/SAFE**, **GND ORIDE**, and the IHADSS flight symbology mode (transition, cruise, hover or bob-up).

**Your own**: your MPD pages, your selected sight, your [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq), your range source and your [weapon action switch]({{ '/weapons/was/' | relative_url }}).

A few things belong to one crew station at a time:

| Shared item | Who has it |
|---|---|
| **Fire control radar** | The last crew station to select FCR as its sight. Only that station can scan, slew and slave it. |
| **Night vision sensors** | One crew station uses the PNVS and the other the TADS. **NVS Select PNVS/TADS** swaps them. |
| **Weapons** | One weapon at a time, held by the last station to action it. Both can hold the rockets together. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}). |

## Changing seats

Change seats with Arma's action menu while the other seat is free. The CPG can fly with Arma's **Take Controls** action, and the pilot can take them back. The flight model carries on from where it was, so the engines, rotor, trim and holds are not reset.

> In multiplayer, each player gets the welcome pop-up the first time they get in. Turn it off in [Addon settings]({{ '/getting-started/settings/' | relative_url }}).
{: .note}
