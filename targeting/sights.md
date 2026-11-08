---
title: Sights and acquisition
lead: The selected sight aims the crew station's weapons; the acquisition source is the line of sight the sight is cued to. Both are crewstation independent. Link, slave, range sources and target storage.
keywords: [sight, hmd, tads, fcr, link, acquisition, acq, slave, cue, cueing dots, range, store, target point]
seats: [PLT, CPG]
redirect_from:
  - /targeting-sights.html
---

## Sights

Each crew station selects one sight, which aims the weapons that crew station fires.

| Sight | Binding | Crew station | Aimed by |
|---|---|---|---|
| HMD | {% include key.html id="fza_ah64_v30_sightSelectHMD" %} | Both | The crewmember's head, through the helmet |
| TADS | {% include key.html id="fza_ah64_v30_sightSelectTADS" %} | CPG only | The TADS turret. See [TADS]({{ '/targeting/tads/' | relative_url }}) |
| FCR | {% include key.html id="fza_ah64_v30_sightSelectFCR" %} | Both, with the radar installed | The radar's next-to-shoot target. See [Fire control radar]({{ '/targeting/fcr/' | relative_url }}) |

The selected sight is displayed on the left of the [HAD]({{ '/displays/ihadss/' | relative_url }}), with a `P-` or `C-` prefix for HMD and FCR (`P-HMD`{: .mpd}, `C-FCR`{: .mpd}), and on the [WPN page]({{ '/displays/mpd/wpn/' | relative_url }}).

The HMD requires the IHADSS helmet; without it there is no head tracking, and head-aimed sights are fixed along the aircraft's nose. Without AC power, every sight is fixed forward.

### Link

{% include key.html id="fza_ah64_v30_sightSelectLink" %} is a CPG control and requires the radar installed, with TADS or FCR as the sight. It links the two sensors:

| Sight | Linked | Effect |
|---|---|---|
| TADS | TADS-L (`TADSL`{: .mpd} on the HAD) | The CPG also owns the radar, and its centerline follows the TADS line of sight. |
| FCR | FCR-L (`C-FCRL`{: .mpd}) | Slave moves the TADS onto the radar's next-to-shoot target. |

Link is cleared by selecting Link again, by selecting any sight, or by the pilot taking the FCR. Selecting TADS while in TADS-L has no effect; only Link clears it.

## Acquisition source {#acq}

The acquisition source (ACQ) is a second line of sight to which the sight can be cued. It drives the cueing dots around the helmet reticle, which point from the crewmember's line of sight toward the source, and it is the line of sight the sight follows when slaved.

The list is opened with `R6`{: .vab} ACQ on the FLT, ENG, TSD or WPN page, and occupies the buttons until a selection is made:

| Button | Source | Line of sight |
|---|---|---|
| `R1`{: .vab} | PHS | Pilot helmet sight |
| `R2`{: .vab} | GHS | CPG (gunner) helmet sight |
| `R5`{: .vab} | FCR | The radar's next-to-shoot target |
| `R6`{: .vab} | FXD | Fixed forward, along the aircraft's nose |
| `B5`{: .vab} | point | The stored coordinate point, set on the [COORD page]({{ '/displays/mpd/tsd/' | relative_url }}#coord) |
| `B6`{: .vab} | TADS | The TADS line of sight |

A point or FCR target can also be selected from the TSD map with the MPD cursor, using [CAQ]({{ '/displays/mpd/tsd/' | relative_url }}#caq).

SKR and RFI are listed but not selectable. Any other button closes the list without a change.

| Source | Pilot | CPG |
|---|---|---|
| PHS | With FCR as sight | Yes |
| GHS | Yes | With TADS or FCR as sight |
| FCR | Unless FCR is the sight | With HMD or TADS as sight |
| TADS | Yes | Unless TADS is the sight |
| FXD, point | Yes | Yes |

FCR requires the radar installed and operative; TADS requires the TADS powered and operative. A helmet source requires that crew station to be occupied. If the selected source becomes unavailable, FXD is used until it is restored.

The defaults are TADS for the pilot and PHS for the CPG.

For the pilot, selecting a new source while owning the radar stops its scan and points the radar centerline along the new source. Selecting a coordinate point also makes that point the navigation range source.

## Slave

{% include key.html id="fza_ah64_sightSlave" %} is a CPG control. It toggles slave:

- With TADS as the sight, the TADS slews to the acquisition source and follows it. Slave again returns manual control.
- With FCR as the sight, the radar centerline is pointed along the acquisition source.
- In FCR-L, the TADS follows the radar's next-to-shoot target, moving to each new target.

Selecting a new acquisition source releases the slave. Slave with the radar owned by the CPG stops its scan.

The CPG's cueing dots are displayed while slaved, or with the acquisition source a point and the TADS as the sight. The pilot's cueing dots are always displayed.

With the CPG crew station empty or occupied by AI, the pilot's acquisition source points the TADS.

## Range {#range}

Ballistics and the displays require a range to the target. Each crew station has a range source, displayed on the HAD as a letter before the range:

| Display | Source | Used with | Origin |
|---|---|---|---|
| `*3420`{: .mpd} | Laser | TADS | Lasing with the [LRFD]({{ '/targeting/laser/' | relative_url }}), 500 to 9,999 m, in meters. After lasing stops the last range is retained, displayed without the `*`. |
| `R2.4`{: .mpd} | Radar | FCR | The radar's next-to-shoot target. |
| `N4.6`{: .mpd} | Navigation | HMD, TADS | A point selected as acquisition source, to 32 km |
| `M1.5`{: .mpd} | Manual | Any | Entered on the KU with `B6`{: .vab} MANRNG> on the WPN page: 100 to 50,000 m |
| `A2.1`{: .mpd} | Automatic | Any | Intersection of the line of sight with the ground, from radar altitude. Requires the line of sight at least 1° below the horizon; otherwise 50 km. |

`A` entered at the MANRNG prompt selects automatic range. The range source also changes automatically:

- Lasing selects laser range for the crew station whose laser fires.
- A new radar next-to-shoot target selects radar range, with FCR as the sight.
- A point as acquisition source selects navigation range: for the pilot on selection, for the CPG when slaved to it.
- Actioning rockets selects the last manual range, or the default.

If the source does not suit the sight, or has no value, the default range is used: 1.5 km for the pilot, 3.0 km for the CPG.

In a cooperative rocket engagement, the pilot uses the CPG's range and range source.

## Target storage

{% include key.html id="fza_ah64_cpgStoreUpdate" %} is a CPG control. It stores a target point along the sight's line of sight (TADS, HMD or FCR) at the displayed range, as the next free point from `T01`{: .mpd} to `T50`{: .mpd}; when all 50 are used, it overwrites from `T01`{: .mpd}. The point identifier is displayed on the HAD for three seconds.

Stored points are displayed on the [TSD]({{ '/displays/mpd/tsd/' | relative_url }}) and are selectable as acquisition source. See [Points and routes]({{ '/mission/points/' | relative_url }}).

## Radial menu

The [radial menu]({{ '/targeting/radial/' | relative_url }}) provides sight select, link and the TADS and FCR selections on one binding.
