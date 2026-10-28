---
title: ENG page
lead: Engines, rotor and hydraulics at a glance. The page you watch during start-up, and the one that tells you what is wrong, and what to do, when something is.
keywords: [eng, engine, torque, tgt, np, nr, ng, oil, hydraulics, start, limits, timers, emergency, procedure]
seats: [PLT, CPG]
redirect_from:
  - /mpd-eng.html
---

Open it with the **A/C** button, from MENU, or by pressing the boxed tab on any aircraft page.

{% include fig.html id="mpd-eng" %}

## Formats

The lower half of the page changes with what you are doing:

| Format | When | Lower half |
|---|---|---|
| **Ground** | On the ground, with no warning or caution | Engine oil pressure for both engines, and the hydraulic pressures. |
| **Flight** | Airborne, with no warning or caution | Empty. |
| **WCA** | Any warning or caution active | A box listing up to five of them. |
| **Emergency** | A warning with an emergency procedure active | That warning's immediate action steps. See [Emergency format](#emergency-format). |

In every format but Ground, the hydraulic pressures are at the top right.

While a starter is turning, a **START** box shows **ON** beside the engine being started.

{% include fig.html id="mpd-eng-start" %}

## Buttons

| Button | Label | Action |
|---|---|---|
| `T2`{: .vab} | `FLT`{: .mpd} | Opens FLT. |
| `T3`{: .vab} | `FUEL`{: .mpd} | Opens FUEL. |
| `T4`{: .vab} | `PERF`{: .mpd} | Opens PERF. |
| `T6`{: .vab} | `UTIL`{: .mpd} | Opens UTIL. |
| `R6`{: .vab} | `ACQ`{: .mpd} | Opens the [acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list. |
| `B1`{: .vab} | | MENU. |
| `B6`{: .vab} | `WCA`{: .mpd} | Opens the [WCA page]({{ '/displays/mpd/wca/' | relative_url }}). |

**SYS** and **ETF** are not simulated.

## Reading the tapes

Torque and TGT have one tape per engine, with the digital value above it. In the middle, the two Np tapes sit either side of the rotor speed chevron, which should rest at 101% in flight. Ng is digital only, at the right.

The torque and TGT tapes change width and colour with the range they are in:

| Tape | Range |
|---|---|
| Narrow, green | Normal. |
| Wider, yellow | A time-limited range. A timer counts down the time left. |
| Widest, red | Past the maximum. |

The Np tapes and their digits, and the Ng digits, turn yellow and red the same way. Ng is also red when it is below 63% with the engine running.

### Limit markings

The markings across the torque and TGT tapes are the aircraft's actual limits:

- The **red bar** across both tapes is the maximum.
- Each **yellow bar** is where a time-limited range starts. There is one for each engine, with a gap between them.

| | Both engines | One engine |
|---|---|---|
| **Torque** | Yellow at 100%, red at 115%. | Yellow at 110% and 122%, red at 125%. |
| **TGT** | Yellow at 810 and 870 °C, red at 949 °C. | Yellow at 810, 870, 878 and 896 °C, red at 949 °C. |

The markings move when the limits do:

- They switch to the one-engine set when the aircraft counts as single-engine: when one engine's torque falls below about half of the other's.
- With low rotor speed, torque is limited further. Below 90% Nr the red bar is at 70%, and below 50% Nr at 30%, with no time-limited range.

How long each range allows is on the [HeliSim flight model]({{ '/flying/flight-model/' | relative_url }}#limits) page.

### Timers

{% include fig.html id="mpd-eng-limits" %}

A white timer counts down the time left in a time-limited range, in minutes and seconds.

- **Torque, TGT and Ng** have one timer each.
  - With one engine in a timed range, the timer takes the place of that engine's number under its column.
  - With both engines in one, a single timer sits centred between the two columns and shows the shorter time.
- **Np** has a timer for each engine, in place of its number.

When a timer reaches **0:00**, the allowance is used up and the engine or drivetrain starts taking damage. A range with no allowance shows 0:00 as soon as you enter it.

Each range has its own allowance. It starts again from full each time you enter the range, so climbing into the next range and coming back resets it.

## Emergency format

{% include fig.html id="mpd-eng-emergency" %}

When a warning with an emergency procedure is active, the lower half of the page shows that warning's immediate action steps. The title is black on white; the steps are white and numbered, with conditions and continuations indented under the step they belong to.

| Warning | Procedure |
|---|---|
| `ENGINE 1 FIRE`{: .mpd} or `ENGINE 2 FIRE`{: .mpd} | Engine fire in flight, or on the ground. |
| `APU FIRE`{: .mpd} | APU fire in flight, or on the ground. |
| `AFT DECK FIRE`{: .mpd} | Aft deck fire. |
| `ENGINE 1 OUT`{: .mpd} or `ENGINE 2 OUT`{: .mpd} | Single engine failure. Both together: dual engine failure. |
| `LOW ROTOR RPM`{: .mpd} | Low rotor RPM, Np failed low. |
| `ENG1 OVSP`{: .mpd} or `ENG2 OVSP`{: .mpd} | Engine overspeed, Np failed high. |
| `HYD FAILURE`{: .mpd} | Hydraulic failure. |
| `TAIL ROTOR HYD`{: .mpd} | Tail rotor hydraulic failure. |

`HIGH ROTOR RPM`{: .mpd} has no procedure, so it shows in the WCA list instead.

With more than one warning active, the page shows the most urgent: fires first, then engine failures, low rotor RPM, overspeed and hydraulics.

The full procedures, and what to do after the immediate actions, are on the [Emergency procedures]({{ '/flying/emergency/' | relative_url }}) page.
