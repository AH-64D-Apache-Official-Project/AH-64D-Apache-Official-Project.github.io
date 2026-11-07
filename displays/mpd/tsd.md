---
title: TSD page
lead: The tactical situation display. Your own aircraft at the centre of a moving plot of waypoints, routes, targets, threats and radar returns.
keywords: [tsd, tactical situation display, map, nav, atk, phase, scale, show, waypoint, route, threat, coord, abr, hsi, wind, endurance, cursor, frz, freeze, pan, zoom, caq, cursor acquisition, zn, zone, priority fire zone, no fire zone, pfz, nfz, trp, line, area, flot, flet, phase line]
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
| **Zones** | Priority fire (PF) zones in white, no fire (NF) zones in yellow. See [Zones on the map](#zones-on-the-map). |
| **Lines and areas** | Lines and engagement areas from the [DTC]({{ '/mission/planner/' | relative_url }}#dtc). See [Zones on the map](#zones-on-the-map). |

## Root page buttons

| Button | Label | Action |
|---|---|---|
| `T2`{: .vab} | `ASE`{: .mpd} | Opens the [ASE page]({{ '/displays/mpd/ase/' | relative_url }}). |
| `T3`{: .vab} | `PAN`{: .mpd} | Opens [PAN](#pan). |
| `T5`{: .vab} | `COORD`{: .mpd} | Opens the [COORD page](#coord). |
| `L6`{: .vab} | `SHOW`{: .mpd} | Opens [SHOW](#show). |
| `R1`{: .vab} | `ZOOM`{: .mpd} | Draws the map 20% larger about your aircraft, or back. Boxed while on. The range marks and scale move out to match. |
| `R2`{: .vab} | `SC`{: .mpd} | Opens the scale choices: `R1`{: .vab} 50 km, `R2`{: .vab} 25 km, `R3`{: .vab} 10 km, `R4`{: .vab} 5 km. |
| `R3`{: .vab} | `CTR`{: .mpd} | Moves your aircraft between the bottom of the page (more look-ahead) and the centre. |
| `R4`{: .vab} | `CAQ`{: .mpd} | Cursor acquisition: see [CAQ](#caq). |
| `R5`{: .vab} | `FRZ`{: .mpd} | Freezes the map, or back to the live map. See [FRZ](#frz). |
| `R6`{: .vab} | `ACQ`{: .mpd} | Opens the [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list. |
| `B1`{: .vab} | | MENU. |
| `B2`{: .vab} | `PHASE`{: .mpd} | NAV or ATK. |
| `B3`{: .vab} | `ZN`{: .mpd} | Opens [ZN](#zn), the zone page. |
| `B4`{: .vab} | `WPT`{: .mpd} | Opens [WPT](#wpt). |
| `B5`{: .vab} | `RTE`{: .mpd} | Opens [RTE](#rte). |
| `B6`{: .vab} | `THRT`{: .mpd} | Opens [THRT](#thrt). |

ZOOM, CTR and FRZ work the same on the WPT, THRT and PAN pages. **RPT**, **PP**, **UTIL** and **ADF** are not simulated.

## The MPD cursor on the TSD {#cursor}

The [MPD cursor]({{ '/displays/mpd/' | relative_url }}#cursor) works on the map as well as on the buttons. Over the map, inside its border, it shows a white **X**. Where the page takes a point, moving the cursor onto one draws that point over a black circle, and **Cursor Enter** chooses it.

| Page | Cursor Enter on the map |
|---|---|
| Root, with **CAQ** | Makes the point or radar target your acquisition source. See [CAQ](#caq). |
| **WPT** or **THRT**, top level, **DEL** or **EDT** | Chooses the point, as if typed with **POINT>**. |
| **WPT** or **THRT** **ADD** | Adds a point of the chosen type at the cursor, at ground level: ident `WP`, `TU`, `CP` or `TG`. |
| **RTE** **ADD** | Chooses the waypoint, hazard or control measure to insert. |
| **RTE** **DIR** | Flies direct to the point. |
| **PAN** | Pans the map to put that spot in the middle. |
| **ZN** | Places a corner of the zone being drawn. See [ZN](#zn). |
| Any page with a **GRID** prompt on the KU | Fills the prompt with the cursor's grid. |

Points hidden outside the map border cannot be chosen.

## FRZ {#frz}

`R5`{: .vab} **FRZ** freezes the map where it is: your aircraft carries on flying across a still map. The frozen picture of your aircraft is white with its rotors stopped, and the map border turns dashed. Threat symbols from the ASE turn with the frozen map. Press **FRZ** again to return to the live map.

PAN, CAQ and ZN freeze the map for you.

## CAQ {#caq}

`R4`{: .vab} **CAQ**, cursor acquisition, freezes the map and lets you choose your [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) from it with the MPD cursor:

1. Press **CAQ**.
2. Put the cursor on a waypoint, hazard, control measure, target or threat, or on a radar target.
3. **Cursor Enter**. The point becomes your acquisition source.
{: .steps}

A radar target chosen this way is stored as target point `T50`{: .mpd}, which becomes the acquisition source. If you own the radar it also becomes the NTS. CAQ ends when you choose a point, press it again, or leave the TSD's top level.

## PAN {#pan}

`T3`{: .vab} **PAN** freezes the map so you can move it to look somewhere else. Press **PAN** again to return to the TSD.

| Button | Label | Action |
|---|---|---|
| `T2`{: .vab} | `LAST PAN`{: .mpd} | Back to where you last panned to. |
| `T4`{: .vab} / `T6`{: .vab} | arrows | Turns the map a degree left or right. Held, it turns at 40° a second. |
| `T5`{: .vab} | `HDG>`{: .mpd} | Turns the map to a heading typed on the KU. |
| `L1`{: .vab} | `POINT>`{: .mpd} | Pans to a point (`W01`, `C51`, `T01`) or a grid typed on the KU. |
| `L2`{: .vab} / `L5`{: .vab} | arrows | Pans to the next or the last waypoint of the route, with the leg to it up the page. Held, it steps twice a second. |
| `L3`{: .vab} / `L4`{: .vab} | arrows | Moves forward or back along the route, a twentieth of the map at a time. Held, it runs along the route. |
| `B4`{: .vab}–`B6`{: .vab} | | WPT, RTE and THRT. |

**Cursor Enter** on the map pans to the spot under the cursor. ZOOM, SC, CTR and FRZ are on the right as usual. **RPT** is not simulated.

### Data block

Along the bottom of the root page, in the NAV phase:

- the point you are flying to, its distance in km, your ground speed in knots, and the time to reach it, blank at 15 kt or less;
- **ENDR**: endurance on the fuel you have, at your current burn rate;
- **WIND**: direction and speed, or **CALM** below 5 kt.

## SHOW {#show}

SHOW chooses what each phase draws. A filled box beside a label means it is shown.

| Button | NAV phase | ATK phase |
|---|---|---|
| `T1`{: .vab} | **HSI**: a compass rose around your aircraft | Same |
| `L1`{: .vab} | **INACTIVE ZONES**: zones that are not active. Off by default. | Same. On by default. |
| `L2`{: .vab} | **AREAS**: engagement areas. Off by default. | Same. On by default. |
| `L3`{: .vab} | **LINES**: lines from the DTC. Off by default. | Same. Off by default. |
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

The active zones are always drawn. **RFI THREATS** and **OBSTACLES** are not simulated.

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

## ZN {#zn}

`B3`{: .vab} **ZN** is where you draw **priority fire (PF)** and **no fire (NF)** zones, with the [MPD cursor](#cursor) on a frozen map. The radar uses them to sort its targets: see [Zones]({{ '/targeting/fcr/' | relative_url }}#zones). Press **ZN** again to return to the TSD. **PAN** works from here too.

{% include fig.html id="mpd-tsd-zn" %}

`L1`{: .vab} **TYPE** switches the page between **PF** and **NF** zones. While you draw, the other type's inactive zones are hidden, and every zone of the type you are working on is shown.

### Drawing a zone

`L6`{: .vab} **DR** sets how a zone is drawn:

- **BX**, box: two cursor presses on opposite corners give a box square to the map.
- **LN**, lines: four cursor presses give its four corners, in order.

Put the cursor on the map and press **Cursor Enter** for each corner. A corner that would make the sides cross, or leave the zone with no area, is refused. While a zone is being drawn, `B2`{: .vab} shows **CLR** in place of PHASE: each press takes back the last corner.

### PF zones

| Button | Label | Action |
|---|---|---|
| `L2`{: .vab} | `OPT`{: .mpd} | How the zones are made: **AUTO**, **MAN** or **TRP**. See below. |
| `L3`{: .vab} | `ACT`{: .mpd} | Steps the active PF zone through the zones drawn, then none. Shown once there are PF zones. |
| `L4`{: .vab} | `DEL`{: .mpd} | Deletes all the PF zones, after `L2`{: .vab} **YES**. `L3`{: .vab} **NO** cancels. |
| `L5`{: .vab} | `#Z`{: .mpd} or `KM`{: .mpd} | AUTO and MAN: how many zones, 1 to 8. TRP: the size of each square, 1 to 3 km. |
| `T4`{: .vab} | `ASN`{: .mpd} | Opens the assign list. Choose a zone (`T2`{: .vab} PF1, `T1`{: .vab} PF2, `L1`{: .vab}–`L6`{: .vab} PF3–PF8), then `B6`{: .vab} **OWN** to make it yours and active. `T4`{: .vab} returns. |

| OPT | You draw | You get |
|---|---|---|
| **AUTO** | One zone. | That zone cut into **#Z** strips of equal width, parallel to its first side and numbered from it. |
| **MAN** | **#Z** zones, one after another. | Each zone as drawn. |
| **TRP** | One cursor press, on a target reference point. | Four squares of **KM** a side around it: PF1 upper left, PF2 upper right, PF3 lower right, PF4 lower left. |

A new set of PF zones replaces the old ones. PF1 becomes active and is assigned to you (OWN).

### NF zones

| Button | Label | Action |
|---|---|---|
| `T1`{: .vab} | `ACTIVE`{: .mpd} | **MULTI**: any number of NF zones can be active. **SINGLE**: only one. Can only be changed while the radar is off or not fitted. |
| `L2`{: .vab} | `SEL`{: .mpd} | Chooses the NF zone to work on, NF1 to NF8: `T2`{: .vab} NF1, `T1`{: .vab} NF2, `L1`{: .vab}–`L6`{: .vab} NF3–NF8. |
| `L3`{: .vab} | `ACT`{: .mpd} | Makes the chosen NF zone active, or not. Boxed while it is active. |
| `L4`{: .vab} | `DEL`{: .mpd} | Deletes the chosen NF zone, after `L2`{: .vab} **YES**. |

An NF zone is stored, and made active, as soon as its last corner is placed. **SEL** then moves on to the next empty zone.

**SEND**, **XMIT BOTH** and the PF page's **OWN** are not simulated: there is no datalink to share zones with.

### Zones on the map {#zones-on-the-map}

| Item | Drawn as |
|---|---|
| **PF zone** | White and dashed. The active one has alternating dashes. Each is labelled PF1 to PF8, except the active one; the one assigned to you is labelled **OWN**. |
| **NF zone** | Yellow and dashed, labelled NF1 to NF8. Active ones have alternating dashes. |
| **Line** | By its ident: **FLOT** blue, **FLET** red, **FSCL** white, boundary (**BL**) and phase (**PL**) lines green. A phase line has its ident at both ends. |
| **Area** | Red, labelled **EA01** to **EA12**. |

Active zones are always drawn; inactive zones, lines and areas follow [SHOW](#show). With a great many dashed edges on the map at once, zoomed in on large zones, the last ones drawn are solid. Lines and areas come from a [DTC]({{ '/mission/planner/' | relative_url }}#dtc): they cannot be drawn in the cockpit.

## COORD {#coord}

`T5`{: .vab} **COORD** lists the stored points, six to a page. `B2`{: .vab} and `B3`{: .vab} page back and forward, wrapping round at the ends.

{% include fig.html id="mpd-coord" %}

| Button | Label | Lists |
|---|---|---|
| `T1`{: .vab} | `WPTHZ`{: .mpd} | Waypoints and hazards. |
| `T2`{: .vab} | `CTRLM`{: .mpd} | Control measures. |
| `T3`{: .vab} | `LINE`{: .mpd} | Lines, three to a page: each line's number and ident, with a row for each of its points' grid and altitude. |
| `T4`{: .vab} | `AREA`{: .mpd} | Engagement areas, the same way. |
| `T5`{: .vab} | `COORD`{: .mpd} | Targets and threats. Pressed again, returns to the TSD. |
| `T6`{: .vab} | `SHOT`{: .mpd} | Your last Hellfire shots: missile type, time and where they were fired at. |
| `R1`{: .vab}–`R6`{: .vab} | | Expands that line with the time and distance to the point, its bearing, and its latitude and longitude. |
| `L1`{: .vab}–`L6`{: .vab} | | Makes that line's point your [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq). |

Every list shows all its slots: empty ones are blank. **SRCH** and **FARM** are not simulated.

## ABR {#abr}

`T4`{: .vab} **ABR**, on the WPT and THRT pages, lists every ident the aircraft knows, with its name and icon, over several pages (`B2`{: .vab} **PAGE**). `B4`{: .vab}–`B6`{: .vab} return to WPT, RTE or THRT, and `T4`{: .vab} back to the TSD.
