---
title: FCR page
lead: The fire control radar display — ground and air targeting formats, radar map and terrain profile, buttons and target symbols.
keywords: [fcr, radar, longbow, gtm, atm, rmap, tpm, nts, ants, c scp, cscope, scan, centerline, target symbols, lobl, loal, terrain profile, clearance, tgt, store, zoom, cursor, zone]
seats: [PLT, CPG]
redirect_from:
  - /mpd-fcr.html
---

The FCR page is selected with the FCR button. An aircraft without the radar installed displays FCR NOT INSTALLED. Scanning, mode selection and engagement are described in [Fire control radar]({{ '/targeting/fcr/' | relative_url }}).

The page follows the radar mode, which is selected with the mode bindings:

| Mode | Display |
|---|---|
| GTM, ground targeting mode | Ground targets ahead, in a sector |
| ATM, air targeting mode | Moving aircraft and helicopters around the aircraft, on a circle |
| RMAP, radar map | The GTM sector with an image of the terrain returns behind the targets |
| TPM, terrain profile mode | The terrain ahead and its clearance below the aircraft; no targets |

{% include fig.html id="mpd-fcr" %}

## Scope

Ownship is at the bottom of the GTM scan sector, or the center of the ATM scan sector. Range arcs are at 2, 4, 6 and 8 km. The scan sector symbol for the selected scan size is presented in full intensity; the wider scan sectors are presented in partial intensity. In ATM, the wide scan sector covers all azimuths except approximately 12° either side of the tail.

The display is drawn about the radar centerline, not the nose: with the centerline slewed 30° right, the center of the sector is 30° right of the nose.

While the FCR is transmitting, the scan wiper symbol moves across the scan sector with the antenna: white during a single scanburst, green during continuous scan.

### Data around the scope

| Item | Display |
|---|---|
| Heading scale | Magnetic heading; along the bottom of the heading scale, the FCR centerline bearing (solid mark), the last scan direction, the command heading chevron and the alternate sensor bearing |
| Total target count status window, top right | Total number of targets detected within the scanburst |
| HAD sight select status and range and range source status fields, bottom left | Selected sight (such as `C-FCR`{: .mpd}, `P-HMD`{: .mpd}, `TADS`{: .mpd}, or `TADSL`{: .mpd} when linked) and the range with its source. See [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}) |
| FOR symbols, bottom center | Field of regard, with the field of view box (TADS line of sight) and the cued LOS dot (acquisition source) |
| HAD weapon status field, bottom right | The actioned weapon: for the pilot, its status (rounds, rocket type and quantity, or missile trajectory and mode); for the CPG, `CGUN`{: .mpd}, `CRKT`{: .mpd} or `CMSL`{: .mpd}; `COOP`{: .mpd} in a cooperative rocket engagement |
| Elevation scale, lower left | Antenna elevation pointer; fixed (ELEV is AUTO) |

## Buttons

