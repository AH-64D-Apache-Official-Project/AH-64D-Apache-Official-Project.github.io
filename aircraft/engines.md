---
title: Engines, drive train and rotor
lead: The T700-GE-701C engines, their operating limits and performance, the drive train from the engines to the rotors, and the rotor brake.
keywords: [engine, turboshaft, t700, 701c, ng, np, nr, tgt, torque, oil, limits, tgt limiter, overspeed, performance, drive train, nose gearbox, transmission, gearbox, rotor brake]
seats: [PLT]
---

## Engines

The AH-64D is powered by two General Electric T700-GE-701C turboshaft engines, which provide power to the main and tail rotors through the drive train. Each engine provides 50% of the power required by the rotor. In the event of an engine failure, a single engine can sustain flight provided the helicopter remains above the calculated velocity safe single engine (VSSE) for the given conditions.

Each engine is comprised of the following sections:

- **Cold**: contains the inlet and compressor.
- **Hot**: contains the combustion section.
- **Power turbine**: converts energy from the hot section to shaft power, which in turn drives the rotor.
- **Accessory**: contains the support modules for the engine, i.e. oil and fuel pumps, air turbine starter, hydromechanical unit, alternator and others.

## Indications and limits

All engine outputs are color coded. **Green** indicates the value is within its normal operating range. **Yellow** indicates a cautionary range and typically has a timer associated with it; exceeding the timer incurs damage. **Red** indicates a value that has been exceeded or is below the minimum required for operation. Any time a value is red, it can be assumed that damage has been incurred.

The normal limits for the helicopter are:

**Oil (psi)**
- 23: minimum, power lever at IDLE (< 23 red)
- 23 to 120: normal operation (green)
- 120: maximum (> 120 red with box)

**Ng (%)**
- 63: minimum; engine out warning annunciated (red with box)
- 63.1 to 102.2: normal operation (green)
- 102.3 to 105.1: transient for 12 seconds (yellow)
- 105.1: maximum (> 105.1 red)

Both engines have mechanical Ng overspeed protection that trips between 108 and 112%. Reaching this value causes the engine to shut down.

**Np (%)**
- 0 to 105: normal operation (green)
- 106 to 121: transient for 12 seconds (yellow, boxed at 107)
- 115: engine overspeed annunciated
- 121: maximum (> 121 red with box)

Both engines have electrical Np overspeed protection that trips at 119.6%. Reaching this value causes the engine to shut down.

**TGT (°C)**
- 0 to 810: normal operation (green)
- 810: maximum continuous power
- 811 to 870: intermediate rated power, 30 minute limit (yellow)
- 851: maximum during start
- 871 to 878: intermediate rated power, 10 minute limit (yellow)
- 879 to 896: single engine contingency, 2.5 minute limit (yellow)
- 897 to 949: single engine transient, 12 seconds (yellow)
- 949: maximum (> 949 red)

**Nr (%)**
- 0 to 94: transient operation (red)
- 95 to 105: normal operation (green)
- 106: high rotor annunciated
- 106 to 110: transient operation (yellow)
- 110: maximum (> 110 red)

**Torque, dual engine (DE) (%)**
- 0 to 100: normal operation (green)
- 101 to 115: transient for 6 seconds (yellow)
- 115: maximum (> 115 red)

**Torque, single engine (SE) (%)**
- 0 to 110: normal operation (green)
- 110: single engine maximum continuous power (green)
- 111 to 122: single engine contingency for 2.5 minutes (yellow)
- 123 to 125: transient for 6 seconds (yellow)
- 125: maximum (> 125 red)

## TGT limiter and engine performance

Each engine features a solid-state TGT limiter. The dual engine TGT limiter is 867 °C and the single engine TGT limiter is 896 °C. These values correspond to the maximum torque available dual engine and single engine respectively. When the limit is reached, TGT no longer increases and the engine restricts fuel flow; no additional power is provided to the rotor, and Nr begins to slow down, or droop.

The combined effects of altitude and temperature on engine performance are simulated. As the helicopter climbs, or as temperature increases, engine performance decreases, and the maximum torque limit can be reached earlier. Maximum torque available dual engine and single engine, by free air temperature and pressure altitude, is shown on the [PERF page]({{ '/displays/mpd/perf/' | relative_url }}).

