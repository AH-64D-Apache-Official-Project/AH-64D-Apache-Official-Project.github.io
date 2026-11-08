---
title: Addon settings
lead: The options the AH-64D and HeliSim add to the Arma addon options, and their function.
keywords: [settings, cba, addon options, realism, casual, mouse, keyboard, sticky, environment, volume, radial, rearm]
redirect_from:
  - /Settings.html
---

The settings are under **Esc → Options → Addon Options**: the aircraft's under **AH-64D Official Project**, the flight model's under **BradMick's HeliSim**. The tabs select client, mission or server settings. A value forced by the server or mission overrides the client setting.

## AH-64D Official Project

### UI

| Setting | Default | Function |
|---|---|---|
| Show Popup Intro | On | Displays the introduction pop-up on entering an aircraft. |
| Show Vanilla Targeting Information | On | Arma lock boxes and target markers. Requires a game restart. |

### Coms Panel

| Setting | Default | Function |
|---|---|---|
| Master volume Knob | 3 | Volume of the cockpit voice warnings and tones, 0 to 5. |
| RLWR volume Knob | 3 | Volume of the radar and laser warning receiver, 0 to 5. |

### TADS Controls

| Setting | Default | Function |
|---|---|---|
| NV Cycle Include DTV | On | The **Night vision** binding also selects the DTV, in addition to white-hot and black-hot FLIR. |
| NV Cycle Include DVO | On | The **Night vision** binding also selects the DVO. |
| TADS input ignores the detached cursor | Off | With TADS video on the HDU, the aim input slews the TADS and LMC while the Hatchet detached cursor is on. Holding the cursor key stops TADS input. |
| LMC Sensitivity | 0.5 | Gain of the aim input on the [linear motion compensator]({{ '/targeting/tads/' | relative_url }}#lmc). |

### Radial Menu

| Setting | Default | Function |
|---|---|---|
| Stick dwell time | 0.8 s | Time a radial menu direction binding must be held on a sector to select it. |
| Keep open after selecting | Off | The [radial menu]({{ '/targeting/radial/' | relative_url }}) remains open after a selection. |

### Animations

| Setting | Default | Function |
|---|---|---|
| Control Input Animations | On | Animates the cockpit cyclic and collective with control inputs. |
| Air Data Probe Animations | On | Animates the air data probe vanes with the airflow, including rotor wash. Server setting. |
| Rotor Swashplate Animations | On | Animates the swashplate, blade pitch and tail rotor. Server setting. |

### Mission Planner

Server settings, set by the mission maker or server administrator.

| Setting | Default | Function |
|---|---|---|
| Rearm Mode | 30 Seconds | Time to apply a loadout from the [mission planner]({{ '/mission/planner/' | relative_url }}): **Instant**, a fixed **30 Seconds**, or **ACE Settings** (ACE rearm times). |
| No Ammo Source Required | On | Pylons and gun ammunition can be changed without an ammunition source nearby. |
| No Fuel Source Required | On | Fuel can be changed without a fuel source nearby. |

## BradMick's HeliSim {#helisim}

These settings determine how the flight model responds to control inputs.

### Control scheme

| Controls | Settings |
|---|---|
| Joystick, throttle and pedals | **Realistic**; **Keyboard Auto Pedal** off (it is on by default and operates in Realistic as well). Other keyboard and mouse options off. |
| Springless or force-feedback joystick | As above, plus **Springless Cyclic** (and **Springless Pedals** for springless pedals). |
| Keyboard | **Casual**. **Keyboard Auto Pedal** and **Keyboard Auto Pitch** are on by default; **Keyboard Auto Roll** assists roll control. |
| Mouse | **Casual**, **Mouse as Joystick**, and **Mouse Sensitivity** as required. |

### Options

| Setting | Default | Function |
|---|---|---|
| Aircraft Realism Settings | Casual | **Casual** adds keyboard assists; **Realistic** is the unassisted flight model. |
| Cyclic Center Trim Mode | Off | After a force trim release, the cyclic has no effect until returned to centre. Prevents a control jump when the stick is not at the trim position. |
| Pedal Center Trim Mode | Off | As above, for the pedals. |
| Springless Cyclic | Off | Disables cyclic force trim, for sticks without a centring spring. |
| Springless Pedals | Off | Disables pedal force trim; also disables heading hold. |
| Keyboard Sticky Pitch / Roll / Yaw | Off | Keyboard input accumulates while the key is held instead of returning to centre. Not used with a stick or gamepad. |
| Keyboard Auto Pedal | On | Operates the pedals automatically, in either realism setting, in place of heading hold. Not compatible with Sticky Yaw. |
| Keyboard Auto Pitch | On | Casual only. Holds the level-flight pitch attitude. |
| Keyboard Auto Roll | Off | Casual only. The roll keys command a bank angle (up to 30°) and return to wings level when released. |
| Mouse as Joystick | Off | The mouse controls the cyclic; freelook no longer moves the controls. Not used with a stick or gamepad. |
| Mouse Sensitivity | 1.0 | Sensitivity for Mouse as Joystick, 0.1 to 1. |
| Aircraft Environmental Settings | Europe - Summer | Base pressure altitude and temperature: Standard Day (sea level, 15 °C), Europe summer/winter (800 ft, 20 °C / 0 °C), Middle East (1,800 ft, 30 °C), Central Asia summer/winter (5,000 ft, 30 °C / −5 °C), Asia (3,100 ft, 25 °C). See [Environment simulation]({{ '/flying/flight-model/' | relative_url }}#environment-simulation). |
| Enable VRS Warning | Off | On-screen warning as the aircraft approaches vortex ring state. See [Vortex ring state]({{ '/flying/flight-model/' | relative_url }}#vortex-ring-state). |
| Rotor Model | Simple | **BET** is a higher-fidelity rotor model under development; Simple is used. |
| Control Input Visualiser: Colour Scheme | Default | Colours for the control input overlay. |

The remaining HeliSim options (**Fixed Test Gross Weight**, **Disable Wind**, the debugging displays and the **Flight Log**) are for flight model testing and are left off for normal operation.
