---
title: AGM-114 Hellfire
lead: Laser-guided and radar-guided anti-tank missiles, four to a launcher. How to set them up, fire them lock-on before or after launch, and what each message means.
keywords: [hellfire, agm-114, missile, sal, rf, laser, radar, lobl, loal, trajectory, direct, lo, hi, mode, norm, man, ripl, channel, code, align, handoff, hftof, lase trgt]
seats: [PLT, CPG]
redirect_from:
  - /weapons-hellfire.html
  - /weapons-ammo-hellfires.html
---

## Types

| Missile | Guidance | Warhead |
|---|---|---|
| **AGM-114K** | Laser (SAL2) | Anti-armour. |
| **AGM-114K2A** | Laser (SAL2) | As the K, with a blast-fragmentation sleeve against people and soft targets. |
| **AGM-114N** | Laser (SAL2) | Thermobaric, against buildings and bunkers. |
| **AGM-114FA** | Laser (SAL1) | Older seeker, with a blast-fragmentation sleeve. |
| **AGM-114L** | Radar (RF) | Anti-armour, fire-and-forget. Needs the [fire control radar]({{ '/targeting/fcr/' | relative_url }}) or a TADS handoff. |

They come on four-rail M299 launchers. Choose the missile type to fire with `R1`{: .vab} **TYPE** (SAL or RF) and, for laser missiles, `L3`{: .vab} **SAL SEL** on the [WPN page]({{ '/displays/mpd/wpn/' | relative_url }}).

## Missile mode {#modes}

Each crew station sets its own mode with `R2`{: .vab} **MODE** on the WPN page's missile format:

| Mode | Behaviour |
|---|---|
| **NORM** | The next missile of the selected type is chosen for you, working through the launchers in turn. |
| **MAN** | You choose which missile is next, with {% include key.html id="fza_ah64_missileAdvance" %}. It does nothing in the other modes. |
| **RIPL** | Can be selected, but ripple fire is not simulated: it behaves as NORM. |

The HAD shows the trajectory and your mode, for example `LO-NORM`{: .mpd}.

## Laser Hellfires (SAL)

A laser Hellfire homes on a laser spot of the code on its **primary channel**. The spot can be your own laser or anyone else's on that code. See [Laser]({{ '/targeting/laser/' | relative_url }}) and the [COM pages]({{ '/displays/mpd/com/' | relative_url }}) for codes.

### Lock-on before launch (LOBL)

If the missile's seeker can already see a spot on its code when you fire, it locks on before launch and flies **directly** to it. The WPN page's missile symbol shows **T** while the seeker sees the spot.

1. Action missiles with {% include key.html id="fza_ah64_wasMsl" %}.
2. CPG: select the TADS, put it on the target and lase ({% include key.html id="fza_ah64_laserDesig" %}). Keep lasing.
3. Check the missile shows **T** and the HAD shows no inhibit.
4. Fire, and keep the laser on the target until impact. The HAD counts down `HFTOF=nn`{: .mpd}.
{: .steps}

### Lock-on after launch (LOAL)

If no spot is visible at launch, the missile flies the selected **trajectory** towards your range source's range, and looks for the spot on the way. Use it to fire from behind cover, or for someone else's laser.

| Trajectory | `R3`{: .vab} **TRAJ** | Flight |
|---|---|---|
| **DIR** | Direct | The most direct path. The default. |
| **LO** | Low | A low climb. |
| **HI** | High | A high climb and steep dive, to clear terrain between you and the target. |

Have the range set (MANRNG, a stored point, or an earlier lase). For the best chance, fire with the target within 7.5° of the nose and no more than 10° of bank; outside that the HAD warns **YAW LIMIT** or **ROLL LIMIT**. About 12 seconds before impact the HAD shows `LASE nn TRGT`{: .mpd}: lase the target then, and keep lasing until impact.

### Messages

- **BACKSCATTER** stops the launch: the seeker is not tracking where your TADS is lasing, either because the spot is off the TADS line of sight or the laser is stopping on foliage with nothing solid behind it.
- `REMOTE`{: .mpd} on the HAD: missiles are actioned and the primary channel's code is not your laser's. The missile will guide on someone else's laser.

## Radar Hellfires (RF) {#rf}

The AGM-114L carries its own radar seeker. Once fired it finds the target by itself: you are free to turn away.

### Power and alignment

A radar missile must be powered and aligned before it can be fired. Set **MSL PWR** on the WPN page's RF format:

| Setting | Powers |
|---|---|
| **ALL** | Every RF missile. |
| **AUTO** | The next few: 4 with eight or more loaded, 2 with four or more, 1 with two or more. |
| **NONE** | None. |

Whatever the setting, the next missile is powered while missiles are actioned with RF selected. A newly powered missile takes 2 to 3 seconds to align. The missile symbol shows **S** while aligning and **R** when ready; until then the HAD shows **MSL NOT RDY** and it will not fire.

### Firing on a radar target

Selecting the FCR as your sight selects RF missiles automatically, and **TYPE** cannot be changed while the FCR is your sight.

1. Scan with the radar and step the next-to-shoot (NTS) target to the one you want. See [Fire control radar]({{ '/targeting/fcr/' | relative_url }}).
2. Action missiles. Keep the target within 20° of the nose and no more than 20° of bank, or the HAD warns **YAW LIMIT** or **ROLL LIMIT**.
3. Fire. The missile goes for the NTS.
{: .steps}

Within 2.5 km, with the target inside the seeker's view, the missile locks on before launch and flies straight at it; the symbol shows **T**. Further out it flies a lofted path (high beyond 3.5 km, low inside it) and switches its seeker on as it nears the target. Against a stationary target beyond 2.5 km it approaches from the side.

If the seeker never finds the target, the HAD shows `NO ACQUIRE`{: .mpd}.

### Firing with the TADS

The CPG can fire RF missiles at a target found with the TADS:

1. Select the TADS and RF missiles.
2. Lase the target continuously. After 2.5 to 5 seconds the target data is handed to the missile. Until then the HAD shows **TGT DATA?**.
3. Fire. You can stop lasing once the handoff is made; it lasts until you fire, change weapon or leave the TADS.
{: .steps}

### Countermeasures

Chaff near the target can defeat the radar seeker: each chaff cloud in the seeker's view has a chance to break its lock.

## Inhibits

The full list of messages that stop or warn about a missile launch is on the [Weapon action switch]({{ '/weapons/was/' | relative_url }}) page. In short: no launch beyond 8 km, below 0.5 G, or with the aircraft rolling or turning faster than 30° a second (a warning only).
