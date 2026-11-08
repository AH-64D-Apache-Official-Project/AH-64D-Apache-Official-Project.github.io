---
title: Fire control radar
lead: Operation of the fire control radar — radar ownership, scanning, modes, scan size, detection, target priority, zones, the centerline and use with the TADS.
keywords: [fcr, radar, longbow, scan, single scan, continuous, gtm, atm, rmap, tpm, scan size, nts, ants, centerline, owner, link, slave, detection, zone, priority fire zone, no fire zone, tgt, cursor]
seats: [PLT, CPG]
redirect_from:
  - /targeting-fcr.html
---

The fire control radar is mounted on the mast above the main rotor, on aircraft with the radar installed; see [Variants and configuration]({{ '/aircraft/variants/' | relative_url }}). Its display is described on the [FCR page]({{ '/displays/mpd/fcr/' | relative_url }}).

## Radar ownership {#owner}

The radar is aircraft common, and is controlled by one crew station at a time, the owner:

- The crew station that last selected FCR as its sight owns the radar.
- The CPG also owns the radar while linked with TADS as the sight (TADS-L). See [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}).
- Taking the radar from the other crew station stops its scan.
- Selecting a different sight releases the radar and stops the scan.

Only the owner can scan, change the mode or scan size, slew the centerline and step the next-to-shoot target. The other crew station's radar bindings have no effect.

## Requirements

- AC and DC power, and an undamaged radar.
- Airborne, or GND ORIDE selected on the ground.

A radar that loses power or is damaged displays `FCR FAIL`{: .mpd} on the HAD and the `FCR FAULT`{: .mpd} advisory.

## Scanning

| Scan | Binding | Function |
|---|---|---|
| Single scan | {% include key.html id="fza_ah64_fcrSingleScan" %} | One scanburst, then stops. Pressed again, stops early. |
| Continuous scan | {% include key.html id="ActiveSensorsToggle" %} | Continuous scanbursts until deselected. |

While the radar transmits, the HAD displays `FCR XMIT`{: .mpd}, and the scan wiper symbol moves across the scan sector with the antenna on the [FCR page]({{ '/displays/mpd/fcr/' | relative_url }}).

One scan is a near bar and a far bar: a sweep of the antenna from one scan limit to the other, and back. A scanburst consists of multiple scans: in GTM and RMAP, 2 scans in Wide and Medium, 3 in Narrow and 4 in Zoom; in ATM, always 2. The antenna rotates at 60° per second (120° in TPM), so one wide GTM scan takes 3 seconds and a single scanburst approximately 6 seconds. The antenna slews to the scan limit before the first bar starts.

Targets are updated at the end of each scan. A new scanburst clears the previous targets.

## Modes

Changing mode stops a scan in progress.

| Mode | Binding | Use |
|---|---|---|
| GTM | {% include key.html id="fza_ah64_fcrModeGTM" %} | Ground targets |
| ATM | {% include key.html id="fza_ah64_fcrModeATM" %} | Aircraft and helicopters, all azimuths |
| RMAP | {% include key.html id="fza_ah64_fcrModeRMAP" %} | Ground targets over a terrain image. Selecting RMAP again toggles the image. |
| TPM | {% include key.html id="fza_ah64_fcrModeTPM" %} | Terrain profile for low-level flight at night; no targets |

## Scan size

The scan size sets the width of the sector. A new size stops a scan in progress and applies from the next scan.

| Size | Binding | GTM and RMAP | ATM |
|---|---|---|---|
| Wide | {% include key.html id="fza_ah64_fcrScanSize_W" %} | 90° | All azimuths except approximately 12° either side of the tail |
| Medium | {% include key.html id="fza_ah64_fcrScanSize_M" %} | 45° | 180° |
| Narrow | {% include key.html id="fza_ah64_fcrScanSize_N" %} | 30° | 90° |
| Zoom | {% include key.html id="fza_ah64_fcrScanSize_Z" %} | 15° | 45° |

The scan size bindings have no default key; they are selected with the [radial menu]({{ '/targeting/radial/' | relative_url }}) or user bindings.

