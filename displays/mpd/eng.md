---
title: Engine (ENG) page
lead: Engine, rotor and hydraulic indications, the ground, in-flight and emergency formats, limit markings and count-down timers.
keywords: [eng, engine, torque, tgt, np, nr, ng, oil, hydraulics, start, limits, timers, emergency, procedure]
seats: [PLT, CPG]
redirect_from:
  - /mpd-eng.html
---

The ENG page is selected with the A/C fixed action button, from the MENU page, or with the boxed page button on any aircraft page.

{% include fig.html id="mpd-eng" %}

## Formats

The ENG page has ground, in-flight and emergency formats. The upper half of the page is the same in each; the lower half changes with the aircraft's state:

| Format | Condition | Lower half |
|---|---|---|
| Ground | On the ground, no warning or caution | Engine oil pressure (ENGINE OIL PSI) and hydraulic pressure (HYD PSI) status windows |
| In-flight | Airborne, no warning or caution | Blank |
| In-flight, active warnings and cautions | Any warning or caution active | Up to five active warnings (red) and cautions (yellow) |
| Emergency | A warning with a procedure active | The immediate action steps for that warning; see [Emergency format](#emergency-format) |

In all formats except Ground, the HYD PSI status window is displayed in the upper right area of the page. While a starter is engaged, the start status (START) window and the starter mode ON label are displayed beside the engine being started.

{% include fig.html id="mpd-eng-start" %}

## Buttons

| Button | Label | Function |
|---|---|---|
| `T2`{: .vab} | `FLT`{: .mpd} | FLT page |
| `T3`{: .vab} | `FUEL`{: .mpd} | FUEL page |
| `T4`{: .vab} | `PERF`{: .mpd} | PERF page |
| `T6`{: .vab} | `UTIL`{: .mpd} | UTIL page |
| `R6`{: .vab} | `ACQ`{: .mpd} | [Acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list |
| `B1`{: .vab} | | MENU page |
| `B6`{: .vab} | `WCA`{: .mpd} | [WCA page]({{ '/displays/mpd/wca/' | relative_url }}) |

SYS and ETF are not simulated.

## Indications

Engine torque and turbine gas temperature (TGT) are displayed as a vertical tape for each engine, with a digital readout above. In the centre, the two power turbine speed (Np) tapes are displayed either side of the main rotor speed (Nr) tape, a chevron, which rests at 101% in flight. Gas generator speed (Ng) is displayed as a digital readout on the right. Hydraulic pressure for the primary (PRI), utility (UTIL) and accumulator (ACC) systems is displayed as digital readouts in the HYD PSI status window.

The torque, TGT, Np and Ng indications are colour coded: **green** in the normal range, **yellow** in a time-limited range, **red** beyond a maximum or below a minimum. The torque and TGT tapes widen as they rise: torque above 100% and above 115%, TGT above 810 °C. Ng is also displayed red below 63% with the engine running. The limits are listed in [Engines, drive train and rotor]({{ '/aircraft/engines/' | relative_url }}#indications-and-limits).

### Limit markings

A red bar across both torque tapes, and another across both TGT tapes, marks the maximum:

| | Dual engine (DE) | Single engine (SE) |
|---|---|---|
| Torque | 115% | 125% |
| TGT | 949 °C | 949 °C |

The markings change with the operating condition:

- They change to the single engine maximum when the aircraft is operating single engine, that is, when one engine's torque falls below approximately half of the other's.
- At low rotor speed, torque is further limited: below 90% Nr the red bar is at 70%, and below 50% Nr at 30%, with no time-limited range.

### Count-down timers

{% include fig.html id="mpd-eng-limits" %}

A white count-down timer displays the time remaining in a time-limited range, in minutes and seconds.

- Torque, TGT and Ng each have one timer. With one engine in a time-limited range, the timer replaces that engine's digital readout; with both engines in one, a single timer is centred between the columns and displays the shorter time.
- Np has a timer for each engine, in place of its digital readout.

When a timer reaches 0:00, the allowance is exhausted and the engine or drive train begins to incur damage. A range with no allowance displays 0:00 on entry. Each range has its own allowance, which resets to full each time the range is entered.

## Emergency format {#emergency-format}

{% include fig.html id="mpd-eng-emergency" %}

When a warning with a procedure is active, the lower half of the page displays that warning's immediate action steps. The title is displayed black on white; the steps are white and numbered.

| Warning | Procedure displayed |
|---|---|
| ENGINE 1 FIRE / ENGINE 2 FIRE | Engine fire, in flight or on the ground |
| APU FIRE | APU fire, in flight or on the ground |
| AFT DECK FIRE | Aft deck fire |
| ENGINE 1 OUT / ENGINE 2 OUT | Single engine failure |
| LOW ROTOR RPM | Low rotor RPM |
| ENG1 OVSP / ENG2 OVSP | Engine overspeed |
| HYD FAILURE | Hydraulic failure |
| TAIL ROTOR HYD | Tail rotor hydraulic failure |

HIGH ROTOR RPM and dual engine failure have no displayed procedure and are listed as active warnings in the in-flight format. With more than one warning active, the highest priority is displayed: fires, then engine failures, low rotor RPM, overspeed and hydraulics.

The complete warning, caution and advisory list, with corrective actions, is on [Emergency procedures]({{ '/flying/emergency/' | relative_url }}).
