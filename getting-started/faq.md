---
title: FAQ and troubleshooting
lead: Common questions, with references to the full description.
keywords: [faq, troubleshooting, help, problems, questions, symbology, hdu, collective, start, rearm, radar, stinger, pnvs zoom, cursor]
redirect_from:
  - /faq.html
---

## Setup

<span id="cockpit-switches"></span>**Operating the cockpit switches.**
The cockpit cursor is placed on a switch and **Interact** (<kbd>F</kbd> by default) pressed. The cursor is provided by the Hatchet Interaction Framework. See [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}#cockpit-cursor).

<span id="hotas"></span>**Binding switches to a HOTAS.**
Every cockpit switch and MPD button has a binding under **AH-64D Official Project: Cockpit Controls**; the engine panel positions are under **AH-64D HeliSim Cockpit Controls**. See the [keybind reference]({{ '/reference/keybinds/' | relative_url }}#cockpit-controls).

<span id="aircraft-startup"></span>**Starting the aircraft.**
See [Start-up]({{ '/flying/startup/' | relative_url }}).

**The mod does not load, or the aircraft is not listed.**
A required mod is not loaded. HeliSim Core 1.5.0 or later and CBA_A3 3.16 or later are required. See [Installation]({{ '/getting-started/installation/' | relative_url }}).

**The UFD displays `VERS MISM`{: .mpd}.**
The mod's files are from different builds. The files are verified in Steam, or the release is reinstalled. See [DMS]({{ '/displays/mpd/dms/' | relative_url }}#ver).

## Flight

<span id="cannot-fly"></span>**The engines are running but the aircraft does not lift off.**
The collective is not bound. A throttle is bound to **Collective Up/Down** in **HeliSim Flight Controls**; on a keyboard, the **Keyboard Collective** bindings are used. The matching control scheme is selected in [Addon settings]({{ '/getting-started/settings/' | relative_url }}#helisim). See [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}#flight-controls). The rotor brake must be OFF and both power levers at FLY.

**The aircraft jumps when force trim is released.**
**Cyclic Center Trim Mode** and **Pedal Center Trim Mode** are selected on or, for a springless stick, **Springless Cyclic** and **Springless Pedals**. See [Flight control modes]({{ '/flying/flight-control/' | relative_url }}#force-trim).

## Helmet

<span id="attach-hdu"></span>**Fitting the HDU.**
The IHADSS helmet is worn and **HDU stowage** selected in the cockpit. See [IHADSS]({{ '/displays/ihadss/' | relative_url }}#hdu).

<span id="power-hdu"></span>**The HDU is fitted but displays no symbology.**
The HDU requires AC and DC power: battery on, then the APU or the engines for the generators. Symbology is displayed in the first-person view only. See [Electrical, APU and hydraulics]({{ '/aircraft/electrical/' | relative_url }}).

**The HDU stows.**
The HDU is stowed on each entry to the aircraft, when the helmet is removed, and when Arma night vision is selected outside the optics view.

<span id="pnvs-zoom"></span>**PNVS zoom.**
The PNVS has a single, unmagnified field of view for flight. The TADS FLIR used as a night vision sensor is held in the wide field of view. See [Night vision]({{ '/targeting/nvs/' | relative_url }}).

<span id="headtracking-cursor-move"></span>**The cockpit cursor follows head tracking.**
With head tracking, the Hatchet cursor follows the view: a switch is operated by looking at it and pressing **Interact**. A separately moved cursor is provided by Hatchet's detached cursor in **Addon Options → Hatchet Interaction Framework**. See [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}#cockpit-cursor).

## Weapons and sensors

<span id="rearm"></span>**Changing the loadout or rearming.**
In the editor with the **Pylons** attribute, in the field with ACE or the mission planner, or with Zeus Enhanced. See [Rearm and refuel]({{ '/mission/rearm/' | relative_url }}).

<span id="pilot-weapons"></span>**Stores loaded on the pilot move to the CPG.**
In Arma, wing stores belong to the CPG's turret. The pilot actions and fires them with the weapon action switch. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}).

**No weapon fires on the ground.**
On the ground the aircraft is held safe until GND ORIDE is selected, and it must be armed. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}).

<span id="radar-salute"></span>**Operating the radar.**
The radar must be installed. FCR is selected as the sight, then {% include key.html id="fza_ah64_fcrSingleScan" %} for a single scan or {% include key.html id="ActiveSensorsToggle" %} for continuous scan. On the ground, GND ORIDE is required. See [Fire control radar]({{ '/targeting/fcr/' | relative_url }}).

**The TADS bindings have no effect.**
The TADS may be a crewmember's night vision sensor, in which case it is not available as a sight. With A3 Thermal Improvement loaded, the sensor bindings operate only with the DTV or DVO. See [TADS]({{ '/targeting/tads/' | relative_url }}).

<span id="stinger"></span>**Stinger.**
The mod does not include an air-to-air Stinger.
