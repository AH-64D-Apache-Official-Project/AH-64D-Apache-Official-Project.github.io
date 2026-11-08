---
title: Warnings, cautions and advisories (WCA) page
lead: The WCA page lists every active warning, caution and advisory. The complete list of messages, with the UFD and MPD text and the corrective action for each.
keywords: [wca, warning, caution, advisory, master caution, master warning, mstr caut, mstr warn, fault, failure, list, corrective action]
seats: [PLT, CPG]
redirect_from:
  - /mpd-wca.html
---

{% include fig.html id="mpd-wca" %}

The WCA page lists up to 18 active messages, warnings first. The same messages are displayed on the [UFD]({{ '/displays/ufd/' | relative_url }}), and the first five warnings and cautions are also displayed on the ENG page.

- A **warning** (red) indicates a hazardous condition requiring immediate corrective action. It illuminates the MSTR WARN lighted button and plays a voice message.
- A **caution** (yellow) indicates an impending dangerous condition requiring attention but not necessarily immediate action. It illuminates the MSTR CAUT lighted button and plays a caution tone.
- An **advisory** (green) indicates a safe or normal configuration, condition or performance, or imparts information for routine action.

The crewmember presses the illuminated MSTR WARN or MSTR CAUT lighted button on the glareshield to acknowledge it.

## Buttons

