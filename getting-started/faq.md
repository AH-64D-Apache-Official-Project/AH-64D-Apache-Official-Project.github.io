---
title: FAQ and troubleshooting
lead: Quick answers to the questions that come up most, with links to the full explanation.
keywords: [faq, troubleshooting, help, problems, questions, symbology, monocle, hdu, collective, start, rearm, radar, stinger, pnvs zoom, cursor]
redirect_from:
  - /faq.html
---

## Getting going

<span id="cockpit-switches"></span>**How do I work the cockpit switches?**
Point the cockpit cursor at a switch and press **Interact** (<kbd>F</kbd> by default). The cursor comes from the Hatchet Interaction Framework. See [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}#1-the-cockpit-cursor).

<span id="hotas"></span>**How do I put switches on my HOTAS?**
Every cockpit switch and MPD button has its own binding under **AH-64D Official Project: Cockpit Controls**, and the engine panel's positions are under **AH-64D HeliSim Cockpit Controls**. See the [keybind reference]({{ '/reference/keybinds/' | relative_url }}#cockpit-controls).

<span id="aircraft-startup"></span>**How do I start the aircraft?**
Follow [Start-up]({{ '/flying/startup/' | relative_url }}).

**The mod does not load, or the aircraft is missing.**
Check every required mod is loaded, including **HeliSim Core 1.4** or later and **CBA_A3 3.16** or later. See [Installation]({{ '/getting-started/installation/' | relative_url }}).

**The UFD shows `VERS MISM`{: .mpd}.**
The mod's files do not match each other: verify the files in Steam, or reinstall. See [DMS]({{ '/displays/mpd/dms/' | relative_url }}).

## Flying

<span id="cannot-fly"></span>**The engines are running but the aircraft will not fly.**
Usually the collective. With a throttle, bind it to **Collective Up/Down** in **HeliSim Flight Controls**; on a keyboard, use the **Keyboard Collective** bindings. Then pick the matching control scheme in [Addon settings]({{ '/getting-started/settings/' | relative_url }}#helisim). See [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}#2-flying). Also check the rotor brake is off and both power levers are at FLY.

**The aircraft jumps when I release force trim.**
Turn on **Cyclic Center Trim Mode** and **Pedal Center Trim Mode**, or with a stick that has no springs, **Springless Cyclic** and **Springless Pedals**. See [Flight control modes]({{ '/flying/flight-control/' | relative_url }}#force-trim).

## Helmet

<span id="attach-hdu"></span>**How do I get the monocle down?**
Wear the **IHADSS** helmet, then click **HDU stowage** in the cockpit. See [IHADSS]({{ '/displays/ihadss/' | relative_url }}#monocle).

<span id="power-hdu"></span>**The monocle is down but shows no symbology.**
It needs both AC and DC power: battery on, then the APU or the engines for the generators. The symbology only shows in the first person view. See [Electrical, APU and hydraulics]({{ '/aircraft/electrical/' | relative_url }}).

**The monocle keeps stowing itself.**
It stows each time you get in, if you take the helmet off, and if you turn on Arma's own night vision outside the optics view.

<span id="pnvs-zoom"></span>**How do I zoom the PNVS?**
You can't. The PNVS has a single, unmagnified view for flying. The TADS FLIR used as a night vision sensor does not zoom either. See [Night vision]({{ '/targeting/nvs/' | relative_url }}).

<span id="headtracking-cursor-move"></span>**The cockpit cursor follows my head tracking.**
That is how Hatchet works with head tracking: look at a switch and press **Interact**. For a cursor you move separately, see Hatchet's detached cursor in **Addon Options → Hatchet Interaction Framework**. See [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}#1-the-cockpit-cursor).

## Weapons and sensors

<span id="rearm"></span>**How do I change the loadout or rearm?**
In the editor with the **Pylons** attribute, in the field with ACE or the mission planner, or with Zeus Enhanced. See [Rearm and refuel]({{ '/mission/rearm/' | relative_url }}).

<span id="pilot-weapons"></span>**Why do stores loaded on the pilot move to the CPG?**
The wing stores always belong to the CPG's turret in Arma. The pilot can still action and fire them with the weapon action switch. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}).

**Nothing fires on the ground.**
On the ground the aircraft stays safe until you turn on **GND ORIDE**, and it must be armed. See [Weapon action switch]({{ '/weapons/was/' | relative_url }}).

<span id="radar-salute"></span>**How do I turn on the radar?**
The radar must be fitted. Select it as your sight, then scan with {% include key.html id="fza_ah64_fcrSingleScan" %} for one burst or {% include key.html id="ActiveSensorsToggle" %} to keep scanning. On the ground it needs **GND ORIDE**. See [Fire control radar]({{ '/targeting/fcr/' | relative_url }}).

**The TADS keys do nothing.**
The TADS may be someone's night vision sensor, in which case it is not a sight. With A3 Thermal Improvement loaded, the sensor keys only work on the DTV or DVO. See [TADS]({{ '/targeting/tads/' | relative_url }}).

<span id="stinger"></span>**Can the Apache carry Stingers?**
No. The mod has no air-to-air Stinger.
