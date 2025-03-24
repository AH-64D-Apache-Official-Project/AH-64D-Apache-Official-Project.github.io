---
title: Logic Entities
tags: [getting_started]
sidebar: ah64d_sidebar
permalink: logicentities.html
folder: root
stub: true
---

## Introduction

This section will explain the new logic entities provided by the Apache mod and how they can be used exclusively with the helicopter for gameplay. The mission maker has access to them and should be used for a proper gameplay experince for the players.

Each logic entity has three fields which can be chnaged by the mission maker. These are : 
1. Point Index : Serial Number of the logic entity placed down. This automatically updates when another previously placed logic entity is placed again. For Waypoint/Hazard and Target Points, the index starts at 1, while for Control Measure it starts at 51. Advised not to change them manually.
2. Point Ident : Dropdown menu cotanining all possible point identifications for the logic entity.
3. Point Free Text : __This can only take 3 characters__. I would advise make them capital letters. Extra information regarding the waypoint or control measure or target/threat can be inserted here.

### Waypoint/Hazard

This logic entity provides waypoints which the helicotper can use. These waypoints are pertinent to the flight plan of the helicopter. This will appear in the NAV and ATK phase of the TSD. There are different types of waypoints which can be specified through the logic menu. These are listed down below, they can be changed from the `Point Ident` dropdown menu in the logic entity. A few definitions for the different types have been provided.
1. WP -> Standard Waypoint for Navigation.
2. CC 
3. LZ -> Landing Zone
4. PP
5. RP
6. SP
7. TO
8. TU
9. WL
10. WS

### Control Measure

This logic entities provides mission makers to place information regarding the broader area of operations rather than an individual flight plan. This will appear in the NAV and ATK phase of the TSD. The different types of control points are listed below along with a few definitions: 
1. AA
2. AE
3. AG
4. AI
5. AL
6. AM
7. AP
8. AP
9. BP -> Battle Point
10. BR
11. CP -> Control Point
12. EF -> Enemy Forces(?)
13. EI -> Enemy Infantry
14. EM -> Enemy Mechanised
15. EU
16. F1
17. F2
18. FC
19. FF
20. FI
21. FL
22. FM
23. FU
24. GL
25. HA
26. ID
27. MI

### Target Points

This is to create points where known targets are. They mostly include known SAM or AAA or AA sites on the map. This will only appear on the ATK phase of the TSD by default. This can be changed on the TSD page. The list of targets which can be changed via the `Point Ident` dropdown in the logic entity :
1. 1
2. 10
3. 11
4. 12
5. 13
6. 14
7. 15
8. 16
7. 17
8. 2
9. 3
10. 4
11. 5
12. 6
13. 7
14. 8
15. 9
16. GU
17. S6
18. SR
19. TG
20. TR
21. ZU