TPM selects its own width: 180° below 45 kt, 90° above 55 kt.

## Detection

- Range 500 m to 8 km, with line of sight required.
- Stationary ground targets are displayed to 6 km; moving targets and aircraft to 8 km.
- GTM and RMAP ignore targets more than 25° above the antenna. ATM displays only moving aircraft and helicopters, down to 22.5° below the antenna.
- Targets are classified as tracked, wheeled, helicopter, aircraft or air defense; any other target is unknown.

Detection is probabilistic. In each scanburst a target may be displayed in full intensity, in partial intensity, or not at all:

- Moving targets are distinct from the ground return and are displayed in full intensity in most scans.
- Stationary targets are detected less reliably. Detection improves at smaller scan sizes, and each target keeps its best result from the last three scanbursts.
- A small number of false ground returns (clutter) are displayed in GTM and RMAP.

## Target priority and next-to-shoot

Targets are ranked: full intensity before partial intensity, then air defense, wheeled, tracked, helicopter, flyer, unknown. The FCR page, the HMD and the TSD NAV phase display the top 16; the TSD ATK phase displays all.

The highest-priority target is the next-to-shoot (NTS), and the next is the alternate (ANTS). The owner steps the NTS through the top 16 with `L1`{: .vab} NTS on the FCR page or {% include key.html id="vehLockTargets" %}, with FCR as the sight. The NTS remains on its target while that target remains in the top 16.

With FCR as the sight, the NTS can also be selected with the [MPD cursor]({{ '/displays/mpd/fcr/' | relative_url }}#cursor). TGT on the FCR page stores radar targets as target points `T01`{: .mpd} to `T50`{: .mpd}; see [TGT]({{ '/displays/mpd/fcr/' | relative_url }}#tgt).

With FCR as the sight, a new NTS becomes the [range source]({{ '/targeting/sights/' | relative_url }}#range), and RF Hellfires are launched at it; see [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}#rf).

## Zones {#zones}

Priority fire (PF) and no fire (NF) zones, drawn on the TSD [ZN page]({{ '/displays/mpd/tsd/' | relative_url }}#zn) or loaded from a [DTC]({{ '/mission/planner/' | relative_url }}#dtc), change the target priority:

- Targets in the active PF zone rank above all others. After a scan, if the NTS is outside the PF zone and targets exist inside it, the NTS moves into the zone.
- Targets in an active NF zone are not displayed on the FCR page, the TSD or the HMD, and cannot become the NTS or ANTS.

Zones take effect from the next scan. The active zones are drawn on the GTM and ATM pages.

## Centerline {#centerline}

The centerline is the center of the scan sector.

- `L2`{: .vab} and `R2`{: .vab} on the FCR page slew it: 90° per press in Wide, 22.5° in Medium, 15° in Narrow, 7.5° in Zoom. Slewing stops a scan in progress.
- A slewed centerline holds its bearing as the aircraft turns. Slewed back to the nose, it follows the nose.
- It cannot be slewed in TPM or in ATM Wide.

Some sight configurations point the centerline automatically:

- **Pilot**: the centerline can be slewed only with FXD as the acquisition source. Otherwise it follows the acquisition source (the pilot's head with PHS), updating at most four times per second and not during a scan. Selecting FCR as the sight points it along the acquisition source.
- **CPG**: the centerline cannot be slewed while slaved or in TADS-L. Slaved with FCR as the sight, it points along the acquisition source; in TADS-L it follows the TADS.

## C-scope {#on-the-helmet}

`T1`{: .vab} C SCP on the FCR page presents the FCR target symbols in the C-scope format on the HMD and the VIDEO page, or in TPM the terrain profile lines and obstacle symbols. It is crewstation independent.

## Use with the TADS

In FCR-L (FCR as the sight, linked), {% include key.html id="fza_ah64_sightSlave" %} slaves the TADS onto the NTS, for visual identification of each radar target before engagement. In TADS-L, the radar scans along the TADS line of sight.
