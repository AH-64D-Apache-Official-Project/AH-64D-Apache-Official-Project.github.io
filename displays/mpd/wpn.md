---
title: Weapons (WPN) page
lead: Sight, acquisition source and range for the crew station, the status of every weapon, and the gun, rocket and missile settings.
keywords: [wpn, weapons, gun, cannon, burst, rocket, salvo, quantity, missile, hellfire, sal, rf, trajectory, lobl, loal, mode, channel, laser code, manual range, lrfd]
seats: [PLT, CPG]
redirect_from:
  - /mpd-wpn.html
---

The WPN page is selected with the WPN fixed action button. The sight, acquisition source and range displayed are those of the crew station; weapon settings are aircraft common, except where stated as crewstation independent.

{% include fig.html id="mpd-wpn" %}

## Status windows

| Item | Display |
|---|---|
| SIGHT | SIGHT select status window: the selected sight, HMD, TADS or FCR. See [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}). |
| ACQ | ACQ select status window: the selected acquisition source |
| LST / LRFD | LST and LRFD status windows: the LST and LRFD code selections. See [Laser codes]({{ '/displays/mpd/code/' | relative_url }}). |
| SAFE / ARM | ARM/SAFE status window: the aircraft status, from the A/S button. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}). |
| CHAFF | CHAFF status: the chaff cartridges remaining and the dispenser status, SAFE or ARM; with British equipment, flares also. |

Below the status windows, the gun icon displays the rounds counter, and the missile and rocket launcher icons display each wing station's load. A failed gun or pylon displays the FAIL indicator. The gun fails without utility hydraulics, without AC and DC power, or with the turret damaged. The pylons cannot articulate without utility hydraulics.

## Buttons on every format

| Button | Label | Function |
|---|---|---|
| `T1`{: .vab} | `CHAN`{: .mpd} | [CHAN page]({{ '/displays/mpd/code/' | relative_url }}#chan) |
| `T2`{: .vab} | `ASE`{: .mpd} | [ASE page]({{ '/displays/mpd/ase/' | relative_url }}) |
| `T4`{: .vab} | `CODE`{: .mpd} | [CODE page]({{ '/displays/mpd/code/' | relative_url }}#code) |
| `T5`{: .vab} | `COORD`{: .mpd} | [COORD page]({{ '/displays/mpd/tsd/' | relative_url }}#coord) |
| `R5`{: .vab} | `LRFD`{: .mpd} | Fires the laser, or stops it if firing. See [Laser]({{ '/targeting/laser/' | relative_url }}). |
| `R6`{: .vab} | `ACQ`{: .mpd} | [Acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list |
| `B1`{: .vab} | | MENU page |
| `B2`{: .vab} | `GUN`{: .mpd} | Gun format |
| `B3`{: .vab} | `MSL`{: .mpd} | Missile format |
| `B5`{: .vab} | `RKT`{: .mpd} | Rocket format |
| `B6`{: .vab} | `MANRNG>`{: .mpd} | Manual range on the KU: 100 to 50,000 m, or `A` for automatic range. See [Range]({{ '/targeting/sights/' | relative_url }}#range). |

`B2`{: .vab}, `B3`{: .vab} and `B5`{: .vab} operate only with no weapon actioned. When a weapon is actioned, the page displays that weapon's format, and returns when the weapon is de-actioned.

UTIL, BORESIGHT, GRAYSCALE, TRAIN and HARMONIZE are not simulated.

## GUN

| Button | Label | Function |
|---|---|---|
| `L1`{: .vab}–`L5`{: .vab} | `10` `20` `50` `100` `ALL` | BURST LIMIT: rounds per trigger pull |
| `R2`{: .vab} | `MODE`{: .mpd} | NORM: the gun follows the selected sight. FXD: the gun is fixed to the centreline of the aircraft. Crewstation independent. |

See [M230 chain gun]({{ '/weapons/cannon/' | relative_url }}).

## RKT

The INVENTORY buttons on the left list the rocket types loaded, up to five, with the quantity of each. The rocket launcher icons show the location of each type.

| Button | Label | Function |
|---|---|---|
| `L1`{: .vab}–`L5`{: .vab} | INVENTORY | Selects the rocket warhead and type to be fired. With a player in the CPG crew station, only the CPG can change it. |
| `R1`{: .vab} | `QTY`{: .mpd} | Rockets per trigger pull: `R1`{: .vab} 1, `R2`{: .vab} 2, `R3`{: .vab} 4, `R4`{: .vab} 8, `R5`{: .vab} 12, `R6`{: .vab} 24, `B6`{: .vab} ALL |

The TOTAL ROCKETS status window displays the quantity of the selected type remaining. See [Hydra 70 rockets]({{ '/weapons/rockets/' | relative_url }}).

## MSL

The MSL format changes with the missile TYPE selected. `R1`{: .vab} TYPE selects SAL (laser-guided) or RF (radar-guided, AGM-114L). TYPE is inhibited with FCR as the sight, which selects RF missiles.

| Button | Label | Function |
|---|---|---|
| `R1`{: .vab} | `TYPE`{: .mpd} | SAL or RF |
| `R2`{: .vab} | `MODE`{: .mpd} | Missile mode for the crew station: `R1`{: .vab} NORM, `R2`{: .vab} MAN, `R3`{: .vab} RIPL. See [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}#modes). |

### SAL missiles {#sal-missiles}

| Button | Label | Function |
|---|---|---|
| `L1`{: .vab} | `PRI`{: .mpd} | Channel options on `L1`{: .vab}–`L5`{: .vab}: CHAN 1–4 for the priority channel, or NONE |
| `L2`{: .vab} | `ALT`{: .mpd} | As PRI, for the alternate channel; requires a priority channel |
| `L3`{: .vab} | `SAL SEL`{: .mpd} | Steps through the SAL Hellfire types loaded: SAL2 for the K, K2A and N; SAL1 for the FA |
| `R3`{: .vab} | `TRAJ`{: .mpd} | Trajectory: `R1`{: .vab} HI, `R2`{: .vab} LO, `R3`{: .vab} DIR |

The SAL missile status window displays the code held by each of the four missile channels. The SAL missile icon of the next missile displays the priority channel code and, below it, **T** when the missile seeker is in track mode, or **R** when it is not.

HFMSN, DEICE and MSL CCM are not simulated.

### RF missiles

| Button | Label | Function |
|---|---|---|
| `L1`{: .vab}–`L3`{: .vab} | `ALL` `AUTO` `NONE` | MSL PWR: the method of RF missile power management. ALL commands power to all RF missiles, AUTO powers the missiles next to be launched, and NONE removes power. A missile requires several seconds after power-up before it is ready to receive a target. |

The RF missile icon of the next missile displays **S** while powered but not yet aligned, **R** when ready to receive a target, and **T** when the missile seeker is in track mode.

LOBL INHIBIT and 2ND TARGET INHIBIT are not simulated. See [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}#rf).
