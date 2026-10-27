---
title: Survivability (ASE)
lead: What warns you that you are being targeted, and what you can do about it. The equipment depends on whether the aircraft carries US or British mission equipment.
keywords: [ase, survivability, rlwr, radar warning, laser warning, missile warning, mws, chaff, flares, ir jammer, countermeasures, sam, aaa, threats]
seats: [PLT, CPG]
---

## What each aircraft has

| | US equipment | British equipment |
|---|---|---|
| Radar and laser warning receiver (RLWR) | Yes | Yes |
| Chaff | Yes | Yes |
| IR jammer | Yes | |
| Flares | | Yes |
| Missile warning system (MWS) | | Yes |

Choose the equipment in the editor or the [mission planner]({{ '/mission/planner/' | relative_url }}); see [Variants and customisation]({{ '/aircraft/variants/' | relative_url }}). Everything here needs DC power.

## Turning it on

After start-up, on the [ASE page]({{ '/displays/mpd/ase/' | relative_url }}):

1. `R6`{: .vab} **RLWR** on. You hear a tone as it comes on.
2. `T1`{: .vab} **CHAFF** (or **CMS**) to **ARM**.
3. `R1`{: .vab} **IRJAM** (US) or **MWS** (British) on.
4. Pick an **autopage** level, so the ASE page comes up by itself when it matters.
{: .steps}

## Warnings

### Radar warning

The RLWR hears radars. Within about 8 km, each radar is placed on the ASE page (and on the TSD, if shown there) at its bearing, and called out by voice: what it is, its clock direction, and what it is doing.

| State | Meaning | Heard |
|---|---|---|
| **Searching** | Its radar is sweeping the sky. | Once, when it first appears |
| **Acquisition** | It has picked you out. | When it moves up to acquisition |
| **Tracking** | It is tracking you and can fire. | When it moves up to tracking |
| **Launch** | A radar-guided missile is on its way. | "Missile launch", with the direction |

What the RLWR calls a threat depends on the vehicle's config. Vehicles from the mods the Apache has [compatibility]({{ '/mission/compatibility/' | relative_url }}) for are named by type, such as SA-6 or ZSU-23. Anything else with a radar shows as a generic search radar.

### Laser warning

The RLWR also warns when a laser designator or rangefinder is aimed at your aircraft, with the voice message and the direction.

### Missile warning

British equipment only, with **MWS** on: the MWS sees any missile or rocket coming at you from within 3 km, whatever guides it, and calls "missile" with its direction. This is the only warning of an IR missile.

Aircraft with US equipment get no warning of an IR missile. The IR jammer has to deal with it without being told.

## Countermeasures

| Countermeasure | Defeats | Fire it with |
|---|---|---|
| **Chaff** | Radar-guided missiles | Arma's **Countermeasures** binding. Needs chaff at **ARM**. |
| **Flares** (British) | IR-guided missiles | {% include key.html id="fza_ah64_flare" %}. Needs the MWS on. |
| **IR jammer** (US) | IR-guided missiles | Nothing: once it reads **OPER**, it works continuously. |

Full, the ASE page counts 30 chaff and, with British equipment, 60 flares. Rearming refills them. See [Rearm and refuel]({{ '/mission/rearm/' | relative_url }}).

> Chaff does nothing against an IR missile and flares nothing against a radar missile. Use the RLWR's call to tell them apart: a **launch** call is a radar missile, so dispense chaff. A **missile** call from the MWS with no launch call before it is probably IR.
{: .tip}

## Volume

The RLWR's voice messages have their own volume, **RLWR volume Knob**, in [Addon settings]({{ '/getting-started/settings/' | relative_url }}).
