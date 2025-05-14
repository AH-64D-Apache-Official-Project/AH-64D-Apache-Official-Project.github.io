---
title: Logic Entities
tags: [getting_started]
sidebar: ah64d_sidebar
permalink: logicentities.html
folder: root
stub: true
---

*ADD LOGIC ENTITIES EDEN IMAGE HERE*

## Introduction

This section will explain the new logic entities provided by the Apache mod and how they can be used exclusively with the helicopter for gameplay. The mission maker has access to them and should be used for a proper gameplay experince for the players.

Each logic entity has three fields which can be chnaged by the mission maker. These are : 
1. Point Index : Serial Number of the logic entity placed down. This automatically updates when another previously placed logic entity is placed again. For Waypoint/Hazard and Target Points, the index starts at 1, while for Control Measure it starts at 51, if logic entitys with overlapping index values appear, only one will be recognised by the system
2. Point Ident : Dropdown menu cotanining all possible point identifications for the logic entity.
3. Point Free Text : __This can only take 3 characters__. Extra information regarding the waypoint or control measure or target/threat can be inserted here.

### Waypoint/Hazard

This logic entity provides waypoints which the helicotper can use. These waypoints are pertinent to the flight plan of the helicopter. This will appear in the NAV and ATK phase of the TSD. There are different types of waypoints which can be specified through the logic menu. These are listed down below, they can be changed from the `Point Ident` dropdown menu in the logic entity. A few definitions for the different types have been provided.
#### Waypoints
- WP - Waypoint
- CC - Comm Check Point
- LZ - Landing Zone
- PP - Passage Point
- RP - Release Point
- SP - Start point

#### Hazards
- TO - Tower Over 1000
- TU - Tower under 1000
- WL - Wires Power
- WS - Wires Tele/Elec

### Control Measure

This logic entities provides mission makers to place information regarding the broader area of operations rather than an individual flight plan. This will appear in the NAV and ATK phase of the TSD. The different types of control points are listed below along with a few definitions: 
- AA - Assembly Area
- AE - Armor Enemy
- AG - Airfield General
- AI - Airfield Instrum
- AL - Airfield Lighted
- AM - Armor Friend
- AP - Air Control Point
- BP - Battle Point
- BR - Bridge or Gap
- CP - Control Point
- EF - Enemy Forces(?)
- EI - Enemy Infantry
- EM - Enemy Mechanised
- EU - Unit ID Enemy
- F1 - Arty Fire Pt 1
- F2 - Arty Fire Pt 2
- FF - FARP Fuel Only
- FM - FARP Ammo Only
- FC - FARP Fuel/Ammo
- FI - Infantry Friend
- FL - Field Arty Friend
- FU - Unit ID Friend
- GL - Grnd lite/Sm Town
- HA - Holding Area
- ID - IDM Subscriber
- MI - Mech Infantry

### Target Points

This is to create points where known targets are. They mostly include known SAM or AAA or AA sites on the map. This will only appear on the ATK phase of the TSD by default. This can be changed on the TSD page. The list of targets which can be changed via the `Point Ident` dropdown in the logic entity :

- 1 - SAM SA-1
- 2 - SAM SA-2
- 3 - SAM SA-3
- 4 - SAM SA-4
- 5 - SAM SA-5
- 6 - SAM SA-6
- 7 - SAM SA-7
- 8 - SAM SA-8
- 9 - SAM SA-9
- 10 - SAM SA-10
- 11 - SAM SA-11
- 12 - SAM SA-12
- 13 - SAM SA-13
- 14 - SAM SA-14
- 15 - SAM SA-15
- 16 - SAM SA-16
- 17 - SAM SA-17
- GU - Gun Generic
- S6 - ADU 2S6/SA-13
- SR - RADAR BATTL SURV
- TG - TARGET REF POINT
- TR - RADAR TGT ACQ
- ZU - GUN ZSU-23
- ST - SAM STINGER
- VU - SAM VULCAN