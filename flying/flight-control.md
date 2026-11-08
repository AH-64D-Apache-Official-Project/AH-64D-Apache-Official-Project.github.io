---
title: Flight control modes
lead: The flight management computer (FMC), stability augmentation, the attitude, altitude and heading hold modes, and force trim.
keywords: [fmc, sas, scas, hold, attitude hold, altitude hold, heading hold, position hold, velocity hold, force trim, trim, hover hold, turn coordination]
---

## Flight management computer

The flight management computer (FMC) provides stability augmentation and the hold modes. It requires DC power and primary hydraulic pressure, since the FMC moves the flight controls only through the primary side of the servos. The `FMC DISENG`{: .mpd} caution is displayed when the primary hydraulic pump has failed or any FMC axis (pitch, roll, yaw or collective) is selected off on the [UTIL page]({{ '/displays/mpd/util/' | relative_url }}). With the FMC disengaged, the helicopter is flown on the mechanical flight controls alone.

| Function | Description | Control |
|---|---|---|
| Stability augmentation | Damps the aircraft's natural oscillations in pitch, roll and yaw. | Always on. |
| Attitude hold | Holds position, velocity or attitude, depending on ground speed. | **Attitude Hold** binding |
| Altitude hold | Holds radar or barometric altitude with the collective. | **Altitude Hold** binding |
| Heading hold | Holds heading, or coordinates turns, with the pedals. | Automatic with force trim |

**Hold Modes Off** disengages all hold modes. A tone sounds when a hold mode disengages.

## Force trim

Force trim sets the control position the aircraft returns to with the controls released.

1. Force trim interrupt – Press and hold.
2. Flight control – Position in the desired position.
3. Force trim interrupt – Release.
4. Flight control – Re-center (Center Trim Mode only).
{: .steps}

On release, the hold modes take the new attitude, position or heading as their reference.

**Force Trim Reset** zeroes the trim and recenters the controls.

With **Cyclic Center Trim Mode** or **Pedal Center Trim Mode** selected in the HeliSim settings, the control has no effect after a trim release until it is returned to center; this prevents a control jump on release. Springless and force-feedback sticks use **Springless Cyclic** and **Springless Pedals**, which disable force trim for that control.

## Attitude hold

Attitude hold is engaged with **Attitude Hold**. The sub-mode depends on ground speed:

| Ground speed | Sub-mode | Holds |
|---|---|---|
| 5 kt or less | Position hold | Position over the ground |
| Above 5 kt, accelerating, up to 40 kt | Velocity hold | Ground speed and track |
| Above 40 kt (down to 30 kt when decelerating) | Attitude hold | Pitch and roll attitude |

A cyclic input beyond a small breakout releases the hold in that axis while the input is held; the hold re-engages when the cyclic is returned to center. Force trim sets a new reference.

`ATT HOLD`{: .mpd} is displayed on the UFD while attitude hold is engaged. In position hold, a drift of approximately 50 ft from the hold point displays the `HOVER DRIFT`{: .mpd} advisory.

## Altitude hold

Altitude hold is engaged with **Altitude Hold** when the rate of climb or descent is within 200 fpm; it does not engage at a greater rate of climb or descent.

| Conditions at engagement | Holds | UFD |
|---|---|---|
| Below 1,428 ft above ground level and below 40 kt ground speed | Radar altitude | `RAD HOLD`{: .mpd} |
| Otherwise | Barometric altitude | `BAR HOLD`{: .mpd} |

A collective input beyond a small breakout disengages altitude hold.

## Heading hold

Heading hold uses the pedals. Below 5 kt ground speed it holds heading; above that it blends into turn coordination, keeping the skid/slip ball centered so that turns are flown with cyclic alone. A pedal input overrides heading hold; a force trim release sets the new heading.

**Springless Pedals** disables heading hold together with pedal force trim, and **Keyboard Auto Pedal** replaces it.

## Keyboard assists

The keyboard options in the HeliSim settings add their own assistance to the FMC. Auto pedal operates the pedals in either realism setting. In **Casual** only, auto pitch holds the level-flight attitude, and auto roll makes the roll keys command up to 30° of bank and returns the aircraft to wings level when released. See [Addon settings]({{ '/getting-started/settings/' | relative_url }}#helisim).
