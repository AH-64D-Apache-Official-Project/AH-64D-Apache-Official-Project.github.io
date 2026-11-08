---
title: Fuel system
lead: The forward and aft fuel cells, the internal auxiliary fuel system and the external tanks, how fuel is fed and transferred, and the warnings, cautions and advisories presented to the crew.
keywords: [fuel, cells, forward, aft, crossfeed, transfer, xfer, auto, boost, iafs, robbie, external tanks, aux, refuel, leak, jettison, capacity, weight]
seats: [PLT, CPG]
---

## Description

The fuel system consists of the forward fuel cell, the aft fuel cell, the internal auxiliary fuel system (IAFS, also known as the "Robbie") and up to four external tanks. The FUEL page displays the system and contains its controls; see [FUEL page]({{ '/displays/mpd/fuel/' | relative_url }}).

| Tank | Capacity | Feeds | Installed |
|---|---|---|---|
| Forward fuel cell | 1,043 lb | Engine 1 | Always |
| Aft fuel cell | 1,474 lb | Engine 2 and the APU | Always |
| IAFS | 663 lb | Forward and aft fuel cells | In the ammunition bay; reduces the 30 mm load to 300 rounds ([Variants]({{ '/aircraft/variants/' | relative_url }})) |
| External tanks, stations 1–4 | 1,541 lb each | Left side to the forward cell, right side to the aft cell | When loaded on a wing station |

When the fuel level in the forward fuel cell goes below 240 lb, a master caution is presented to the crew. When the fuel level in the aft fuel cell goes below 260 lb, a master caution is also presented. There is no low fuel caution for the IAFS. With both low fuel cautions displayed, the fuel remaining is 500 lb; at a fuel burn of approximately 1,100 lb per hour, the helicopter has approximately 27 minutes of fuel remaining.

## Fuel feed and crossfeed

With crossfeed at NORM, engine 1 draws fuel from the forward cell and engine 2 from the aft cell. Crossfeed FWD feeds both engines from the forward cell; crossfeed AFT feeds both engines from the aft cell. Selecting the boost pump on sets crossfeed to AFT, and crossfeed cannot be changed while the boost pump is on.

The APU draws fuel from the aft cell only, at approximately 175 lb per hour.

## Fuel transfer

The transfer pump moves fuel between the forward and aft cells at approximately 50 lb per minute.

- **FWD** / **AFT**: fuel is transferred into the selected cell until it is full or the other cell is empty.
- **AUTO**: the cells are kept in balance. When a cell falls below approximately 810 lb and the other cell holds more, fuel is transferred to the lighter cell. Transfer out of the forward cell requires both engines running.
- **OFF**: no transfer.

AUTO transfer requires pneumatic air from the APU or an operating engine.

## Auxiliary tanks

L AUX and R AUX on the FUEL page select transfer from the external tanks on each side. With transfer selected, each side's tanks feed their main cell at approximately 50 lb per minute while the cell has room. The inboard tank feeds first; an outboard tank feeds only with the inboard tank installed, since it is pressurised through the inboard tank. Each side's transfer is deselected automatically when its tanks are empty, and an empty tank is indicated by the EXT1 EMPTY to EXT4 EMPTY advisory.

C AUX selects transfer from the IAFS into both main cells. The IAFS transfers only after any selected external tanks are empty.

## Damage

A fuel cell that is damaged leaks, at up to approximately 130 lb per hour per cell; the rate increases with the severity of the damage. The IAFS shares its damage with the ammunition bay. A leaking cell continues to leak until the aircraft is repaired.

An external tank whose pylon is heavily damaged explodes and is lost from the wing; the explosion increases with the fuel in the tank. A tank with less than approximately 200 lb of fuel does not explode.

## Refuelling and jettison

- ACE refuelling from a fuel vehicle or fuel source distributes fuel across the tanks.
- The [mission planner]({{ '/mission/planner/' | relative_url }}) sets the fuel load directly; whether a fuel source is required depends on the server settings.
- Emergency jettison, bound in **AH-64D Official Project**, releases all four wing stations, external tanks included. It requires battery power.

The following table provides a list of Warnings, Cautions and Advisories:

| UFD WARNING | MPD WARNING | CORRECTIVE ACTION |
|---|---|---|
| NONE | NONE | NONE |
| **UFD CAUTION** | **MPD CAUTION** | **CORRECTIVE ACTION** |
| AFT FUEL LO | AFT FUEL LOW | LAND AS SOON AS PRACTICABLE |
| FWD FUEL LO | FORWARD FUEL LOW | LAND AS SOON AS PRACTICABLE |
| **UFD ADVISORY** | **DMS ADVISORY** | **CORRECTIVE ACTION** |
| EXT1 EMPTY – EXT4 EMPTY | EXTERNAL 1–4 EMPTY | |
