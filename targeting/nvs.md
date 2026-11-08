---
title: Night vision (PNVS)
lead: The night vision system displays FLIR video on the HDU beneath the flight symbology, from the PNVS or the TADS FLIR. The NVS MODE switch and sensor selection.
keywords: [nvs, pnvs, night vision, flir, thermal, nvs mode, norm, fixed, nvs select, hdu, night flying]
seats: [PLT, CPG]
---

The night vision system (NVS) displays FLIR video on the helmet display unit beneath the flight symbology, for flight at night without night vision goggles. The sensor follows the crewmember's head.

## NVS MODE switch

Each crew station has an NVS MODE switch on the left console, with positions OFF, NORM and FIXED.

| Position | Video |
|---|---|
| OFF | None |
| NORM | The sensor follows the crewmember's head |
| FIXED | The sensor is fixed forward, 4.9° below the aircraft's nose; the HAD displays `NVS FIXED`{: .mpd} |

The switch can also be bound in **AH-64D Official Project: Cockpit Controls**.

NORM requires the IHADSS helmet for head tracking, and the HDU fitted for the video; see [IHADSS]({{ '/displays/ihadss/' | relative_url }}).

## Sensor selection

Two sensors provide night vision video, and each crew station uses one of them:

| Sensor | Field of regard | Notes |
|---|---|---|
| PNVS | 90° left and right, 20° up, 45° down | The pilot's normal sensor |
| TADS FLIR | 120° left and right, 30° up, 60° down | Held in the wide field of view when used as a night vision sensor |

By default the CPG uses the TADS and the pilot the PNVS. Either crewmember can exchange them:

| Binding | Effect |
|---|---|
| {% include key.html id="fza_ah64_nvsSelectPnvs" %} | This crew station takes the PNVS; the other crew station takes the TADS |
| {% include key.html id="fza_ah64_nvsSelectTads" %} | This crew station takes the TADS; the other crew station takes the PNVS |

The last selection by either crew station applies.

While the TADS is a crewmember's night vision sensor with the NVS MODE switch on, it is not available as a sight: the TADS sight, link, field of view, sensor and LMC bindings have no effect, and the TADS remains on FLIR wide.

At a sensor's limit of travel the reticle flashes and the HAD displays `LIMITS`{: .mpd}. A damaged PNVS displays `NVS FAIL`{: .mpd} to the pilot.

## Operating notes

- FIXED provides a stable forward view, for example on a long approach.
- The FLIR displays temperature differences, not visible light; cold terrain and water can appear without contrast. The radar altimeter and the FCR TPM mode ([Fire control radar]({{ '/targeting/fcr/' | relative_url }})) supplement the FLIR.
- The other crewmember can monitor the sensor video on the [VIDEO page]({{ '/displays/mpd/video/' | relative_url }}).
