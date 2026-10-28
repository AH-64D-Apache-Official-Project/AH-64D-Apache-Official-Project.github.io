---
title: Night vision (PNVS)
lead: At night each crew member flies on a thermal picture in their monocle. It comes from the PNVS turret on top of the nose, or from the TADS FLIR.
keywords: [nvs, pnvs, night vision, flir, thermal, nvs mode, norm, fixed, nvs select, monocle, night flying]
seats: [PLT, CPG]
---

The night vision system (NVS) puts a FLIR picture in your helmet display unit, under the flight symbology, so you can fly at night without night vision goggles. It moves with your head.

## The NVS MODE switch

Each crew station has its own **NVS MODE** switch, on the left console. It steps **OFF → NORM → FIXED → OFF**.

| Position | Picture |
|---|---|
| **OFF** | None. |
| **NORM** | The sensor follows your head. |
| **FIXED** | The sensor looks straight ahead, 4.9° below the aircraft's nose, whatever your head does. The HAD shows `NVS FIXED`{: .mpd}. |

Stepping the switch can also be bound, in **AH-64D Official Project: Cockpit Controls**.

NORM needs the IHADSS helmet to follow your head. The monocle must be down to see the picture: see [IHADSS]({{ '/displays/ihadss/' | relative_url }}).

## Which sensor

Two sensors can give a night picture, and each crew station uses one of them:

| Sensor | Field of regard | Notes |
|---|---|---|
| **PNVS** | 90° left and right, 20° up, 45° down | The pilot's normal sensor. |
| **TADS FLIR** | 120° left and right, 30° up, 60° down | Held in the wide field of view while used this way. |

By default the CPG has the TADS and the pilot the PNVS. Either crew member can swap:

| Binding | Effect |
|---|---|
| {% include key.html id="fza_ah64_nvsSelectPnvs" %} | You take the PNVS; the other crew station gets the TADS. |
| {% include key.html id="fza_ah64_nvsSelectTads" %} | You take the TADS; the other crew station gets the PNVS. |

The last selection made by either seat holds.

While the TADS is someone's night vision sensor with their switch on, it is not a sight. The TADS sight, link, field of view, sensor and LMC keys do nothing, and the TADS stays on FLIR wide. When the pilot has the TADS, the CPG's HAD shows `PLT TADS`{: .mpd}.

Looking past a sensor's limits makes the reticle flash and shows `LIMITS`{: .mpd} on the HAD. A damaged PNVS shows `NVS FAIL`{: .mpd} to the pilot.

## Tips

- Use FIXED when you need a steady forward view, for example on a long approach, or when your head is busy looking elsewhere.
- The FLIR sees heat, not light. Cold terrain and water can look flat; use the radar altimeter and the TPM radar mode ([Fire control radar]({{ '/targeting/fcr/' | relative_url }})) as well.
- The other crew member can watch your sensor's picture on their VIDEO page: see [VIDEO]({{ '/displays/mpd/video/' | relative_url }}).
