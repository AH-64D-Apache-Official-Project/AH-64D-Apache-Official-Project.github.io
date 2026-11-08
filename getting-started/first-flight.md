---
title: Introductory flight
lead: An introductory flight in single player — start-up, hover, traffic pattern and landing — without weapons.
keywords: [first flight, tutorial, hover, takeoff, landing, beginner, quick start]
---

## Setup

1. Bindings – Set the cockpit cursor, flight controls and collective. See [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}).
2. Control scheme – Select under **Addon Options → BradMick's HeliSim**. See [Addon settings]({{ '/getting-started/settings/' | relative_url }}#helisim). Keyboard: **Casual** (**Keyboard Auto Pedal** is on by default). Stick and pedals: **Realistic**, with Keyboard Auto Pedal off.
3. Editor – Place an **AH-64D BLOCK I** on an open area or airfield in daylight, with an **AH-64D Pilot** in the pilot crew station (rear), set playable; **Play Scenario**.
{: .steps}

## Start-up

Perform the [start-up checks]({{ '/flying/startup/' | relative_url }}), from the interior check through the before takeoff check.

The aircraft is ready for flight with Nr at 101% and no warnings or cautions on the UFD.

## Hover

With hover symbology selected ({% include key.html id="fza_ah64_symbologySelectDown" %}), press and hold the force trim interrupt. Apply collective while applying left pedal and left cyclic as required to maintain heading and position. At approximately 20% below hover power the aircraft becomes "light on the wheels". Continue increasing collective until the aircraft settles at 5 ft. Once stabilized at 5 ft, release the force trim and engage the attitude and altitude holds as desired.

Below 5 kt ground speed, attitude hold operates in position hold and holds the aircraft over the ground. A drift of approximately 50 ft from the hold point displays the `HOVER DRIFT`{: .mpd} advisory.

## Traffic pattern

### Takeoff and climb

With transition symbology selected ({% include key.html id="fza_ah64_symbologySelectUp" %}), press and hold the force trim interrupt. Increase the collective a minimum of 10% above hover power, not to exceed maximum torque available or 100%, whichever is lower. Apply pedal as necessary to maintain ground track alignment below 50 ft, or commensurate with obstacles, and apply forward cyclic as necessary to achieve 50 kt by 50 ft.

Once above 50 ft, place the aircraft in aerodynamic trim, ball centered. Maintain a 500 ft per minute rate of climb, ±200 fpm. Within 10% of the rate of climb (approximately 50 ft) of the desired cruise altitude, apply forward cyclic to accelerate to the desired cruise speed and level the VSI at the desired cruise altitude. Once stable, release the force trim and engage the attitude and altitude holds as desired.

### Downwind

On downwind, complete the before landing check:

1. Weapons – Safe; ground override – Off; nothing actioned in the high action display.
2. ASE – Safe.
3. Tail wheel – Locked; TAIL WHEEL button light off (not currently simulated).
4. Parking brake – Released, handle in (not currently simulated).
5. Power – Sufficient for the approach.
{: .steps}

### Base to final

Prior to turning base, press and hold the force trim interrupt and reduce the collective approximately 20% below cruise. Apply aft cyclic as necessary to maintain a 500 fpm ±200 fpm rate of descent while decelerating to approximately 20 kt below cruise speed. Perform a smooth, continuous turn to final. Once at the desired altitude, adjust the collective to arrest the rate of descent and maintain the desired airspeed until the desired approach angle is reached.

Maintain a constant approach angle by keeping the flight path vector slightly above the intended point of landing. Control the flight path vector vertically with a combination of fore/aft cyclic and collective, and laterally with cyclic. Maintain the aircraft in aerodynamic trim until 50 ft, then apply pedal to align the velocity vector with the lubber line.

### Landing

Expect to lose sight of the intended point of landing at approximately 100 to 150 ft AGL. Select reference points to the left and right of the aircraft to assist in maintaining a constant approach angle. At approximately 30 ft, apply aft cyclic and increase the collective to effect a smooth touchdown, or terminate to a 5 ft hover.

> Transition symbology is maintained until the flight path vector disappears, to assist in maintaining orientation during the landing.
{: .note}

> During the approach, the rate of descent must be controlled within the power available. A rate of descent allowed to build at low airspeed places the aircraft behind the power curve, where the helicopter settles with insufficient power applied to arrest the weight of the aircraft: settling with power. Arresting each 100 fpm of descent requires approximately 2% torque above IGE hover torque; the rate of descent must not exceed what the remaining power margin can arrest. See [Settling with power]({{ '/flying/flight-model/' | relative_url }}#settling-with-power).
{: .caution}

## Further reading

- [Flight control modes]({{ '/flying/flight-control/' | relative_url }}): force trim and the hold modes.
- [IHADSS]({{ '/displays/ihadss/' | relative_url }}): the flight and weapon symbology formats.
- [MPDs]({{ '/displays/mpd/' | relative_url }}) and the [TSD]({{ '/displays/mpd/tsd/' | relative_url }}) for navigation.
- With a CPG: [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}) and [Weapons]({{ '/weapons/was/' | relative_url }}).
