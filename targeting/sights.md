---
title: Sights and acquisition
lead: Your sight is what your weapons are aimed with. Your acquisition source is where your sight is cued to look. Both are chosen per crew station.
keywords: [sight, hmd, tads, fcr, link, acquisition, acq, slave, cue, cueing dots, range, store, target point]
seats: [PLT, CPG]
redirect_from:
  - /targeting-sights.html
---

## Sights

Each crew station selects one sight. The weapons that crew station fires are aimed with it.

| Sight | Binding | Who | Aims with |
|---|---|---|---|
| **HMD** | {% include key.html id="fza_ah64_v30_sightSelectHMD" %} | Both | Your head, through the helmet. |
| **TADS** | {% include key.html id="fza_ah64_v30_sightSelectTADS" %} | CPG only | The TADS turret under the nose. See [TADS]({{ '/targeting/tads/' | relative_url }}). |
| **FCR** | {% include key.html id="fza_ah64_v30_sightSelectFCR" %} | Both, with the radar fitted | The radar's next-to-shoot target. See [Fire control radar]({{ '/targeting/fcr/' | relative_url }}). |

The selected sight shows on the left of the [HAD]({{ '/displays/ihadss/' | relative_url }}) at the bottom of your helmet symbology, with a `P-` or `C-` prefix for the HMD and FCR (`P-HMD`{: .mpd}, `C-FCR`{: .mpd}), and on the [WPN page]({{ '/displays/mpd/wpn/' | relative_url }}).

The HMD needs the IHADSS helmet. Without it there is no head tracking, and head-aimed sights look along the aircraft's nose instead.

Without AC power every sight is fixed straight ahead.

### Link

{% include key.html id="fza_ah64_v30_sightSelectLink" %} is the CPG's, and needs the radar fitted with TADS or FCR as the sight. It ties the two sensors together:

| Sight | Linked | What changes |
|---|---|---|
| TADS | **TADS-L** (`TADSL`{: .mpd} on the HAD) | The CPG also owns the radar, and its centreline follows the TADS line of sight. |
| FCR | **FCR-L** (`C-FCRL`{: .mpd}) | Slaving moves the TADS onto the radar's next-to-shoot target. |

Pressing Link again, selecting any sight, or the pilot taking the FCR unlinks. Selecting TADS again while you are in TADS-L does nothing; only Link unlinks it.

## Acquisition source {#acq}

The acquisition source (ACQ) is a second line of sight your sight can be pointed at. It drives the **cueing dots** around your helmet reticle, which point from where you are looking towards the source, and it is what your sight follows when slaved.

Open the list with `R6`{: .vab} **ACQ** on the FLT, ENG, TSD or WPN page. The list takes over the buttons until you press one:

| Button | Source | Points at |
|---|---|---|
| `R1`{: .vab} | **PHS** | The pilot's helmet line of sight. |
| `R2`{: .vab} | **GHS** | The CPG's helmet line of sight. |
| `R5`{: .vab} | **FCR** | The radar's next-to-shoot target. |
| `R6`{: .vab} | **FXD** | Fixed, straight ahead along the aircraft's nose. |
| `B5`{: .vab} | *point* | Your stored coordinate point, set on the [COORD page]({{ '/displays/mpd/tsd/' | relative_url }}#coord). |
| `B6`{: .vab} | **TADS** | The TADS line of sight. |

**SKR** and **RFI** are listed but cannot be selected. Any other button closes the list without changing anything.

Only sources that make sense for your seat and sight are accepted:

| Source | Pilot can select | CPG can select |
|---|---|---|
| PHS | With FCR as sight | Yes |
| GHS | Yes | With TADS or FCR as sight |
| FCR | Unless FCR is the sight | With HMD or TADS as sight |
| TADS | Yes | Unless TADS is the sight |
| FXD, point | Yes | Yes |

The radar must be fitted and working for FCR, and the TADS powered and working for TADS. A crew station needs to be occupied for its helmet to be a source. If the source you chose becomes unavailable, FXD is used until it comes back.

The defaults are **TADS** for the pilot and **PHS** for the CPG.

For the pilot, choosing a new source while owning the radar stops its scan and points the radar's centreline along the new source. Choosing a coordinate point also makes that point your navigation range source.

## Slave

{% include key.html id="fza_ah64_sightSlave" %} is the CPG's. It toggles **slaved**:

- With TADS as the sight, the TADS turns to the acquisition source and follows it. Slew it by hand again by pressing Slave once more.
- With FCR as the sight, the radar's centreline is pointed along the acquisition source.
- In FCR-L, the TADS follows the radar's next-to-shoot target, jumping to each new one.

Choosing a new acquisition source releases the slave. Pressing Slave while the CPG owns the radar stops its scan.

The CPG's cueing dots show while slaved, or when the acquisition source is a point and the sight is the TADS. The pilot's cueing dots always show.

When the CPG seat is empty or held by the AI, the pilot's acquisition source points the TADS.

## Range {#range}

Ballistics and the displays need a range to the target. Each crew station has a range source, shown on the HAD with a letter in front of the range in kilometres:

| Shown as | Source | Used with | Where it comes from |
|---|---|---|---|
| `*3420`{: .mpd} | Laser | TADS | Lasing with the [LRFD]({{ '/targeting/laser/' | relative_url }}), 500 to 9,999 m, in metres. After you stop lasing the last range stays, shown without the `*`. |
| `R2.4`{: .mpd} | Radar | FCR | The radar's next-to-shoot target. `R??`{: .mpd} with no target. |
| `N4.6`{: .mpd} | Navigation | HMD, TADS | A point chosen as the acquisition source, up to 32 km. |
| `M1.5`{: .mpd} | Manual | Any | Entered on the KU with `B6`{: .vab} **MANRNG>** on the WPN page: 100 to 50,000 m. |
| `A2.1`{: .mpd} | Automatic | Any | Where your sight line meets the ground, from radar altitude. Needs the line at least 1° below the horizon; otherwise 50 km. |

Enter `A` at the **MANRNG** prompt to select automatic range. Some actions change the source for you:

- Lasing selects laser range, for the crew station whose laser it is.
- A new radar next-to-shoot target selects radar range, with FCR as the sight.
- A point as the acquisition source selects navigation range: for the pilot when choosing it, for the CPG when slaving to it.
- Actioning the rockets selects your last manual range, or the default if you have not entered one.

If the source does not fit your sight, or has nothing to give, the default range is used: **1.5 km** for the pilot, **3.0 km** for the CPG.

When rockets are fired cooperatively, the pilot uses the CPG's range and range source.

## Storing a target

{% include key.html id="fza_ah64_cpgStoreUpdate" %} is the CPG's. It stores a target point along your sight's line of sight (TADS, HMD or FCR) at the range shown, as the next free point from `T01`{: .mpd} to `T50`{: .mpd}. When all 50 are used it overwrites from `T01`{: .mpd}. The point's name shows on your HAD for three seconds.

Stored points appear on the [TSD]({{ '/displays/mpd/tsd/' | relative_url }}) and can be chosen as an acquisition source. See [Points and routes]({{ '/mission/points/' | relative_url }}).

## Radial menu

The [radial menu]({{ '/targeting/radial/' | relative_url }}) offers sight select, link and the TADS and FCR settings on one binding, without remembering the individual keys.
