---
title: WCA page
lead: Every active warning, caution and advisory, and what each one means.
keywords: [wca, warning, caution, advisory, master caution, master warning, fault, failure, list]
seats: [PLT, CPG]
redirect_from:
  - /mpd-wca.html
---

{% include fig.html id="mpd-wca" %}

The page lists up to 18 active messages, warnings first. The same messages appear in short form on the [UFD]({{ '/displays/ufd/' | relative_url }}), and the first five warnings and cautions also appear on the ENG page.

- A **warning** (red) needs action now. It lights the **MASTER WARNING** button and sounds a voice warning.
- A **caution** (yellow) needs attention soon. It lights **MASTER CAUTION** and sounds a tone.
- An **advisory** (green) is information.

Press the lit **MASTER WARNING** or **MASTER CAUTION** button on the glareshield to acknowledge it.

## Buttons

| Button | Label | Action |
|---|---|---|
| `T1`{: .vab} | `DTU`{: .mpd} | Opens the [DTU page]({{ '/displays/mpd/dms/' | relative_url }}#dtu). |
| `T3`{: .vab} | `IBIT`{: .mpd} | Opens the [MPD games]({{ '/displays/mpd/games/' | relative_url }}). |
| `T5`{: .vab} | `VERS`{: .mpd} | Opens the [VER page]({{ '/displays/mpd/dms/' | relative_url }}#ver). |
| `T6`{: .vab} | `UTIL`{: .mpd} | Opens UTIL. |
| `B1`{: .vab} | | MENU. |
| `B6`{: .vab} | `WCA`{: .mpd .box} | This page; pressed again, opens ENG. |

**FAULT** and **RESET** are not simulated.

## Warnings

| Page text | UFD | Cause | Do |
|---|---|---|---|
| ENGINE 1 FIRE / ENGINE 2 FIRE / APU FIRE | None: the fire panel button lights | Fire detected. | [Engine fire]({{ '/flying/emergency/' | relative_url }}#fire). |
| ENGINE 1 OUT / ENGINE 2 OUT | ENG1 OUT / ENG2 OUT | The engine has failed, or its Ng is below idle with its power lever at FLY. | [Single engine failure]({{ '/flying/emergency/' | relative_url }}#engine-failure). |
| AFT DECK FIRE | DECK FIRE | Shown only by the fire panel's TEST switch. | |
| ENG1 OVSP / ENG2 OVSP | ENG1 OVSP / ENG2 OVSP | Np at or above 115%. | Reduce power; the engine may trip. |
| LOW ROTOR RPM | LOW RTR | Nr below 95% in the air. | Lower the collective. |
| HIGH ROTOR RPM | HIGH RTR | Nr at or above 106%. | Raise the collective, reduce the descent. |
| HYD FAILURE | HYD FAIL | Both hydraulic pumps failed. | Land as soon as possible. |
| TAIL ROTOR HYD | TAIL RTR | Primary pressure and utility fluid both lost. | Land as soon as possible. |

## Cautions

| Page text | UFD | Cause |
|---|---|---|
| GENERATOR 1 FAIL / GENERATOR 2 FAIL | GEN1 FAIL / GEN2 FAIL | Generator damaged. |
| RECTIFIER 1 FAIL / RECTIFIER 2 FAIL | RECT1 FAIL / RECT2 FAIL | Rectifier damaged. |
| ENGINE 1 CHIPS / ENGINE 2 CHIPS | ENG1 CHIPS / ENG2 CHIPS | Metal in the engine oil. |
| ENG 1 OIL PSI LOW / ENG 2 OIL PSI LOW | ENG1 OIL PSI / ENG2 OIL PSI | Engine oil pressure low. |
| GRBX 1 OIL PSI LOW / GRBX 2 OIL PSI LOW | GRBX1 OIL PSI / GRBX2 OIL PSI | Nose gearbox damaged. |
| GEARBOX 1 CHIPS / GEARBOX 2 CHIPS | GRBX1 CHIPS / GRBX2 CHIPS | Nose gearbox badly damaged. |
| GEARBOX VIBRATION | GRBX VIB | Intermediate or tail gearbox damaged. |
| XMSN 1 OIL PSI LOW / XMSN 2 OIL PSI LOW | XMSN1 OIL PSI / XMSN2 OIL PSI | Main transmission damaged. |
| MAIN XMSN CHIPS | XMSN CHIPS | Main transmission badly damaged. |
| FORWARD FUEL LOW / AFT FUEL LOW | FWD FUEL LO / AFT FUEL LO | Fuel cell low. |
| PRI HYD PSI LOW / UTIL HYD PSI LOW | PRI HYD PSI / UTIL HYD PSI | Hydraulic pressure low. |
| PRI HYD LEVEL LOW / UTIL HYD LEVEL LOW | PRI HYD LVL / UTIL HYD LVL | Hydraulic fluid low: a leak. |
| AUTO/MAN STAB FAIL | STAB FAIL | Stabilator damaged. |
| BUCS FAIL | BUCS FAIL | Primary hydraulic pump failed. |
| FMC DISENGAGED | FMC DISENG | Primary hydraulic pump failed, or an FMC channel is off. |
| APU ON | APU ON | APU running in flight. |
| ROTOR BRAKE ON/LK | RTR BRK ON/LK | Rotor brake set with a power lever off OFF. |
| IRJAM FAIL | IRJAM FAIL | IR jammer on but damaged or without DC power (US equipment). |

## Advisories

| Page text | UFD | Meaning |
|---|---|---|
| APU START / APU POWER ON / APU ON / APU STOP | APU START / APU PWR ON / APU ON / APU STOP | APU starting, on line, running on the ground, shutting down. |
| ENGINE 1 START / ENGINE 2 START | ENG1 START / ENG2 START | Starter turning. |
| BATTERY | BATTERY | Battery damaged. |
| ACCUM OIL PRES LO | ACCUM PSI | Hydraulic accumulator pressure low. |
| CANOPY OPEN | CANOPY | A canopy door is open. |
| ATTITUDE HOLD | ATT HOLD | Attitude hold engaged. |
| RAD ALT HOLD / BAR ALT HOLD | RAD HOLD / BAR HOLD | Altitude hold engaged, radar or barometric. |
| HOVER DRIFT | HOVER DRIFT | About 50 ft from the position hold point. |
| ROTOR BRAKE ON | RTR BRK ON | Rotor brake set, both power levers off. |
| TAIL WHEEL LOCK SEL | TW LOCK SEL | On the ground. |
| EXTERNAL 1–4 EMPTY | EXT1–4 EMPTY | An external tank has run dry. |
| FCR FAULT | FCR FAULT | The radar has failed. |
| WAYPOINT APPROACH / WAYPOINT PASSED | WPT APRCH / WPT PASSED | Nearing or past the next point, with no TSD on display. |
| FUEL CHECK | FUEL CHECK | [Fuel check]({{ '/displays/mpd/fuel/' | relative_url }}#fuel-check) results ready. |
| VERSION MISMATCH | VERS MISM | The mod's files are from different builds. See the [VER page]({{ '/displays/mpd/dms/' | relative_url }}#ver). |
