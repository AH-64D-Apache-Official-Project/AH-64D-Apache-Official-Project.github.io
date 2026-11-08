---
title: Compatibility
lead: Built-in support for other mods, and the requirements for each.
keywords: [compatibility, rhs, cup, pook, pracs, sam, acre, radio, doom, a3ti, zeus enhanced, mods]
---

The compatibility patches are built into the mod. Each is activated when its mod is loaded and has no effect otherwise; no additional installation is required.

## Air defense classification

The [warning receivers]({{ '/weapons/ase/' | relative_url }}) and the radar classify air defense vehicles by type, to display the correct threat symbol. The mod classifies the Arma vehicles and the air defense vehicles of the following mods:

| Mod | Vehicles classified |
|---|---|
| RHS | ZSU-23-4 Shilka |
| CUP | M6 Linebacker, M1097 Avenger, M163 Vulcan |
| Pook's SAM Pack | The pack's SAM launchers, radars and guns: NASAMS, Patriot, HAWK, SA-2, SA-3, SA-8, SA-10/20, SA-11/17, SA-15, SA-19, SA-21, ZSU and C-RAM, with their search and tracking radars |
| PRACS | MPQ-64 Sentinel, M163 PIVADS, HAWK and I-HAWK, M48 Chaparral and other US air defense |
| PRACS SLA | 1S91, P-37 radar, ZSU-23, SA-2, SA-6, SA-8, SA-9, SA-13, SA-17 and 2S6 Tunguska |

Vehicles from other mods are valid targets; they are displayed without their specific threat symbol and class on the ASE page.

## Radios: ACRE2

With ACRE2 loaded, the aircraft has a crew intercom and four radio racks, available to the pilot and the CPG:

| Rack | Radio |
|---|---|
| 1 | ARC-186 (VHF) |
| 2 | ARC-164 (UHF) |
| 3 | ARC-201D (FM1) |
| 4 | ARC-201D (FM2) |

The radios are configured through the ACRE interaction menu. The intercom is off until selected on after entering the aircraft.

## Thermal imagery: A3 Thermal Improvement

With [A3 Thermal Improvement](https://steamcommunity.com/workshop/filedetails/?id=2041057379), the TADS FLIR uses its thermal image. The **Night vision** binding then belongs to A3TI, and the TADS sensor bindings operate only with the DTV or DVO selected. See [TADS]({{ '/targeting/tads/' | relative_url }}).

## Zeus Enhanced

With [Zeus Enhanced](https://steamcommunity.com/workshop/filedetails/?id=1779063631), Zeus can edit the aircraft's pylons and loadout.

## Doom

The separate [AH-64D Doom](https://github.com/AH-64D-Apache-Official-Project/AH-64D-Doom-Compat) mod adds Doom to the [MPD games]({{ '/displays/mpd/games/' | relative_url }}). It is loaded alongside the AH-64D mod and detected automatically.
