---
title: HeliSim
tags: [flight_model]
sidebar: ah64d_sidebar
permalink: flight-model-helisim.html
folder: flightmodel
---
# HeliSim – Advanced Helicopter Flight Model for Arma 3  

## Overview  
As of **version 2.2.0**, the previous **SFM+** flight model has been completely removed and replaced with **HeliSim**.  

HeliSim is a **complete physics replacement and evolution of SFM+**, designed primarily for helicopters but adaptable for other air vehicles. It replaces **Arma 3’s Simple and Advanced Flight Models**, offering a comprehensive simulation of **realistic helicopter aerodynamics**.  

### Key Simulated Effects  
HeliSim **accurately simulates** various helicopter flight behaviors, including:  
- **Effective Translational Lift (ETL)**  
- **Ground Effect**  
- **Vortex Ring State (VRS)**  
- **Translating Tendency**  
- **Retreating Blade Stall** *(planned)*  
- **Transient Torque** *(planned)*  

### Current Simulated Systems for the Apache  
The AH-64D Mod includes realistic **mechanical and electronic systems**, such as:  
- **Hydraulics & Pneumatics**  
- **Electrical Systems**  
- **Flight Management Computer**  
- **Stability & Command Augmentation Systems**  
- **Non-boosted flight controls**  
- **Auxiliary Power Unit (APU)**  
- **Turbine Engine & Transmission**  

---

## Flight Dynamics  

### Ground Effect  
- The aircraft operates **In Ground Effect (IGE)** when hovering **within one rotor diameter** (~48 feet AGL for the AH-64D).  
- **IGE reduces power requirements**, as rotor downwash is **restricted** by the proximity to the ground.  
- As altitude **increases**, ground effect **dissipates**, requiring **additional power** for Out of Ground Effect (**OGE**) hovering.  

### Effective Translational Lift (ETL)  
- Occurs **between 16–24 knots**, improving **rotor efficiency** as the aircraft moves into **cleaner air**.  
- Pilots will experience **a slight vertical vibration** during this transition.  

### Translating Tendency  
- Due to the **counterclockwise main rotor rotation**, increasing collective **induces right yaw**.  
- **Tail rotor thrust** counters yaw but causes **lateral drift to the right**.  
- Pilots must **apply left cyclic input**, resulting in an approximate **3° left roll** at hover.  

### Main Rotor Torque Effect  
- Applying **collective** increases rotor torque, causing **right yaw**.  
- Pilots must **apply left pedal input** to counteract yaw.  

---

## Advanced Aerodynamic Effects  

### Vortex Ring State (VRS)  
VRS occurs when the **main rotor enters an aerodynamic stall** due to excessive vertical descent.  
For VRS to develop, all **three conditions must be met simultaneously**:  

1. **Vertical descent rate** exceeding **300 fpm**.  
2. **Power applied** between **20–100%**, but insufficient to arrest descent.  
3. **Forward airspeed** below **ETL (<16 knots)**.  

- The AH-64D Mod enters **fully developed VRS at ~4,800 fpm**.  
- Recovery requires **directional movement** (forward, backward, or sideways).  
- Early warning signs include **progressive rotor shake**.  
- **Collective input** may worsen descent, increasing **over-torque risk and rotor droop**.  

⚠ **Pilots must monitor descent rates, especially in low-speed, high-density altitude conditions!**  

### Settling With Power (SWP) *(Different from VRS!)*  
SWP occurs when the **rate of descent exceeds available engine power**, preventing recovery.  
This is **not the same as VRS**, though symptoms can seem similar.  

#### SWP Example  
A pilot **terminates to an OGE hover after high-speed flight**, requiring **95% torque**—but the **continuous torque limit is 100%**.  

- A **100 fpm descent** demands **~2% torque** to arrest.  
- A **5% torque margin** allows a **maximum descent rate of ~250 fpm**.  
- **Higher aircraft weight, altitude, and temperature worsen the situation.**  

⚠ **Understanding helicopter performance margins is essential to prevent SWP.**  

---

## Additional Flight Phenomena  

### Mushing  
Mushing is a **temporary stall condition** occurring during **aggressive, high-speed dive recoveries**.  

- The helicopter’s **momentum exceeds rotor thrust**, delaying recovery.  
- Pilots should **apply forward cyclic** to regain control.  
- **Pulling aft cyclic** **worsens the stall**, increasing altitude loss.  

### Autorotations  
A **power-on autorotation** must be performed **between 77–107 knots**.  

- **77 knots**: Minimum **rate of descent** speed.  
- **107 knots**: Maximum **glide efficiency** speed.  
- **Unsafe above 145 knots**.  
- Reduce **collective input** until torque is **<10%** with both engines engaged.  

---

## Damage Modeling  

HeliSim **enforces realistic startup procedures**.  
Improper startup **will result in transmission failure**, leading to **aircraft loss** within 30 seconds if limits are exceeded.  

### Engine Start Parameters  

| Torque (Tq) | Rotor RPM (Nr) |  
|:--|:--|  
| ≤ 30% | ≤ 50% |  
| ≤ 70% | ≤ 90% |  

### Single Engine Torque Limits  
Exceeding **critical torque levels** results in **failure**:  

| Tq (%) | Time Limit |  
|:--|:--|  
| 0–110% | Normal Operation |  
| 111–122% | Max **2.5 Minutes** |  
| 123–125% | Max **6 Seconds** |  
| > 125% | Immediate Failure |  

### Dual Engine Torque Limits  

| Tq (%) | Time Limit |  
|:--|:--|  
| 0–100% | Normal Operation |  
| 101–115% | Max **6 Seconds** |  
| > 115% | Immediate Failure |  

---

## Performance Model  

HeliSim considers **aircraft weight and environmental factors** to ensure accurate **performance calculations**.  

### Key Aircraft Performance Figures  

| Metric | Dual Engine | Single Engine |  
|:--|:--|:--|  
| **Max Torque** | 127% | 131% |  
| **Max Continuous Torque** | 100% | 110% |  
| **Max Gross Weight (IGE)** | **20,260 lbs** |  
| **Max Gross Weight (OGE)** | **18,700 lbs** |  