---
title: IHADSS
lead: The helmet display. Flight symbology to fly by, weapon symbology to aim with, and the high action display along the bottom, wherever you look.
keywords: [ihadss, hmd, hdu, helmet, monocle, symbology, transition, cruise, hover, bob-up, bobup, velocity vector, flight path vector, fly-to, head tracker, pitch ladder, had, high action display, constraints box, rocket steering cursor, cueing dots, field of regard]
seats: [PLT, CPG]
redirect_from:
  - /ui-headtracking.html
---

## The monocle {#monocle}

The symbology is drawn on the helmet display unit (HDU), a monocle in front of your right eye. To use it:

{: .steps}
1. Wear the **IHADSS** helmet. Without it the monocle cannot come down, and nothing follows your head.
2. In the cockpit, click **HDU stowage** to bring the monocle down (see the [cockpit tour]({{ '/aircraft/cockpit/' | relative_url }}#hdu)). Click it again to stow it.
3. Turn on power. The symbology needs both the AC and DC buses.

The monocle is stowed each time you get in. It is also stowed if you take the helmet off, or turn on Arma's own night vision outside the optics view.

On the helmet the symbology shows in the first person view only. Behind it, the monocle can show a picture: your [night vision]({{ '/targeting/nvs/' | relative_url }}) sensor, or for the CPG [the TADS]({{ '/targeting/tads/' | relative_url }}).

## Which symbology you get {#formats}

There are two formats: **flight** and **weapon**.

<div class="table-wrap" markdown="1">

| | Pilot | CPG |
|---|---|---|
| **Flight** | Always. | With the HMD as your sight, with your NVS switch on, or with the radar in TPM. |
| **Weapon** | Never. | In the TADS optics view, and on the helmet with TADS or FCR as your sight and your NVS switch off. |

</div>

On the helmet the symbology is green and spread out to fill the monocle. In the CPG's TADS optics view (heads down) it is white and compact. The [VIDEO page]({{ '/displays/mpd/video/' | relative_url }}) can show either crew station's symbology on an MPD.

## Flight symbology {#flight}

Flight symbology has four modes. The mode belongs to the aircraft, so both crew stations see the same one. It starts in transition.

| Binding | Action |
|---|---|
| {% include key.html id="fza_ah64_symbologySelectUp" %} | Transition, or cruise if you are already in transition. |
| {% include key.html id="fza_ah64_symbologySelectDown" %} | Hover, or bob-up if you are already in hover. Selecting bob-up stores where you are and your heading. |
| {% include key.html id="fza_ah64_symbologySelectPress" %} | Opens the [FLT page]({{ '/displays/mpd/flt/' | relative_url }}) on your left MPD. |

The [radial menu]({{ '/targeting/radial/' | relative_url }}) has the same choices under **HMD**.

| Mode | Shows |
|---|---|
| **Transition** | Velocity vector to 60 kt, horizon line, waypoint data. |
| **Cruise** | Pitch ladder, bank, barometric altitude, waypoint data. No velocity vector. |
| **Hover** | Velocity vector to 6 kt. No attitude, no waypoint data. |
| **Bob-up** | Hover, plus a box over the stored point. |

### Transition {#transition}

{% include fig.html id="hud-transition" %}

The **velocity vector** grows from the reticle in the direction you are moving over the ground. Its full length, to the top of the lubber line under the heading tape, is 60 kt. The **acceleration cue**, the circle, shows where the vector is heading.

The **horizon line** banks with the aircraft and moves a quarter as far as the real horizon in pitch, stopping at 30°. It sits a little below the reticle in level flight.

### Cruise {#cruise}

{% include fig.html id="hud-cruise" %}

The **pitch ladder** moves half as far as the real horizon: rungs every 10° to 30°, then 45° and 60°, solid above the horizon and dashed below. `CLIMB`{: .mpd} and `DIVE`{: .mpd} mark straight up and straight down. The **bank triangle** turns about the reticle; read it against the lubber line. The reticle is drawn thicker.

### Hover {#hover}

{% include fig.html id="hud-hover" %}

In hover the velocity vector's full length is 6 kt, so it shows small drift. The acceleration cue starts at the vector's tip up to 6 kt, and at the reticle above that. Hold the vector and the cue on the reticle to stay over one spot.

### Bob-up {#bobup}

{% include fig.html id="hud-bobup" %}

Bob-up adds an octagon, 12 ft across, over the point stored when you selected it. The edge of the display is 40 ft away; further than that, the box waits at the edge. The command heading caret shows the stored heading instead of the next waypoint.

### Symbols in the world {#world}

Three symbols sit on things outside the aircraft, so they move as you turn your head. They show only on the helmet, with flight symbology.

<div class="table-wrap" markdown="1">

| Symbol | Where it is | When |
|---|---|---|
| **Head tracker** (four chevrons) | Straight ahead of the aircraft's nose. | Every mode. |
| **Flight path vector** (circle with wings) | Where the aircraft is going. At the edge of the display it stops and flashes. | Transition and cruise, over 5 kt ground speed. |
| **Fly-to cue** | On the next waypoint, at its altitude if it has one. | Transition and cruise. |

</div>

### Flight data {#flight-data}

<div class="table-wrap" markdown="1">

| Item | Detail |
|---|---|
| **Torque** | The higher engine's torque. Boxed at 98% and over; flashes when the two engines are more than 12% apart. |
| **TGT** | Turbine gas temperature in °C, under the torque: in the last two minutes of an engine temperature time limit, and throughout single engine running above 878 °C. |
| **NVS** | `FLIR`{: .mpd} above the torque while your NVS switch is on. |
| **Airspeed** | True airspeed in knots. Boxed at VNE. |
| **G** | Under the airspeed above 2 G, for at least 2 seconds. |
| **Radar altitude** | Feet above the ground, up to 1,428 ft: to the foot below 50 ft, to 10 ft above. `HI`{: .mpd} over 200 ft, `LO`{: .mpd} under 33 ft. Under 200 ft there is also a bar on the scale beside it. |
| **Vertical speed** | The pointer, with 1,000 ft/min at each end of the scale. A descent of 1,000 ft/min or more is also shown in figures under the scale. |
| **Barometric altitude** | Cruise only. |
| **Holds** | A box around the airspeed while attitude hold is on; a symbol on the vertical speed scale while altitude hold is on. A hold that drops out flashes for 3 seconds, then goes. |
| **Waypoint data** | Transition and cruise: the next waypoint and its distance; ground speed and time to go. Time to go is in minutes and seconds under 5 minutes, hours and minutes above, and blank at 15 kt or less. |
| **Trim ball** | Centre it with the pedals. |

</div>

## Symbols in every format {#common}

**Heading tape.** The aircraft's heading, 105° each side. Under it:

- the **command heading** caret: the next waypoint in flight symbology, the stored heading in bob-up, and the TADS azimuth in weapon symbology;
- a filled triangle for the **other crew station's sight**: their head with the HMD, or the TADS. It needs someone in the other seat; a pilot with an AI CPG sees the TADS;
- with the radar fitted, a pair of marks on the [FCR centreline]({{ '/targeting/fcr/' | relative_url }}#centerline).

**Reticle.** Your line of sight. It flashes when your sight or night vision sensor is at its limit, and when the gun has failed with the gun actioned.

**Cueing dots.** A dot on the side of the reticle towards your [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq), on each axis where it is more than 4° away. Follow them with your head, or with the TADS when it is your sight.

**Cued LOS reticle.** A dashed cross on the acquisition source itself, when it is in view.

**Field of regard.** The box under the reticle. Its outline is the sensor's reach: the PNVS's for the pilot, the TADS's for the CPG. The small box inside is where you are looking; for a CPG whose sight is not the HMD, where the TADS points. The dot is the acquisition source. With the radar fitted, a solid line is its centreline, and a dashed line where the last scan looked.

## Weapon symbology {#weapon}

{% include fig.html id="hud-tads" %}

The CPG's weapon symbology is built around the TADS:

- **TADS reticle**, with longer arms than the helmet reticle.
- **Sensor** in use, top left: `DTV`{: .mpd}, `FLIR`{: .mpd} or `DVO`{: .mpd}.
- **Field of view brackets**: the corners of what the next narrower field of view will show.
- **LMC marks** at the ends of the reticle arms while the [linear motion compensator]({{ '/targeting/tads/' | relative_url }}#lmc) is on.
- **Lasing marks**: four diagonals around the reticle while the laser fires.
- **Airspeed** and **radar altitude** either side of the field of regard.

The brackets, LMC and lasing marks show in the TADS optics view, and on the helmet with the TADS picture.

## Weapon symbols {#weapon-symbols}

These appear in either format.

### Missile constraints box {#constraints}

With missiles actioned, a box shows whether the Hellfire is within its launch constraints. It is placed so that the reticle is inside it exactly when it is.

| Box | Meaning |
|---|---|
| **Solid** | Within constraints. |
| **Dashed** | Outside them. |
| **Large** | The missile can lock on before launch: a laser missile sees a matching laser spot, or a radar missile has a target it can take. |
| **Small** | It cannot. |

The constraint is 7.5° from the line of sight, 20° with a lock or for a radar missile, and 5° for a radar missile tracking a target inside 1 km. A radar missile shows no box until one is powered and aligned. For laser missiles on LO or HI, the box is measured to your **B5** coordinate point; with no point there it sits on the reticle, dashed. See [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}).

### Rocket steering cursor {#rocket-cursor}

{% include fig.html id="hud-rockets" %}

With rockets actioned, an I-beam shows where the rockets will go. Across, it is the direction of the rocket solution from the nose: turn the aircraft until it is centred on the reticle. Up and down it shows the pylons: with the reticle inside its height, the pylons can reach. It is dashed while the rockets are inhibited. See [Hydra 70 rockets]({{ '/weapons/rockets/' | relative_url }}).

### Fixed gun {#gun-fxd}

With the gun in **FXD**, the cued LOS reticle marks where the fixed gun will hit at the range in use. It moves down the display as the range grows. See [M230 cannon]({{ '/weapons/cannon/' | relative_url }}).

### Radar targets {#cscope}

With **C SCP** on, the radar's targets are drawn where they are, with the next-to-shoot and alternate marks; in TPM, the obstacles. See [FCR]({{ '/targeting/fcr/' | relative_url }}#on-the-helmet).

## High action display {#had}

The HAD is the text along the bottom of every format.

<div class="table-wrap" markdown="1">

| Where | Shows | More |
|---|---|---|
| Top line, left | Your sight: `P-HMD`{: .mpd} or `C-HMD`{: .mpd}, `TADS`{: .mpd}, `P-FCR`{: .mpd} or `C-FCR`{: .mpd}. Linked sights end in L: `TADSL`{: .mpd}, `C-FCRL`{: .mpd}. | [Sights]({{ '/targeting/sights/' | relative_url }}) |
| Top line, after the sight | Range and its source, such as `*3420`{: .mpd} or `M3.0`{: .mpd}. | [Range]({{ '/targeting/sights/' | relative_url }}#range) |
| Top line, right of centre | The actioned weapon: `PGUN`{: .mpd}, `CRKT`{: .mpd}, `COOP`{: .mpd}, `CMSL`{: .mpd} and so on. The first letter is the crew station in control. | [Weapon action switch]({{ '/weapons/was/' | relative_url }}) |
| Top line, right | Acquisition source. | [Acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) |
| Bottom line, left | [Sight status](#sight-status). | |
| Bottom line, right of centre | Weapon status. | [Weapon status]({{ '/weapons/was/' | relative_url }}#weapon-status) |
| Centre, above the lines | Inhibits, `ALT LAUNCH`{: .mpd}, and for 3 seconds the number of a target you just stored. | [Inhibits]({{ '/weapons/was/' | relative_url }}#before-it-fires-inhibits) |
| Centre, above that | CPG: the laser spot tracker's status. | [Laser]({{ '/targeting/laser/' | relative_url }}) |

</div>

### Sight status {#sight-status}

One message shows at a time; the highest in this list wins.

<div class="table-wrap" markdown="1">

| Message | Seat | Meaning |
|---|---|---|
| `TADS FAIL`{: .mpd} | CPG | The TADS FLIR and day TV have both failed. |
| `TV FAIL`{: .mpd} | CPG | The day TV has failed. The FLIR and DVO still work. |
| `NVS FAIL`{: .mpd} | Pilot | The PNVS has failed. |
| `FCR FAIL`{: .mpd} | Both | The radar has a fault. |
| `LIMITS`{: .mpd} | Both | Your sight or night vision sensor is at the limit of its travel. |
| `NVS FIXED`{: .mpd} | Both | Your NVS switch is in FIXED. |
| `LSTCODE?`{: .mpd} | CPG | The LST is set to a letter with no code. |
| `RFDCODE?`{: .mpd} | CPG | The LRFD is set to a letter with no code. |
| `FCR XMIT`{: .mpd} | Both | The radar is scanning. |
| `REMOTE`{: .mpd} | CPG | Missiles are actioned and the primary channel's code differs from your LRFD code: your Hellfire will guide on someone else's laser. |
| `PLT TADS`{: .mpd} | CPG | The pilot has the TADS as their night vision sensor. |
| `CSCOPE`{: .mpd} | Both | C SCP is on. |

</div>

Laser codes are set on the [COM pages]({{ '/displays/mpd/com/' | relative_url }}); see [Laser]({{ '/targeting/laser/' | relative_url }}).
