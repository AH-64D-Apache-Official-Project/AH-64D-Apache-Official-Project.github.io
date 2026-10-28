---
title: Weapon action switch
lead: How a crew station takes a weapon, how the two crew stations share them, and what has to be true before anything fires.
keywords: [was, weapon action switch, arm, safe, ground override, gnd oride, trigger, coop, cooperative, inhibit, jettison, weapon?]
seats: [PLT, CPG]
redirect_from:
  - /weapons-was.html
---

## Arming

Two buttons on the **ARMAMENT** panel, in both crew stations, control the aircraft's weapons. They need battery power.

| Button | Effect |
|---|---|
| **ARM/SAFE** | Toggles the aircraft between armed and safe. Nothing fires when safe, and the laser does not fire either. |
| **GND ORIDE** | Ground override. On the ground, the aircraft is held safe, weapons cannot be actioned and the radar does not scan, unless ground override is on. |

On the ground without ground override, or with the battery off, the aircraft goes safe and every weapon is de-actioned. Both buttons can also be bound in **AH-64D Official Project: Cockpit Controls**.

## Actioning a weapon

Each crew station chooses a weapon with its own weapon action switch (WAS):

| Binding | Weapon |
|---|---|
| {% include key.html id="fza_ah64_wasGun" %} | M230 cannon |
| {% include key.html id="fza_ah64_wasRkt" %} | Hydra 70 rockets |
| {% include key.html id="fza_ah64_wasMsl" %} | AGM-114 Hellfires |

Press the same binding again to de-action it. The actioned weapon shows on the top line of the [HAD]({{ '/displays/ihadss/' | relative_url }}#had), right of centre: `CGUN`{: .mpd} or `PGUN`{: .mpd}, `CRKT`{: .mpd} or `PRKT`{: .mpd}, `CMSL`{: .mpd} or `PMSL`{: .mpd}, the first letter saying which crew station is in control.

Then pull the trigger: Arma's **Fire** binding. The weapon is aimed with your [sight]({{ '/targeting/sights/' | relative_url }}).

## Sharing between crew stations

The aircraft has one actioned weapon at a time.

- **The last crew station to action a weapon takes it.** If the pilot actions the gun while the CPG has missiles, the CPG loses the missiles.
- **Rockets can be held by both** at once. When the CPG's sight is the TADS and the pilot's is the HMD, they fire **cooperatively** (`COOP`{: .mpd}): the CPG aims, and the pilot's rocket steering and range are the CPG's.
- With both holding rockets otherwise, the crew station that actioned them last aims.

When the pilot holds a weapon, or there is no player in the CPG seat, the pilot fires it.

## Before it fires: inhibits

When something stops a weapon firing, or means it may miss, the reason shows in the centre of the HAD above the bottom lines. Messages that **stop** the weapon are in bold.

| Message | Weapon | Meaning |
|---|---|---|
| **SAFE** | All | The aircraft is not armed. |
| **NO TARGET** | All | FCR is your sight and there is no next-to-shoot target. |
| **AZ LIMIT** / **EL LIMIT** | Gun | The target is outside the gun's travel: 86° left or right, 11° up, 60° down. |
| **COINCIDENCE** | Gun | The gun is still turning onto where you are looking, more than 1° away. |
| **BAL LIMIT** | All | Beyond range: 7.5 km for rockets, 8 km for Hellfires, or beyond the round's reach for the gun. |
| GUN FIXED | Gun | The gun is in FXD mode, fixed 6° up along the nose. See the [WPN page]({{ '/displays/mpd/wpn/' | relative_url }}). |
| **ALT LAUNCH** | Gun | Gun trigger pulled within 2 seconds of a rocket or missile launch. |
| **ACCEL LIMIT** | Rockets, Hellfires | Below 0.5 G: the rotor could strike the weapon. |
| **PYLON ERROR** | Rockets | The pylons cannot be moved: utility hydraulics failed. |
| PYLON LIMIT | Rockets, Hellfires | The pylons cannot elevate far enough. Stops the weapon on the ground. |
| **MSL NOT RDY** | Hellfire (RF) | The radar missile is not powered and aligned. |
| **TGT DATA?** | Hellfire (RF) | TADS is your sight and no target has been handed over. |
| **BACKSCATTER** | Hellfire (SAL) | The seeker is not tracking your own laser spot. |
| PYLON ANGLE | Hellfires | The launcher is more than 10° from the launch angle. |
| RATE LIMIT | Hellfires | The aircraft is pitching, rolling or yawing faster than 30° a second. |
| ROLL LIMIT | Hellfires | Too much bank: 20°, or 10° for a laser missile fired lock-on after launch. |
| YAW LIMIT | Hellfires | The target is too far off the nose: 20° for RF, 7.5° for a laser missile fired lock-on after launch. |

Pulling the trigger with no weapon actioned shows `WEAPON?`{: .mpd} for a moment.

## Weapon status

The bottom HAD line, right of centre, shows the actioned weapon's status:

| Weapon | Shows |
|---|---|
| Gun | `ROUNDS 1200`{: .mpd}, or `GUN FAIL`{: .mpd} / `GUN JAM`{: .mpd} |
| Rockets | Type, mode and quantity, for example `6PD NORM 14`{: .mpd}; `RTOF=08`{: .mpd} until the last volley arrives; `NO RKTS`{: .mpd} |
| Hellfires | Trajectory and missile mode, for example `LO-NORM`{: .mpd}; `HFTOF=12`{: .mpd} counting down to impact; `MSL LAUNCH`{: .mpd} |

## Emergency jettison

{% include key.html id="fza_ah64_collectiveEmergJett" %} jettisons every wing store: pods, launchers and external tanks, station by station. It needs battery power. Use it to lose weight in an emergency.
