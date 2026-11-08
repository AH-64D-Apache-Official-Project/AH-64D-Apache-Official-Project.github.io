---
title: Emergency procedures
lead: Warnings, cautions and advisories for every system, with the UFD and MPD indications and the corrective action for each.
keywords: [emergency, fire, engine failure, single engine, dual engine, autorotation, hydraulics, emer hyd, tail rotor, low rotor, high rotor, generator, tru, chips, transmission, gearbox, grbx vib, fuel, jettison]
seats: [PLT, CPG]
---

## General

Warnings are displayed in red, cautions in yellow and advisories in green. Each new warning illuminates the MSTR WARN lighted button and plays a voice message; each new caution illuminates the MSTR CAUT lighted button and plays a caution tone. The crewmember presses the illuminated button to acknowledge it.

For warnings with a procedure, the [ENG page]({{ '/displays/mpd/eng/' | relative_url }}#emergency-format) displays the immediate action steps in its lower half.

The corrective actions use the following landing conditions only: **LAND WITHOUT DELAY**, **LAND AS SOON AS POSSIBLE** and **LAND AS SOON AS PRACTICABLE**.

Each system's description, and the effect of each failure, is given on that system's page: [Engines, drive train and rotor]({{ '/aircraft/engines/' | relative_url }}), [Electrical, APU and hydraulics]({{ '/aircraft/electrical/' | relative_url }}), [Fuel system]({{ '/aircraft/fuel/' | relative_url }}), [Fire protection]({{ '/aircraft/fire/' | relative_url }}).

## Fire {#fire}

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| — | ENGINE 1 FIRE | 1. EMER ENG SHUTDOWN (affected engine) – When conditions permit<br>2. Illuminated ENG FIRE button – Press and RDY light illuminates<br>3. FIRE DISCH button(s) – Press<br>4. LAND AS SOON AS POSSIBLE |
| — | ENGINE 2 FIRE | 1. EMER ENG SHUTDOWN (affected engine) – When conditions permit<br>2. Illuminated ENG FIRE button – Press and RDY light illuminates<br>3. FIRE DISCH button(s) – Press<br>4. LAND AS SOON AS POSSIBLE |
| — | APU FIRE | 1. Illuminated APU FIRE button – Press and RDY light illuminates<br>2. FIRE DISCH button(s) – Press<br>3. LAND AS SOON AS POSSIBLE |

The FIRE button for the affected area **must be armed before** a bottle is discharged; a bottle discharged with the button not armed does not reach the fire. See [Fire protection]({{ '/aircraft/fire/' | relative_url }}).

## Engines {#engine-failure}

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| ENG1 OUT | ENGINE 1 OUT | LAND AS SOON AS PRACTICABLE |
| ENG2 OUT | ENGINE 2 OUT | LAND AS SOON AS PRACTICABLE |
| **UFD ADVISORY** | **DMS ADVISORY** | **CORRECTIVE ACTION** |
| ENG1 START | ENGINE 1 START | |
| ENG2 START | ENGINE 2 START | |

Following a single engine failure, the remaining engine can sustain flight provided the helicopter remains above the velocity safe single engine (VSSE) displayed on the [PERF page]({{ '/displays/mpd/perf/' | relative_url }}). Below VSSE, maximum single engine torque is required to maintain level flight, and exceeding the maximum torque available single engine results in rotor droop. Single engine torque limits are given in [Engines, drive train and rotor]({{ '/aircraft/engines/' | relative_url }}#indications-and-limits).

### Dual engine failure {#dual-engine-failure}

On a dual engine failure, the pilot must enter an autorotation: establish an airspeed between 77 and 107 knots and lower the collective to maintain Nr. Autorotation cannot be performed safely above 145 knots true airspeed. See [Autorotation]({{ '/flying/flight-model/' | relative_url }}#autorotation).

## Rotor speed

A low rotor RPM condition occurs when the power demanded exceeds the maximum torque available. To recover, the pilot **MUST** lower the collective to restore Nr. Nr can take several seconds to recover.

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| LOW RTR | LOW ROTOR RPM | Collective – Lower to restore Nr |
| HIGH RTR | HIGH ROTOR RPM | |

## Drive train

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| NONE | NONE | NONE |
| **UFD CAUTION** | **MPD CAUTION** | **CORRECTIVE ACTION** |
| GRBX VIB | GEARBOX VIBRATION | LAND AS SOON AS POSSIBLE |
| GRBX1 CHIPS | GEARBOX 1 CHIPS | LAND AS SOON AS PRACTICABLE |
| GRBX2 CHIPS | GEARBOX 2 CHIPS | LAND AS SOON AS PRACTICABLE |
| XMSN CHIPS | MAIN XMSN CHIPS | LAND AS SOON AS POSSIBLE |

### Gearbox vibration {#gearbox-vibration}

With GRBX VIB displayed, the pilot must accelerate the helicopter above 100 kt, be prepared for a loss of tail rotor thrust, and remain above this airspeed all the way to touchdown to prevent the helicopter from spinning about its yaw axis.

## Electrical

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| NONE | NONE | NONE |
| **UFD CAUTION** | **MPD CAUTION** | **CORRECTIVE ACTION** |
| GEN1 FAIL | GENERATOR 1 FAIL | LAND AS SOON AS PRACTICABLE |
| GEN2 FAIL | GENERATOR 2 FAIL | LAND AS SOON AS PRACTICABLE |
| Both GEN1 FAIL and GEN2 FAIL | | LAND AS SOON AS POSSIBLE |
| RECT1 FAIL | RECTIFIER 1 FAIL | LAND AS SOON AS PRACTICABLE |
| RECT2 FAIL | RECTIFIER 2 FAIL | LAND AS SOON AS PRACTICABLE |
| Both RECT1 FAIL and RECT2 FAIL | | LAND AS SOON AS POSSIBLE |
| **UFD ADVISORY** | **DMS ADVISORY** | **CORRECTIVE ACTION** |
| BATTERY | BATTERY | Repair the battery |

## Hydraulics {#hydraulics}

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| HYD FAIL | HYD FAILURE | 1. EMER HYD button – Press ON<br>2. LAND WITHOUT DELAY |
| TAIL RTR | TAIL ROTOR HYD | LAND AS SOON AS POSSIBLE |
| **UFD CAUTION** | **MPD CAUTION** | **CORRECTIVE ACTION** |
| FMC DISENG | FMC DISENGAGED | |
| BUCS FAIL | BUCS FAIL | LAND AS SOON AS POSSIBLE |
| PRI HYD PSI | PRI HYD PSI LOW | LAND AS SOON AS POSSIBLE |
| UTIL HYD PSI | UTIL HYD PSI LOW | LAND AS SOON AS POSSIBLE |
| Both PRI HYD PSI and UTIL HYD PSI | | See HYD FAIL |
| PRI HYD LVL | PRI HYD LEVEL LOW | LAND AS SOON AS PRACTICABLE |
| UTIL HYD LVL | UTIL HYD LEVEL LOW | LAND AS SOON AS PRACTICABLE |
| Both PRI HYD LVL and UTIL HYD LVL | | Be prepared for HYD FAIL |
| **UFD ADVISORY** | **DMS ADVISORY** | **CORRECTIVE ACTION** |
| ACCUM PSI | ACCUM OIL PRES LO | Information System Status |

A loss of both primary and utility hydraulics results in a complete loss of aircraft control. The crew **MUST** immediately press the EMER HYD button and land the aircraft without delay. Emergency hydraulics provide control for approximately 60 seconds. See [Electrical, APU and hydraulics]({{ '/aircraft/electrical/' | relative_url }}#hydraulic-system).

## APU

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| — | APU FIRE | See [Fire](#fire) |
| **UFD CAUTION** | **MPD CAUTION** | **CORRECTIVE ACTION** |
| APU ON | APU ON | Turn off APU |
| **UFD ADVISORY** | **DMS ADVISORY** | **CORRECTIVE ACTION** |
| APU FAIL | APU FAIL | Repair the APU |

## Fuel

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| NONE | NONE | NONE |
| **UFD CAUTION** | **MPD CAUTION** | **CORRECTIVE ACTION** |
| AFT FUEL LO | AFT FUEL LOW | LAND AS SOON AS PRACTICABLE |
| FWD FUEL LO | FORWARD FUEL LOW | LAND AS SOON AS PRACTICABLE |

With both low fuel cautions displayed, the fuel remaining is 500 lb, approximately 27 minutes at 1,100 lb per hour.

## Flight controls

| UFD CAUTION | MPD CAUTION | CORRECTIVE ACTION |
|---|---|---|
| FMC DISENG | FMC DISENGAGED | |
| STAB FAIL | AUTO/MAN STAB FAIL | |

With FMC DISENG displayed, the hold modes and stability augmentation are lost in the affected axes; the [UTIL page]({{ '/displays/mpd/util/' | relative_url }}) shows whether an FMC axis is selected off. With STAB FAIL displayed, the stabilator remains at its last position and no longer schedules with airspeed.

## Wing stores jettison

Emergency jettison {% include key.html id="fza_ah64_collectiveEmergJett" %} releases all wing stores: rocket launchers, missile launchers and external tanks. It requires battery power.
