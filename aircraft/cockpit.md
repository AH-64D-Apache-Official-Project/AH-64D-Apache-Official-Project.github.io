---
title: Cockpit
lead: The operable controls in both crew stations, by panel.
keywords: [cockpit, panel, switches, console, battery, apu, engine start, power lever, rotor brake, nvs mode, flood light, anti-collision, fire panel, ku, ufd, mpd, hdu, emer hyd, arm safe, ground override, master caution]
seats: [PLT, CPG]
redirect_from:
  - /cockpit.html
---

Each control is operated with the cockpit cursor (see [Controls and bindings]({{ '/getting-started/controls/' | relative_url }})). Most controls can also be bound to a key in **AH-64D Official Project: Cockpit Controls** or **AH-64D HeliSim Cockpit Controls**. The name of a control is displayed when the cursor is placed over it.

> The screenshots are from an earlier build. Panel positions are unchanged; some labels differ.
{: .note}

## Left console

![Pilot's left console, numbered](/images/screenshots/leftPanelPLT.png)
![CPG's left console, numbered](/images/screenshots/leftPanelCPG.png)

| # | Control | Crew station | Function |
|---|---|---|---|
| 1 | Floodlight knob | Both | Cockpit floodlighting on or off. See [Lighting]({{ '/aircraft/lighting/' | relative_url }}). |
| 2 | Anti-collision light switch | PLT | Anti-collision strobes ON or OFF. |
| 3 | ENG 1 and ENG 2 start switches | PLT | START (spring-loaded), OFF, IGN ORIDE. Operated with the engine off, starts the engine; operated during a start, aborts the start. See [Start-up]({{ '/flying/startup/' | relative_url }}). |
| 4 | APU button | PLT | On the power lever quadrant. Starts and stops the APU. See [Electrical, APU and hydraulics]({{ '/aircraft/electrical/' | relative_url }}). |
| 5 | MSTR IGN switch | PLT | Battery on or off. |
| 6 | RTR BRK switch | PLT | 3-position switch on the power lever quadrant: OFF, BRK and LOCK. |
| 7 | NVS MODE switch | Both | OFF, NORM (the night vision sensor follows the crewmember's head) or FIXED (the sensor is fixed forward). See [Night vision]({{ '/targeting/nvs/' | relative_url }}). |
| | Power levers | PLT | One per engine, with OFF, IDLE and FLY detents. Selecting a detent moves the lever to it. With both engines at IDLE, advancing either lever to FLY advances both. |
| | TAIL WHEEL button | Both | Locks and unlocks the tail wheel. Light on: unlocked; light off: locked. Not currently simulated; the `TW LOCK SEL`{: .mpd} advisory is displayed on the ground. |
| | EMER HYD button | Both | On the emergency panel beside the power levers. Applies utility hydraulic accumulator pressure to the flight controls on a loss of both hydraulic systems. See [Electrical, APU and hydraulics]({{ '/aircraft/electrical/' | relative_url }}#hydraulic-system). |

## Front panel

![Pilot's front panel, numbered](/images/screenshots/frontPanelPLT.png)
![CPG's front panel, numbered](/images/screenshots/frontPanelCPG.png)

| # | Control | Crew station | Function |
|---|---|---|---|
| 1 | Keyboard unit (KU) | Both | Data entry. See [Keyboard unit]({{ '/displays/ku/' | relative_url }}). |
| 2 | IHADSS brightness | Both | Not used. The HDU symbology is displayed with power applied once the HDU is fitted. |
| 3 | Fire detection and extinguishing panel | Both | FIRE buttons for ENG 1, APU and ENG 2, the PRI and RES FIRE DISCH buttons and the TEST switch. See [Fire protection]({{ '/aircraft/fire/' | relative_url }}). |
| 4 | Multipurpose displays (MPDs) | Both | Two per crew station. See [MPDs]({{ '/displays/mpd/' | relative_url }}). |
| 5 | Up-front display (UFD) | Both | Warnings, cautions, advisories, fuel and time. See [UFD]({{ '/displays/ufd/' | relative_url }}). |
| 6 | Standby instruments | PLT | Magnetic compass, attitude indicator, airspeed indicator and altimeter. |

On the glareshield and the armament panel in each crew station:

| Control | Function |
|---|---|
| MSTR WARN lighted button | Illuminates with any new warning. Pressed to acknowledge and silence the voice message. |
| MSTR CAUT lighted button | Illuminates with any new caution. Pressed to acknowledge and silence the caution tone. |
| A/S (ARM/SAFE) | Arms or safes the weapons for the aircraft. Requires battery power and, on the ground, GND ORIDE. |
| GND ORIDE | Ground override: permits weapons to be armed, actioned and fired, and the radar to transmit, on the ground. |

## Right console

![Pilot's right console, numbered](/images/screenshots/rightPanelPLT.png)
![CPG's right console, numbered](/images/screenshots/rightPanelCPG.png)

| # | Control | Crew station | Function |
|---|---|---|---|
| 1 | <span id="hdu"></span>HDU stowage | Both | Fits the helmet display unit (HDU) to the helmet, or stows it. Requires the IHADSS helmet. See [IHADSS]({{ '/displays/ihadss/' | relative_url }}). |

## Canopy

The canopy door handle on the inside of each canopy opens and closes that crew station's door. From outside, the ACE interactions **Open/Close Pilot Door** and **Open/Close Gunner Door** operate the doors. An open door is indicated by the `CANOPY`{: .mpd} advisory.
