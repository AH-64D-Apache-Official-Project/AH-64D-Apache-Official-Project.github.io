---
title: TADS
lead: The target acquisition designation sight — the CPG's primary sensor, with FLIR, day TV, direct view optics and the laser. Sensors, fields of view, the linear motion compensator and image auto track.
keywords: [tads, iat, image auto track, image auto tracker, ofs, offset, gates, track, flir, dtv, dvo, fov, zoom, wide, medium, narrow, sensor, lmc, linear motion compensator, slew, polarity, white hot, black hot, a3ti]
seats: [CPG]
---

The TADS is the CPG's sight, selected with {% include key.html id="fza_ah64_v30_sightSelectTADS" %}. The pilot cannot select the TADS as a sight, but can use its FLIR as a night vision sensor (see [Night vision]({{ '/targeting/nvs/' | relative_url }})).

## TADS video

TADS video is displayed:

- **In the sight**: the Arma optics view (**Optics** binding), full screen with weapon symbology.
- **On an MPD**: the [VIDEO page]({{ '/displays/mpd/video/' | relative_url }}), or as an underlay beneath other pages.
- **On the HDU**: with TADS or FCR as the sight and the NVS MODE switch OFF, TADS video is displayed on the CPG's HDU beneath the [weapon symbology]({{ '/displays/ihadss/' | relative_url }}#weapon). The DVO is an optical sight and has no video on the HDU. The HDU also displays the TADS when it is the night vision sensor.

From the cockpit view, the aim input (mouse or stick) slews the TADS at up to 60° per second in the wide field of view, and more slowly in the narrower fields. TADS travel is ±120° in azimuth, 30° up and 60° down. While the radial menu or the Hatchet detached cursor is in use, the aim input operates those instead; see the **TADS input ignores the detached cursor** [setting]({{ '/getting-started/settings/' | relative_url }}). Free look moves the view only from the cockpit view; in the sight, the aim input slews the TADS.

At a travel limit, the reticle flashes and the HAD displays `LIMITS`{: .mpd}.

## Sensors

| Sensor | Binding | Video | Fields of view |
|---|---|---|---|
| FLIR | {% include key.html id="fza_ah64_SensorSelect_FLIR" %} | Thermal, white-hot or black-hot | W, M, N, Z |
| DTV | {% include key.html id="fza_ah64_SensorSelect_DTV" %} | Day TV, monochrome | W, N, Z (M selects W) |
| DVO | {% include key.html id="fza_ah64_SensorSelect_DVO" %} | Direct view optics, color | W and N (M and Z select N) |

{% include key.html id="NightVision" %} cycles FLIR white-hot, FLIR black-hot, then DTV and DVO if the **NV Cycle Include DTV** and **NV Cycle Include DVO** settings are on, then FLIR. A damaged sensor is skipped. The selected sensor is displayed at the top left of the TADS symbology.

With A3 Thermal Improvement loaded, its thermal image is used for the FLIR; the night vision binding then belongs to A3TI, and the sensor bindings operate only with the DTV or DVO selected.

With both cameras damaged, the HAD displays `TADS FAIL`{: .mpd}.

## Field of view

| Binding | Field of view |
|---|---|
| {% include key.html id="fza_ah64_tadsLHGFov_W" %} | Wide |
| {% include key.html id="fza_ah64_tadsLHGFov_M" %} | Medium |
| {% include key.html id="fza_ah64_tadsLHGFov_N" %} | Narrow |
| {% include key.html id="fza_ah64_tadsLHGFov_Z" %} | Zoom |
| {% include key.html id="zoomIn" %} / {% include key.html id="zoomOut" %} | Steps through the sensor's fields of view |

The four field of view bindings have no default key; zoom in and out, the [radial menu]({{ '/targeting/radial/' | relative_url }}), or user bindings select them.

Brackets in the TADS reticle mark the area of the next narrower field of view.

## Linear motion compensator {#lmc}

{% include key.html id="fza_ah64_tadsLHGLmc" %} turns the LMC on or off. The symbology displays LMC while it is on.

- **LMC off**: the aim input slews the TADS, which stops when the input is released.
- **LMC on**: the aim input sets a rate. The TADS continues at that rate after the input is released, matching a moving target. The LMC also compensates for the aircraft's own motion, using the current [range]({{ '/targeting/sights/' | relative_url }}#range), to hold the TADS on a ground point. A lased range gives the best result.

The **LMC Sensitivity** [setting]({{ '/getting-started/settings/' | relative_url }}) scales the input. Slave overrides the LMC; when slave is released, the LMC continues from the TADS position.

## Image auto track {#iat}

Image auto track (IAT) holds the TADS on one target, a vehicle or a person, in the FLIR or the DTV. Its bindings are in **AH-64D Official Project**, unbound by default:

| Binding | Function |
|---|---|
| IAT/OFS: IAT | **Press**: tracks the vehicle or person nearest the reticle; with none near, holds the point on the structure, tree or rock under the reticle. Bare ground and sky cannot be tracked. **Hold**: after approximately half a second the gates expand from the reticle and contract; releasing when they frame the target tracks what is inside them. **Pressed while tracking**: returns to manual track. |
| IAT/OFS: OFS | While tracking: offset track. The aim input moves the line of sight about the target while the target remains in view. Pressed again, returns to the target. |
| IAT Polarity: White / Auto / Black | Polarity switch, three positions; see below. |

Engaging the IAT releases the TADS slave.

### Gates

Four corner gates frame the tracked target in the TADS video, in the sight, on the CPG's HDU and on the [VIDEO page]({{ '/displays/mpd/video/' | relative_url }}). The DVO has no gates, and the IAT does not operate with the DVO.

### Loss of track

The IAT can lose its target to terrain, structures, trees or smoke on the line of sight, to the edge of the field of view or the TADS travel limits, to range (8 km), or to target size. While the target is lost, the IAT continues in the target's last direction of motion and the gates flash. After a field of view change, the IAT takes a moment to reacquire.

If the target is not reacquired within 2 seconds, the IAT enters stop mode: the gates change to four small solid bars and manual control returns. With LMC on, the TADS continues at its last rate.

### Polarity

In the FLIR, a running vehicle or a living person is white in white-hot and black in black-hot; other objects are the reverse. White and Black set the IAT to track that polarity; Auto selects automatically. With the switch against the target's polarity, the IAT requires a larger and clearer target to hold track. The DTV tracks either polarity.

### Track release

The IAT returns to manual track when the TADS is slaved, when the laser spot tracker takes control of the TADS, without AC power, when the TADS is no longer the sight, or when the TADS becomes a night vision sensor.

## Slave and laser spot tracker

When slaved, the TADS slews to the acquisition source and follows it; see [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}). The laser spot tracker can also drive the TADS onto a laser spot; see [Laser]({{ '/targeting/laser/' | relative_url }}).