The following table provides a list of Warnings, Cautions and Advisories:

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| ENG1 OUT | ENGINE 1 OUT | LAND AS SOON AS PRACTICABLE |
| ENG2 OUT | ENGINE 2 OUT | LAND AS SOON AS PRACTICABLE |
| — | ENGINE 1 FIRE | 1. EMER ENG SHUTDOWN (affected engine) – When conditions permit<br>2. Illuminated ENG FIRE button – Press and RDY light illuminates<br>3. FIRE DISCH button(s) – Press<br>4. LAND AS SOON AS POSSIBLE |
| — | ENGINE 2 FIRE | 1. EMER ENG SHUTDOWN (affected engine) – When conditions permit<br>2. Illuminated ENG FIRE button – Press and RDY light illuminates<br>3. FIRE DISCH button(s) – Press<br>4. LAND AS SOON AS POSSIBLE |
| **UFD CAUTION** | **MPD CAUTION** | **CORRECTIVE ACTION** |
| NONE | NONE | NONE |
| **UFD ADVISORY** | **DMS ADVISORY** | **CORRECTIVE ACTION** |
| ENG1 START | ENGINE 1 START | |
| ENG2 START | ENGINE 2 START | |

## Drive train

The drive train consists of the main transmission, two nose gearboxes, and the intermediate and tail rotor gearboxes.

Each engine is connected to a nose gearbox, which reduces the engine output RPM and changes the output direction 90 degrees to connect to the main transmission. When operating single engine, the nose gearboxes alert the crew to impending failure if their limits are exceeded: GRBX1 or GRBX2 OIL PSI, then GRBX1 or GRBX2 CHIPS, each indicating increasing severity. When a nose gearbox fails, the engine it is connected to loses its load, accelerates to maximum power, trips either the Np or Ng overspeed protection and shuts down. The pilot must then execute an autorotation.

The main transmission further reduces the input RPM from the nose gearboxes for the main rotor, turns the generators and hydraulic pumps when the APU is off, and outputs to the intermediate gearbox to turn the tail rotor. When operating dual engine, the main transmission alerts the crew to impending failure if its limits are exceeded: XMSN1 OIL PSI, XMSN2 OIL PSI, then XMSN CHIPS, each indicating increasing severity. When the main transmission fails, the rotor seizes and all hydraulic and electrical power, the main rotor and the tail rotor are lost. This is a catastrophic event.

The intermediate and tail rotor gearboxes change the direction of output and reduce the RPM from the transmission to the tail rotor. An impending failure or critical damage to either gearbox results in the GRBX VIB caution. When this message is displayed, the pilot must accelerate the helicopter above 100 kt, be prepared for a loss of tail rotor thrust, and remain above this airspeed all the way to touchdown to prevent the helicopter from spinning about its yaw axis. If either gearbox is destroyed, an immediate loss of tail rotor thrust takes place and the pilot is unable to control the heading of the helicopter with the pedals.

The following table provides a list of Warnings, Cautions and Advisories:

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| NONE | NONE | NONE |
| **UFD CAUTION** | **MPD CAUTION** | **CORRECTIVE ACTION** |
| GRBX VIB | GEARBOX VIBRATION | LAND AS SOON AS POSSIBLE |
| GRBX1 OIL PSI | GRBX 1 OIL PSI LOW |  |
| GRBX2 OIL PSI | GRBX 2 OIL PSI LOW |  |
| GRBX1 CHIPS | GEARBOX 1 CHIPS | LAND AS SOON AS PRACTICABLE |
| GRBX2 CHIPS | GEARBOX 2 CHIPS | LAND AS SOON AS PRACTICABLE |
| XMSN1 OIL PSI | XMSN 1 OIL PSI LOW |  |
| XMSN2 OIL PSI | XMSN 2 OIL PSI LOW |  |
| XMSN CHIPS | MAIN XMSN CHIPS | LAND AS SOON AS POSSIBLE |
| **UFD ADVISORY** | **DMS ADVISORY** | **CORRECTIVE ACTION** |
| NONE | NONE | NONE |

## Rotor brake

The aircraft is provided with a rotor brake. The rotor brake slows the rotor to a stop, or locks the rotor during high winds. Its default state is OFF. The RTR BRK switch on the power lever quadrant is a 3-position switch: OFF, BRK and LOCK. With the rotor brake in the LOCK position, a rotor lock start may be performed; with the rotor brake in LOCK, there is no increase in Np or Nr.

| UFD CAUTION | MPD CAUTION | CORRECTIVE ACTION |
|---|---|---|
| RTR BRK ON/LK | ROTOR BRAKE ON/LK |  |
| **UFD ADVISORY** | **DMS ADVISORY** | **CORRECTIVE ACTION** |
| RTR BRK ON | ROTOR BRAKE ON | |
