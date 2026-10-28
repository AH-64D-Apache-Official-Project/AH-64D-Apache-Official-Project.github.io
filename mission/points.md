---
title: Points and routes
lead: Every place the aircraft knows about is a numbered point with a two-letter ident. Routes string waypoints together; targets and threats sit alongside them on the TSD.
keywords: [points, waypoint, hazard, control measure, target, threat, ident, route, direct, dms, w01, c51, t01, icon, abr]
seats: [PLT, CPG]
---

## Point types

| Type | Numbers | Shown as | What for |
|---|---|---|---|
| **Waypoint** | `W01`{: .mpd}–`W50`{: .mpd} | Green | Places to fly to: start, release and passage points, landing zones. |
| **Hazard** | shares `W01`–`W50` | Yellow | Towers and wires to avoid. |
| **Control measure** | `C51`{: .mpd}–`C99`{: .mpd} | Green, blue (friendly) or red (enemy) | The wider battlefield: assembly areas, battle positions, FARPs, units. |
| **Target / threat** | `T01`{: .mpd}–`T50`{: .mpd} | Red | Known targets and air defences. |

Waypoints and hazards share the numbers 1 to 50. When you type a point's name on the KU, it is the letter and two digits: `W03`, `C51`, `T12`.

Points are the aircraft's own, shared by both crew stations. Each aircraft has its own set.

## Where points come from

- **The mission.** The mission maker places points in the editor ([For mission makers]({{ '/mission/editor/' | relative_url }}#points)). Load them into the aircraft with **MASTER LOAD** on the [DTU page]({{ '/displays/mpd/dms/' | relative_url }}#dtu). A master load replaces the points the aircraft holds.
- **The TSD.** Add, edit, delete or store points on the [WPT and THRT pages]({{ '/displays/mpd/tsd/' | relative_url }}#wpt). **STO NOW** stores your present position: a waypoint, or a target on the THRT page in the ATK phase.
- **The sights.** The CPG's **Store/Update** stores a target where the sight is looking, and the radar's **TGT** button stores its next-to-shoot. Both take the next free `T` number, overwriting from `T01` when all 50 are used. See [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}#storing-a-target).

## Using points

- **Routes**: build one on the [RTE page]({{ '/displays/mpd/tsd/' | relative_url }}#rte) from waypoints, hazards and control measures.
- **Direct to**: **DIR** on the RTE page flies straight to any point.
- **Acquisition source**: any point can be your sight's [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq), from the [COORD page]({{ '/displays/mpd/tsd/' | relative_url }}#coord), which also gives range to it.
- The TSD's [SHOW page]({{ '/displays/mpd/tsd/' | relative_url }}) sets which kinds of point are drawn in each phase.

## Flying a route

The point you are flying to drives the FLT page's command heading and fly-to cue, the navigation box on the FLT and TSD pages, and the waypoint data and heading caret on your helmet.

The route moves on to the next point by itself as you pass each one, abeam the turn. About a minute before a point you get the `WPT APRCH`{: .mpd} advisory, and on passing it `WPT PASSED`{: .mpd}. Both appear only when neither crew member has a TSD up.

## Idents {#idents}

The ident sets a point's icon. It must suit the point's type: a waypoint cannot be `AE`, a target cannot be `WP`. The same list is on the TSD's [ABR page]({{ '/displays/mpd/tsd/' | relative_url }}#abr).

{% capture i %}<img class="sym" src="{{ '/assets/icons/tsd/mpd/' | relative_url }}{% endcapture %}

### Waypoints

| Icon | Ident | Name |
|---|---|---|
| {{ i }}WP.png" alt=""> | `WP` | Waypoint |
| {{ i }}SP.png" alt=""> | `SP` | Start point |
| {{ i }}RP.png" alt=""> | `RP` | Release point |
| {{ i }}PP.png" alt=""> | `PP` | Passage point |
| {{ i }}CC.png" alt=""> | `CC` | Communications check point |
| {{ i }}LZ.png" alt=""> | `LZ` | Landing zone |

### Hazards

| Icon | Ident | Name |
|---|---|---|
| {{ i }}TO.png" alt=""> | `TO` | Tower over 1,000 ft |
| {{ i }}TU.png" alt=""> | `TU` | Tower under 1,000 ft |
| {{ i }}WL.png" alt=""> | `WL` | Wires, power |
| {{ i }}WS.png" alt=""> | `WS` | Wires, telephone or electric |

### Control measures

| Icon | Ident | Name |
|---|---|---|
| {{ i }}AP.png" alt=""> | `AP` | Air control point |
| {{ i }}AG.png" alt=""> | `AG` | Airfield, general |
| {{ i }}AI.png" alt=""> | `AI` | Airfield, instrumented |
| {{ i }}AL.png" alt=""> | `AL` | Airfield, lighted |
| {{ i }}F1.png" alt=""> | `F1` / `F2` | Artillery fire point 1 / 2 |
| {{ i }}AA.png" alt=""> | `AA` | Assembly area |
| {{ i }}BP.png" alt=""> | `BP` | Battle position |
| {{ i }}BR.png" alt=""> | `BR` | Bridge or gap |
| {{ i }}CP.png" alt=""> | `CP` | Checkpoint |
| {{ i }}FF.png" alt=""> | `FF` | FARP, fuel only |
| {{ i }}FM.png" alt=""> | `FM` | FARP, ammunition only |
| {{ i }}FC.png" alt=""> | `FC` | FARP, fuel and ammunition |
| {{ i }}GL.png" alt=""> | `GL` | Ground light or small town |
| {{ i }}HA.png" alt=""> | `HA` | Holding area |
| {{ i }}ID.png" alt=""> | `ID` | IDM subscriber |
| {{ i }}AM.png" alt=""> | `AM` | Armour, friendly |
| {{ i }}FL.png" alt=""> | `FL` | Field artillery, friendly |
| {{ i }}FI.png" alt=""> | `FI` | Infantry, friendly |
| {{ i }}MI.png" alt=""> | `MI` | Mechanised infantry, friendly |
| {{ i }}FU.png" alt=""> | `FU` | Unit, friendly |
| {{ i }}AE.png" alt=""> | `AE` | Armour, enemy |
| {{ i }}EF.png" alt=""> | `EF` | Field artillery, enemy |
| {{ i }}EI.png" alt=""> | `EI` | Infantry, enemy |
| {{ i }}EM.png" alt=""> | `EM` | Mechanised infantry, enemy |
| {{ i }}EU.png" alt=""> | `EU` | Unit, enemy |

### Targets and threats

| Icon | Ident | Name |
|---|---|---|
| {{ i }}TG.png" alt=""> | `TG` | Target reference point |
| {{ i }}GU.png" alt=""> | `GU` | Gun, generic |
| {{ i }}ZU.png" alt=""> | `ZU` | Gun, ZSU-23 |
| {{ i }}S6.png" alt=""> | `S6` | Air defence, 2S6 / SA-13 |
| {{ i }}1.png" alt=""> | `1`–`17` | SAM, SA-1 to SA-17 |
| {{ i }}CT.png" alt=""> | `CT` | SAM, Crotale |
| {{ i }}CH.png" alt=""> | `CH` | SAM, Chaparral |
| {{ i }}HK.png" alt=""> | `HK` | SAM, Hawk |
| {{ i }}ST.png" alt=""> | `ST` | SAM, Stinger |
| {{ i }}VU.png" alt=""> | `VU` | SAM, Vulcan |
| {{ i }}SR.png" alt=""> | `SR` | Radar, battlefield surveillance |
| {{ i }}TR.png" alt=""> | `TR` | Radar, target acquisition |

