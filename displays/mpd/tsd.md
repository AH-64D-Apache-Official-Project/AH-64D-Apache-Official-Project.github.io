---
title: TSD page
lead: The tactical situation display. Your own aircraft at the centre of a moving plot of waypoints, routes, targets, threats and radar returns.
keywords: [tsd, tactical situation display, map, nav, atk, phase, scale, show, waypoint, route, threat, coord, abr, hsi, wind, endurance]
seats: [PLT, CPG]
redirect_from:
  - /mpd-tsd.html
---

Open it with the **TSD** button on either MPD. The page is drawn heading up: your aircraft is the symbol near the bottom (or in the centre with **CTR**), and everything else moves around it as you fly.

The TSD has no terrain map. It plots points, lines and symbols on black, at the chosen scale. Use the Arma map for the ground.

{% include fig.html id="mpd-tsd" %}

## Phases

`B2`{: .vab} **PHASE** switches between **NAV** and **ATK**. Each phase remembers its own SHOW settings, so you can keep a clean navigation picture and a busy attack picture and swap between them with one button.

| | NAV | ATK |
|---|---|---|
| Data block along the bottom | Shown, unless turned off in SHOW | Not shown |
| Radar targets | The top 16 | All of them |
| Hazards | Always shown | Shown or hidden in SHOW |

## What is drawn

| Symbol | Meaning |
|---|---|
| Your aircraft | Fixed, pointing up. |
| **Route** | Green lines joining the points of the current route. |
| **Direct-to line** | A green line from where you selected direct-to, to the point you are flying to. |
| **Points** | Waypoints, hazards, control measures and targets/threats, each with its own icon. See [Points and routes]({{ '/mission/points/' | relative_url }}). |
| **Friendly units** | Blue markers for friendly vehicles and aircraft reported over the datalink. |
| **Radar targets** | The FCR's targets, as on the [FCR page]({{ '/displays/mpd/fcr/' | relative_url }}). At the 25 and 50 km scales they shrink to small yellow squares. |
| **Shot at** | Where your Hellfires were fired at. |
| **Threats** | Radar and laser warnings from the [ASE]({{ '/weapons/ase/' | relative_url }}), placed on the ring at their bearing. A launch flashes. |
| **TADS line of sight** | While the CPG's sight is the TADS: a line out to the TADS range, with a crosshair at its end. |
| **Radar footprint** | While your sight is the FCR (or the CPG is linked TADS-FCR): the scan sector out to 8 km. Green while scanning continuously or idle, white for a single scan. |

## Root page buttons

