---
title: TADS
lead: The target acquisition designation sight is the CPG's main sensor. A turret under the nose with a thermal camera, a day TV camera, direct view optics and the laser.
keywords: [tads, iat, image auto tracker, ofs, offset, gates, track, flir, dtv, dvo, fov, zoom, wide, medium, narrow, sensor, lmc, linear motion compensator, slew, polarity, white hot, black hot, a3ti]
seats: [CPG]
---

The TADS is the CPG's sight. Select it with {% include key.html id="fza_ah64_v30_sightSelectTADS" %}. The pilot cannot use it as a sight, but can borrow its FLIR as a night vision sensor (see [Night vision]({{ '/targeting/nvs/' | relative_url }})).

## Looking through it

There are three ways to see the TADS picture:

- **Through the sight**: Arma's optics view (your **Optics** binding). You see the TADS picture full screen with its weapon symbology.
- **On an MPD**: the [VIDEO page]({{ '/displays/mpd/video/' | relative_url }}), or as an underlay behind other pages.
- **On the helmet**: with the monocle down, TADS or FCR as your sight and your NVS switch off, the TADS picture fills the CPG's monocle under the [weapon symbology]({{ '/displays/ihadss/' | relative_url }}#weapon). The DVO is a direct view optic, so it has no picture there. The helmet also shows the TADS when it is your night vision sensor.

From the cockpit view, your aim input (mouse or stick) slews the TADS at up to 60° a second in the wide field of view, slower in the narrower ones. It turns ±120° left and right, 30° up and 60° down. While you use the radial menu or Hatchet's detached cursor, the aim input moves those instead; see the **TADS input ignores the detached cursor** [setting]({{ '/getting-started/settings/' | relative_url }}). Free look moves your view only from the cockpit: through the sight, the aim input still slews the TADS.

At a turret limit the reticle flashes and the HAD shows `LIMITS`{: .mpd}.

## Sensors

| Sensor | Binding | Picture | Fields of view |
|---|---|---|---|
| **FLIR** | {% include key.html id="fza_ah64_SensorSelect_FLIR" %} | Thermal, white-hot or black-hot. | W, M, N, Z |
| **DTV** | {% include key.html id="fza_ah64_SensorSelect_DTV" %} | Day TV, black and white. | W, N, Z (M gives W) |
| **DVO** | {% include key.html id="fza_ah64_SensorSelect_DVO" %} | Direct view optics, colour. | W and N (M and Z give N) |

{% include key.html id="NightVision" %} cycles: FLIR white-hot, FLIR black-hot, then DTV and DVO if the **NV Cycle Include DTV** and **NV Cycle Include DVO** settings are on, then back to FLIR. A damaged sensor is skipped. The selected sensor shows at the top left of the TADS symbology.

With **A3 Thermal Improvement** loaded, its thermal picture is used for the FLIR. The night vision key then belongs to A3TI, and the sensor keys only work while the DTV or DVO is selected.

If the day TV is damaged the HAD shows `TV FAIL`{: .mpd}; with both cameras damaged, `TADS FAIL`{: .mpd}.

## Field of view

| Binding | FOV |
|---|---|
| {% include key.html id="fza_ah64_tadsLHGFov_W" %} | Wide |
| {% include key.html id="fza_ah64_tadsLHGFov_M" %} | Medium |
| {% include key.html id="fza_ah64_tadsLHGFov_N" %} | Narrow |
| {% include key.html id="fza_ah64_tadsLHGFov_Z" %} | Zoom |
| {% include key.html id="zoomIn" %} / {% include key.html id="zoomOut" %} | Step in and out through the fields of view the sensor has. |

The four field of view bindings have no default key. Use zoom in and out, the [radial menu]({{ '/targeting/radial/' | relative_url }}), or bind them yourself.

Brackets in the TADS reticle show the size of the next narrower field of view.

## Linear motion compensator {#lmc}

{% include key.html id="fza_ah64_tadsLHGLmc" %} turns the LMC on or off. The symbology shows **LMC** while it is on.

- **LMC off**: your aim input moves the TADS, and it stops when you let go.
- **LMC on**: your aim input sets a rate. The TADS keeps moving at that rate after you let go, so you can match a moving target and then take your hands off. It also allows for the aircraft's own movement, using your current [range]({{ '/targeting/sights/' | relative_url }}#range), so the TADS stays on a point on the ground while you fly. Lase the target for the best result.

The **LMC Sensitivity** [setting]({{ '/getting-started/settings/' | relative_url }}) scales how strongly your input drives it. Slaving the TADS overrides the LMC; when you release the slave, the LMC carries on from where the TADS was.

## Image auto tracker {#iat}

The image auto tracker (IAT) keeps the TADS on one target for you, a vehicle or a man, in the FLIR or the DTV. It tracks one target at a time. Its bindings are in **AH-64D Official Project**, unbound by default:

| Binding | Action |
|---|---|
| **IAT/OFS: IAT** | **Tap**: tracks the vehicle or man nearest the reticle. With none near, it holds the point on the building, tree or rock under the reticle. Bare ground and sky give it nothing to track. **Hold**: after about half a second the gates grow out from the reticle and back; let go when they frame the target to track what is inside them. **Pressed while tracking**: back to manual track. |
| **IAT/OFS: OFS** | While tracking: offset track. Your aim input moves the line of sight about the target, kept so the target stays in view. Press again to return to the target. |
| **IAT Polarity: White / Auto / Black** | The polarity switch, three positions. See below. |

Engaging the IAT takes the TADS off slave.

### Gates

Four corner **gates** frame the tracked target in the TADS picture: through the sight, on the CPG's helmet and on the [VIDEO page]({{ '/displays/mpd/video/' | relative_url }}). The DVO has no gates, and the IAT does not work in it.

### Losing the target

The IAT can lose its target to terrain, buildings, trees or smoke between you, to the edge of the field of view or the TADS's limits, to range (8 km), or by the target getting too small. While it is lost the IAT carries on in the direction the target was moving, and the gates flash. After a field of view change it takes a moment to find the target again.

If it has not found the target again after 2 seconds, it goes to **stop mode**: the gates become four small solid bars and the TADS is yours again. With LMC on, the TADS carries on turning at the rate it was.

### Polarity

In the FLIR, a running vehicle or a living man shows white in white-hot and black in black-hot; anything else shows the other way round. **White** and **Black** tell the IAT which to look for; **Auto** lets it choose. With the switch against how the target shows, the IAT needs the target bigger and clearer to hold it. The DTV tracks either way.

### What stops it

The IAT drops back to manual track when you slave the TADS, when the laser spot tracker takes the TADS, without AC power, when the TADS stops being your sight, or when the TADS becomes a night vision sensor.

## Slaving and the laser spot tracker

Slaved, the TADS turns to your acquisition source and follows it: see [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}). The laser spot tracker can also drive the TADS onto a laser spot: see [Laser]({{ '/targeting/laser/' | relative_url }}).
