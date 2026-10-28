---
title: Hydra 70 rockets
lead: Unguided 2.75 inch rockets from 19-tube pods. The pylons elevate for range; you point the aircraft for azimuth.
keywords: [rockets, hydra, 2.75, m151, m255, flechette, m261, mpsm, m257, m278, illumination, pod, zone, rtof, coop, steering cursor, quantity]
seats: [PLT, CPG]
redirect_from:
  - /weapons-rockets.html
  - /weapons-ammo-rockets.html
---

## Rocket types

| Type | Short code | Warhead | Use |
|---|---|---|---|
| **M151 HEDP** | `6PD`{: .mpd} | 10 lb high-explosive, pre-fragmented | Light vehicles, personnel. |
| **M255A1 FLEC** | `6FL`{: .mpd} | Over 1,000 flechettes | Personnel in the open. |
| **M261 MPSM** | `6MP`{: .mpd} | Nine parachute-retarded submunitions | Personnel and light armour over an area. |
| **M257 IL** | `6IL`{: .mpd} | Parachute flare, visible light | Lights up about a square kilometre for about 100 s, about 3.5 km out. |
| **M278 IR IL** | `6IR`{: .mpd} | Parachute flare, infrared | As M257, but seen only through night vision and thermal sights. |

## Pods and zones

Each pod holds 19 rockets in three zones, and each zone can be loaded with a different type:

| Zone | Rockets |
|---|---|
| A / C | 12 |
| B / D | 4 |
| E (centre) | 3 |

The pylon loadout sets which type is in which zone: see [Rearm and refuel]({{ '/mission/rearm/' | relative_url }}). The [WPN page]({{ '/displays/mpd/wpn/' | relative_url }}) lists up to five types loaded, with the count of each, and shows the pods.

## Firing

1. Action the rockets with {% include key.html id="fza_ah64_wasRkt" %}.
2. On the WPN page, choose the **type** (`L1`{: .vab}–`L5`{: .vab}) and the **quantity** per trigger pull (`R1`{: .vab} **QTY**: 1, 2, 4, 8, 12, 24 or all).
3. Set a range. Actioning the rockets starts you on your last manual range, so enter one with **MANRNG** before you need it, or lase with the TADS. See [Range]({{ '/targeting/sights/' | relative_url }}#range).
4. Look at the target with your sight. The pylons elevate to the solution for that range.
5. Turn the aircraft to put the **rocket steering cursor** on your helmet reticle. The rockets only fly where the nose points; the pylons do not turn sideways.
6. Pull the trigger. Rockets in a volley leave 0.09 s apart.
{: .steps}

After a launch, the HAD counts down the time of flight to the last volley's arrival as `RTOF=nn`{: .mpd}.

The pylons move from 4° up to 15° down in the air, and only 5° down on the ground. Outside that the HAD shows **PYLON LIMIT**; in the air it is only a warning, on the ground it stops the launch. With utility hydraulics failed the pylons cannot move and the rockets are inhibited (**PYLON ERROR**). Rockets will not fire beyond 7.5 km, or below 0.5 G. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}).

The solution leads a moving target you are tracking with the radar.

## Cooperative firing

When both crew stations action the rockets, with the CPG on the TADS and the pilot on the HMD, the rockets are fired cooperatively (`COOP`{: .mpd}). The CPG aims with the TADS and lases; the pilot flies the aircraft onto the steering cursor using the CPG's range.
