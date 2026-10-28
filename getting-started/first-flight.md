---
title: Your first flight
lead: Start up, hover, fly a circuit and land. About fifteen minutes, single player, no weapons.
keywords: [first flight, tutorial, hover, takeoff, landing, beginner, quick start]
---

## Set up

1. Bind the cockpit cursor, the flight controls and the collective. See [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}).
2. Choose your control scheme under **Addon Options → BradMick's HeliSim**. See [Addon settings]({{ '/getting-started/settings/' | relative_url }}#helisim). On a keyboard, start with **Casual**; **Keyboard Auto Pedal** is on by default. With a stick and pedals, choose **Realistic** and turn Keyboard Auto Pedal off.
3. In the editor, place an **AH-64D BLOCK I** on an open field or an airfield in daylight, put an **AH-64D Pilot** in the pilot seat (the rear seat), make it playable and press **Play Scenario**.
{: .steps}

## Start the aircraft

Follow the [start-up checklist]({{ '/flying/startup/' | relative_url }}). In short: rotor brake off, battery on, fit the monocle, APU on, start each engine (power lever to IDLE above 23% Ng), both levers to FLY, APU off.

When Nr reaches 101% and the UFD shows no warnings or cautions, you are ready.

## Hover

1. Press {% include key.html id="fza_ah64_symbologySelectDown" %} for **hover** symbology on your monocle. The velocity vector now shows drift at 6 kt full scale.
2. Raise the collective slowly. The aircraft gets light, then lifts. Keep the nose straight with the pedals.
3. Settle at about 10 ft on the radar altimeter. Keep the velocity vector inside the reticle: no drift.
4. Below 5 kt ground speed, the flight computer's attitude hold sits in **position hold** and holds the aircraft over the ground. If you drift more than about 50 ft from where it engaged, the `HOVER DRIFT`{: .mpd} advisory shows.
{: .steps}

> Small inputs. The Apache is heavy and responds late, then too much; wait for each correction to take effect before adding another.
{: .tip}

## Fly a circuit

1. Press {% include key.html id="fza_ah64_symbologySelectUp" %} for **transition** symbology.
2. Lower the nose a little and raise the collective to keep your height as you accelerate. Watch torque on the monocle; keep it below 100%.
3. Climb to about 500 ft and settle at 100 kt.
4. Turn with the cyclic, using pedal to keep the trim ball centred.
5. Fly back towards your take-off point, slowing to about 40 kt on the final approach, and descend.
6. Below 40 kt and 50 ft, switch back to **hover** symbology, come to a hover, then lower the collective gently until you are on the ground.
7. Collective fully down.
{: .steps}

## Next steps

- [Flight control modes]({{ '/flying/flight-control/' | relative_url }}): force trim and the hold modes make the Apache much easier to fly.
- [IHADSS]({{ '/displays/ihadss/' | relative_url }}): what every symbol on the monocle means.
- [Using the MPDs]({{ '/displays/mpd/' | relative_url }}) and the [TSD]({{ '/displays/mpd/tsd/' | relative_url }}) for navigation.
- When you are comfortable, add a CPG and work through [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}) and [Weapons]({{ '/weapons/was/' | relative_url }}).
