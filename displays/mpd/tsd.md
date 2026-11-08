---
title: Tactical situation display (TSD)
lead: The TSD is the primary means of interacting with the helicopter's navigation system — phases, symbols, the WPT, RTE, THRT, ZN, PAN, COORD and ABR pages, and the procedures for points and routes.
keywords: [tsd, tactical situation display, map, nav, atk, phase, scale, show, waypoint, route, threat, coord, abr, hsi, wind, endurance, cursor, frz, freeze, pan, zoom, caq, cursor acquisition, zn, zone, priority fire zone, no fire zone, pfz, nfz, trp, line, area, flot, flet, phase line]
seats: [PLT, CPG]
redirect_from:
  - /mpd-tsd.html
---

The TSD is selected with the TSD button on either MPD. It is the primary means of interacting with the helicopter's navigation system: waypoints, hazards, control measures, targets and threats are added, edited and deleted on the TSD with the KU. The map is heading up, with the ownship symbol near the bottom of the page (or in the center with CTR).

The TSD has no terrain map; it displays points, lines and symbols on a black background at the selected map scale. The Arma map provides terrain.

{% include fig.html id="mpd-tsd" %}

## Phases

The TSD has two phases, NAV and ATK, which provide decluttering options. The default phase is NAV. `B2`{: .vab} PHASE selects the phase. Each phase retains its own SHOW selections.

| | NAV | ATK |
|---|---|---|
| Next waypoint status window | Displayed, unless deselected in SHOW | Not displayed |
| FCR target symbols | The top 16 | All |
| Hazards | Always displayed | Selected in SHOW |

## Symbols

