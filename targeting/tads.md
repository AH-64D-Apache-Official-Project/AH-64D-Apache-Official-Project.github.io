---
title: TADS
lead: The target acquisition designation sight is the CPG's main sensor. A turret under the nose with a thermal camera, a day TV camera, direct view optics and the laser.
keywords: [tads, flir, dtv, dvo, fov, zoom, wide, medium, narrow, sensor, lmc, linear motion compensator, slew, polarity, white hot, black hot, a3ti]
seats: [CPG]
---

The TADS is the CPG's sight. Select it with {% include key.html id="fza_ah64_v30_sightSelectTADS" %}. The pilot cannot use it as a sight, but can borrow its FLIR as a night vision sensor (see [Night vision]({{ '/targeting/nvs/' | relative_url }})).

## Looking through it

There are three ways to see the TADS picture:

- **Through the sight**: Arma's optics view (your **Optics** binding). You see the TADS picture full screen with its weapon symbology.
- **On an MPD**: the [VIDEO page]({{ '/displays/mpd/video/' | relative_url }}), or as an underlay behind other pages.
- **On the helmet**: with the monocle down, TADS or FCR as your sight and your NVS switch off, the TADS picture fills the CPG's monocle under the [weapon symbology]({{ '/displays/ihadss/' | relative_url }}#weapon). The DVO is a direct view optic, so it has no picture there. The helmet also shows the TADS when it is your night vision sensor.

From the cockpit view, your aim input (mouse or stick) slews the TADS at up to 60° a second in the wide field of view, slower in the narrower ones. It turns ±120° left and right, 30° up and 60° down. While you use free look, the radial menu or Hatchet's detached cursor, the aim input moves those instead; see the **TADS input ignores the detached cursor** [setting]({{ '/getting-started/settings/' | relative_url }}).

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

## Slaving and the laser spot tracker

Slaved, the TADS turns to your acquisition source and follows it: see [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}). The laser spot tracker can also drive the TADS onto a laser spot: see [Laser]({{ '/targeting/laser/' | relative_url }}).
