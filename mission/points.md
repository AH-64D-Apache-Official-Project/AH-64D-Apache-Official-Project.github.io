---
title: Points and routes
lead: DMS point types and numbering, their sources and uses, lines, areas and zones, route sequencing, and the ident list.
keywords: [points, waypoint, hazard, control measure, target, threat, ident, route, direct, dms, w01, c51, t01, icon, abr]
seats: [PLT, CPG]
---

## Point types

| Type | Numbers | Colour | Use |
|---|---|---|---|
| Waypoint/Hazard | `W01`{: .mpd}–`W50`{: .mpd} | Green (waypoint), yellow (hazard) | Navigation points: start, release and passage points, landing zones; towers and wires |
| Control measure | `C51`{: .mpd}–`C99`{: .mpd} | Green, blue (friendly) or red (enemy) | Battlefield graphics: assembly areas, battle positions, FARPs, units |
| Target/Threat | `T01`{: .mpd}–`T50`{: .mpd} | Red | Known targets and air defences |

A point is identified on the KU by its letter and two digits: `W03`, `C51`, `T12`.

Points are aircraft common to both crew stations. Each aircraft holds its own set.

## Point sources

- **Mission**: points placed in the editor ([Mission editor]({{ '/mission/editor/' | relative_url }}#points)) are loaded with MASTER LOAD on the [DTU page]({{ '/displays/mpd/dms/' | relative_url }}#dtu). MASTER LOAD replaces the points held by the aircraft.
- **DTC**: points, routes, lines, areas and zones planned in the [mission planner]({{ '/mission/planner/' | relative_url }}#dtc) and uploaded to the aircraft are loaded by the same MASTER LOAD, over the mission data.
- **TSD**: points are added, edited, deleted or stored on the [WPT and THRT pages]({{ '/displays/mpd/tsd/' | relative_url }}#wpt), by KU entry or with the [MPD cursor]({{ '/displays/mpd/tsd/' | relative_url }}#cursor). STO NOW stores the present position: a waypoint, or a target on the THRT page in the ATK phase.
- **Sights**: the CPG's Store/Update stores a target along the sight's line of sight, and the FCR page [TGT]({{ '/displays/mpd/fcr/' | relative_url }}#tgt) stores radar targets. Both take the next free `T` number, overwriting from `T01` when all 50 are used. An FCR target selected with the TSD [CAQ]({{ '/displays/mpd/tsd/' | relative_url }}#caq) is stored as `T50`. See [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}#target-storage).

## Point uses

Points are used for navigation and sensor cueing. To use a point for navigation, the aircrew selects the point as their Navigation Fly To Cue and updates the relevant symbology. To use a point to cue a sensor or sight, and provide ranging information for weapons release, the crew selects the point as their acquisition source via the [TSD > COORD]({{ '/displays/mpd/tsd/' | relative_url }}#coord) or `R6`{: .vab} on the MPD where ACQ is displayed.

Points are also used to build routes. Valid point types for routes include Waypoint/Hazards and Control Measures.

Points may be shown or hidden by category on the [TSD > SHOW]({{ '/displays/mpd/tsd/' | relative_url }}#show) page.

## Lines, areas and zones

In addition to points, the aircraft holds up to 15 lines (phase and boundary lines, FLOT, FLET and FSCL), 12 engagement areas, 8 priority fire zones and 8 no fire zones. Lines and areas are loaded only from a [DTC]({{ '/mission/planner/' | relative_url }}#dtc); zones can also be drawn on the TSD [ZN page]({{ '/displays/mpd/tsd/' | relative_url }}#zn). The TSD displays them, the [COORD page]({{ '/displays/mpd/tsd/' | relative_url }}#coord) lists lines and areas, and the radar uses the zones to [prioritise targets]({{ '/targeting/fcr/' | relative_url }}#zones).

## Route sequencing

The destination point drives the FLT page command heading and navigation fly-to cue, the navigation data on the FLT and TSD pages, and the HMD navigation data and command heading chevron.

The route sequences to the next point automatically abeam each point. Approximately one minute before a point the `WPT APRCH`{: .mpd} advisory is displayed, and on passing it `WPT PASSED`{: .mpd}, when neither crewmember is displaying a TSD page.

## Idents {#idents}

The ident sets a point's symbol and must be valid for the point type (a waypoint cannot be `AE`; a target cannot be `WP`). The same list is on the TSD [ABR page]({{ '/displays/mpd/tsd/' | relative_url }}#abr).

Each symbol is shown as it is drawn on the TSD. The point numbers and the free text (`AAA`) are samples; the letters and numbers on threats are fixed by the ident.

{% capture i %}<img class="sym sym-pt" src="{{ '/assets/icons/tsd/labelled/' | relative_url }}{% endcapture %}

### Waypoints (WP)

| Symbol | Ident | Description |
|---|---|---|
| {{ i }}WP.png" alt=""> | `WP` | Waypoint |
| {{ i }}SP.png" alt=""> | `SP` | Start point |
| {{ i }}RP.png" alt=""> | `RP` | Release point |
| {{ i }}PP.png" alt=""> | `PP` | Passage point |
| {{ i }}CC.png" alt=""> | `CC` | Communications checkpoint |
| {{ i }}LZ.png" alt=""> | `LZ` | Landing zone |

### Hazards (HZ)

| Symbol | Ident | Description |
|---|---|---|
| {{ i }}TO.png" alt=""> | `TO` | Tower over 1,000 ft AGL |
| {{ i }}TU.png" alt=""> | `TU` | Tower under 1,000 ft AGL |
| {{ i }}WL.png" alt=""> | `WL` | Wires – power transmission lines |
| {{ i }}WS.png" alt=""> | `WS` | Wires – telephone and electric |

### Control measures (CM)

| Symbol | Ident | Description |
|---|---|---|
| {{ i }}AP.png" alt=""> | `AP` | Air control point |
| {{ i }}AG.png" alt=""> | `AG` | Airfield, general |
| {{ i }}AI.png" alt=""> | `AI` | Airfield, instrumented |
| {{ i }}AL.png" alt=""> | `AL` | Lighted airport |
| {{ i }}F1.png" alt=""> | `F1` | Artillery firing point 1 |
| {{ i }}F2.png" alt=""> | `F2` | Artillery firing point 2 |
| {{ i }}AA.png" alt=""> | `AA` | Assembly area |
| {{ i }}BP.png" alt=""> | `BP` | Battle position |
| {{ i }}BR.png" alt=""> | `BR` | Bridge |
| {{ i }}CP.png" alt=""> | `CP` | Checkpoint |
| {{ i }}FF.png" alt=""> | `FF` | FARP with fuel only |
| {{ i }}FM.png" alt=""> | `FM` | FARP with ammunition only |
| {{ i }}FC.png" alt=""> | `FC` | FARP with fuel and ammunition |
| {{ i }}GL.png" alt=""> | `GL` | Ground light / small town |
| {{ i }}HA.png" alt=""> | `HA` | Holding area |
| {{ i }}ID.png" alt=""> | `ID` | IDM subscriber |
| {{ i }}AM.png" alt=""> | `AM` | Friendly armour |
| {{ i }}FL.png" alt=""> | `FL` | Friendly artillery |
| {{ i }}FI.png" alt=""> | `FI` | Friendly infantry |
| {{ i }}MI.png" alt=""> | `MI` | Friendly mechanised infantry |
| {{ i }}FU.png" alt=""> | `FU` | Friendly unit |
| {{ i }}AE.png" alt=""> | `AE` | Enemy armour |
| {{ i }}EF.png" alt=""> | `EF` | Enemy artillery |
| {{ i }}EI.png" alt=""> | `EI` | Enemy infantry |
| {{ i }}EM.png" alt=""> | `EM` | Enemy mechanised infantry |
| {{ i }}EU.png" alt=""> | `EU` | Enemy unit |

### Targets and threats (TG)

| Symbol | Ident | Description |
|---|---|---|
| {{ i }}TG.png" alt=""> | `TG` | Target point |
| {{ i }}GU.png" alt=""> | `GU` | Generic air defence unit (ADU) |
| {{ i }}ZU.png" alt=""> | `ZU` | ZSU-23-4 ADU |
| {{ i }}S6.png" alt=""> | `S6` | 2S6 / SA-13 ADU |
| {{ i }}1.png" alt=""> | `1` | SA-1 ADU |
| {{ i }}2.png" alt=""> | `2` | SA-2 ADU |
| {{ i }}3.png" alt=""> | `3` | SA-3 ADU |
| {{ i }}4.png" alt=""> | `4` | SA-4 ADU |
| {{ i }}5.png" alt=""> | `5` | SA-5 ADU |
| {{ i }}6.png" alt=""> | `6` | SA-6 ADU |
| {{ i }}7.png" alt=""> | `7` | SA-7 ADU |
| {{ i }}8.png" alt=""> | `8` | SA-8 ADU |
| {{ i }}9.png" alt=""> | `9` | SA-9 ADU |
| {{ i }}10.png" alt=""> | `10` | SA-10 ADU |
| {{ i }}11.png" alt=""> | `11` | SA-11 ADU |
| {{ i }}12.png" alt=""> | `12` | SA-12 ADU |
| {{ i }}13.png" alt=""> | `13` | SA-13 ADU |
| {{ i }}14.png" alt=""> | `14` | SA-14 ADU |
| {{ i }}15.png" alt=""> | `15` | SA-15 ADU |
| {{ i }}16.png" alt=""> | `16` | SA-16 ADU |
| {{ i }}17.png" alt=""> | `17` | SA-17 ADU |
| {{ i }}CT.png" alt=""> | `CT` | Crotale SAM |
| {{ i }}CH.png" alt=""> | `CH` | Chaparral SAM |
| {{ i }}HK.png" alt=""> | `HK` | Hawk SAM |
| {{ i }}ST.png" alt=""> | `ST` | Stinger SAM |
| {{ i }}VU.png" alt=""> | `VU` | Vulcan |
| {{ i }}SR.png" alt=""> | `SR` | Battlefield surveillance radar |
| {{ i }}TR.png" alt=""> | `TR` | Target acquisition radar |
