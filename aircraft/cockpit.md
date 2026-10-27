---
title: Cockpit tour
lead: Every working control in both crew stations, panel by panel.
keywords: [cockpit, panel, switches, console, battery, apu, engine start, power lever, rotor brake, nvs mode, flood light, anti-collision, fire panel, ku, ufd, mpd, hdu, monocle, emer hyd, arm safe, ground override, master caution]
seats: [PLT, CPG]
redirect_from:
  - /cockpit.html
---

Every control on this page is clicked with the cockpit cursor (see [Controls and bindings]({{ '/getting-started/controls/' | relative_url }})). Most can also be bound to a key in **AH-64D Cockpit Controls** or **AH-64D HeliSim Cockpit Controls**. Hover the cursor over a control to see its name.

> These screenshots are from an earlier build. The panels have not moved, but a few labels on them have changed.
{: .note}

## Left console

![Pilot's left console, numbered](/images/screenshots/leftPanelPLT.png)
![CPG's left console, numbered](/images/screenshots/leftPanelCPG.png)

| # | Control | Seat | What it does |
|---|---|---|---|
| 1 | **Floodlight knob** | Both | Cockpit floodlighting on or off. See [Lighting]({{ '/aircraft/lighting/' | relative_url }}). |
| 2 | **Anti-collision light switch** | PLT | Red anti-collision strobes, **ON** or **OFF**. |
| 3 | **ENG 1** and **ENG 2 start switches** | PLT | **START** (springs back), **OFF**, **IGN ORIDE** (stays). Clicked when the engine is off, it starts it; clicked while it is starting, it aborts the start. See [Start-up]({{ '/flying/startup/' | relative_url }}). |
| 4 | **APU pushbutton** | PLT | Starts and stops the APU. See [Electrical, APU and hydraulics]({{ '/aircraft/electrical/' | relative_url }}). |
| 5 | **MSTR IGN switch** | PLT | Battery on or off. |
| 6 | **Rotor brake switch** | PLT | Steps **OFF → BRK → LOCK → OFF**. |
| 7 | **NVS mode switch** | Both | **OFF**, **NORM** (the night vision sensor follows your head) or **FIXED** (it looks straight ahead). See [Night vision]({{ '/targeting/nvs/' | relative_url }}). |
| | **Power levers** | PLT | One per engine, with **OFF**, **IDLE** and **FLY** detents. Click the detent you want and the lever moves there. With both engines at idle, moving either lever to **FLY** takes both. |
| | **EMER HYD** | Both | On the yellow-and-black emergency panel next to the power levers. Puts the hydraulic accumulator's pressure on the flight controls. See [Electrical, APU and hydraulics]({{ '/aircraft/electrical/' | relative_url }}#emergency-hydraulics). |

## Front panel

![Pilot's front panel, numbered](/images/screenshots/frontPanelPLT.png)
![CPG's front panel, numbered](/images/screenshots/frontPanelCPG.png)

| # | Control | Seat | What it does |
|---|---|---|---|
| 1 | **Keyboard unit (KU)** | Both | Click it to type into the aircraft with your keyboard; click again to stop. See [Keyboard unit]({{ '/displays/ku/' | relative_url }}). |
| 2 | **IHADSS brightness** | Both | Not used. The helmet display comes on with power once the HDU is fitted. |
| 3 | **Fire detection and extinguishing panel** | Both | Fire warning lights, the **ENG 1**, **APU** and **ENG 2** fire handles, the **PRI** and **RES** extinguisher bottles and the **TEST** switch. See [Fire protection]({{ '/aircraft/fire/' | relative_url }}). |
| 4 | **Multipurpose displays** | Both | Two per seat. See [Using the MPDs]({{ '/displays/mpd/' | relative_url }}). |
| 5 | **Up-front display (UFD)** | Both | Warnings, cautions, advisories, fuel and the clock. See [UFD]({{ '/displays/ufd/' | relative_url }}). |
| 6 | **Standby instruments** | PLT | Magnetic compass, attitude indicator, airspeed and altimeter. |

On the glareshield and the armament panel in each seat:

| Control | What it does |
|---|---|
| **MASTER WARNING** | Lights with any new warning. Press to acknowledge and silence the voice message. |
| **MASTER CAUTION** | Lights with any new caution. Press to acknowledge and silence the tone. |
| **A/S** (ARM/SAFE) | Arms or safes the weapons for the whole aircraft. Needs battery power, and on the ground also **GND ORIDE**. |
| **GND ORIDE** | Ground override: lets weapons be armed, actioned and fired, and the radar transmit, while on the ground. |

## Right console

![Pilot's right console, numbered](/images/screenshots/rightPanelPLT.png)
![CPG's right console, numbered](/images/screenshots/rightPanelCPG.png)

| # | Control | Seat | What it does |
|---|---|---|---|
| 1 | <span id="hdu"></span>**HDU stowage** | Both | Click to fit the helmet display unit to your helmet, or to stow it. You must be wearing the **IHADSS** helmet. See [IHADSS]({{ '/displays/ihadss/' | relative_url }}). |

## Canopy

Click the door handle on the inside of the canopy to open or close your door. From outside, use the ACE interactions **Open/Close Pilot Door** and **Open/Close Gunner Door**. An open door shows the `CANOPY`{: .mpd} advisory.
