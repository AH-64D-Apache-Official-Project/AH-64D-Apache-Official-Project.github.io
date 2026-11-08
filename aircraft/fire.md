---
title: Fire protection
lead: Fire detection for both engines and the APU, the two extinguisher bottles and the fire test, and the warnings and corrective actions for a fire.
keywords: [fire, engine fire, apu fire, extinguisher, bottle, primary, reserve, fire button, rdy, fire disch, fire test]
seats: [PLT, CPG]
---

## Description

Both crew stations have a fire detection and extinguishing panel on the glareshield, and either crew station can operate it. The panel requires battery power.

| Control | Function |
|---|---|
| ENG 1, APU and ENG 2 FIRE buttons | Illuminate red when a fire is detected in that area. Pressing the illuminated button arms it: the RDY light illuminates, fuel to that engine or the APU is shut off (with DC power available), and that fire's voice message and the MSTR WARN lighted button stop. Pressing it again disarms it. |
| FIRE DISCH buttons, PRI and RES | Discharge the primary or reserve extinguisher bottle into the armed area. Each bottle discharges once; its light illuminates when it has been used. |
| TEST switch | TEST 1 illuminates every FIRE button and RDY light, plays each fire voice message, illuminates the MSTR WARN lighted button and displays DECK FIRE. TEST 2 also illuminates both bottle discharge lights. The switch is returned to the centre to end the test. |

## Fire

A fire can be started by:

- **Battle damage**: heavy damage to a running engine or a running APU.
- **Oil starvation**: an engine that fails after losing all oil pressure catches fire in most cases. See [Engines, drive train and rotor]({{ '/aircraft/engines/' | relative_url }}).

A fire is indicated by ENGINE 1 FIRE, ENGINE 2 FIRE or APU FIRE on the MPD, the voice message, the MSTR WARN lighted button, the FIRE button illuminated red, and smoke and flame from the affected side of the aircraft. A fire damages the engine or APU for as long as it burns.

An extinguisher bottle reaches a fire only if that fire's FIRE button is **armed before** the bottle is discharged. A bottle discharged before the button is armed, or with a different button armed, is lost. A bottle that reaches the fire extinguishes it unless the bottle fails; each bottle has a one-in-four chance of failing, which is the purpose of the reserve bottle. With the engine or APU shut down, a fire that is not extinguished burns out in approximately 30 seconds, and continues to cause damage until it does.

While a fire warning is active, the [ENG page]({{ '/displays/mpd/eng/' | relative_url }}#emergency-format) displays the immediate action steps. Discharged bottles are refilled when the aircraft is repaired.

The following table provides a list of Warnings, Cautions and Advisories:

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| — | ENGINE 1 FIRE | 1. EMER ENG SHUTDOWN (affected engine) – When conditions permit<br>2. Illuminated ENG FIRE button – Press and RDY light illuminates<br>3. FIRE DISCH button(s) – Press<br>4. LAND AS SOON AS POSSIBLE |
| — | ENGINE 2 FIRE | 1. EMER ENG SHUTDOWN (affected engine) – When conditions permit<br>2. Illuminated ENG FIRE button – Press and RDY light illuminates<br>3. FIRE DISCH button(s) – Press<br>4. LAND AS SOON AS POSSIBLE |
| — | APU FIRE | 1. Illuminated APU FIRE button – Press and RDY light illuminates<br>2. FIRE DISCH button(s) – Press<br>3. LAND AS SOON AS POSSIBLE |
| DECK FIRE | AFT DECK FIRE | Displayed by the fire test only (not simulated as a fire). |
| **UFD CAUTION** | **MPD CAUTION** | **CORRECTIVE ACTION** |
| NONE | NONE | NONE |
| **UFD ADVISORY** | **DMS ADVISORY** | **CORRECTIVE ACTION** |
| NONE | NONE | NONE |
