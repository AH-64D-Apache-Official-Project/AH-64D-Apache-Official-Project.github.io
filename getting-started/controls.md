---
title: Controls and bindings
lead: The binding categories used by the AH-64D, the cockpit cursor, the HeliSim flight controls, and the aircraft's own bindings.
keywords: [keybinds, bindings, hotas, joystick, keyboard, mouse, collective, cyclic, hatchet, interact, cursor, controls]
redirect_from:
  - /setup.html
  - /keybinds.html
---

Bindings are set in **Options → Controls**, with the **Show** list selecting the category. They can be changed from the main menu or in a mission (<kbd>Esc</kbd>) without a restart.

| Category | Contents |
|---|---|
| Hatchet Interaction Framework | The cockpit cursor, for operating switches and buttons |
| HeliSim Flight Controls | Cyclic, pedals, collective, trim and hold modes |
| AH-64D Official Project | Sights, weapons, radar, TADS and laser |
| AH-64D Official Project: Cockpit Controls | One binding per cockpit switch and MPD button, for HOTAS and button boxes (optional) |
| AH-64D HeliSim Cockpit Controls | Battery, APU, engine start switches, rotor brake and power levers as discrete positions, for switch panels (optional) |
| AH-64D MPD Minigames | Inputs for the MPD games (optional) |

## Cockpit cursor

Cockpit controls are operated through the Hatchet Interaction Framework; these bindings are required.

| Binding | Default | Function |
|---|---|---|
| Interact | <kbd>F</kbd> | Operates the control under the cursor |
| Mouse Cursor (Hold) | <kbd>Right Win</kbd> | While held, the mouse moves a cursor instead of the view, and the fire button operates controls |
| Mouse Cursor (Toggle) | unbound | As above, toggled |
| Previous / Next Setting | mouse side buttons | Steps a multi-position switch or knob back or forward |

With head tracking, the cursor follows the center of the view; a control is operated by looking at it and pressing **Interact**. Hatchet's options (cursor shape, color, labels, and a detached cursor for TrackIR users) are in **Addon Options → Hatchet Interaction Framework**.

> The control label is displayed with the cursor over a control. **Show labels** in the Hatchet options also displays the binding for each control.
{: .note}

## Flight controls

HeliSim replaces the Arma helicopter controls. The bindings are in **HeliSim Flight Controls**; the matching control scheme is selected in [Addon settings]({{ '/getting-started/settings/' | relative_url }}#helisim).

| Binding | Default | Notes |
|---|---|---|
| Cyclic Forward / Backward / Left / Right | <kbd>W</kbd> <kbd>S</kbd> <kbd>A</kbd> <kbd>D</kbd> | Stick axes |
| Pedal Left / Right | <kbd>Q</kbd> <kbd>E</kbd> | Rudder pedals or a twist axis |
| Collective Up / Down | unbound | Analog: the throttle axis, one direction per binding |
| Keyboard Collective Up / Down | <kbd>Left Shift</kbd> <kbd>Left Ctrl</kbd> | Keys: the collective moves while held |
| Force Trim | unbound | Held to fly through the holds; released to set new trim references. Bound on a spring-centered stick |
| Force Trim Reset | unbound | Zeroes the trim references and recenters the controls |
| Attitude Hold / Altitude Hold / Hold Modes Off | unbound | See [Flight control modes]({{ '/flying/flight-control/' | relative_url }}) |
| Sticky Control Interrupt | <kbd>Space</kbd> | Keyboard only: stops sticky cyclic and pedal inputs accumulating while held |
| Control Input Visualizer: Toggle | <kbd>Ctrl</kbd>+<kbd>I</kbd> | Overlay showing control positions |

The FD (flight director) bindings have no function in the AH-64D.

> A HOTAS throttle is bound to **Collective Up/Down**, not to the keyboard collective. Using both leaves the collective where the keys last set it.
{: .caution}

## AH-64D bindings

The following bindings in **AH-64D Official Project** are the primary weapon and sensor controls:

| Binding | Function |
|---|---|
| {% include key.html id="fza_ah64_wasGun" %} | WAS – gun |
| {% include key.html id="fza_ah64_wasRkt" %} | WAS – rockets |
| {% include key.html id="fza_ah64_wasMsl" %} | WAS – missiles |
| {% include key.html id="fza_ah64_v30_sightSelectHMD" %} | Sight select – HMD |
| {% include key.html id="fza_ah64_v30_sightSelectTADS" %} | Sight select – TADS (CPG) |
| {% include key.html id="fza_ah64_v30_sightSelectFCR" %} | Sight select – FCR |
| {% include key.html id="fza_ah64_laserDesig" %} | Laser, while held |
| {% include key.html id="fza_ah64_sightSlave" %} | Slave the sight to the acquisition source |
| {% include key.html id="fza_ah64_flare" %} | One flare |
| {% include key.html id="fza_ah64_symbologySelectUp" %} | Symbology select – transition/cruise |
| {% include key.html id="fza_ah64_symbologySelectDown" %} | Symbology select – hover/bob-up |
| {% include key.html id="fza_ah64_mpdCursorUp" %}, Down, Left, Right | [MPD cursor]({{ '/displays/mpd/' | relative_url }}#cursor) |
| {% include key.html id="fza_ah64_mpdCursorEnter" %} | MPD cursor enter |
| {% include key.html id="fza_ah64_iatEngage" %} | CPG: TADS [image auto track]({{ '/targeting/tads/' | relative_url }}#iat) |

The complete list, with defaults, is in the [keybind reference]({{ '/reference/keybinds/' | relative_url }}).

### Arma bindings with AH-64D functions

| Arma binding | AH-64D function |
|---|---|
| Fire | Fires the weapon actioned in the crew station |
| Countermeasures | Releases chaff |
| Toggle active sensors | Starts or stops continuous radar scan, for the crew station that owns the radar |
| Lock target | Steps the radar next-to-shoot target |
| Zoom in / Zoom out | CPG: TADS field of view |
| Night vision | CPG: cycles the TADS sensor and FLIR polarity |
| Lights | Searchlight |

## HOTAS and switch panels

Every cockpit switch and MPD button has a binding in **AH-64D Official Project: Cockpit Controls**, named `system: control` (for example `left mpd: left mpd l1`).

**AH-64D HeliSim Cockpit Controls** has one binding per switch position (**Battery - On**, **Engine 1 Power Lever - Idle**, and so on), for physical toggles and detented throttles: each binding sets a position rather than stepping through positions.