| Button | Label | Function |
|---|---|---|
| `T1`{: .vab} | `DTU`{: .mpd} | [DTU page]({{ '/displays/mpd/dms/' | relative_url }}#dtu) |
| `T3`{: .vab} | `IBIT`{: .mpd} | [MPD games]({{ '/displays/mpd/games/' | relative_url }}) |
| `T5`{: .vab} | `VERS`{: .mpd} | [VERS page]({{ '/displays/mpd/dms/' | relative_url }}#ver) |
| `T6`{: .vab} | `UTIL`{: .mpd} | UTIL page |
| `B1`{: .vab} | | MENU page |
| `B6`{: .vab} | `WCA`{: .mpd .box} | This page; pressed again, the ENG page |

FAULT and RESET are not simulated.

## Message list

The following table provides a list of Warnings, Cautions and Advisories:

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| — | ENGINE 1 FIRE | 1. EMER ENG SHUTDOWN (affected engine) – When conditions permit<br>2. Illuminated ENG FIRE button – Press and RDY light illuminates<br>3. FIRE DISCH button(s) – Press<br>4. LAND AS SOON AS POSSIBLE |
| — | ENGINE 2 FIRE | As ENGINE 1 FIRE |
| — | APU FIRE | 1. Illuminated APU FIRE button – Press and RDY light illuminates<br>2. FIRE DISCH button(s) – Press<br>3. LAND AS SOON AS POSSIBLE |
| DECK FIRE | AFT DECK FIRE | Displayed by the fire test only |
| ENG1 OUT | ENGINE 1 OUT | LAND AS SOON AS PRACTICABLE |
| ENG2 OUT | ENGINE 2 OUT | LAND AS SOON AS PRACTICABLE |
| ENG1 OVSP | ENG1 OVSP | |
| ENG2 OVSP | ENG2 OVSP | |
| LOW RTR | LOW ROTOR RPM | Collective – Lower to restore Nr |
| HIGH RTR | HIGH ROTOR RPM | |
| HYD FAIL | HYD FAILURE | 1. EMER HYD button – Press ON<br>2. LAND WITHOUT DELAY |
| TAIL RTR | TAIL ROTOR HYD | LAND AS SOON AS POSSIBLE |
| **UFD CAUTION** | **MPD CAUTION** | **CORRECTIVE ACTION** |
| GEN1 FAIL | GENERATOR 1 FAIL | LAND AS SOON AS PRACTICABLE |
| GEN2 FAIL | GENERATOR 2 FAIL | LAND AS SOON AS PRACTICABLE |
| Both GEN1 FAIL and GEN2 FAIL | | LAND AS SOON AS POSSIBLE |
| RECT1 FAIL | RECTIFIER 1 FAIL | LAND AS SOON AS PRACTICABLE |
| RECT2 FAIL | RECTIFIER 2 FAIL | LAND AS SOON AS PRACTICABLE |
| Both RECT1 FAIL and RECT2 FAIL | | LAND AS SOON AS POSSIBLE |
| ENG1 CHIPS | ENGINE 1 CHIPS | |
| ENG2 CHIPS | ENGINE 2 CHIPS | |
| ENG1 OIL PSI | ENG 1 OIL PSI LOW | |
| ENG2 OIL PSI | ENG 2 OIL PSI LOW | |
| GRBX1 OIL PSI | GRBX 1 OIL PSI LOW | |
| GRBX2 OIL PSI | GRBX 2 OIL PSI LOW | |
| GRBX1 CHIPS | GEARBOX 1 CHIPS | LAND AS SOON AS PRACTICABLE |
| GRBX2 CHIPS | GEARBOX 2 CHIPS | LAND AS SOON AS PRACTICABLE |
| GRBX VIB | GEARBOX VIBRATION | LAND AS SOON AS POSSIBLE |
| XMSN1 OIL PSI | XMSN 1 OIL PSI LOW | |
| XMSN2 OIL PSI | XMSN 2 OIL PSI LOW | |
| XMSN CHIPS | MAIN XMSN CHIPS | LAND AS SOON AS POSSIBLE |
| FWD FUEL LO | FORWARD FUEL LOW | LAND AS SOON AS PRACTICABLE |
| AFT FUEL LO | AFT FUEL LOW | LAND AS SOON AS PRACTICABLE |
| PRI HYD PSI | PRI HYD PSI LOW | LAND AS SOON AS POSSIBLE |
| UTIL HYD PSI | UTIL HYD PSI LOW | LAND AS SOON AS POSSIBLE |
| Both PRI HYD PSI and UTIL HYD PSI | | See HYD FAIL |
| PRI HYD LVL | PRI HYD LEVEL LOW | LAND AS SOON AS PRACTICABLE |
| UTIL HYD LVL | UTIL HYD LEVEL LOW | LAND AS SOON AS PRACTICABLE |
| Both PRI HYD LVL and UTIL HYD LVL | | Be prepared for HYD FAIL |
| BUCS FAIL | BUCS FAIL | LAND AS SOON AS POSSIBLE |
| FMC DISENG | FMC DISENGAGED | |
| STAB FAIL | AUTO/MAN STAB FAIL | |
| APU ON | APU ON | Turn off APU |
| RTR BRK ON/LK | ROTOR BRAKE ON/LK | |
| IRJAM FAIL | IRJAM FAIL | |
| **UFD ADVISORY** | **DMS ADVISORY** | **CORRECTIVE ACTION** |
| APU START | APU START | |
| APU PWR ON | APU POWER ON | |
| APU ON | APU ON | |
| APU STOP | APU STOP | |
| APU FAIL | APU FAIL | Repair the APU |
| ENG1 START | ENGINE 1 START | |
| ENG2 START | ENGINE 2 START | |
| BATTERY | BATTERY | Repair the battery |
| ACCUM PSI | ACCUM OIL PRES LO | Information System Status |
| CANOPY | CANOPY OPEN | |
| ATT HOLD | ATTITUDE HOLD | |
| RAD HOLD / BAR HOLD | RAD ALT HOLD / BAR ALT HOLD | |
| HOVER DRIFT | HOVER DRIFT | |
| RTR BRK ON | ROTOR BRAKE ON | |
| TW LOCK SEL | TAIL WHEEL LOCK SEL | |
| EXT1 EMPTY – EXT4 EMPTY | EXTERNAL 1–4 EMPTY | |
| FCR FAULT | FCR FAULT | |
| WPT APRCH / WPT PASSED | WAYPOINT APPROACH / WAYPOINT PASSED | |
| FUEL CHECK | FUEL CHECK | |
| VERS MISM | VERSION MISMATCH | |

The conditions that raise each message are described on the corresponding system page; see [Emergency procedures]({{ '/flying/emergency/' | relative_url }}).
