---
title: IHADSS
lead: The integrated helmet and display sight system — the HDU, flight and weapon symbology formats, and the high action display.
keywords: [ihadss, hmd, hdu, helmet, symbology, transition, cruise, hover, bob-up, bobup, velocity vector, acceleration cue, flight path vector, fly-to cue, head tracker, attitude indicator, pitch ladder, horizon line, los reticle, had, high action display, missile constraints box, rocket steering cursor, cueing dots, field of regard]
seats: [PLT, CPG]
redirect_from:
  - /ui-headtracking.html
---

## Helmet display unit (HDU) {#hdu}

Symbology is displayed on the helmet display unit (HDU) in front of the crewmember's right eye.

1. IHADSS helmet – Worn. Without it the HDU cannot be fitted and head tracking is not available.
2. HDU stowage – Select to fit the HDU (see [Cockpit]({{ '/aircraft/cockpit/' | relative_url }}#hdu)); select again to stow it.
3. Power – Applied. The symbology requires both the AC and DC buses.
{: .steps}

The HDU is stowed on each entry to the aircraft, when the helmet is removed, and when Arma night vision is selected outside the optics view.

On the HMD, symbology is displayed in the first-person view only. Behind the symbology the HDU can display video: the crewmember's [night vision]({{ '/targeting/nvs/' | relative_url }}) sensor or, for the CPG, [the TADS]({{ '/targeting/tads/' | relative_url }}).

## Symbology formats {#formats}

There are two formats, flight and weapon.

<div class="table-wrap" markdown="1">

| | Pilot | CPG |
|---|---|---|
| Flight | Always | With HMD as sight, with the NVS MODE switch on, or with the FCR in TPM |
| Weapon | Never | In the TADS optics view, and on the HMD with TADS or FCR as sight and the NVS MODE switch off |

</div>

On the HMD the symbology is green and scaled to the HDU. In the CPG's TADS optics view (heads down) it is white and compact. The [VIDEO page]({{ '/displays/mpd/video/' | relative_url }}) can display either crew station's symbology on an MPD.

## Flight symbology {#flight}

Flight symbology has four modes. The mode is aircraft common; both crew stations display the same mode. The default mode is transition.

| Binding | Function |
|---|---|
| {% include key.html id="fza_ah64_symbologySelectUp" %} | Transition; cruise if already in transition. |
| {% include key.html id="fza_ah64_symbologySelectDown" %} | Hover; bob-up if already in hover. Selecting bob-up stores the present position and heading. |
| {% include key.html id="fza_ah64_symbologySelectPress" %} | FLT page on the left MPD. |

The [radial menu]({{ '/targeting/radial/' | relative_url }}) provides the same selections under HMD.

| Mode | Displays |
|---|---|
| Transition | Velocity vector to 60 kt, horizon line, navigation data |
| Cruise | Attitude indicator, bank angle, barometric altitude, navigation data; no velocity vector |
| Hover | Velocity vector to 6 kt; no attitude indicator, no navigation data |
| Bob-up | Hover mode symbology, plus the bob-up box and bob-up heading |

### Transition {#transition}

{% include fig.html id="hud-transition" %}

The **velocity vector** indicates the magnitude and direction of the aircraft velocity relative to the nose of the aircraft. Its origin is the centre of the LOS reticle, and in transition mode full scale represents 60 kt ground speed. The **acceleration cue** (circle) indicates the magnitude and direction of the aircraft's acceleration; in transition mode it is referenced to the tip of the velocity vector.

The **horizon line** is an artificial horizon relative to the LOS reticle. It moves one quarter of the true pitch angle, limited at ±30° in pitch, and is presented slightly below the LOS reticle in level flight.

### Cruise {#cruise}

{% include fig.html id="hud-cruise" %}

The **attitude indicator** pitch ladder moves one half of the true pitch angle, with rungs every 10° to 30°, then 45° and 60°; solid above the horizon line and dashed below. 5° tic marks are not presented in cruise mode. `CLIMB`{: .mpd} and `DIVE`{: .mpd} mark the vertical. The **bank angle** triangle is presented without its tic mark scale and is read against the lubber line. The **LOS reticle** is a bold cross-hair.

### Hover {#hover}

{% include fig.html id="hud-hover" %}

In hover mode, full scale of the velocity vector represents 6 kt ground speed. The acceleration cue originates at the outer end of the velocity vector when the vector is less than full scale, and at the centre of the LOS reticle when the vector is at or greater than full scale. With the velocity vector and the acceleration cue held on the LOS reticle, the aircraft remains over one position.

### Bob-up {#bobup}

{% include fig.html id="hud-bobup" %}

Bob-up mode adds the **bob-up box**, an octagon representing an area approximately 12 ft square on the ground. The box initialises at the centre of the LOS reticle on selection of bob-up mode and moves to indicate the position of the helicopter relative to that point. Maximum displacement to the edge of the format represents approximately 40 ft laterally or longitudinally; beyond that the box remains at the edge. The **bob-up heading** chevron presents the heading of the helicopter at the initiation of bob-up mode, in place of the command heading.

The aircraft is returned over the bob-up position by placing the acceleration cue inside the bob-up box.

### Symbols conformal to the outside world {#world}

The following symbols are positioned on objects outside the aircraft and move with head movement. They are displayed on the HMD with flight symbology only.

<div class="table-wrap" markdown="1">

| Symbol | Position | Displayed |
|---|---|---|
| Head tracker (four chevrons) | The nose of the helicopter; indicates the head position relative to it | All modes |
| Flight path vector (circle with tic marks) | The projected flight path: the point towards which the helicopter is flying. Flashes when edge limited | Transition and cruise, above 5 kt ground speed |
| Navigation fly-to cue (diamond) | The active next navigation waypoint, at its altitude if defined; used with the flight path vector | Transition and cruise |

</div>

### Flight data {#flight-data}

<div class="table-wrap" markdown="1">

| Item | Description |
|---|---|
| Engine torque | Higher of the two engine torques. Boxed at 98% and above; flashes with a torque split greater than 12%. |
| TGT | Turbine gas temperature, °C, below the engine torque: during the last two minutes of a TGT time limit, and throughout single engine operation above 878 °C. |
| Selected PNVS sensor | `FLIR`{: .mpd} above the engine torque with the NVS MODE switch on. |
| Airspeed | True airspeed, knots. Boxed at VNE. |
| G status | Load factor digital readout below the airspeed above 2 g; presented for a minimum of 2 seconds. |
| Radar altitude | Digital readout, feet AGL, to 1,428 ft: 1 ft increments below 50 ft, 10 ft above. Radar altitude `HI`{: .mpd} indication above 200 ft, `LO`{: .mpd} indication below 33 ft. Below 200 ft the radar altitude vertical scale is also presented. |
| Rate of climb | Rate of climb scale with a filled triangle pointer; the ends of the scale are 1,000 fpm. A rate of descent greater than 1,000 fpm is also presented as a digital readout. |
| Barometric altitude | Cruise mode only. |
| Hold modes | Attitude hold: a status window around the airspeed digital readout. Altitude hold: a home plate symbol at the zero rate of climb position. A hold mode that disengages flashes for 3 seconds and is removed. |
| Navigation data | Transition and cruise modes: destination point, distance to go, ground speed and time to go. The seconds digits of the time to go are presented only below 5 minutes; time to go is not presented at a ground speed of 15 kt or less. |
| Skid/slip ball | Indicates side acceleration and how well a turn is coordinated. |

</div>

## Common symbols {#common}

**Heading scale.** Magnetic heading, 105° either side, with the lubber line. Along the bottom of the heading scale:

- the command heading chevron: the heading to the next navigation waypoint; in bob-up mode, the bob-up heading; in weapon symbology, the CPG LOS bearing (the TADS line of sight);
- the alternate sensor bearing, a filled triangle: the line of sight azimuth of the other crewmember's selected sight (the other crewmember's HMD, or the TADS); with an AI CPG, the pilot sees the TADS;
- with the radar installed, the [FCR centerline bearing]({{ '/targeting/fcr/' | relative_url }}#centerline).

**LOS reticle.** The line of sight of the crewmember's selected sight. It flashes when the line of sight is invalid or the selected sensor is at its limit, and when the gun is the selected weapon and the gun system has failed.

**Cueing dots.** Presented at the outer tips of the LOS reticle to indicate the quadrant containing the selected [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq): at the upper or lower tip when a change in elevation is required, and at the left or right tip when a change in azimuth is required. They are not presented when the acquisition source is within 4° of the line of sight. They are followed with the head, or with the TADS when the TADS is the selected sight.

**Cued LOS reticle.** A dashed cross-hair representing the selected acquisition source, when it is within the display.

**Field of regard (FOR).** The box at the bottom of the format; its edges mark the limits of the sensor: the PNVS for the pilot, the TADS for the CPG. The field of view box represents the crewmember's HMD, or the TADS for a CPG whose selected sight is TADS or FCR. The cued LOS dot represents the active acquisition source. With the radar installed, the FCR current centerline (solid line) and the FCR last scan centerline (dashed line) are presented.

## Weapon symbology {#weapon}

{% include fig.html id="hud-tads" %}

The CPG's weapon symbology is based on the TADS:

- TADS LOS reticle: the TADS line of sight, with longer lines than the HMD LOS reticle.
- TADS selected sensor, top left: `DTV`{: .mpd}, `FLIR`{: .mpd} or `DVO`{: .mpd}.
- TADS FOV brackets: the imagery that will be displayed in the next narrower field of view.
- LMC on indicator: four short end-cap lines at the ends of the TADS LOS reticle while the [linear motion compensator]({{ '/targeting/tads/' | relative_url }}#lmc) is on.
- Laser firing indicator: a large X with the TADS LOS reticle while the LRFD is lasing.
- Airspeed and radar altitude, either side of the field of regard.

The TADS FOV brackets, the LMC on indicator and the laser firing indicator are presented in the TADS optics view, and on the HMD with TADS video.

## Weapon symbols {#weapon-symbols}

The following symbols are displayed in either format.

### Missile constraints box {#constraints}

With missiles actioned, the missile constraints box indicates the delivery mode and the direction to orient the aircraft for the Hellfire launch. It is positioned so that the LOS reticle is inside the box exactly when the missile is in constraints.

| Box | Meaning |
|---|---|
| Solid | In constraints |
| Dashed | Out of constraints |
| Large (LOBL) | A SAL missile is tracking a matching laser spot, or an RF missile has a target |
| Small (LOAL) | The missile is not tracking |

The constraint is 7.5° from the line of sight; 20° with a lock or for an RF missile; and 5° for an RF missile tracking a target within 1 km. For an RF missile, no box is displayed until a missile is powered and aligned. For SAL missiles on LO or HI trajectory, the box is referenced to the B5 coordinate point; with no point stored, it is displayed dashed on the reticle. See [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}).

### Rocket steering cursor {#rocket-cursor}

{% include fig.html id="hud-rockets" %}

With rockets actioned, the rocket steering cursor, a dynamic I-beam, indicates how to point the aircraft for rocket delivery. Its lateral position is the azimuth of the solution relative to the nose; the aircraft is turned to align it with the LOS reticle. Its vertical extent indicates the pylon elevation range: with the LOS reticle within it, the pylons can reach the solution. The cursor is dashed while a safety or performance inhibit is in force. See [Hydra 70 rockets]({{ '/weapons/rockets/' | relative_url }}).

### Fixed gun {#gun-fxd}

With the gun actioned in the fixed mode (FXD), the fixed gun aiming reticle, graphically the same as the cued LOS reticle, represents the impact point for the selected range, moving down the display as range increases. See [M230 chain gun]({{ '/weapons/cannon/' | relative_url }}).

### Radar targets {#cscope}

With C SCP selected, FCR target symbols are presented in the C-scope format at their azimuth and elevation, with the NTS and ANTS symbols; in TPM, terrain profile lines and obstacle symbols are presented. See [FCR]({{ '/targeting/fcr/' | relative_url }}#on-the-helmet).

## High action display (HAD) {#had}

The high action display (HAD) is located along the bottom of the flight and weapon symbology formats. It is subdivided into status message fields and provides information independently by crew station.

<div class="table-wrap" markdown="1">

| Field | Location | Content | Reference |
|---|---|---|---|
| Sight select status | Top line, left | Selected sight: `P-HMD`{: .mpd} or `C-HMD`{: .mpd}, `TADS`{: .mpd}, `P-FCR`{: .mpd} or `C-FCR`{: .mpd}. Linked sights end in L: `TADSL`{: .mpd}, `C-FCRL`{: .mpd}. | [Sights]({{ '/targeting/sights/' | relative_url }}) |
| Range and range source status | Top line, after the sight | Range and range source, for example `*3420`{: .mpd} or `M3.0`{: .mpd}. | [Range]({{ '/targeting/sights/' | relative_url }}#range) |
| Weapon control status | Top line, right of centre | Actioned weapon: `PGUN`{: .mpd}, `CRKT`{: .mpd}, `COOP`{: .mpd}, `CMSL`{: .mpd} and so on; the first letter is the crew station in control. | [Weapon action switch]({{ '/weapons/was/' | relative_url }}) |
| Acquisition select status | Top line, right | Selected acquisition source. | [Acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) |
| Sight status | Bottom line, left | [Sight status](#sight-status) messages. | |
| Weapon status | Bottom line, right of centre | Weapon status messages. | [Weapon status]({{ '/weapons/was/' | relative_url }}#weapon-status) |
| Weapon inhibit status | Centre, above the lines | Safety and performance inhibits, `ALT LAUNCH`{: .mpd}, and for 3 seconds the number of a target just stored. | [Inhibits]({{ '/weapons/was/' | relative_url }}#inhibits) |

</div>

### Sight status {#sight-status}

One message is displayed at a time; the highest in the list takes priority.

<div class="table-wrap" markdown="1">

| Message | Crew station | Meaning |
|---|---|---|
| `TADS FAIL`{: .mpd} | CPG | TADS FLIR and DTV both failed |
| `NVS FAIL`{: .mpd} | Pilot | PNVS failed |
| `FCR FAIL`{: .mpd} | Both | Radar fault |
| `TARGET DATA?`{: .mpd} | Both | No target data for the actioned weapon: FCR as sight with no next-to-shoot target, or RF missiles with TADS as sight and no target handed over. The launch is inhibited. |
| `LIMITS`{: .mpd} | Both | Sight or night vision sensor at its limit of travel |
| `NVS FIXED`{: .mpd} | Both | NVS MODE switch at FIXED |
| `LST CODE ?`{: .mpd} | CPG | LST set to a code letter with no code |
| `LRFD CODE ?`{: .mpd} | CPG | LRFD set to a code letter with no code |
| `FCR XMIT`{: .mpd} | Both | Radar transmitting |
| `REMOTE`{: .mpd} | CPG | Missiles actioned with the priority missile channel code different from the LRFD code: the missile guides on another designator |

</div>

Laser codes are set on the [laser code pages]({{ '/displays/mpd/code/' | relative_url }}); see [Laser]({{ '/targeting/laser/' | relative_url }}).
