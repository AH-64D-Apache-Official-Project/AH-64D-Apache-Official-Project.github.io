---
title: M230 cannon
lead: The 30 mm chain gun under the nose. It follows your sight, works out its own lead and drop, and fires high-explosive dual-purpose rounds.
keywords: [m230, cannon, gun, 30mm, m789, hedp, burst, fxd, norm, jam, overheat, cookoff, rounds]
seats: [PLT, CPG]
redirect_from:
  - /weapons-m230.html
  - /weapons-ammo-m789.html
---

## The gun

| | |
|---|---|
| Ammunition | M789 HEDP (high-explosive dual-purpose), 805 m/s at the muzzle |
| Rate of fire | About 550 rounds a minute |
| Rounds | 300 with the IAFS fitted (the default), 1,200 with the 1,200-round magazine. See [Variants and customisation]({{ '/aircraft/variants/' | relative_url }}). |
| Travel | 86° left and right, 11° up, 60° down |

## Firing

1. Action the gun with {% include key.html id="fza_ah64_wasGun" %}. The HAD shows `CGUN`{: .mpd} or `PGUN`{: .mpd} and the rounds left.
2. Look at the target with your sight: your head with the HMD, the TADS, or the radar's next-to-shoot target with the FCR.
3. Get a good range. The gun aims at your [range source]({{ '/targeting/sights/' | relative_url }}#range)'s range, so lase with the TADS if you can.
4. Pull the trigger. One pull fires the burst set on the [WPN page]({{ '/displays/mpd/wpn/' | relative_url }}): 10, 20, 50, 100 or all.
{: .steps}

The gun works out its own superelevation for the range, and leads a moving target when you are tracking it with the radar. It turns towards the solution at its own rate; until it is within 1° the HAD shows **COINCIDENCE** and it will not fire. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}) for every message.

## Modes

Each crew station sets its own gun mode with `R2`{: .vab} **MODE** on the WPN page's gun format:

- **NORM**: the gun follows your sight.
- **FXD**: the gun is fixed along the nose, 6° up. Use it if the gun's aiming is damaged or for a strafing run. The HAD shows `GUN FIXED`{: .mpd}.

Without AC power, the gun is fixed forward regardless.

## Failures

| HAD | Cause |
|---|---|
| `GUN JAM`{: .mpd} | The ammunition feed is damaged, with the 1,200-round magazine fitted. |
| `GUN FAIL`{: .mpd} | The gun turret is damaged, or utility hydraulic pressure or fluid is too low. |

When the gun has failed the reticle flashes.

The barrel heats as you fire, using ACE's overheating model. Fire long bursts and let it get hot enough, and a round cooks off in the chamber: the gun turret is damaged and the gun fails. Fire in bursts and let it cool.