| Symbol | Meaning |
|---|---|
| Ownship symbol | The helicopter position, pointing up |
| Route line | Green lines connecting the points of the current route |
| Direct-to line | Green line from the point where direct-to was selected to the destination |
| Coordinate point icons | Waypoint/hazard (WPTHZ), control measure (CTRLM) and target/threat (THRT/TGT) icons; see [Points and routes]({{ '/mission/points/' | relative_url }}) |
| Friendly units | Blue symbols for friendly vehicles and aircraft reported over the datalink |
| FCR target symbols | As on the [FCR page]({{ '/displays/mpd/fcr/' | relative_url }}); at the 25 and 50 km scales, small yellow squares |
| Shot-at icon | An X at each location at which a Hellfire missile has been launched |
| RLWR threat icons | On the ASE footprint at their bearing; launch mode flashes. See [ASE]({{ '/weapons/ase/' | relative_url }}) |
| TADS footprint symbol | With TADS as the CPG's selected sight: a line from the ownship symbol to the TADS range, with a crosshair at its end |
| FCR footprint symbol | With FCR as sight (or the CPG linked TADS-FCR): the scan sector to 8 km; green for continuous scan or idle, white for a single scan |
| Zones | Priority fire (PF) zones white, no fire (NF) zones yellow; see [Zones on the map](#zones-on-the-map) |
| LINE and AREA icons | Lines and engagement areas from the [DTC]({{ '/mission/planner/' | relative_url }}#dtc) |

## TSD page buttons

| Button | Label | Function |
|---|---|---|
| `T2`{: .vab} | `ASE`{: .mpd} | [ASE page]({{ '/displays/mpd/ase/' | relative_url }}) |
| `T3`{: .vab} | `PAN`{: .mpd} | [PAN](#pan) |
| `T5`{: .vab} | `COORD`{: .mpd} | [COORD page](#coord) |
| `L6`{: .vab} | `SHOW`{: .mpd} | [SHOW](#show) |
| `R1`{: .vab} | `ZOOM`{: .mpd} | Magnifies the map scale by 20% about the ownship symbol, or returns; boxed while on |
| `R2`{: .vab} | `SC`{: .mpd} | Map scale: `R1`{: .vab} 50 km, `R2`{: .vab} 25 km, `R3`{: .vab} 10 km, `R4`{: .vab} 5 km |
| `R3`{: .vab} | `CTR`{: .mpd} | Ownship symbol at the bottom of the page or in the center |
| `R4`{: .vab} | `CAQ`{: .mpd} | Cursor acquisition; see [CAQ](#caq) |
| `R5`{: .vab} | `FRZ`{: .mpd} | Freezes the map; see [FRZ](#frz) |
| `R6`{: .vab} | `ACQ`{: .mpd} | [Acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list |
| `B1`{: .vab} | | MENU page |
| `B2`{: .vab} | `PHASE`{: .mpd} | NAV or ATK |
| `B3`{: .vab} | `ZN`{: .mpd} | [ZN](#zn) zone page |
| `B4`{: .vab} | `WPT`{: .mpd} | [WPT](#wpt) |
| `B5`{: .vab} | `RTE`{: .mpd} | [RTE](#rte) |
| `B6`{: .vab} | `THRT`{: .mpd} | [THRT](#thrt) |

ZOOM, CTR and FRZ operate the same on the WPT, THRT and PAN pages. RPT, PP, UTIL and ADF are not simulated.

## MPD cursor on the TSD {#cursor}

Over the map, the [MPD cursor]({{ '/displays/mpd/' | relative_url }}#cursor) is displayed as a white X. Where a page accepts a point, a point under the cursor is drawn over a black circle, and Cursor Enter selects it.

| Page | Cursor Enter on the map |
|---|---|
| TSD, with CAQ | Selects the point or FCR target as acquisition source |
| WPT or THRT, top level, DEL or EDT | Selects the point, as if entered with POINT> |
| WPT or THRT ADD | Adds a point of the selected type at the cursor, at ground level: ident `WP`, `TU`, `CP` or `TG` |
| RTE ADD | Selects the waypoint, hazard or control measure to insert |
| RTE DIR | Direct-to the point |
| PAN | Centers the map on the cursor position |
| ZN | Places a zone corner; see [ZN](#zn) |
| Any page with a GRID prompt on the KU | Enters the cursor's grid |

Points outside the map border cannot be selected.

## FRZ {#frz}

`R5`{: .vab} FRZ freezes the map; the dynamic ownship symbol (cyan) continues across the frozen map. The frozen ownship symbol is white with stopped rotors, and the map frozen cue, a bold dashed line, is displayed around the map border. ASE threat symbols rotate with the frozen map. FRZ again returns to the active map. PAN, CAQ and ZN freeze the map automatically.

## CAQ {#caq}

`R4`{: .vab} CAQ (cursor acquisition) freezes the map and selects the [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) with the MPD cursor:

1. CAQ (R4) – Select.
2. MPD cursor – Place on a waypoint, hazard, control measure, target, threat or FCR target.
3. Cursor Enter – Press. The point becomes the acquisition source.
{: .steps}

An FCR target selected with CAQ is stored as target point `T50`{: .mpd} and becomes the acquisition source; with the radar owned by that crew station, it also becomes the NTS. CAQ ends when a point is selected, when CAQ is selected again, or when the TSD top level is exited.

## PAN {#pan}

`T3`{: .vab} PAN freezes the map so that it can be moved. PAN again returns to the TSD.

| Button | Label | Function |
|---|---|---|
| `T2`{: .vab} | `LAST PAN`{: .mpd} | Returns to the last pan position |
| `T4`{: .vab} / `T6`{: .vab} | arrows | Rotates the map 1° left or right; held, 40° per second |
| `T5`{: .vab} | `HDG>`{: .mpd} | Rotates the map to a heading entered on the KU |
| `L1`{: .vab} | `POINT>`{: .mpd} | Pans to a point (`W01`, `C51`, `T01`) or a grid entered on the KU |
| `L2`{: .vab} / `L5`{: .vab} | arrows | Pans to the next or previous route waypoint, with the leg to it up the page; held, two steps per second |
| `L3`{: .vab} / `L4`{: .vab} | arrows | Moves along the route, one twentieth of the map per press; held, continuous |
| `B4`{: .vab}–`B6`{: .vab} | | WPT, RTE and THRT |

Cursor Enter on the map pans to the cursor position. ZOOM, SC, CTR and FRZ are on the right. RPT is not simulated.

## Status windows

Along the bottom of the TSD page in the NAV phase:

- **Next waypoint status window**: the destination point, distance to go in km, ground speed in knots, and time to go (blank at 15 kt or less);
- **ENDR**: endurance status window: total fuel endurance at the present power setting;
- **WIND**: wind direction/velocity status window; CALM below 5 kt.

## SHOW {#show}

The SHOW page manages the symbology displayed on the TSD page during the selected phase. A filled box beside a label indicates the item is displayed.

| Button | NAV phase | ATK phase |
|---|---|---|
| `T1`{: .vab} | HSI: magnetic compass rose around the ownship symbol | Same |
| `L1`{: .vab} | INACTIVE ZONES (default off) | Same (default on) |
| `L2`{: .vab} | AREAS: engagement areas (default off) | Same (default on) |
| `L3`{: .vab} | LINES: lines from the DTC (default off) | Same (default off) |
| `L4`{: .vab} | WAYPOINT DATA: the next waypoint status window | CURRENT ROUTE (no effect; the route is displayed in both phases) |
| `L5`{: .vab} | PLANNED TGT/THRT | Same |
| `R1`{: .vab} | CONTROL MEASURES (green) | Same |
| `R2`{: .vab} | ENEMY UNITS (red control measures) | Same |
| `R3`{: .vab} | FRIENDLY UNITS (blue control measures, and friendly units from the datalink) | Same |
| `R5`{: .vab} | RLWR THREATS | Same |
| `B3`{: .vab} | ENDR | Same |
| `B4`{: .vab} | | SHOT: shot-at icons |
| `B5`{: .vab} | WIND | Same |
| `B6`{: .vab} | | HAZARDS |
| `L6`{: .vab} | TSD page | Same |

Active zones are always displayed. RFI THREATS and OBSTACLES are not simulated.

## Data entry

Data entry pushbuttons, labeled with `>` (`POINT>`{: .mpd}, `IDENT>`{: .mpd}), enter data on the [keyboard unit]({{ '/displays/ku/' | relative_url }}). An invalid entry displays an error, which is cleared with Enter before the value is re-entered.

Points are identified by a letter and a number: **W01**–**W50** waypoints and hazards, **C51**–**C99** control measures, **T01**–**T50** targets and threats.

## WPT {#wpt}

`B4`{: .vab} WPT operates on waypoints, hazards and control measures.

| Button | Label | Function |
|---|---|---|
| `L1`{: .vab} | `POINT>`{: .mpd} | Selects a point by its identifier. The waypoint review status window at the top of the page displays its identifier, free text, estimated time enroute (ETE) and estimated time of arrival (ETA), grid, bearing and distance to go, latitude and longitude, and altitude. |
| `L2`{: .vab} | `ADD`{: .mpd} | Adds a point |
| `L3`{: .vab} | `DEL`{: .mpd} | Deletes the selected point after `L2`{: .vab} YES; `L3`{: .vab} NO cancels |
| `L4`{: .vab} | `EDT`{: .mpd} | Edits the selected point: `L1`{: .vab} presents the same entries as ADD, with the current values |
| `L5`{: .vab} | `STO`{: .mpd} | Stores the present position: `L1`{: .vab} NOW |
| `T4`{: .vab} | `ABR`{: .mpd} | [ABR page](#abr), the list of idents |
| `R3`{: .vab} | `CTR`{: .mpd} | As on the TSD page |

XMIT is not simulated.

### Adding a waypoint, hazard or control measure

1. TSD (FAB) – Press if a TSD page is not already displayed.
2. WPT (B4) – Select.
3. ABR (T4) – Select if the desired point type is unknown.
4. ADD (L2) – Select.
5. TYPE (L4 through L6) – Select WP, HZ or CM as desired.
6. IDENT (L1) – Press.
7. KU – Interact with.
   1. Enter the IDENT for the selected point (it must suit the point type; see [ABR](#abr)).
   2. Enter FREE text (maximum of 3 characters).
   3. Enter GRID (maximum of 8 characters). Present position is entered by default.
   4. Enter ALTITUDE (barometric, feet). The ground elevation at the grid is entered by default.
{: .steps}

The point takes the next free number of its type and becomes the selected point.

## RTE {#rte}

`B5`{: .vab} RTE builds the route. The route POINT buttons are on the right, `R2`{: .vab} to `R5`{: .vab}, with the first point at the bottom; the route scroll buttons, `R1`{: .vab} and `R6`{: .vab}, scroll the list. The active destination point is boxed.

| Button | Label | Function |
|---|---|---|
| `L2`{: .vab} | `ADD`{: .mpd} | `L1`{: .vab} POINT> selects a waypoint, hazard or control measure; the route POINT button at the insertion point is then pressed |
| `L3`{: .vab} | `DEL`{: .mpd} | A route POINT button is pressed to remove that point from the route |
| `L4`{: .vab} | `DIR`{: .mpd} | Direct-to: a route POINT button, or `L1`{: .vab} POINT> for any stored point |
| `L5`{: .vab} | `RVW`{: .mpd} | Review: a route POINT button displays that point's data in the RTE review status window; pressed again, clears it |

RTM is not simulated.

### Updating the current direct-to waypoint

1. TSD (FAB) – Press if a TSD page is not already displayed.
2. RTE (B5) – Select.
3. DIR (L4) – Select.
4. POINT (L1) – Select and enter the desired W##, C## or T## via the KU.
{: .steps}

### Route sequencing

When flying to a route point, the route sequences to the next point automatically abeam each point. Approximately one minute before a point the `WPT APRCH`{: .mpd} advisory is displayed, and on passing it `WPT PASSED`{: .mpd}, when neither crew station is displaying a TSD page. The destination point drives the FLT page command heading and navigation fly-to cue, the navigation data on the FLT and TSD pages, and the HMD navigation data and command heading chevron.

## THRT {#thrt}

`B6`{: .vab} THRT operates as WPT, on targets and threats (**T01**–**T50**, ident `TG` by default, or a threat type such as a SAM system). STO in the ATK phase stores a target at the present position.

## ZN {#zn}

`B3`{: .vab} ZN draws priority fire (PF) and no fire (NF) zones with the [MPD cursor](#cursor) on a frozen map. The radar uses the zones to prioritize targets; see [Zones]({{ '/targeting/fcr/' | relative_url }}#zones). ZN again returns to the TSD; PAN is available.

{% include fig.html id="mpd-tsd-zn" %}

`L1`{: .vab} TYPE selects PF or NF zones. While a zone is drawn, the other type's inactive zones are hidden and every zone of the selected type is displayed.

### Drawing a zone

`L6`{: .vab} DR selects the drawing method:

- **BX** (box): two cursor entries on opposite corners give a box aligned with the map.
- **LN** (lines): four cursor entries give the four corners in order.

A corner that would make the sides cross, or leave the zone without area, is rejected. While a zone is being drawn, `B2`{: .vab} displays CLR in place of PHASE; each press removes the last corner.

### PF zones

| Button | Label | Function |
|---|---|---|
| `L2`{: .vab} | `OPT`{: .mpd} | Zone creation method: AUTO, MAN or TRP |
| `L3`{: .vab} | `ACT`{: .mpd} | Steps the active PF zone through the zones drawn, then none; displayed once PF zones exist |
| `L4`{: .vab} | `DEL`{: .mpd} | Deletes all PF zones after `L2`{: .vab} YES; `L3`{: .vab} NO cancels |
| `L5`{: .vab} | `#Z`{: .mpd} or `KM`{: .mpd} | AUTO and MAN: number of zones, 1 to 8. TRP: square size, 1 to 3 km |
| `T4`{: .vab} | `ASN`{: .mpd} | Assignment list: select a zone (`T2`{: .vab} PF1, `T1`{: .vab} PF2, `L1`{: .vab}–`L6`{: .vab} PF3–PF8), then `B6`{: .vab} OWN to assign and activate it; `T4`{: .vab} returns |

| OPT | Drawn | Result |
|---|---|---|
| AUTO | One zone | The zone divided into #Z strips of equal width, parallel to its first side and numbered from it |
| MAN | #Z zones in sequence | Each zone as drawn |
| TRP | One cursor entry on a target reference point | Four squares of KM side around it: PF1 upper left, PF2 upper right, PF3 lower right, PF4 lower left |

A new set of PF zones replaces the previous set. PF1 becomes active and is assigned (OWN).

### NF zones

| Button | Label | Function |
|---|---|---|
| `T1`{: .vab} | `ACTIVE`{: .mpd} | MULTI: any number of NF zones active. SINGLE: one only. Changeable only with the radar off or not installed |
| `L2`{: .vab} | `SEL`{: .mpd} | Selects the NF zone, NF1 to NF8: `T2`{: .vab} NF1, `T1`{: .vab} NF2, `L1`{: .vab}–`L6`{: .vab} NF3–NF8 |
| `L3`{: .vab} | `ACT`{: .mpd} | Activates or deactivates the selected NF zone; boxed while active |
| `L4`{: .vab} | `DEL`{: .mpd} | Deletes the selected NF zone after `L2`{: .vab} YES |

An NF zone is stored and activated when its last corner is placed; SEL then advances to the next empty zone.

SEND, XMIT BOTH and the PF page OWN are not simulated (no datalink).

### Zones on the map {#zones-on-the-map}

| Item | Display |
|---|---|
| PF zone | White, dashed; the active zone has alternating dashes. Labeled PF1 to PF8, the assigned zone OWN |
| NF zone | Yellow, dashed, labeled NF1 to NF8; active zones have alternating dashes |
| LINE icon | By ident: FLOT blue, FLET red, FSCL white, boundary (BL) and phase (PL) lines green; a phase line has its ident at both ends |
| AREA icon | Red, labeled EA01 to EA12 |

Active zones are always displayed; inactive zones, lines and areas follow [SHOW](#show). Lines and areas are loaded from a [DTC]({{ '/mission/planner/' | relative_url }}#dtc) and cannot be drawn in the cockpit.

## COORD {#coord}

`T5`{: .vab} COORD lists the stored points, six per page. `B2`{: .vab} and `B3`{: .vab} page back and forward.

{% include fig.html id="mpd-coord" %}

| Button | Label | Lists |
|---|---|---|
| `T1`{: .vab} | `WPTHZ`{: .mpd} | Waypoints and hazards |
| `T2`{: .vab} | `CTRLM`{: .mpd} | Control measures |
| `T3`{: .vab} | `LINE`{: .mpd} | Lines, three per page: number, ident, and grid and altitude of each point |
| `T4`{: .vab} | `AREA`{: .mpd} | Engagement areas, as lines |
| `T5`{: .vab} | `COORD`{: .mpd} | Targets and threats; pressed again, returns to the TSD |
| `T6`{: .vab} | `SHOT`{: .mpd} | Recent Hellfire launches: missile type, time and aim point |
| `R1`{: .vab}–`R6`{: .vab} | | Point expansion buttons: expand that line with ETE, ETA, bearing, distance to go, latitude and longitude |
| `L1`{: .vab}–`L6`{: .vab} | | Acquisition selection buttons: select that line's point as [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) |

Empty slots are displayed blank. SRCH and FARM are not simulated.

## ABR {#abr}

`T4`{: .vab} ABR, on the WPT and THRT pages, lists every ident with its name and symbol over several pages (`B2`{: .vab} PAGE). `B4`{: .vab}–`B6`{: .vab} return to WPT, RTE or THRT, and `T4`{: .vab} to the TSD.
