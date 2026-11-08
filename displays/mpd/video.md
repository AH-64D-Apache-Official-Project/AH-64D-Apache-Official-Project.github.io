---
title: VIDEO page
lead: Sensor video on the MPD — the TADS, or either crew station's night vision — with its symbology, and as an underlay beneath other pages.
keywords: [video, vid, tads, pnvs, underlay, symbology, wide, norm, zoom, color, gray scale, c-flt, p-flt, mpd video]
seats: [PLT, CPG]
---

The VIDEO page is selected with the VID button. It presents sensor video with the corresponding symbology: weapon symbology over the TADS, or a crew station's flight symbology over its night vision sensor.

When first selected, the underlay defaults to the CPG's sight video for the CPG, and to the pilot's HMD underlay for the pilot.

## Decluttered mode

The default VIDEO page presentation is decluttered mode, with the Video Symbology Select (VSEL) button selected. The display is cleared of all button labels other than the VSEL button and the abbreviated VIEW buttons:

| Button | Label | Function |
|---|---|---|
| `T6`{: .vab} | VSEL: `TADS`{: .mpd}, `C-FLT`{: .mpd}, `P-FLT`{: .mpd}, `C-FCR`{: .mpd} or `P-FCR`{: .mpd} | Deselects decluttered mode |
| `L1`{: .vab}–`L3`{: .vab} | `W` `N` `Z` | VIEW: WIDE, NORM or ZOOM |
| `B1`{: .vab} | | MENU page |

Symbology is presented on the video in decluttered mode only.

{% include fig.html id="mpd-video" %}

## VSEL deselected

| Button | Label | Function |
|---|---|---|
| `T6`{: .vab} | VSEL | Selects decluttered mode |
| `L1`{: .vab}–`L3`{: .vab} | `WIDE` `NORM` `ZOOM` | VIEW: the video view mode |
| `L6`{: .vab} | `COLOR`{: .mpd} | WHITE or GREEN video |
| `R1`{: .vab}–`R6`{: .vab} | | UNDERLAY: see below |
| `B2`{: .vab} | `SYMB`{: .mpd} | NORM, or dimmed video for symbology contrast |
| `B3`{: .vab} | `RESET`{: .mpd} | VIEW to NORM and COLOR to WHITE |
| `B6`{: .vab} | `G/S`{: .mpd} | Grayscale reference strip |

VCR and SHARP are not simulated.

### Underlay buttons

| Button | Underlay | Video | Symbology |
|---|---|---|---|
| `R1`{: .vab} | TADS | TADS FLIR or DTV, whichever is selected; none for the DVO | TADS |
| `R2`{: .vab} | CPG SIGHT | The TADS with the CPG's sight TADS or FCR; otherwise the CPG's night vision | TADS, C-FCR or C-FLT |
| `R3`{: .vab} | CPG HMD | The CPG's night vision sensor | C-FLT |
| `R4`{: .vab} | PLT SIGHT | The pilot's night vision; none with the pilot's sight FCR | P-FLT or P-FCR |
| `R5`{: .vab} | PLT HMD | The pilot's night vision sensor | P-FLT |
| `R6`{: .vab} | NO VIDEO | None | |

Over TADS video, the [image auto track (IAT)]({{ '/targeting/tads/' | relative_url }}#iat) gates are presented while tracking.

A night vision underlay displays no video while that crew station's NVS MODE switch is OFF, or with the sensor damaged. See [Night vision]({{ '/targeting/nvs/' | relative_url }}).

## Underlay

The selected underlay is also displayed beneath every other page on that MPD (for example, the TADS behind the TSD or WPN page). NO VIDEO removes it. Each MPD has its own underlay and settings.
