---
title: ASE page
lead: Aircraft survivability equipment — the threat indications on the ASE footprint, and the controls for the warning receivers, chaff, and the IR jammer or missile warning system.
keywords: [ase, rlwr, rwr, lwr, radar warning, laser warning, chaff, flares, ir jammer, mws, autopage, threats]
seats: [PLT, CPG]
redirect_from:
  - /mpd-ase.html
---

The ASE page is selected from the TSD (`T2`{: .vab} ASE), the WPN page or the MENU page. Detection and countermeasures are described in [Survivability (ASE)]({{ '/weapons/ase/' | relative_url }}).

{% include fig.html id="mpd-ase" %}

## Threat indications

The ownship icon is in the centre of the ASE footprint, the circular area in the centre of the page, nose up. Each RLWR threat indication is displayed on the ASE footprint at its bearing relative to the ownship, with a symbol that identifies the threat and indicates its mode:

| Mode | Meaning |
|---|---|
| Search mode | The radar is searching. |
| Acquisition mode | The radar has acquired the aircraft. |
| Tracking mode | The radar is tracking the aircraft and can fire. |
| Launch mode | A radar-guided missile has been launched. The symbol flashes. |
| Laser | The aircraft is being ranged or designated by a laser. |
| Missile | British equipment only: the missile warning system has detected an approaching missile or rocket. The symbol flashes. |

From tracking mode upward, including laser and missile, a dashed yellow line is displayed between the ownship icon and the threat symbol. The number beside RLWR is the number of RLWR threats displayed.

## Buttons

| Button | Label | Function |
|---|---|---|
| `T1`{: .vab} | `CHAFF`{: .mpd} (US) / `CMS`{: .mpd} (British) | Modes the chaff dispense system between SAFE and ARM; ARM is required to dispense chaff |
| `T2`{: .vab} | | TSD page |
| `L3`{: .vab}–`L6`{: .vab} | `SRH` `ACQ` `TRK` `OFF` | AUTOPAGE threshold: when a new RLWR threat is detected in the selected mode, or a threat transitions to a higher mode, the right MPD changes to this page, unless an MPD in the crew station already displays it. A laser designating the aircraft is treated as above track. |
| `R1`{: .vab} | `IRJAM`{: .mpd} (US) / `MWS`{: .mpd} (British) | IR jammer or missile warning system on or off. The IR jammer displays WARM for two seconds, then OPER. |
| `R6`{: .vab} | `RLWR`{: .mpd} | RLWR on or off; a tone sounds when it is powered on |
| `B1`{: .vab} | | MENU page |

The CHAFF status window below the ownship icon displays the chaff cartridges remaining and, with British equipment, the flares (CH/FL).

CHAFF MODE, CAQ, UTIL and 360 are not simulated.

> The RLWR, chaff and the IR jammer or MWS are off or SAFE at power-up and are selected on after start-up. Without DC power the RLWR turns off and chaff reverts to SAFE.
{: .note}
