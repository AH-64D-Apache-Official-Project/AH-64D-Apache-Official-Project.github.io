---
title: Compatibility
lead: What the mod does with other popular mods, and what you need to load for each.
keywords: [compatibility, rhs, cup, pook, pracs, sam, acre, radio, doom, a3ti, zeus enhanced, mods]
---

The compatibility patches are built into the mod. Each one switches itself on when its mod is loaded and stays out of the way when it is not, so there is nothing extra to install.

## Air defence classification

The [warning receivers]({{ '/weapons/ase/' | relative_url }}) and the radar need to know which vehicles are air defences, and what kind, to show the right threat symbol. The mod classifies the vanilla Arma vehicles, and these mods' air defence vehicles:

| Mod | Vehicles classified |
|---|---|
| **RHS** | ZSU-23-4 Shilka |
| **CUP** | M6 Linebacker, M1097 Avenger, M163 Vulcan |
| **Pook's SAM Pack** | The pack's SAM launchers, radars and guns: NASAMS, Patriot, HAWK, SA-2, SA-3, SA-8, SA-10/20, SA-11/17, SA-15, SA-19, SA-21, ZSU and C-RAM, with their search and tracking radars |
| **PRACS** | MPQ-64 Sentinel, M163 PIVADS, HAWK and I-HAWK, M48 Chaparral and the other US air defence |
| **PRACS SLA** | 1S91, P-37 radar, ZSU-23, SA-2, SA-6, SA-8, SA-9, SA-13, SA-17 and 2S6 Tunguska |

Vehicles from other mods still work as targets; they are only missing their specific threat symbol and class on the ASE page.

## Radios: ACRE2

With ACRE2 loaded, the Apache has an **intercom** for the crew and four radio racks, usable by the pilot and the CPG:

| Rack | Radio |
|---|---|
| 1 | ARC-186 (VHF) |
| 2 | ARC-164 (UHF) |
| 3 | ARC-201D (FM1) |
| 4 | ARC-201D (FM2) |

Configure them through ACRE's own interaction menu. The intercom is off until you turn it on after getting in.

## Thermal imagery: A3 Thermal Improvement

With [A3 Thermal Improvement](https://steamcommunity.com/workshop/filedetails/?id=2041057379), the TADS FLIR uses its thermal picture. The **Night vision** key then belongs to A3TI, and the TADS sensor keys only work while the DTV or DVO is selected. See [TADS]({{ '/targeting/tads/' | relative_url }}).

## Zeus Enhanced

With [Zeus Enhanced](https://steamcommunity.com/workshop/filedetails/?id=1779063631), a Zeus can edit the Apache's pylons and loadout.

## Doom

The separate [AH-64D Doom](https://github.com/AH-64D-Apache-Official-Project/AH-64D-Doom-Compat) mod adds Doom to the [MPD games]({{ '/displays/mpd/games/' | relative_url }}). Load it alongside the Apache; the games page picks it up by itself.
