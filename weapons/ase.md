---
title: Aircraft survivability equipment (ASE)
lead: The radar and laser warning receivers, missile warning system, chaff, flares and IR jammer, by mission equipment fit.
keywords: [ase, survivability, rlwr, radar warning, laser warning, missile warning, mws, chaff, flares, ir jammer, countermeasures, sam, aaa, threats]
seats: [PLT, CPG]
---

## Equipment

| | US equipment | British equipment |
|---|---|---|
| Radar and laser warning receiver (RLWR) | Yes | Yes |
| Chaff | Yes | Yes |
| IR jammer | Yes | |
| Flares | | Yes |
| Missile warning system (MWS) | | Yes |

The equipment fit is selected in the editor or the [mission planner]({{ '/mission/planner/' | relative_url }}); see [Variants and configuration]({{ '/aircraft/variants/' | relative_url }}). All ASE requires DC power.

## Activation

After start-up, on the [ASE page]({{ '/displays/mpd/ase/' | relative_url }}):

1. `R6`{: .vab} RLWR – On. A tone sounds when the receivers come on.
2. `T1`{: .vab} CHAFF (US) or CMS (British) – ARM.
3. `R1`{: .vab} IRJAM (US) or MWS (British) – On.
4. Autopage – Select the threat level.
{: .steps}

## Warning receivers

### Radar warning

The RLWR detects radar emitters within approximately 8 km. Each emitter is displayed on the ASE page (and the TSD, when selected) at its bearing, and announced by voice with its type, clock position and state.

| State | Meaning | Voice |
|---|---|---|
| Search | The radar is searching. | Once, on first detection |
| Acquisition | The radar has acquired the aircraft. | On transition to acquisition |
| Track | The radar is tracking the aircraft and can fire. | On transition to track |
| Launch | A radar-guided missile has been launched. | "Missile launch", with direction |

Threat identification depends on the vehicle's configuration. Vehicles from mods with [compatibility]({{ '/mission/compatibility/' | relative_url }}) support are identified by type (for example SA-6, ZSU-23); any other vehicle with a radar is identified as a generic search radar.

### Laser warning

The RLWR also warns when a laser designator or rangefinder illuminates the aircraft, with a voice message and direction.

### Missile warning

With British equipment and the MWS on, the MWS detects any missile or rocket approaching the aircraft within 3 km, regardless of guidance, and announces "missile" with its direction. The MWS is the only warning of an IR-guided missile. Aircraft with US equipment receive no warning of an IR-guided missile; the IR jammer operates without cueing.

## Countermeasures

| Countermeasure | Effective against | Release |
|---|---|---|
| Chaff | Radar-guided missiles | Arma **Countermeasures** binding, with chaff at ARM |
| Flares (British) | IR-guided missiles | {% include key.html id="fza_ah64_flare" %}, with the MWS on |
| IR jammer (US) | IR-guided missiles | Continuous once the jammer displays OPER |

Chaff is not effective against IR-guided missiles, and flares are not effective against radar-guided missiles. A launch call from the RLWR indicates a radar-guided missile; a missile call from the MWS without a preceding launch call indicates a probable IR-guided missile.

A full load is 30 chaff and, with British equipment, 60 flares, displayed on the ASE page. Rearming refills them; see [Rearm and refuel]({{ '/mission/rearm/' | relative_url }}).

The RLWR voice volume is set with **RLWR volume Knob** in [Addon settings]({{ '/getting-started/settings/' | relative_url }}).
