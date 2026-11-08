---
title: AGM-114 Hellfire
lead: Laser-guided (SAL) and radar-guided (RF) Hellfire missiles — types, missile mode, trajectories, engagement sequences and messages.
keywords: [hellfire, agm-114, missile, sal, rf, laser, radar, lobl, loal, trajectory, direct, lo, hi, mode, norm, man, ripl, channel, code, align, handoff, hf tof, lase trgt, swarm]
seats: [PLT, CPG]
redirect_from:
  - /weapons-hellfire.html
  - /weapons-ammo-hellfires.html
---

## Types

| Missile | Guidance | Warhead |
|---|---|---|
| AGM-114K | Laser (SAL2) | Anti-armor |
| AGM-114K2A | Laser (SAL2) | Anti-armor, with a blast-fragmentation sleeve for personnel and soft targets |
| AGM-114N | Laser (SAL2) | Blast, for structures and bunkers |
| AGM-114FA | Laser (SAL1) | Earlier seeker, with a blast-fragmentation sleeve |
| AGM-114L | Radar (RF) | Anti-armor, fire-and-forget; requires the [fire control radar]({{ '/targeting/fcr/' | relative_url }}) or a TADS handover |

Missiles are carried on four-rail M299 launchers. The missile type is selected with `R1`{: .vab} TYPE (SAL or RF) and, for laser missiles, `L3`{: .vab} SAL SEL on the [WPN page]({{ '/displays/mpd/wpn/' | relative_url }}).

## Missile mode {#modes}

Each crew station sets its missile mode with `R2`{: .vab} MODE on the WPN page missile format:

| Mode | Function |
|---|---|
| NORM | The next missile of the selected type is selected automatically, in launcher sequence. |
| MAN | The crewmember selects the next missile with {% include key.html id="fza_ah64_missileAdvance" %}. |
| RIPL | Selectable; ripple fire is not simulated, and RIPL operates as NORM. |

The HAD displays the trajectory and mode, for example `LO NORM`{: .mpd}. RF missiles have no trajectory and display `LOBL NORM`{: .mpd}, or `LOAL NORM`{: .mpd} when not locked on before launch.

## Laser Hellfire (SAL)

A SAL Hellfire guides on laser energy of the code on its priority channel, from the aircraft's own laser or any other designator on that code. See [Laser]({{ '/targeting/laser/' | relative_url }}) and [Laser codes]({{ '/displays/mpd/code/' | relative_url }}).

**Lock-on before launch (LOBL).** If the seeker detects laser energy on its code at launch, the missile locks on before launch and flies directly to the target. The missile symbol on the WPN page displays **T** while the seeker detects the spot.

**Lock-on after launch (LOAL).** If no spot is detected at launch, the missile flies the selected trajectory toward the range of the range source and searches for the spot in flight. LOAL is used for launches from masked positions and for remote designation.

| Trajectory | `R3`{: .vab} TRAJ | Profile |
|---|---|---|
| DIR | Direct | Most direct path (default) |
| LO | Low | Low climb |
| HI | High | High climb and steep dive, to clear terrain between the aircraft and the target |

For a LOAL launch, the target must be within 7.5° of the nose and the aircraft within 10° of bank; outside these limits the HAD displays YAW LIMIT or ROLL LIMIT. Approximately 12 seconds before impact the HAD displays `LASE nn TRGT`{: .mpd}; the target must be lased from that point until impact.

### SAL Hellfire autonomous engagement sequence {#sal-engagement}

A target is engaged with a SAL Hellfire using the following sequence, known as SWARM:

1. **Sight**: select TADS {% include key.html id="fza_ah64_v30_sightSelectTADS" %}.
2. **Weapon**: WAS the missiles {% include key.html id="fza_ah64_wasMsl" %}.
3. **Armed**: arm the aircraft with the A/S button on the armament panel, and verify the ARMED indication on the WPN page.
4. **Range**: lase continuously {% include key.html id="fza_ah64_laserDesig" %}. Verify the range is outside the minimum (500 m) and within the maximum (6,000 m).
5. **Messages**: verify the trajectory (DIR, LO or HI), the mode (NORM, MAN or RIPL) and the constraints box.
{: .steps}

Fire with the weapon trigger and lase the target until impact. The HAD counts down the time of flight as `HF TOF=nn`{: .mpd}.

| HAD | Meaning |
|---|---|
| BACKSCATTER | Launch inhibited: the seeker is not tracking the laser spot at the TADS line of sight (the spot is off the TADS line of sight, or the laser is returning from foliage with no solid surface behind it). |
| `REMOTE`{: .mpd} | Missiles actioned with the priority missile channel code different from the LRFD code: the missile guides on another designator. |

## Radar Hellfire (RF) {#rf}

The AGM-114L has its own radar seeker. After launch it acquires and guides to the target independently.

### Power and alignment

An RF missile must be powered and aligned before launch. **MSL PWR** on the WPN page RF format selects:

| Setting | Missiles powered |
|---|---|
| ALL | Every RF missile |
| AUTO | The next missiles to be fired: 4 with eight or more loaded, 2 with four or more, 1 with two or more |
| NONE | None |

With missiles actioned and RF selected, the next missile is powered regardless of the setting. A newly powered missile aligns in 2 to 3 seconds; the missile symbol displays **S** while aligning and **R** when ready. Until it is ready, the HAD displays MSL NOT RDY and the missile cannot be fired.

Selecting FCR as the sight selects RF missiles; TYPE cannot be changed with FCR as the sight. Within 2.5 km, with the target in the seeker's field of view, the missile locks on before launch (**T**). Beyond 2.5 km it flies a lofted trajectory and activates its seeker as it approaches the target. If the seeker does not acquire the target, the HAD displays `NO ACQUIRE`{: .mpd}. Chaff near the target can break the seeker's track.

### RF Hellfire autonomous engagement sequence {#rf-engagement}

Orient the aircraft toward the threat, then engage the target with an RF Hellfire using the following sequence, known as SWARM:

1. **Sight**: select FCR {% include key.html id="fza_ah64_v30_sightSelectFCR" %}.
   1. Conduct a single scan {% include key.html id="fza_ah64_fcrSingleScan" %}.
   2. Select the desired next-to-shoot (NTS) target {% include key.html id="vehLockTargets" %}.
2. **Weapon**: WAS the missiles {% include key.html id="fza_ah64_wasMsl" %}.
3. **Armed**: arm the aircraft with the A/S button on the armament panel, and verify the ARMED indication on the WPN page.
4. **Range**: verify the range is outside the minimum (500 m) and within the maximum: 6,000 m for a stationary target, 8,000 m for a moving target.
5. **Messages**: verify the constraints box. The target must be within 20° of the nose and the aircraft within 20° of bank; outside these limits the HAD displays YAW LIMIT or ROLL LIMIT.
{: .steps}

Fire with the weapon trigger. The missile is launched at the NTS target.

### RF Hellfire with a TADS handover

The CPG can engage a target acquired with the TADS:

1. TADS – Select as sight; RF missiles – Select.
2. Target – Lase continuously. After 2.5 to 5 seconds the target data is handed over to the missile; until then the HAD displays `TARGET DATA?`{: .mpd}.
3. Weapon trigger – Fire. The handover is retained until the missile is fired, the weapon is changed or the TADS is deselected.
{: .steps}

## Inhibits

The complete list of messages that inhibit or qualify a missile launch is on the [Weapon action switch]({{ '/weapons/was/' | relative_url }}) page.
