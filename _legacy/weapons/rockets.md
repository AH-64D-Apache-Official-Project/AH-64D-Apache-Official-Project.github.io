---
title: Rockets
tags: [weapons]
sidebar: ah64d_sidebar
permalink: weapons-rockets.html
folder: weapons
---

Version 2.0 introduced a more accurate rocket steering cursor which uses the currently selected sight to provide maneuver cues to the crew in order to align the aircraft with the target. The following procedures outline how to engage a target cooperatively from a hover, but apply during running fire or diving fire engagements as well.

## Rocket Steering Cursor

The fixed point of reference for the rocket steering cursor is the aircraft centerline, also known as the Armament Datum Line (ADL). The rocket steering cursor is dynamic and moves with the selected sight (HMD, TADS, FCR).

As an example, the PLT has HMD as their currently selected sight, and they have a target they wish to engage to the left. When they look to the left, the rocket steering cursor will displace to the left indicating that the pilot needs to turn left to align the nose of the aircraft with the target. As they apply left pedal or maneuver the aircraft to the left the rocket steering cursor will move right. When the rocket steering cursor is centered with the LOS, the nose is aligned with the target. The critical piece to this is that the PLT keeps the LOS on the target! Any movement of the PLT LOS will result in movement of the rocket steering cursor and add to frustrations in lining the aircraft up. A common technique which works well in ARMA since there are no winds, is to ignore the rocket steering cursor and instead use the head tracker for azimuth and then the LOS for elevation. So long as the head tracker is aligned with the target, and the LOS is correct in elevation, the rocket will hit the target. The images below illustrate this sequence.

## HMD Engagement Procedure (NORM)

| Step | Image |
| :-: | :-- |
| Step 1 | ![1](/images/weapons/rktEngage_01.png) |
| Step 2 | ![2](/images/weapons/rktEngage_02.png) |
| Step 3 | ![3](/images/weapons/rktEngage_03.png) |
| Step 4 | ![4](/images/weapons/rktEngage_04.png) |

Advantages associated with the NORM mode include shallower dive angles as a result of the articulating pylons and when employed cooperatively, a more stable platform and accurate range to target. Disadvantages include a more 'complex' and 'confusing' setup, particularly when firing HMD due to the dynamic nature of the rocket steering cursor. 

## Rocket Engagment Sequence

To engage a target with Rockets, use the following sequence, known as SWARM:

1. **S**ight - Select HMD {% include keybind.html name="sight-select-hmd"%}, TADS {% include keybind.html name="sight-select-tads"%} or FCR {% include keybind.html name="sight-select-fcr"%}
2. **W**eapon - WAS (Weapon Action Switch) the Rockets {% include keybind.html name="was-rkt"%}
3. **A**rm - The aircraft by pressing Arm button on the armament panel, verify ARM indication on WPN page
4. **R**ange - Single Detent Range {% include keybind.html name="target-range" %} if stationary or Continuous Lase (Second Detent) (G) if moving. Verify outside of minimum (500m), within maximum (7500m)
5. **M**essages - Verify Type Selection (6PD, 6FL, etc.), Quantity OR no PYLON LIMIT, AZ LIMIT, etc. displayed

When engaging cooperatively, the CPG uses the TADS to acquire the target which provides steering information to the PLT via the rocket steering cursor. Once the CPG has acquired the target, they call 'match', the PLT then responds with 'matching' and once the rocket steering cursor is centered in the LOS the PLT then calls 'shoot' and the CPG fires.
