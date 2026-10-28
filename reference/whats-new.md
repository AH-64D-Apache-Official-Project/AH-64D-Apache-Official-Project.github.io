---
title: What's new in 3.0
lead: The big changes since 2.2.8, the last full release, with links to where each is explained.
keywords: [whats new, new, changes, release, 3.0, helisim, ihadss, helmet, tpm, rmap, video, radial, minigames]
---

> Version 3.0 needs **HeliSim Core 1.4** or later and **CBA_A3 3.16** or later. See [Installation]({{ '/getting-started/installation/' | relative_url }}).
{: .note}

The first sections are new since the 2.3 release candidates. [Also new since 2.2.8](#since-228) lists what those pre-releases added.

## Flying

- **HeliSim Core.** The flight model and the aircraft systems (engines, electrics, hydraulics, fuel, rotor) now come from the separate HeliSim Core mod, which must be loaded, in place of the flight model built into the mod. See [HeliSim flight model]({{ '/flying/flight-model/' | relative_url }}).
- **Flight control modes** run on HeliSim Core's flight management computer. Attitude hold picks position, velocity or attitude hold by your ground speed, and heading hold blends into turn coordination. See [Flight control modes]({{ '/flying/flight-control/' | relative_url }}).
- The main and tail rotors can now be **destroyed**. See [Damage and failures]({{ '/aircraft/damage/' | relative_url }}).
- The [PERF page]({{ '/displays/mpd/perf/' | relative_url }}) shows the same figures in both crew stations, and the [mission planner]({{ '/mission/planner/' | relative_url }}) works out weight and performance from HeliSim's data, at your pressure altitude and temperature.

## Helmet and symbology

- A new **IHADSS helmet**, now the AH-64D pilot's default headgear. It is needed to bring the monocle down and for head tracking.
- **New helmet symbology**: four flight modes (transition, cruise, hover and bob-up), the CPG's weapon symbology, missile constraints, the rocket steering cursor and the high action display. See [IHADSS]({{ '/displays/ihadss/' | relative_url }}).
- The PNVS picture fills the monocle's lens, and the CPG can have the TADS picture there. Either crew station can take the PNVS or the TADS FLIR as its night vision sensor. See [Night vision]({{ '/targeting/nvs/' | relative_url }}).

## Sensors and targeting

- **Range sources**: laser, radar, navigation, manual and automatic, shown on the HAD. Targets can be **stored** along your sight. See [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}).
- The **laser spot tracker** finds someone else's laser spot and turns the TADS onto it. See [Laser]({{ '/targeting/laser/' | relative_url }}).
- The radar gains **TPM** (terrain profile) and **RMAP** modes. In TPM, **C SCP** draws the terrain profile and obstacles on the helmet. See [Fire control radar]({{ '/targeting/fcr/' | relative_url }}).
- A **radial menu** for your sight, the TADS, the radar, the laser spot tracker and your symbology. See [Radial menu]({{ '/targeting/radial/' | relative_url }}).

## Weapons

- Radar Hellfires are **powered and aligned** before they can be fired. See [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}#rf).
- With the gun in FXD, a reticle marks where it will hit. See [IHADSS]({{ '/displays/ihadss/' | relative_url }}#gun-fxd).
- **ALT LAUNCH** stops the gun firing straight after a rocket or missile launch. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}#before-it-fires-inhibits).

## MPDs

- The **VIDEO page** shows the TADS, the PNVS or either crew station's helmet symbology. See [VIDEO]({{ '/displays/mpd/video/' | relative_url }}).
- **Games** on the MPD, for the long wait on the ground. See [MPD games]({{ '/displays/mpd/games/' | relative_url }}).

## Also new since 2.2.8 {#since-228}

These came in the 2.2.9, 2.2.91 and 2.3 pre-releases:

- The **mission planner**, for loadout, fuel and performance on the ground. See [Mission planner]({{ '/mission/planner/' | relative_url }}).
- A more detailed **fuel system**, with leaking cells, and a new FUEL page. See [Fuel system]({{ '/aircraft/fuel/' | relative_url }}).
- **Transmission and gearbox damage** that grows with torque, with their own oil pressure cautions. See [Damage and failures]({{ '/aircraft/damage/' | relative_url }}).
- Radar Hellfires can be fired with a **TADS handoff**, without the radar. See [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}#rf).
- **Shot-at** markers on the TSD and FCR pages, and the TSD's [COORD]({{ '/displays/mpd/tsd/' | relative_url }}#coord) page for reviewing stored data.
- The **VERS** page, which checks the mod's files are intact. See [DMS]({{ '/displays/mpd/dms/' | relative_url }}).
- Air defence classification for **PRACS** and **PRACS SLA**. See [Compatibility]({{ '/mission/compatibility/' | relative_url }}).
- Stores loaded onto the wrong crew station or mixed on one station are corrected. See [Rearm and refuel]({{ '/mission/rearm/' | relative_url }}#pylon-rules).
- Translations of the mod's text, apart from the MPDs, into more languages.

For the full list of changes, see the [releases on GitHub]({{ site.links.github }}/releases).
