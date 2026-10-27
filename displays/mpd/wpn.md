---
title: WPN page
lead: The weapons page. What each crew station's sight and acquisition source are, the state of every weapon, and the settings for the cannon, rockets and Hellfires.
keywords: [wpn, weapons, gun, cannon, burst, rocket, salvo, quantity, missile, hellfire, sal, rf, trajectory, lobl, loal, mode, channel, laser code, manual range, lrfd]
seats: [PLT, CPG]
redirect_from:
  - /mpd-wpn.html
---

Open it with the **WPN** button. Each crew station sees its own sight, acquisition source and range on the page. The weapon settings are the aircraft's, shared by both.

{% include fig.html id="mpd-wpn" %}

## Status window

The top of the page always shows:

| Item | Shows |
|---|---|
| **SIGHT** | Your selected sight: HMD, TADS or FCR. See [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}). |
| **ACQ** | Your acquisition source. |
| **LST** / **LRFD** | The codes the laser spot tracker and the laser rangefinder/designator are set to. See [COM pages]({{ '/displays/mpd/com/' | relative_url }}). |
| **SAFE** / **ARMED** | The aircraft's arm state, from the **A/S** button. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}). |
| **CHAFF** | Chaff remaining, armed or safe. With British equipment, flares as well. |

Below them, the aircraft diagram shows the cannon, rounds remaining and each wing station's load. A failed cannon or pylon is marked on the diagram. The cannon fails without utility hydraulics, AC and DC power, or with its turret damaged. The pylons cannot move without utility hydraulics.

## Buttons on every format

| Button | Label | Action |
|---|---|---|
| `T1`{: .vab} | `CHAN`{: .mpd} | Opens the [CHAN page]({{ '/displays/mpd/com/' | relative_url }}#chan). |
| `T2`{: .vab} | `ASE`{: .mpd} | Opens the [ASE page]({{ '/displays/mpd/ase/' | relative_url }}). |
| `T4`{: .vab} | `CODE`{: .mpd} | Opens the [CODE page]({{ '/displays/mpd/com/' | relative_url }}#code). |
| `T5`{: .vab} | `COORD`{: .mpd} | Opens the [COORD page]({{ '/displays/mpd/tsd/' | relative_url }}#coord). |
| `R5`{: .vab} | `LRFD`{: .mpd} | Fires the laser, or stops it if it is firing. See [Laser]({{ '/targeting/laser/' | relative_url }}). |
| `R6`{: .vab} | `ACQ`{: .mpd} | Opens the [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list. |
| `B1`{: .vab} | | MENU. |
| `B2`{: .vab} | `GUN`{: .mpd} | Shows the gun format. |
| `B3`{: .vab} | `MSL`{: .mpd} | Shows the missile format. |
| `B5`{: .vab} | `RKT`{: .mpd} | Shows the rocket format. |
| `B6`{: .vab} | `MANRNG>`{: .mpd} | Sets a manual range on the KU: a range in metres from 100 to 50,000, or `A` for automatic range. See [Sights and acquisition]({{ '/targeting/sights/' | relative_url }}#range). |

`B2`{: .vab}, `B3`{: .vab} and `B5`{: .vab} only work while no weapon is actioned. Once a crew member actions a weapon, the page shows that weapon's format by itself, and returns when it is de-actioned.

**UTIL**, **BORESIGHT**, **GRAYSCALE**, **TRAIN** and **HARMONIZE** are not simulated.

## GUN

| Button | Label | Action |
|---|---|---|
| `L1`{: .vab}–`L5`{: .vab} | `10` `20` `50` `100` `ALL` | **Burst limit**: how many rounds one trigger pull fires. |
| `R2`{: .vab} | `MODE`{: .mpd} | **NORM**: the gun follows your sight. **FXD**: the gun is fixed straight ahead along the aircraft centreline. Each crew station has its own. |

See [M230 cannon]({{ '/weapons/cannon/' | relative_url }}).

## RKT

The left side lists the rocket types loaded, up to five, with how many of each. The pods on the diagram show which type is where.

| Button | Label | Action |
|---|---|---|
| `L1`{: .vab}–`L5`{: .vab} | rocket types | Selects the rocket type to fire. |
| `R1`{: .vab} | `QTY`{: .mpd} | Opens the quantity choices, how many rockets one trigger pull fires: `R1`{: .vab} 1, `R2`{: .vab} 2, `R3`{: .vab} 4, `R4`{: .vab} 8, `R5`{: .vab} 12, `R6`{: .vab} 24, `B6`{: .vab} ALL. |

**TOTAL ROCKETS** shows how many of the selected type are left. See [Hydra 70 rockets]({{ '/weapons/rockets/' | relative_url }}).

## MSL

The missile format changes with the type of Hellfire selected. `R1`{: .vab} **TYPE** switches between **SAL** (laser-guided) and **RF** (radar-guided, the AGM-114L). It does not work while your sight is the FCR, which always selects RF missiles.

These are on both formats:

| Button | Label | Action |
|---|---|---|
| `R1`{: .vab} | `TYPE`{: .mpd} | SAL or RF. |
| `R2`{: .vab} | `MODE`{: .mpd} | Opens your crew station's missile mode: `R1`{: .vab} **NORM**, `R2`{: .vab} **MAN** or `R3`{: .vab} **RIPL**. See [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}#modes). |

### SAL missiles

| Button | Label | Action |
|---|---|---|
| `L1`{: .vab} | `PRI`{: .mpd} | Opens the channel list on `L1`{: .vab}–`L5`{: .vab}: choose **CHAN 1**–**CHAN 4** for the primary laser code, or **NONE**. |
| `L2`{: .vab} | `ALT`{: .mpd} | The same for the alternate code. Needs a primary first. |
| `L3`{: .vab} | `SAL SEL`{: .mpd} | Steps through the SAL Hellfire types loaded. The label reads **SAL2** for the K, K2A and N, and **SAL1** for the FA. |
| `R3`{: .vab} | `TRAJ`{: .mpd} | Opens the trajectory choices: `R1`{: .vab} **HI**, `R2`{: .vab} **LO**, `R3`{: .vab} **DIR**. |

The **CHANNELS** row along the bottom shows the four laser codes the channels hold. The missile symbol on the diagram reads the primary code and, below it, **T** when the seeker sees laser energy on that code, or **R** when it does not.

**HFMSN**, **DEICE** and **MSL CCM** are not simulated.

### RF missiles

| Button | Label | Action |
|---|---|---|
| `L1`{: .vab}–`L3`{: .vab} | `ALL` `AUTO` `NONE` | **MSL PWR**: which radar missiles are powered. **AUTO** powers the ones about to be fired. A missile needs some seconds after power-up before it can take a target. |

The selected missile shows **S** while it is aligning, **R** when ready, and **T** when it has a target it can lock before launch.

**LOBL INHIBIT** and **2ND TARGET INHIBIT** are not simulated. See [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}#rf).