| Button | Label | Function |
|---|---|---|
| `T1`{: .vab} | `C SCP`{: .mpd} | Presents the FCR target symbols in the C-scope format on that crew station's flight and weapon symbology formats, or in the TADS video when selected. Boxed when on. Crewstation independent. |
| `L1`{: .vab} | `NTS`{: .mpd} | Steps the next-to-shoot to the next target; equivalent to the Arma **Lock target** binding |
| `L2`{: .vab} / `R2`{: .vab} | arrows | Slews the scan centerline left or right. See [Fire control radar]({{ '/targeting/fcr/' | relative_url }}#centerline) |
| `L4`{: .vab} | `TGT`{: .mpd} | Selects [TGT](#tgt), for storing radar targets as target points; boxed while selected |
| `L5`{: .vab} | `ALL`{: .mpd} | With TGT selected: stores every target symbol on the page |
| `R1`{: .vab} | `ZOOM`{: .mpd} | GTM only: [zoom](#zoom) on an area selected with the cursor, or return |
| `R6`{: .vab} | `ACQ`{: .mpd} | [Acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list |
| `B1`{: .vab} | | MENU page |

NTS, TGT, RF HO and the arrows are displayed only with FCR as the sight. NTS and the arrows operate only for the crew station that [owns the radar]({{ '/targeting/fcr/' | relative_url }}#owner).

UTIL, RF HO and ELEV are not simulated, nor is ZOOM in RMAP.

## Target selection with the cursor {#cursor}

With FCR as the sight, the [MPD cursor]({{ '/displays/mpd/' | relative_url }}#cursor) selects a target on the GTM, ATM or RMAP page. Over the scan area the cursor is displayed as a white X; over a target symbol, the symbol is drawn over a black circle. Cursor Enter then:

- stores the target, with [TGT](#tgt) selected; or
- makes it the NTS, for the crew station that [owns the radar]({{ '/targeting/fcr/' | relative_url }}#owner).

After the first scan of a burst, the cursor is placed on `L1`{: .vab} NTS for the owning crew station, so that Cursor Enter steps the NTS. It is not repositioned after a target has been selected with it.

## TGT {#tgt}

`L4`{: .vab} TGT stores radar targets as target points. It is selectable only with FCR as the sight and targets displayed, and can be deselected at any time.

While TGT is selected:

- a window at the top right displays the target point at which the next target will be stored, and below it the points stored since TGT was selected, latest last;
- Cursor Enter on a target stores it;
- `L5`{: .vab} ALL stores every target symbol on the page;
- RF HO, ELEV, the centerline arrows and ACQ are removed.

Targets are stored at the next free number from `T01`{: .mpd} to `T50`{: .mpd}. A target already stored since TGT was selected is not stored again, even after a scan has moved it.

## ZOOM {#zoom}

In GTM, `R1`{: .vab} ZOOM places a white box with an X on the cursor, sized by the scan size. The box is placed over the area of interest and Cursor Enter pressed: the page enlarges that area, approximately six times in a wide scan. Outside the target area the normal cursor is displayed. ZOOM again returns to the full display.

## Target symbols

FCR target symbols indicate the target type and whether it is moving or stationary. Symbols are yellow; a symbol in partial intensity is a weaker return, sorted to the end of the list.

<div class="table-wrap" markdown="1">

| Target | LOBL (stationary, within 1.5 km) | LOAL (stationary, beyond 1.5 km) | Moving |
|---|---|---|---|
| Air defense unit | <img class="sym" src="{{ '/assets/icons/fcr/mpd/aduLOBL.png' | relative_url }}" alt="Solid triangle"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/aduLOAL.png' | relative_url }}" alt="Outline triangle"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/aduMOVE.png' | relative_url }}" alt="Solid triangle with a dot"> |
| Tracked | <img class="sym" src="{{ '/assets/icons/fcr/mpd/trackLOBL.png' | relative_url }}" alt="Solid track symbol"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/trackLOAL.png' | relative_url }}" alt="Outline track symbol"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/trackMOVE.png' | relative_url }}" alt="Track symbol with a dot"> |
| Wheeled | <img class="sym" src="{{ '/assets/icons/fcr/mpd/wheelLOBL.png' | relative_url }}" alt="Solid circle"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/wheelLOAL.png' | relative_url }}" alt="Outline circle"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/wheelMOVE.png' | relative_url }}" alt="Solid circle with a dot"> |
| Helicopter | <img class="sym" src="{{ '/assets/icons/fcr/mpd/heliLOBL.png' | relative_url }}" alt="Solid bow tie"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/heliLOAL.png' | relative_url }}" alt="Outline bow tie"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/heliMOVE.png' | relative_url }}" alt="Bow tie with a dot"> |
| Unknown | <img class="sym" src="{{ '/assets/icons/fcr/mpd/unkLOBL.png' | relative_url }}" alt="Solid square"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/unkLOAL.png' | relative_url }}" alt="Outline square"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/unkMOVE.png' | relative_url }}" alt="Square with a dot"> |
| Flyer | <img class="sym" src="{{ '/assets/icons/fcr/mpd/flyer.png' | relative_url }}" alt="Flyer symbol"> | | |

