---
title: FCR page
lead: The fire control radar's display. Its ground and air targeting formats, the radar map and the terrain profile, the buttons, and what each symbol means.
keywords: [fcr, radar, longbow, gtm, atm, rmap, tpm, nts, ants, c scp, cscope, scan, centerline, target symbols, lobl, loal, terrain profile, clearance]
seats: [PLT, CPG]
redirect_from:
  - /mpd-fcr.html
---

Open it with the **FCR** button. Only an aircraft with the radar fitted has one; any other shows **FCR NOT INSTALLED**. How to scan, choose a mode and engage with the radar is on the [Fire control radar]({{ '/targeting/fcr/' | relative_url }}) page.

The page follows the radar's mode, which is set with the mode keys, not on the page:

| Mode | Shows |
|---|---|
| **GTM**, ground targeting | Ground targets ahead, in a wedge. |
| **ATM**, air targeting | Moving aircraft and helicopters all round, on a circle. |
| **RMAP**, radar map | The GTM wedge with a picture of the terrain the radar sees behind the targets. |
| **TPM**, terrain profile | The terrain ahead and whether it clears you. No targets. |

{% include fig.html id="mpd-fcr" %}

## The scope

Your aircraft is at the bottom of the GTM wedge, or the centre of the ATM circle. The arcs are every 2 km, out to 8 km. The **sector being scanned** is drawn bright, set by the scan size; the rest of the wide sector stays dim. In ATM the wide sector covers everything except about 12° either side of the tail.

The display is drawn about the radar's **centerline**, not the nose: slew the centerline 30° right and the middle of the wedge looks 30° right of the nose.

While the radar scans, the **scan bar** sweeps across the sector: green for a continuous scan, white for a single scan.

### Around the scope

| Item | Shows |
|---|---|
| **Heading tape** | Your heading. Below it: the FCR centerline (the solid mark), where the last scan looked, the next waypoint's bearing (the caret), and the other crew station's sensor. |
| **Target count**, top right | How many targets the radar has. |
| **Sight and range**, bottom left | Your sight (such as `C-FCR`{: .mpd}, `P-HMD`{: .mpd}, `TADS`{: .mpd}, or `TADSL`{: .mpd} while linked) and the range with its source. See [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}). |
| **Sensor window**, bottom centre | Where the TADS is looking, as a box, and where your acquisition source points, as a diamond. |
| **Weapon**, bottom right | The weapon actioned: for the pilot's, its state (rounds, rocket type and count, or the missile trajectory and mode); for the CPG's, `CGUN`{: .mpd}, `CRKT`{: .mpd} or `CMSL`{: .mpd}. `COOP`{: .mpd} in a cooperative rocket engagement. |
| **Elevation scale**, far left | The antenna elevation. It does not move: ELEV is always AUTO. |

## Buttons

| Button | Label | Action |
|---|---|---|
| `T1`{: .vab} | `C SCP`{: .mpd} | Shows the radar's targets on your helmet display, at their places in the outside world, or in the TADS picture when it is up. Boxed when on. Only on your own display. |
| `L1`{: .vab} | `NTS`{: .mpd} | Steps the next-to-shoot to the next target. The same as Arma's **Lock target** key. |
| `L2`{: .vab} / `R2`{: .vab} | arrows | Slews the scan centerline left or right. See [Fire control radar]({{ '/targeting/fcr/' | relative_url }}#centerline). |
| `L4`{: .vab} | `TGT`{: .mpd} | Stores the NTS as the next free target point, **T01** to **T50**. Barriered while there is no NTS. |
| `R6`{: .vab} | `ACQ`{: .mpd} | Opens the [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list. |
| `B1`{: .vab} | | MENU. |

`NTS`, `TGT`, `RF HO` and the arrows are shown only while the FCR is your sight. NTS and the arrows work only for the crew station that [owns the radar]({{ '/targeting/fcr/' | relative_url }}#owner).

**UTIL**, **ZOOM**, **RF HO** and **ELEV** are not simulated.

## Target symbols

Each symbol shows what the target is and how it sits. Symbols are yellow; a **dim** one is a weaker return, sorted to the end of the list.

<div class="table-wrap" markdown="1">

| Target | Stationary, within 1.5 km | Stationary, beyond 1.5 km | Moving |
|---|---|---|---|
| Air defence unit | <img class="sym" src="{{ '/assets/icons/fcr/mpd/aduLOBL.png' | relative_url }}" alt="Solid triangle"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/aduLOAL.png' | relative_url }}" alt="Outline triangle"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/aduMOVE.png' | relative_url }}" alt="Solid triangle with a dot"> |
| Tracked vehicle | <img class="sym" src="{{ '/assets/icons/fcr/mpd/trackLOBL.png' | relative_url }}" alt="Solid track symbol"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/trackLOAL.png' | relative_url }}" alt="Outline track symbol"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/trackMOVE.png' | relative_url }}" alt="Track symbol with a dot"> |
| Wheeled vehicle | <img class="sym" src="{{ '/assets/icons/fcr/mpd/wheelLOBL.png' | relative_url }}" alt="Solid circle"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/wheelLOAL.png' | relative_url }}" alt="Outline circle"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/wheelMOVE.png' | relative_url }}" alt="Solid circle with a dot"> |
| Helicopter | <img class="sym" src="{{ '/assets/icons/fcr/mpd/heliLOBL.png' | relative_url }}" alt="Solid bow tie"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/heliLOAL.png' | relative_url }}" alt="Outline bow tie"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/heliMOVE.png' | relative_url }}" alt="Bow tie with a dot"> |
| Unknown | <img class="sym" src="{{ '/assets/icons/fcr/mpd/unkLOBL.png' | relative_url }}" alt="Solid square"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/unkLOAL.png' | relative_url }}" alt="Outline square"> | <img class="sym" src="{{ '/assets/icons/fcr/mpd/unkMOVE.png' | relative_url }}" alt="Square with a dot"> |
| Aircraft | <img class="sym" src="{{ '/assets/icons/fcr/mpd/flyer.png' | relative_url }}" alt="Aircraft symbol"> | | |

