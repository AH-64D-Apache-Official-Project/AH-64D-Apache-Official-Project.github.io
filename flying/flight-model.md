---
title: HeliSim flight model
lead: The HeliSim flight dynamics model, the performance and environment simulation, and the aerodynamic effects the crew must manage — translational lift, ground effect, translating tendency, vortex ring state, settling with power, mushing and autorotation.
keywords: [helisim, flight model, physics, torque, performance, environment, etl, ground effect, translating tendency, vrs, vortex ring state, settling with power, swp, mushing, autorotation, weight]
redirect_from:
  - /flight-model-helisim.html
---

## HeliSim

HeliSim is a complete replacement of the Arma 3 Advanced Flight Model (AFM). It is a separate mod, [**HeliSim Core**](https://steamcommunity.com/workshop/filedetails/?id=3806917476), which must be loaded. HeliSim provides a helicopter flight dynamics model that simulates airframe drag and rotor thrust, and expands the SFM+ stabilator system. It simulates main rotor torque, translational lift, ground effect, translating tendency, vortex ring state and autorotation. The AH-64D supplies its own aircraft data to HeliSim: weights, rotor, engines, transmission, fuel, hydraulics and electrical system.

Engine, drive train and rotor limits are given in [Engines, drive train and rotor]({{ '/aircraft/engines/' | relative_url }}#indications-and-limits). Exceeding a limit beyond its time allowance damages the engine or drive train.

## Limits {#limits}

All operating limits — oil, Ng, Np, TGT, Nr and torque, dual and single engine — and the TGT limiters are listed in [Engines, drive train and rotor]({{ '/aircraft/engines/' | relative_url }}#indications-and-limits).

## Performance simulation

The performance simulation models the helicopter's performance from 0 to 8,000 ft pressure altitude and from −40 to +40 °C.

Gaining altitude decreases available power. A heavier helicopter requires more torque to hover: more weight requires more torque. As the helicopter gains altitude, the air becomes less dense and the rotor system produces less thrust; the pilot must increase collective to generate the same lift as at a lower altitude.

Altitude and temperature also affect the maximum torque the engines can produce. Higher altitudes and higher temperatures reduce engine power. When the maximum torque available is reached, the rotor begins to slow down (droop), since the engines can no longer supply the power to hold Nr at 101%. This results in a loss of lift.

To recover from a low rotor RPM condition, the pilot **MUST** lower the collective to restore Nr. Nr can take several seconds to recover; close to the ground, there may not be sufficient height to recover before ground contact.

Maximum torque available, hover torque required and maximum gross weight for the current conditions are displayed on the [PERF page]({{ '/displays/mpd/perf/' | relative_url }}).

## Weight

| | |
|---|---|
| Empty, without the radar | 13,920 lb |
| Empty, with the radar | 14,570 lb |
| Maximum gross weight for combat | 20,260 lb |

## Environment simulation

The environment model sets the base pressure altitude and temperature the helicopter operates at. As the helicopter climbs, temperature decreases at a lapse rate of 2 °C per 1,000 ft. Each preset represents the average altitude and temperature of a region where common Arma maps are set. The preset is selected in **Aircraft Environmental Settings** ([Addon settings]({{ '/getting-started/settings/' | relative_url }}#helisim)).

| Environment | Base pressure altitude | Base temperature |
|---|---|---|
| Standard Day (ISA) | 0 ft | 15 °C |
| Europe – Summer (default) | 800 ft | 20 °C |
| Europe – Winter | 800 ft | 0 °C |
| Middle East | 1,800 ft | 30 °C |
| Central Asia – Summer | 5,000 ft | 30 °C |
| Central Asia – Winter | 5,000 ft | −5 °C |
| Asia | 3,100 ft | 25 °C |

Wind from the mission weather is included.

## Main rotor torque effect

When collective is applied, torque increases and is transferred into the helicopter, turning the nose to the right. The pilot applies left pedal to counteract the rotation. This effect can be disabled in Addon Options for users without rudder pedals or a twist-grip joystick.

## Effective translational lift (ETL)

As the helicopter transitions through 16 to 24 knots, a small vertical vibration develops as the helicopter outruns its own rotor downwash and begins operating in cleaner air.

## Ground effect

The helicopter is in ground effect (IGE) when hovering within one rotor diameter of the ground: 48 ft above ground level for the AH-64D. Hovering IGE reduces the power required, since the induced flow (downwash) of the rotor cannot fully develop. As the helicopter gains height this effect is lost, and additional power is required to hover out of ground effect (OGE).

## Translating tendency

The main rotor rotates counter-clockwise. When collective is increased, the nose of the helicopter turns to the right; tail rotor thrust, directed to the right, opposes this. As a result, the helicopter drifts in the direction of tail rotor thrust. The pilot counters the drift with left cyclic, which results in an approximately 3° left roll at a hover.

## Vortex ring state (VRS) {#vortex-ring-state}

Vortex ring state is an aerodynamic stall of the main rotor that develops as the result of an excessive vertical rate of descent. For the helicopter to enter VRS, the following three conditions **MUST EXIST SIMULTANEOUSLY**; if any one condition does not exist, the helicopter cannot enter VRS:

1. A vertical or near-vertical rate of descent greater than 300 fpm.
2. Power applied, 20 to 100% of power available, with insufficient power to arrest the descent.
3. Little or no forward airspeed, generally less than ETL.

The helicopter enters fully developed VRS at approximately 4,800 fpm. Before entering VRS, the aircraft begins to shake, with the shaking increasing in severity as the rotor system approaches the stall. Before this point, recovery by applying collective is possible provided engine power is available; depending on conditions, the pilot is likely to overtorque and droop the rotor, which increases the rate of descent. The helicopter can be flown out of VRS by gaining directional airspeed (forward, aft, left or right).

Rates of descent must not be allowed to build at low airspeed, particularly in high or hot conditions.

**Enable VRS Warning** in the HeliSim settings provides an on-screen warning below ETL in three stages: entering VRS from 2,000 fpm, developing from approximately 2,900 fpm, and fully developed VRS imminent from approximately 3,900 fpm.

## Settling with power (SWP) {#settling-with-power}

Settling with power is a condition in which a rate of descent is allowed to build that cannot be arrested with the engine power available. **It is not the same as VRS.** The most likely situation for SWP is a termination to an OGE hover from high-speed flight.

For example, with 95% torque required to hover OGE and a continuous torque limit of 100%, the power margin is 5%. For the AH-64D, arresting a 100 fpm rate of descent requires approximately 2% torque above IGE hover torque. A 5% margin therefore permits a rate of descent of **no more than 250 fpm** (5% ÷ 2% × 100 fpm) without exceeding 100% and potentially overtorquing the helicopter. The margin decreases as weight, pressure altitude and temperature increase.

SWP results from operating without knowledge of the helicopter's performance capability. The pilot must know the power margin available throughout the flight; see [PERF page]({{ '/displays/mpd/perf/' | relative_url }}).

## Mushing

Mushing is a temporary stall condition that can occur during aggressive, high-speed dive recoveries. The momentum of the helicopter overcomes the thrust of the rotor system, and the helicopter continues along its original flight path until the rotor recovers. If mushing occurs, and altitude and terrain allow, the pilot applies forward cyclic to reduce the severity of the maneuver and restore normal rotor thrust; continuing to apply aft cyclic aggravates the condition.

## Autorotation

To perform a power-on autorotation, establish an airspeed between 77 and 107 knots and reduce collective until torque is less than 10% with both engines operating. 77 knots is the minimum rate of descent true airspeed and 107 knots the maximum glide true airspeed. Autorotation cannot be performed safely above 145 knots true airspeed.
