---
title: Fire control radar
lead: How to use the Longbow radar. Who controls it, how to scan, what it can see, and how to step through its targets.
keywords: [fcr, radar, longbow, scan, single scan, continuous, gtm, atm, rmap, tpm, scan size, nts, ants, centerline, owner, link, slave, detection]
seats: [PLT, CPG]
redirect_from:
  - /targeting-fcr.html
---

The radar sits in the dome above the rotor. Only aircraft with it fitted can use it: see [Variants and customisation]({{ '/aircraft/variants/' | relative_url }}). What it shows is described on the [FCR page]({{ '/displays/mpd/fcr/' | relative_url }}).

## Who controls it {#owner}

The radar is shared, and only one crew station controls it at a time: the **owner**.

- The crew station that last selected the FCR as its sight owns it.
- The CPG also owns it while linked with TADS as the sight (TADS-L). See [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}).
- Taking the radar from the other crew station stops its scan.
- Selecting a different sight gives it up and stops the scan.

Only the owner can scan, change the mode or scan size, slew the centreline and step the next-to-shoot target. The other crew station's radar keys do nothing.

## Before it will scan

- AC and DC power, and an undamaged radar.
- In the air, or **GND ORIDE** on when on the ground.

A radar that loses power or is damaged shows `FCR FAIL`{: .mpd} on the HAD and the `FCR FAULT`{: .mpd} advisory.

## Scanning

| How | Binding | Behaviour |
|---|---|---|
| **Single scan** | {% include key.html id="fza_ah64_fcrSingleScan" %} | One scan burst, then it stops by itself. Press again to stop early. |
| **Continuous scan** | {% include key.html id="ActiveSensorsToggle" %} | Keeps scanning until you toggle it off. |

While the radar transmits, the HAD shows `FCR XMIT`{: .mpd}.

A scan burst is a number of full sweeps of the sector, there and back. In GTM and RMAP it is 2 sweeps in Wide and Medium, 3 in Narrow and 4 in Zoom; in ATM always 2. The antenna turns at 60° a second (120° in TPM), so a wide GTM sweep takes 3 seconds and a single scan about 6. It first slews to the edge of the sector before the sweep starts.

Targets are updated each time a sweep completes. Starting a new scan clears the old targets.

## Modes

Select the mode with the mode keys. Changing mode stops a running scan.

| Mode | Binding | Use |
|---|---|---|
| **GTM** | {% include key.html id="fza_ah64_fcrModeGTM" %} | Ground targets. |
| **ATM** | {% include key.html id="fza_ah64_fcrModeATM" %} | Aircraft and helicopters, all round. |
| **RMAP** | {% include key.html id="fza_ah64_fcrModeRMAP" %} | Ground targets over a picture of the terrain. Select RMAP again to turn the picture on or off. |
| **TPM** | {% include key.html id="fza_ah64_fcrModeTPM" %} | Terrain profile for flying low at night. No targets. |

## Scan size

The scan size sets the width of the sector. A new size stops a running scan and takes effect from the next one.

| Size | Binding | GTM and RMAP | ATM |
|---|---|---|---|
| **W**ide | {% include key.html id="fza_ah64_fcrScanSize_W" %} | 90° | All round, except about 12° either side of the tail |
| **M**edium | {% include key.html id="fza_ah64_fcrScanSize_M" %} | 45° | 180° |
| **N**arrow | {% include key.html id="fza_ah64_fcrScanSize_N" %} | 30° | 90° |
| **Z**oom | {% include key.html id="fza_ah64_fcrScanSize_Z" %} | 15° | 45° |

The scan size bindings have no default key. Use the [radial menu]({{ '/targeting/radial/' | relative_url }}), or bind them yourself.

TPM chooses its own width: 180° below 45 kt, 90° above 55 kt.

## What it sees

- Range 500 m to 8 km, and it needs line of sight.
- Stationary ground targets show out to 6 km. Moving targets and aircraft show out to 8 km.
- GTM and RMAP ignore anything more than 25° above the antenna. ATM shows only aircraft and helicopters that are moving, down to 22.5° below the antenna.
- Targets are classed as tracked, wheeled, helicopter, aircraft or air defence. Anything else is unknown.

Detection is not certain. Each scan burst a target may show bright, dim or not at all:

- **Moving targets** stand out from the ground, and show bright most of the time.
- **Stationary targets** are harder. They show better in the smaller scan sizes, and keep their best result from the last three scan bursts.
- A few false returns from the ground (clutter) appear in GTM and RMAP.

## Priority and the next-to-shoot target

Targets are ranked: bright before dim, then air defence, wheeled, tracked, helicopter, aircraft, unknown. The FCR page, the helmet and the TSD's NAV phase show the top 16; the TSD's ATK phase shows them all.

The highest-priority target is the **next to shoot** (NTS), and the one after it the **alternate** (ANTS). Step the NTS through the top 16 with `L1`{: .vab} **NTS** on the FCR page or {% include key.html id="vehLockTargets" %}, as the owner with FCR as your sight. The NTS stays on its target as long as that target remains in the top 16.

`L4`{: .vab} **TGT** on the FCR page stores the NTS as a target point, the next free from `T01`{: .mpd} to `T50`{: .mpd}.

With FCR as your sight, a new NTS also becomes your [range source]({{ '/targeting/sights/' | relative_url }}#range), and the radar-guided Hellfires are fired at it: see [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}#rf).

## The centreline {#centerline}

The centreline is where the middle of the scan sector points.

- Slew it with `L2`{: .vab} and `R2`{: .vab} on the FCR page: 90° a press in Wide, 22.5° in Medium, 15° in Narrow, 7.5° in Zoom. Slewing stops a running scan.
- A slewed centreline holds its compass bearing as the aircraft turns. Slew it back to the nose and it follows the nose again.
- It cannot be slewed in TPM or in wide ATM.

Some sight settings point it for you:

- **Pilot**: you can slew it only with **FXD** as your acquisition source. Otherwise it follows your acquisition source (your head, with PHS), updating at most four times a second and not during a scan. Selecting the FCR as sight points it along your acquisition source.
- **CPG**: you cannot slew it while slaved or in TADS-L. Slaved with FCR as the sight, it points along your acquisition source. In TADS-L it follows the TADS.

## On the helmet

`T1`{: .vab} **C SCP** on the FCR page puts the radar's targets on your helmet and the VIDEO page, or in TPM the terrain profile lines and obstacles. It is your own setting; the other crew station's is separate. The HAD shows `CSCOPE`{: .mpd} while it is on.

## Using it with the TADS

With **FCR-L** (FCR as the sight, linked), pressing {% include key.html id="fza_ah64_sightSlave" %} slaves the TADS onto the NTS, so the CPG can look at each radar target before engaging. With **TADS-L**, the radar scans wherever the TADS is pointing.
