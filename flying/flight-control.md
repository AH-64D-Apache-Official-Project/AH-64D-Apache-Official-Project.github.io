---
title: Flight control modes
lead: The flight management computer stabilises the Apache and can hold its attitude, position, altitude and heading for you. Knowing what it is doing is the key to flying the aircraft smoothly.
keywords: [fmc, sas, hold, attitude hold, altitude hold, heading hold, position hold, force trim, trim, beep, hover hold]
---

The flight management computer (FMC) runs four features. All of them need DC power and pressure to the flight controls (primary hydraulics, or utility down to the accumulator). The `FMC DISENG`{: .mpd} caution shows when the primary hydraulic pump has failed or any of the FMC's pitch, roll, yaw or collective channels is off; see the [UTIL page]({{ '/displays/mpd/util/' | relative_url }}). Without the FMC you fly on the mechanical controls alone.

| Feature | What it does | How you control it |
|---|---|---|
| **Stability augmentation** | Damps the aircraft's natural wobbles in pitch, roll and yaw. | Always on. |
| **Attitude hold** | Holds position, velocity or attitude, depending on your speed. | **Attitude Hold** binding. |
| **Altitude hold** | Holds radar or barometric altitude with the collective. | **Altitude Hold** binding. |
| **Heading hold** | Holds heading, or coordinates turns, with the pedals. | Automatic with force trim. |

**Hold Modes Off** disengages all of them. When a hold drops out you hear a tone.

## Force trim

Trim sets the control position the aircraft returns to with your hands off. On a sprung stick:

1. Hold **Force Trim**. The holds stop working against you, so you can fly freely.
2. Fly the aircraft to the attitude you want.
3. Release **Force Trim**. The current control positions become the new trim, and the holds take the new attitude, position or heading as their reference.
{: .steps}

**Force Trim Reset** zeroes the trim and recentres the controls. **Beep Trim** moves the cyclic trim a little at a time, and moves the reference of an engaged attitude hold with it.

With **Cyclic Center Trim Mode** or **Pedal Center Trim Mode** on (in the HeliSim settings), the control does nothing after a trim release until you bring your stick or pedals back to centre. Turn these on if the aircraft jumps when you release force trim. Spring-less and force-feedback sticks should use **Springless Cyclic** and **Springless Pedals** instead, which turn force trim off for that control.

## Attitude hold

Press **Attitude Hold** to engage it. What it holds depends on your ground speed:

| Ground speed | Sub-mode | Holds |
|---|---|---|
| 5 kt or less | **Position hold** | Your position over the ground. |
| Above 5 kt, accelerating, up to 40 kt | **Velocity hold** | Your speed and direction over the ground. |
| Above 40 kt (and down to 30 kt as you slow) | **Attitude hold** | Your pitch and roll. |

Move the cyclic past a small breakout and that axis lets go while you fly through it; centre the stick and it takes hold again. Use force trim to give it a new reference.

`ATT HOLD`{: .mpd} shows on the UFD while it is engaged. In position hold, drifting about 50 ft from the hold point raises `HOVER DRIFT`{: .mpd}.

## Altitude hold

Press **Altitude Hold** when you are close to level, within 200 ft/min of vertical speed. It will not engage while you are climbing or descending faster.

| Conditions at engagement | Holds | UFD |
|---|---|---|
| Below 1,428 ft above the ground and 40 kt ground speed | Radar altitude | `RAD HOLD`{: .mpd} |
| Otherwise | Barometric altitude | `BAR HOLD`{: .mpd} |

Moving the collective more than a small amount from where it was disengages altitude hold. **Altitude Beep Up/Down** raises or lowers the held altitude a step per tap, or climbs and descends while held.

## Heading hold

Heading hold uses the pedals. Below 5 kt ground speed it holds your heading. Faster than that it blends into turn coordination, keeping the trim ball centred so you can turn with the cyclic alone. Pressing the pedals flies through it; releasing force trim takes the new heading.

**Springless Pedals** turns heading hold off along with pedal force trim, and **Keyboard Auto Pedal** replaces it.

## Keyboard assists

The keyboard options in the HeliSim settings add their own help on top of the FMC. Auto pedal flies the pedals in either realism setting; in **Casual** only, auto pitch holds the level-flight attitude and auto roll makes the roll keys command up to 30° of bank and roll level when released. See [Addon settings]({{ '/getting-started/settings/' | relative_url }}#helisim).
