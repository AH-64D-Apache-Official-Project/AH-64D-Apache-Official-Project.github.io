---
title: VIDEO page
lead: Sensor video on the MPD. The TADS picture, or either crew station's night vision, with its symbology, and as an underlay beneath the other pages.
keywords: [video, vid, tads, pnvs, underlay, symbology, wide, norm, zoom, color, gray scale, c-flt, p-flt, mpd video]
seats: [PLT, CPG]
---

Open it with the **VID** button. It shows the picture from a sensor, with the matching symbology on top: the CPG's TADS symbology over the TADS, or a crew station's flight symbology over its night vision.

The first time you open it, it picks a sensor for you: the CPG gets the CPG's sight, the pilot their own helmet's night vision.

## Two views

The page opens on the **video view**: the picture fills the screen, with only these buttons:

| Button | Label | Action |
|---|---|---|
| `T6`{: .vab} | the source's symbology, e.g. `TADS`{: .mpd} | Opens the **menu view**. |
| `L1`{: .vab}–`L3`{: .vab} | `W` `N` `Z` | Picture size: wide, normal or zoomed in. |
| `B1`{: .vab} | | MENU. |

The symbology is drawn on the picture only in the video view.

{% include fig.html id="mpd-video" %}

## Menu view

| Button | Label | Action |
|---|---|---|
| `T6`{: .vab} | symbology | Back to the video view. |
| `L1`{: .vab}–`L3`{: .vab} | `WIDE` `NORM` `ZOOM` | **VIEW**: picture size. |
| `L6`{: .vab} | `COLOR`{: .mpd} | **WHITE** or **GREEN** picture. |
| `R1`{: .vab}–`R6`{: .vab} | | **UNDERLAY**: the source, below. |
| `B2`{: .vab} | `SYMB`{: .mpd} | **NORM**, or a dimmed picture so the symbology stands out. |
| `B3`{: .vab} | `RESET`{: .mpd} | VIEW back to NORM and COLOR back to WHITE. |
| `B6`{: .vab} | `G/S`{: .mpd} | Gray scale: a strip of reference shades for setting up the picture. |

**VCR** and **SHARP** are not simulated.

### Sources

| Button | Source | Picture | Symbology |
|---|---|---|---|
| `R1`{: .vab} | **TADS** | The TADS: FLIR or day TV, whichever is selected. Nothing for the direct view optics. | TADS |
| `R2`{: .vab} | **CPG SIGHT** | The TADS while the CPG's sight is the TADS or FCR, otherwise the CPG's night vision. | TADS, C-FCR or C-FLT |
| `R3`{: .vab} | **CPG HMD** | The CPG's night vision sensor. | C-FLT |
| `R4`{: .vab} | **PLT SIGHT** | The pilot's night vision, or nothing while the pilot's sight is the FCR. | P-FLT or P-FCR |
| `R5`{: .vab} | **PLT HMD** | The pilot's night vision sensor. | P-FLT |
| `R6`{: .vab} | **NO VIDEO** | None. | |

A night vision source shows nothing while that crew station's NVS mode switch is OFF. A damaged sensor shows nothing either. See [Night vision]({{ '/targeting/nvs/' | relative_url }}).

## The underlay

The source you choose here also runs **under every other page** on this MPD, so you can watch the TADS behind the TSD or the WPN page. Choose **NO VIDEO** to take it away. Each MPD has its own source and settings.