</div>

The 1.5 km distinction selects the symbol only; it does not determine the missile launch mode.

The active [zones]({{ '/targeting/fcr/' | relative_url }}#zones) are presented on the GTM and ATM formats as on the TSD: the active priority fire (PF) zone in white, active no fire (NF) zones in yellow. They are not presented in RMAP.

| Symbol | Meaning |
|---|---|
| <img class="sym" src="{{ '/assets/icons/fcr/mpd/nts.png' | relative_url }}" alt="Diamond"> | NTS symbol, next-to-shoot: the highest priority target, assigned to an RF Hellfire |
| <img class="sym" src="{{ '/assets/icons/fcr/mpd/nts_noMSL.png' | relative_url }}" alt="Dashed diamond"> | NTS symbol, dashed: no weapon system actioned |
| <img class="sym" src="{{ '/assets/icons/fcr/mpd/ants.png' | relative_url }}" alt="Inverted triangle"> | ANTS symbol, alternate next-to-shoot: the second priority target |
| <img class="sym" src="{{ '/assets/icons/fcr/mpd/shotAT.png' | relative_url }}" alt="Green cross"> | Shot-at symbol: a location at which a Hellfire missile has been launched |
| <img class="sym" src="{{ '/assets/icons/fcr/mpd/fcrObstacle.png' | relative_url }}" alt="Obstacle symbol"> | Obstacle symbol, in TPM |
{: .sym-table}

The radar also detects clutter: false ground returns, two or three at a time, displayed as unknown or vehicle symbols that change from scan to scan.

## RMAP

The radar map is the GTM page with an image of terrain return strength behind the targets: brighter for a stronger return, black where terrain is masked from the radar. The near half, to 4 km, is painted during the near bar; the far half, 4 to 8 km, during the far bar. The image remains after a scan until the next scan starts.

Selecting RMAP again toggles the image. The buttons are as in GTM.

## TPM

The terrain profile mode supports low-level flight at night and in poor visibility. It scans 2.5 km ahead, across 180° below 45 kt and 90° above 55 kt, and shades the terrain against a clearance plane set below the aircraft's wheels:

| Shade | Terrain |
|---|---|
| Black | Below the clearance plane: clear |
| Dark gray | Above the clearance plane, below the aircraft |
| White | At or above the aircraft's height |
| Gray | Masked from the radar, or not measured |

Up to four terrain profile lines indicate the greatest elevation detected at set ranges. Obstacle symbols mark towers and masts of 8 m or more, or any object of 13 m or more, and the total obstacle count status window at the top right presents their number.

| Button | Label | Function |
|---|---|---|
| `T1`{: .vab} | `C SCP`{: .mpd} | Presents the terrain profile lines and obstacle symbols in the C-scope format |
| `L1`{: .vab} | `PROF`{: .mpd} | Terrain profile line ranges. GEOM: 100–300, 300–500, 500–1,000 and 1,000–2,500 m. ARITH: four equal bands from 100 to 2,500 m. TEST: 500, 1,000, 1,500 and 2,000 m |
| `L2`{: .vab} | `LINES`{: .mpd} | Number of terrain profile lines, 0 to 4 |
| `R1`{: .vab} | `CLEARANCE`{: .mpd} | Clearance plane: 20, 50, 100 or 200 ft below the aircraft |
| `R2`{: .vab} | `ELEV`{: .mpd} | Antenna elevation: FAR (near level, terrain to 2.5 km) or NEAR (depressed, close terrain) |
| `B1`{: .vab} | | MENU page |

PROF, CLEARANCE and ELEV are changed only by the crew station that owns the radar.
