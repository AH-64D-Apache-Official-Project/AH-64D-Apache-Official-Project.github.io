---
title: Electrical, APU and hydraulics
lead: How electrical, hydraulic and pneumatic power is provided to the helicopter, what is lost when it fails, and the warnings, cautions and advisories presented to the crew.
keywords: [electrical, battery, battery bus, apu, generator, transformer rectifier, tru, ac, dc, hydraulics, primary, utility, accumulator, emer hyd, emergency hydraulics, pneumatic, ipas, accessory section, transmission]
seats: [PLT]
---

## Accessory section

The generators and hydraulic pumps are mounted on the accessory section of the main transmission. Under normal operating conditions, with one or both engines running, the accessory section is driven by the primary and secondary drives.

During start, the accessory section is driven by the No. 7 drive shaft, which is connected to the APU. As the power levers are advanced to FLY, the APU is disengaged between 94 and 96% Nr, and the engines take over driving the accessory section.

Electrical power is lost at approximately 85% Nr, because the generators are no longer turning fast enough to provide electrical power. This results in a loss of primary AC and DC power. Systems on the battery bus continue to operate for approximately 12 minutes, after which all electrical power is lost.

Hydraulic power is lost at approximately 45% Nr, because the hydraulic pumps are no longer turning fast enough to provide hydraulic pressure. This results in a loss of aircraft control, as the flight controls are no longer able to affect the main and tail rotors.

## Auxiliary power unit (APU)

The APU provides hydraulic pressure and electrical power to the helicopter by turning the No. 7 drive shaft, which is connected to the accessory section of the main transmission. It also provides pressurized air to start the engines.

The APU is started by the utility hydraulic accumulator and requires a minimum of 2600 psi in the accumulator. The APU requires battery power to start. The APU takes approximately 5 seconds to start from the time the APU button is pressed. During this time the crew will see the APU START and APU PWR ON advisories in the UFD, and the ACCUM PSI advisory, indicating that the accumulator has discharged its available pressure to start the APU. The ACCUM PSI advisory clears during the start, when the accumulator has been recharged to 3000 psi. Once the APU is on, the APU button is illuminated ON and the UFD displays APU ON in the advisory column.

The APU provides all low pressure and high pressure air, via the load control valve, until a single engine is started. From that point the operating engine provides all high pressure air and the APU continues to provide low pressure air. After both engines are at FLY and the APU is turned off, the engines provide low pressure air to the IPAS. The APU continues to provide electrical and hydraulic power until approximately 95% Nr, after which the engines turn the accessory section.

The APU is shut down by the APU button on the pilot's power lever quadrant, by the APU FIRE button on the fire panel, or by fuel starvation. APU STOP is displayed in the UFD after the APU is selected off. The APU draws fuel from the aft fuel cell only, and burns approximately 175 pounds of fuel per hour.

The following table provides a list of Warnings, Cautions and Advisories:

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| — | APU FIRE | 1. Illuminated APU FIRE button – Press and RDY light illuminates<br>2. FIRE DISCH button(s) – Press<br>3. LAND AS SOON AS POSSIBLE |
| **UFD CAUTION** | **MPD CAUTION** | **CORRECTIVE ACTION** |
| APU ON | APU ON | Turn off APU |
| **UFD ADVISORY** | **DMS ADVISORY** | **CORRECTIVE ACTION** |
| APU FAIL | APU FAIL | Repair the APU |
| APU ON | APU ON | |
| APU PWR ON | APU POWER ON | |
| APU START | APU START | |
| APU STOP | APU STOP | |

## Electrical system

The electrical system consists of two AC generators, two transformer rectifier units (TRUs) and the battery. The generators are mounted on the accessory section of the transmission and provide power above 85% Nr. Each generator provides AC power to its respective TRU for conversion to DC power; each TRU requires its respective generator to function. AC power flows from the generators through the high power switching modules (HPSMs, not simulated) into the TRUs, and returns to the HPSMs as DC power.

There are three buses: the AC bus, powered by the generators; the DC bus, powered by the TRUs; and the battery bus, powered by the battery.

On a loss of a single generator, the other generator powers the AC bus. A loss of both generators results in a loss of all systems on the AC bus and all systems on the DC bus, since the TRUs require the generators to operate. On a loss of a single TRU, the other TRU powers the DC bus. A loss of both TRUs results in a loss of all systems on the DC bus.

The battery bus is powered only when BOTH generators are off or have been destroyed; in the simulation, this is whenever the engines and APU are off, since nothing is turning the accessory section. The battery bus provides approximately 12 minutes of power, after which the battery must be recharged. **There is NO indication of the battery's charge level in the aircraft.** The battery is recharged automatically once the generators are online.

The following table provides a list of Warnings, Cautions and Advisories:

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

## Hydraulic system

The hydraulic system consists of the primary and utility pumps, the primary and utility reservoirs, the utility hydraulic accumulator, and the four flight control servos. Both pumps are mounted on the accessory section of the transmission, and each pump services its respective system. A loss of a single pump does not result in a loss of helicopter control, since the other pump continues to provide pressure to its side of the four flight control servos.

The primary system powers the primary side of the flight controls, the SCAS and the BUCS (not simulated). The utility reservoir supplies the utility hydraulic accumulator, the 30 mm ammunition handling system, the 30 mm azimuth and elevation motors, the pylon articulation servos, the tail wheel unlock actuator (not simulated) and the utility side of the flight controls. If the utility reservoir is damaged and loses all its fluid, all of these systems are lost except the pitch, roll and collective servos.

The primary and utility reservoirs can leak when damaged; the severity of the damage determines how quickly the reservoir leaks.

On a loss of primary hydraulic pressure together with a utility reservoir level low condition, the tail rotor (yaw) servo is lost. The tail rotor remains fixed in the last commanded position, and the pilot is unable to control the heading of the helicopter with the pedals.

A loss of **both** primary and utility hydraulic pumps results in a complete loss of aircraft control until the crew presses the EMER HYD button. The crew **MUST** immediately press the EMER HYD button and land the aircraft without delay.

The utility hydraulic accumulator provides pressurized hydraulic fluid to the APU start motor, the rotor brake and emergency hydraulics. Emergency hydraulic power is available when the EMER HYD button is pressed in either crew station with primary and utility hydraulic pressure below 1260 psi, and provides control for approximately 60 seconds. Accumulator (ACC) pressure remaining is displayed on the ENG page. When the accumulator reaches 1650 psi, ALL hydraulic power is lost, the accumulator reads 0, and the pilot is no longer able to control the helicopter.

> The emergency hydraulic duration is adjusted in the simulation for gameplay and does not represent the aircraft's exact figure.
{: .note}

The following table provides a list of Warnings, Cautions and Advisories:

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
