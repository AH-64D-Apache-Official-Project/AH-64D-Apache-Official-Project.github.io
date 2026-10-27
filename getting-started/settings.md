---
title: Addon settings
lead: Every option the Apache and HeliSim add to Arma's addon options, and what each one does.
keywords: [settings, cba, addon options, realism, casual, mouse, keyboard, sticky, environment, volume, radial, rearm]
redirect_from:
  - /Settings.html
---

Open **Esc → Options → Addon Options**. The Apache's options are under **AH-64D Official Project**; the flight model's are under **BradMick's HeliSim**. The tabs at the top choose whether you are changing your own client settings, the mission's or the server's. A server or mission can force a value, and then your client setting is ignored.

## AH-64D Official Project

### UI

| Setting | Default | What it does |
|---|---|---|
| Show Popup Intro | On | Shows the welcome pop-up when you get into an Apache. |
| Show Vanilla Targeting Information | On | Arma's own lock boxes and target markers. Turn off for a cleaner view. Needs a game restart. |

### Coms Panel

| Setting | Default | What it does |
|---|---|---|
| Master volume Knob | 3 | Volume of the cockpit's voice warnings and tones, 0 to 5. |
| RLWR volume Knob | 3 | Volume of the radar and laser warning receiver, 0 to 5. |

### TADS Controls

| Setting | Default | What it does |
|---|---|---|
| NV Cycle Include DTV | On | The **Night vision** key also steps through the day TV, not only white-hot and black-hot FLIR. |
| NV Cycle Include DVO | On | The **Night vision** key also steps through the direct view optics. |
| TADS input ignores the detached cursor | Off | With the TADS on your helmet display, slew the TADS and LMC with your aim input even while Hatchet's detached cursor is on. Holding the cursor key still stops TADS input. |
| LMC Sensitivity | 0.5 | How strongly your input drives the [linear motion compensator]({{ '/targeting/tads/' | relative_url }}#lmc). |

### Radial Menu

| Setting | Default | What it does |
|---|---|---|
| Stick dwell time | 0.8 s | How long a radial menu direction binding must be held on a sector to select it. |
| Keep open after selecting | Off | Leaves the [radial menu]({{ '/targeting/radial/' | relative_url }}) open so you can make several selections. |

### Animations

| Setting | Default | What it does |
|---|---|---|
| Control Input Animations | On | Moves the cyclic and collective in the cockpit with your inputs. |
| Air Data Probe Animations | On | Turns the air data probe vanes with the airflow, rotor wash included. Server setting. |
| Rotor Swashplate Animations | On | Animates the swashplate, blade pitch and tail rotor. Server setting. |

### Mission Planner

These are server settings, set by the mission maker or server admin.

| Setting | Default | What it does |
|---|---|---|
| Rearm Mode | 30 Seconds | How long applying a loadout from the [mission planner]({{ '/mission/planner/' | relative_url }}) takes: **Instant**, a fixed **30 Seconds**, or **ACE Settings** (ACE's rearm timers). |
| No Ammo Source Required | On | The planner can change pylons and cannon ammunition without an ammo truck nearby. |
| No Fuel Source Required | On | The planner can change fuel without a fuel source nearby. |

## BradMick's HeliSim {#helisim}

HeliSim is the flight model, so these settings decide how the aircraft responds to your controls.

### Choosing a control scheme

| You fly with | Set |
|---|---|
| Joystick, throttle and pedals | **Realistic**. Leave every keyboard and mouse option off. |
| Joystick with a spring-less or force-feedback stick | As above, plus **Springless Cyclic** (and **Springless Pedals** if they are spring-less too). |
| Keyboard | **Casual**, with **Keyboard Auto Pedal**. Try **Keyboard Auto Pitch** and **Keyboard Auto Roll** if the aircraft is hard to hold level. |
| Mouse | **Casual**, **Mouse as Joystick**, and set **Mouse Sensitivity**. |

### All options

| Setting | Default | What it does |
|---|---|---|
| Aircraft Realism Settings | Casual | **Casual** adds keyboard assists; **Realistic** is the flight model as is. |
| Cyclic Center Trim Mode | Off | After a force trim release, the cyclic does nothing until you bring it back to centre. Stops the aircraft jumping when your stick is not where the trim is. |
| Pedal Center Trim Mode | Off | The same for the pedals. |
| Springless Cyclic | Off | Disables cyclic force trim, for sticks without a centring spring. |
| Springless Pedals | Off | Disables pedal force trim. This also disables heading hold. |
| Keyboard Sticky Pitch / Roll / Yaw | Off | Keyboard input keeps building while the key is held, instead of springing back. Do not use with a stick or gamepad. |
| Keyboard Auto Pedal | Off | The pedals are flown for you. Does not work with Sticky Yaw. |
| Keyboard Auto Pitch | Off | Casual only. Holds the level flight pitch attitude. |
| Keyboard Auto Roll | Off | Casual only. The roll keys command a bank angle (up to 30° in the Apache) and roll level when released. |
| Mouse as Joystick | Off | The mouse flies the cyclic. Freelook stops moving the controls. Do not use with a stick or gamepad. |
| Mouse Sensitivity | 1.0 | Sensitivity for Mouse as Joystick, 0.1 to 1. |
| Aircraft Environmental Settings | Europe - Summer | The base altitude and temperature the engines and rotor see: **Standard Day** (sea level, 15 °C), **Europe** summer/winter (800 ft, 20 °C / 0 °C), **Middle East** (1,800 ft, 30 °C), **Central Asia** summer/winter (5,000 ft, 30 °C / -5 °C), **Asia** (3,100 ft, 25 °C). Hot and high costs power. |
| Enable VRS Warning | Off | Warns you as the aircraft enters vortex ring state. |
| Rotor Model | Simple | **BET** is a higher-fidelity rotor model that is not finished. Leave it on Simple. |
| Control Input Visualiser: Colour Scheme | | Colours for the control overlay. |

The remaining HeliSim options (**Fixed Test Gross Weight**, **Disable Wind**, the debugging displays and the **Flight Log**) are for testing the flight model. Leave them off for normal play.
