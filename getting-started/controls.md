---
title: Controls and bindings
lead: Three groups of bindings fly the Apache. Set up the handful in each that you need now; add the rest as you learn the aircraft.
keywords: [keybinds, bindings, hotas, joystick, keyboard, mouse, collective, cyclic, hatchet, interact, cursor, controls]
redirect_from:
  - /setup.html
  - /keybinds.html
---

Bindings live in **Options → Controls**. Use the **Show** drop-down to pick a category. You can change them from the main menu or in a mission (press <kbd>Esc</kbd>) without restarting.

| Category | Covers |
|---|---|
| **Hatchet Interaction Framework** | The cockpit cursor: clicking switches and buttons. |
| **HeliSim Flight Controls** | Cyclic, pedals, collective, trim and hold modes. |
| **AH-64D Official Project** | Sights, weapons, the radar, the TADS, the laser. |
| **AH-64D Cockpit Controls** | One binding per cockpit switch and MPD button, for HOTAS and button boxes. Optional. |
| **AH-64D HeliSim Cockpit Controls** | Battery, APU, engine start switches, rotor brake and power levers as discrete positions, for switch panels. Optional. |
| **AH-64D MPD Minigames** | Inputs for the games on the MPD. Optional. |

## 1. The cockpit cursor

Almost everything in the cockpit is a clickable switch. Clicking goes through the Hatchet Interaction Framework, so these bindings are not optional.

| Binding | Default | What it does |
|---|---|---|
| **Interact** | <kbd>F</kbd> | Operates the control under the cursor. |
| **Mouse Cursor (Hold)** | <kbd>Right Win</kbd> | While held, the mouse moves a cursor instead of your head, and the fire button clicks. |
| **Mouse Cursor (Toggle)** | unbound | As above, toggled. |
| **Previous / Next Setting** | mouse side buttons | Step a multi-position switch or knob back or forward. |

With head tracking, the cursor follows the centre of your view; look at a switch and press **Interact**. Hatchet's own options (cursor shape, colour, labels, a detached cursor for TrackIR users) are in **Addon Options → Hatchet Interaction Framework**.

> Hover over a control to see its label. Set **Show labels** in Hatchet's options to also show the bindings for each control.
{: .tip}

## 2. Flying

HeliSim replaces Arma's helicopter controls with its own. Bind them in **HeliSim Flight Controls**, then pick the matching control scheme in [Addon settings]({{ '/getting-started/settings/' | relative_url }}#helisim).

| Binding | Default | Notes |
|---|---|---|
| Cyclic Forward / Backward / Left / Right | <kbd>W</kbd> <kbd>S</kbd> <kbd>A</kbd> <kbd>D</kbd> | Bind your stick axes here. |
| Pedal Left / Right | <kbd>Q</kbd> <kbd>E</kbd> | Rudder pedals or a twist axis. |
| Collective Up / Down | unbound | **Analogue**: bind your throttle axis to both, one per direction. |
| Keyboard Collective Up / Down | <kbd>Left Shift</kbd> <kbd>Left Ctrl</kbd> | **Keys**: the collective moves while held. |
| Force Trim | unbound | Hold to fly through the holds, release to set new trim references. Bind this on a sprung stick. |
| Force Trim Reset | unbound | Zeroes the trim references and recentres the controls. |
| Attitude Hold / Altitude Hold / Hold Modes Off | unbound | See [Flight control modes]({{ '/flying/flight-control/' | relative_url }}). |
| Beep Trim (4 directions), Altitude Beep Up / Down | unbound | Fine trim and altitude reference adjustment. |
| Sticky Control Interrupt | <kbd>Space</kbd> | Keyboard only: stops sticky cyclic and pedal inputs from accumulating while held. |
| Control Input Visualiser: Toggle | <kbd>Ctrl</kbd>+<kbd>I</kbd> | An overlay showing where your controls are. |

The **FD** (flight director) bindings in the same list do nothing in the Apache; they are for other HeliSim aircraft.

> Bind your HOTAS throttle to **Collective Up/Down**, not to the keyboard collective. Mixing the two leaves the collective where the keys last put it.
{: .caution}

## 3. The Apache's own bindings

These are in **AH-64D Official Project**. The ones worth binding first:

| Binding | Default | |
|---|---|---|
| {% include key.html id="fza_ah64_wasGun" %} | | Action the cannon. |
| {% include key.html id="fza_ah64_wasRkt" %} | | Action the rockets. |
| {% include key.html id="fza_ah64_wasMsl" %} | | Action the missiles. |
| {% include key.html id="fza_ah64_v30_sightSelectHMD" %} | | Helmet sight. |
| {% include key.html id="fza_ah64_v30_sightSelectTADS" %} | | TADS sight (CPG). |
| {% include key.html id="fza_ah64_v30_sightSelectFCR" %} | | Radar sight. |
| {% include key.html id="fza_ah64_laserDesig" %} | | Laser while held. |
| {% include key.html id="fza_ah64_sightSlave" %} | | Slave the sight to the acquisition source. |
| {% include key.html id="fza_ah64_flare" %} | | One flare. |
| {% include key.html id="fza_ah64_symbologySelectUp" %} | | Transition/cruise symbology. |
| {% include key.html id="fza_ah64_symbologySelectDown" %} | | Hover/bob-up symbology. |

The full list, with defaults, is in the [keybind reference]({{ '/reference/keybinds/' | relative_url }}).

### Game controls the Apache takes over

Some of Arma's standard bindings do different things in the Apache:

| Arma binding | In the Apache |
|---|---|
| **Fire** | Fires the weapon actioned in your crew station. |
| **Countermeasures** | Fires chaff. |
| **Toggle active sensors** | Starts or stops continuous radar scan, for the crew station that owns the radar. |
| **Lock target** | Steps the radar's next-to-shoot target. |
| **Zoom in / Zoom out** | CPG: TADS field of view. |
| **Night vision** | CPG: cycles the TADS sensor and FLIR polarity. |
| **Lights** | Search light. |

## HOTAS and switch panels

Every cockpit switch and MPD button has its own binding in **AH-64D Cockpit Controls**, named `system: control` (for example `left mpd: l1`). Bind them to a button box or the buttons on your grip.

For the engine panel, **AH-64D HeliSim Cockpit Controls** has one binding per switch position: **Battery - On**, **Engine 1 Power Lever - Idle**, and so on. These suit physical toggles and detented throttles, because the binding sets a position instead of stepping through them.
