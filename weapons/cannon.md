---
title: M230 chain gun
lead: The 30 mm M230 chain gun, its operation, the engagement sequence and the messages presented to the crew.
keywords: [m230, cannon, gun, 30mm, m789, hedp, aws, area weapon system, burst limit, norm, fxd, swarm, gun fail, gun jam]
seats: [PLT, CPG]
redirect_from:
  - /weapons-m230.html
  - /weapons-ammo-m789.html
---

## Description

The M230 is a single-barrel 30 mm chain gun, mounted in a turret on the underside of the forward fuselage. Its bolt is cycled by an electrically driven chain, and it is fed linkless ammunition by the ammunition handling system. The turret is driven by the utility hydraulic system. The gun fires M789 high explosive dual purpose (HEDP) rounds, which are capable of engaging infantry, mechanised and motorised units, and lightly armoured targets.

When not in use, or on a loss of utility hydraulics, the gun moves to a stowed position of 11° up. It only moves from this position after being actioned by either crewmember.

The gun carries 300 rounds with the IAFS installed, or 1,200 rounds with the 1,200-round magazine. The gun aims at the crewmember's selected sight.

## Operation

The gun is actioned with the weapon action switch (WAS), {% include key.html id="fza_ah64_wasGun" %}. On the WPN page gun format, the crewmember selects the burst limit (10, 20, 50, 100 or ALL rounds per trigger pull) and the gun mode:

- **NORM**: the gun follows the selected sight.
- **FXD**: the gun is fixed along the aircraft's centreline.

## Engagement sequence

A target is engaged with the gun using the following sequence, known as SWARM:

1. **Sight**: select HMD {% include key.html id="fza_ah64_v30_sightSelectHMD" %}, TADS {% include key.html id="fza_ah64_v30_sightSelectTADS" %} or FCR {% include key.html id="fza_ah64_v30_sightSelectFCR" %}.
2. **Weapon**: WAS the gun {% include key.html id="fza_ah64_wasGun" %}.
3. **Armed**: arm the aircraft with the A/S button on the armament panel, and verify the ARMED indication on the WPN page.
4. **Range**: lase once for a stationary target, or lase continuously for a moving target. Verify the range is outside the minimum (500 m) and within the maximum (4,200 m).
5. **Messages**: verify the round count, the gun mode (NORM or FXD), and that no inhibit such as EL LIMIT or AZ LIMIT is displayed.
{: .steps}

## Messages

| HAD | Condition |
|---|---|
| `GUN FAIL`{: .mpd} | Gun turret damaged, or utility hydraulic pressure or fluid lost. |
| `GUN JAM`{: .mpd} | Ammunition feed damaged (1,200-round magazine installed). |
| `AZ LIMIT`{: .mpd} / `EL LIMIT`{: .mpd} | Target outside the gun's azimuth or elevation travel. |
| `COINCIDENCE`{: .mpd} | Gun not yet aligned with the selected sight. |
| `ALT LAUNCH`{: .mpd} | Gun inhibited following a rocket or missile launch. |

When the gun has failed with the gun actioned, the LOS reticle flashes.

Barrel heating is simulated. Firing long bursts without allowing the barrel to cool results in a round cooking off in the chamber, which damages the gun turret and fails the gun.
