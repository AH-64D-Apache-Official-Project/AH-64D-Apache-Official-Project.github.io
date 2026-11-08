---
title: Weapon action switch
lead: Arming the aircraft, actioning a weapon in each crew station, weapon control between crew stations, inhibits and weapon status.
keywords: [was, weapon action switch, arm, safe, ground override, gnd oride, trigger, coop, cooperative, inhibit, jettison, weapon?, swarm]
seats: [PLT, CPG]
redirect_from:
  - /weapons-was.html
---

## Engagement sequence

Every engagement is conducted with the sequence known as SWARM:

1. **Sight**: select the sight for the engagement.
2. **Weapon**: action the weapon with the WAS.
3. **Armed**: arm the aircraft with the A/S button and verify ARMED on the WPN page.
4. **Range**: establish range and verify it is within the weapon's minimum and maximum range.
5. **Messages**: verify the weapon status and that no inhibit is displayed.
{: .steps}

The weapon-specific sequences are given on the [M230 chain gun]({{ '/weapons/cannon/' | relative_url }}#engagement-sequence), [Hydra 70 rockets]({{ '/weapons/rockets/' | relative_url }}#engagement-sequence) and [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}#sal-engagement) pages.

## Arming

Two buttons on the armament panel in each crew station control the aircraft's weapons. Both require battery power.

| Button | Function |
|---|---|
| A/S (ARM/SAFE) | Selects the aircraft armed or safe. Weapons and the laser do not fire with the aircraft safe. |
| GND ORIDE | Ground override. On the ground, the aircraft is held safe, weapons cannot be actioned and the radar does not transmit unless GND ORIDE is selected. |

On the ground without GND ORIDE, or with battery power removed, the aircraft is safed and every weapon is de-actioned. Both buttons can be bound in **AH-64D Official Project: Cockpit Controls**.

## Actioning a weapon

Each crew station actions a weapon with its own weapon action switch (WAS):

| Binding | Weapon |
|---|---|
| {% include key.html id="fza_ah64_wasGun" %} | M230 chain gun |
| {% include key.html id="fza_ah64_wasRkt" %} | Hydra 70 rockets |
| {% include key.html id="fza_ah64_wasMsl" %} | AGM-114 Hellfire |

Selecting the same weapon again de-actions it. The actioned weapon is displayed on the top line of the [HAD]({{ '/displays/ihadss/' | relative_url }}#had), right of center: `CGUN`{: .mpd} or `PGUN`{: .mpd}, `CRKT`{: .mpd} or `PRKT`{: .mpd}, `CMSL`{: .mpd} or `PMSL`{: .mpd}; the first letter identifies the crew station in control. The weapon is fired with the Arma **Fire** binding and aimed with the selected [sight]({{ '/targeting/sights/' | relative_url }}).

## Sharing between crew stations

One weapon is actioned at a time for the aircraft.

- The crew station that last actions a weapon takes it. If the pilot actions the gun while the CPG has missiles actioned, the CPG's missiles are de-actioned.
- Both crew stations can action rockets together. With the CPG's sight TADS and the pilot's sight HMD, the rockets are fired cooperatively (`COOP`{: .mpd}): the CPG aims, and the pilot's steering and range are the CPG's.
- With both crew stations holding rockets otherwise, the crew station that actioned them last aims.

When the pilot holds a weapon, or the CPG seat has no player, the pilot fires it.

## Inhibits

A condition that inhibits a weapon, or that may cause a miss, is displayed in the center of the HAD above the bottom lines. Messages that inhibit launch or firing are shown in bold.

| Message | Weapon | Condition |
|---|---|---|
| **SAFE** | All | Aircraft not armed |
| **AZ LIMIT** / **EL LIMIT** | Gun | Target outside the gun's travel: 86° left or right, 11° up, 60° down |
| **COINCIDENCE** | Gun | Gun not yet aligned with the line of sight |
| **BAL LIMIT** | All | Beyond range: 7.5 km for rockets, 8 km for Hellfires, or beyond the gun's ballistic range |
| **ALT LAUNCH** | Gun | Gun trigger within 2 seconds of a rocket or missile launch |
| **ACCEL LIMIT** | Rockets, Hellfires | Load factor below 0.5 g |
| **PYLON ERROR** | Rockets | Pylons cannot articulate: utility hydraulics failed |
| PYLON LIMIT | Rockets, Hellfires | Pylons cannot articulate far enough; inhibits launch on the ground |
| **MSL NOT RDY** | Hellfire (RF) | RF missile not powered and aligned |
| **BACKSCATTER** | Hellfire (SAL) | Seeker not tracking the aircraft's own laser spot |
| PYLON ANGLE | Hellfires | Launcher more than 10° from the launch angle |
| RATE LIMIT | Hellfires | Aircraft pitch, roll or yaw rate above 30° per second |
| ROLL LIMIT | Hellfires | Bank above 20°, or above 10° for a SAL missile fired LOAL |
| YAW LIMIT | Hellfires | Target more than 20° off the nose for RF, or 7.5° for a SAL missile fired LOAL |

With no target data for the actioned weapon (FCR as sight with no next-to-shoot target, or RF missiles with TADS as sight and no target handed over), the launch is inhibited and the [sight status]({{ '/displays/ihadss/' | relative_url }}#sight-status) displays `TARGET DATA?`{: .mpd}.

Pulling the trigger with no weapon actioned displays `WEAPON?`{: .mpd} momentarily.

## Weapon status

The bottom line of the HAD, right of center, displays the actioned weapon's status:

| Weapon | Status |
|---|---|
| Gun | `ROUNDS 1200`{: .mpd}, or `GUN FAIL`{: .mpd} / `GUN JAM`{: .mpd} |
| Rockets | Type, mode and quantity, for example `6PD NORM 14`{: .mpd}; `RKT TOF=08`{: .mpd} until the last volley impacts; `NO ROCKETS`{: .mpd} |
| Hellfires | Trajectory and mode, for example `LO NORM`{: .mpd}; for RF missiles `LOBL NORM`{: .mpd} or `LOAL NORM`{: .mpd}; `HF TOF=12`{: .mpd} counting down to impact; `MSL LAUNCH`{: .mpd} |

## Emergency jettison

Emergency jettison {% include key.html id="fza_ah64_collectiveEmergJett" %} releases every wing store — rocket launchers, missile launchers and external tanks — station by station. It requires battery power.