</div>

The 1.5 km split is only how the symbol is drawn. It does not decide how a missile is launched.

| Symbol | Meaning |
|---|---|
| <img class="sym" src="{{ '/assets/icons/fcr/mpd/nts.png' | relative_url }}" alt="Diamond"> | **NTS**, the next-to-shoot: the target a radar-guided Hellfire will be given. |
| <img class="sym" src="{{ '/assets/icons/fcr/mpd/nts_noMSL.png' | relative_url }}" alt="Dashed diamond"> | The NTS while no weapon is actioned. |
| <img class="sym" src="{{ '/assets/icons/fcr/mpd/ants.png' | relative_url }}" alt="Inverted triangle"> | **ANTS**, the alternate: the target NTS steps to next. |
| <img class="sym" src="{{ '/assets/icons/fcr/mpd/shotAT.png' | relative_url }}" alt="Green cross"> | **Shot at**: where a missile has been fired. |
| <img class="sym" src="{{ '/assets/icons/fcr/mpd/fcrObstacle.png' | relative_url }}" alt="Obstacle symbol"> | An obstacle, in TPM. |
{: .sym-table}

The radar also picks up some **clutter**: false returns from the ground, two or three at a time, that look like unknown or vehicle symbols and come and go from one scan to the next.

## RMAP

The radar map is the GTM page with a picture behind the targets: the strength of the radar return from the terrain, brighter for stronger, black where the terrain is hidden from the radar. The near half, to 4 km, is painted as the bar sweeps one way, the far half, 4 to 8 km, as it sweeps back. The picture stays up after a scan until the next one starts.

Select RMAP again to turn the picture off and on. The buttons are the same as GTM's.

## TPM

The terrain profile mode is for flying low at night and in bad weather. It scans ahead 2.5 km, across 180° below 45 knots and 90° above 55 knots, and shades the terrain against a **clearance plane** set below your wheels:

| Shade | Terrain |
|---|---|
| Black | Below the clearance plane: clear. |
| Dark grey | Above the clearance plane but below you. |
| White | At or above your height. |
| Grey | Hidden from the radar, or not measured. |

Up to four **profile lines** join the highest terrain the radar sees at set distances. Obstacles, such as towers and masts at least 8 m high or anything 13 m high, are marked, and their number shows top right.

| Button | Label | Action |
|---|---|---|
| `T1`{: .vab} | `C SCP`{: .mpd} | Shows the profile lines and obstacles on your helmet display. |
| `L1`{: .vab} | `PROF`{: .mpd} | Where the profile lines are taken. **GEOM**: 100–300, 300–500, 500–1,000 and 1,000–2,500 m. **ARITH**: four equal bands from 100 to 2,500 m. **TEST**: 500, 1,000, 1,500 and 2,000 m. |
| `L2`{: .vab} | `LINES`{: .mpd} | How many profile lines are drawn, 0 to 4. |
| `R1`{: .vab} | `CLEARANCE`{: .mpd} | The clearance plane: 20, 50, 100 or 200 ft below you. |
| `R2`{: .vab} | `ELEV`{: .mpd} | The antenna's look: **FAR**, nearly level, for terrain out to 2.5 km, or **NEAR**, tilted down, for close terrain. |
| `B1`{: .vab} | | MENU. |

PROF, CLEARANCE and ELEV can only be changed by the crew station that owns the radar.