| Button | Label | Action |
|---|---|---|
| `T2`{: .vab} | `ASE`{: .mpd} | Opens the [ASE page]({{ '/displays/mpd/ase/' | relative_url }}). |
| `T5`{: .vab} | `COORD`{: .mpd} | Opens the [COORD page](#coord). |
| `L6`{: .vab} | `SHOW`{: .mpd} | Opens [SHOW](#show). |
| `R2`{: .vab} | `SC`{: .mpd} | Opens the scale choices: `R1`{: .vab} 50 km, `R2`{: .vab} 25 km, `R3`{: .vab} 10 km, `R4`{: .vab} 5 km. |
| `R3`{: .vab} | `CTR`{: .mpd} | Moves your aircraft between the bottom of the page (more look-ahead) and the centre. |
| `R6`{: .vab} | `ACQ`{: .mpd} | Opens the [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list. |
| `B1`{: .vab} | | MENU. |
| `B2`{: .vab} | `PHASE`{: .mpd} | NAV or ATK. |
| `B4`{: .vab} | `WPT`{: .mpd} | Opens [WPT](#wpt). |
| `B5`{: .vab} | `RTE`{: .mpd} | Opens [RTE](#rte). |
| `B6`{: .vab} | `THRT`{: .mpd} | Opens [THRT](#thrt). |

**RPT**, **PAN**, **PP**, **UTIL**, **ADF**, **CAQ**, **FRZ** and **ZN** are not simulated.

### Data block

Along the bottom of the root page, in the NAV phase:

- the point you are flying to, its distance in km, your ground speed in knots, and the time to reach it;
- **ENDR**: endurance on the fuel you have, at your current burn rate;
- **WIND**: direction and speed, or **CALM** below 5 kt.

## SHOW {#show}

SHOW chooses what each phase draws. A filled box beside a label means it is shown.

| Button | NAV phase | ATK phase |
|---|---|---|
| `T1`{: .vab} | **HSI**: a compass rose around your aircraft | Same |
| `L4`{: .vab} | **WAYPOINT DATA**: the data block | **CURRENT ROUTE**: no effect yet; the route is drawn in both phases |
| `L5`{: .vab} | **PLANNED TGT/THRT**: targets and threats | Same |
| `R1`{: .vab} | **CONTROL MEASURES** (green) | Same |
| `R2`{: .vab} | **ENEMY UNITS** (red control measures) | Same |
| `R3`{: .vab} | **FRIENDLY UNITS** (blue control measures, and friendly units from the datalink) | Same |
| `R5`{: .vab} | **RLWR THREATS**: warning receiver threats | Same |
| `B3`{: .vab} | **ENDR** | Same |
| `B4`{: .vab} | | **SHOT**: shot-at markers |
| `B5`{: .vab} | **WIND** | Same |
| `B6`{: .vab} | | **HAZARDS** |
| `L6`{: .vab} | Back to the root page | Same |

**INACTIVE ZONES**, **AREAS**, **LINES**, **RFI THREATS** and **OBSTACLES** are not simulated.

## Entering text: the keyboard unit

Buttons marked with `>` (`POINT>`{: .mpd}, `IDENT>`{: .mpd}) ask for typed input. The prompt appears on the [keyboard unit]({{ '/displays/ku/' | relative_url }}). Click the KU to start typing, type the value and press <kbd>Enter</kbd>. A value the aircraft cannot use shows an error: press <kbd>Enter</kbd> to clear it and try again.

Points are named by a letter and a number: **W01**–**W50** waypoints and hazards, **C51**–**C99** control measures, **T01**–**T50** targets and threats.

## WPT {#wpt}

`B4`{: .vab} **WPT** works on waypoints, hazards and control measures.

| Button | Label | Action |
|---|---|---|
| `L1`{: .vab} | `POINT>`{: .mpd} | Selects a point by typing its name. Its details show at the top of the page: ident, free text, time and clock time to reach it, grid, bearing and distance, latitude and longitude, and altitude. |
| `L2`{: .vab} | `ADD`{: .mpd} | Adds a point; see below. |
| `L3`{: .vab} | `DEL`{: .mpd} | Deletes the selected point, after `L2`{: .vab} **YES**. `L3`{: .vab} **NO** cancels. |
| `L4`{: .vab} | `EDT`{: .mpd} | Edits the selected point: `L1`{: .vab} runs through the same prompts as ADD, filled in with its current values. |
| `L5`{: .vab} | `STO`{: .mpd} | Stores a point where you are now: `L1`{: .vab} **NOW**. |
| `T4`{: .vab} | `ABR`{: .mpd} | Opens the [ABR page](#abr), the list of idents. |
| `R3`{: .vab} | `CTR`{: .mpd} | As on the root page. |

**XMIT** is not simulated.

### Adding a point

1. `L2`{: .vab} **ADD**.
2. Choose the type: `L4`{: .vab} **WP** waypoint, `L5`{: .vab} **HZ** hazard, or `L6`{: .vab} **CM** control measure.
3. `L1`{: .vab} **IDENT>**. The KU then asks for four things in turn:
   - **IDENT**: the two-letter code for what the point is, which sets its icon, for example `WP`, `LZ`, `TO`, `BP`. It must suit the type. See the [ABR page](#abr) or [Points and routes]({{ '/mission/points/' | relative_url }}#idents).
   - **FREE**: up to three characters of your own, drawn beside the icon.
   - **GRID**: its map grid, up to eight digits. Your own position is filled in to start with.
   - **ALTITUDE**: in feet, as your barometric altimeter reads. The ground height at the grid is filled in.
{: .steps}

The point takes the next free number of its type and becomes the selected point.

## RTE {#rte}

`B5`{: .vab} **RTE** builds the route you fly. The route's points are listed down the right side, `R2`{: .vab} to `R5`{: .vab}, with the first at the bottom. `R1`{: .vab} and `R6`{: .vab} scroll the list. The point you are flying to is boxed.

| Button | Label | Action |
|---|---|---|
| `L2`{: .vab} | `ADD`{: .mpd} | `L1`{: .vab} **POINT>** picks a waypoint, hazard or control measure. Then press the route button where it should go: the new point is inserted there. |
| `L3`{: .vab} | `DEL`{: .mpd} | Press a route button to take that point out of the route. |
| `L4`{: .vab} | `DIR`{: .mpd} | Fly direct. Press a route button to fly to that route point, or `L1`{: .vab} **POINT>** to fly to any stored point, on the route or not. |
| `L5`{: .vab} | `RVW`{: .mpd} | Review. Press a route button to see that point's details. Press it again to clear them. |

**RTM** is not simulated.

### Flying the route

Once you are flying to a route point, the aircraft moves on to the next one by itself as you pass abeam. Within a minute of a point you get the `WPT APRCH`{: .mpd} advisory, and as you pass it `WPT PASSED`{: .mpd}, unless one of the crew has a TSD up.

The point you are flying to feeds the FLT page, the IHADSS, and the data block above.

## THRT {#thrt}

`B6`{: .vab} **THRT** works exactly like WPT, but on targets and threats (**T01**–**T50**, ident `TG` by default, or a threat type such as a SAM system). **STO** in the ATK phase stores a target where you are.

## COORD {#coord}

`T5`{: .vab} **COORD** lists the stored points, six to a page. `B2`{: .vab} **PAGE** moves through the pages.

| Button | Label | Lists |
|---|---|---|
| `T1`{: .vab} | `WPTHZ`{: .mpd} | Waypoints and hazards. |
| `T2`{: .vab} | `CTRLM`{: .mpd} | Control measures. |
| `T5`{: .vab} | `COORD`{: .mpd} | Targets and threats. Pressed again, returns to the TSD. |
| `T6`{: .vab} | `SHOT`{: .mpd} | Your last Hellfire shots: missile type, time and where they were fired at. |
| `R1`{: .vab}–`R6`{: .vab} | | Expands that line with the time and distance to the point, its bearing, and its latitude and longitude. |
| `L1`{: .vab}–`L6`{: .vab} | | Makes that line's point your [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq). |

**LINE**, **AREA**, **SRCH** and **FARM** are not simulated.

## ABR {#abr}

`T4`{: .vab} **ABR**, on the WPT and THRT pages, lists every ident the aircraft knows, with its name and icon, over several pages (`B2`{: .vab} **PAGE**). `B4`{: .vab}–`B6`{: .vab} return to WPT, RTE or THRT, and `T4`{: .vab} back to the TSD.
