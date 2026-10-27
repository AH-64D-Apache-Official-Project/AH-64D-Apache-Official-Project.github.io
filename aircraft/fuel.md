---
title: Fuel system
lead: Two main cells feed the engines, and optional tanks top them up. How fuel moves around the aircraft, and what happens when a cell is hit.
keywords: [fuel, cells, forward, aft, crossfeed, transfer, xfer, auto, iafs, external tanks, aux, refuel, leak, jettison, capacity, weight]
seats: [PLT, CPG]
---

The [FUEL page]({{ '/displays/mpd/fuel/' | relative_url }}) shows all of this and holds the switches. This page explains what is going on behind it.

## Tanks

| Tank | Capacity | Feeds | Fitted |
|---|---|---|---|
| **Forward cell** | 1,043 lb | Engine 1 | Always |
| **Aft cell** | 1,474 lb | Engine 2, and the APU | Always |
| **IAFS** (internal auxiliary fuel system) | 663 lb | Both main cells | When the IAFS is in the ammunition bay ([Variants]({{ '/aircraft/variants/' | relative_url }})) |
| **External tanks**, stations 1–4 | 1,541 lb each | Left side into the forward cell, right side into the aft cell | When hung on a wing station |

That makes 2,517 lb in the main cells, 3,180 lb with the IAFS, and over 9,000 lb with four external tanks. Full external tanks are heavy, so check the [PERF page]({{ '/displays/mpd/perf/' | relative_url }}) or the [mission planner]({{ '/mission/planner/' | relative_url }}) before loading them.

## Feeding the engines

With crossfeed in **NORM**, each engine draws from its own cell. **FWD** or **AFT** feeds both engines from one cell. Use it to balance the cells, or to keep both engines running when one cell is damaged or empty. Turning the **boost pump** on sets crossfeed to AFT and locks it there until the pump is off.

The APU always draws from the aft cell, at 175 lb/h.

## Transfer pump

The transfer pump moves fuel between the main cells at about 50 lb/min.

| Mode | What it does |
|---|---|
| **FWD** / **AFT** | Pumps into the named cell until it is full or the other is empty. |
| **AUTO** | Keeps the cells in balance. When a cell falls below about 810 lb and the other holds noticeably more, fuel is moved into the lighter one. Moving fuel *out* of the forward cell needs both engines running, so after a single-engine failure the system cannot strand fuel away from the working engine. |
| **OFF** | No transfer. |

AUTO needs air to run the pump: the APU, or an engine running.

## Auxiliary tanks

**L AUX** and **R AUX** on the FUEL page turn each side's external tanks on. Once on, a side's tanks empty into their main cell at about 50 lb/min each, as long as the cell has room. On each side the inboard tank feeds first. An outboard tank only feeds with the inboard tank fitted, because it is pressurised through it. A side's switch turns itself off when its tanks are empty, and an empty tank shows the `EXT1 EMPTY`{: .mpd} (to `EXT4 EMPTY`{: .mpd}) advisory until you look at the FUEL page.

**C AUX** turns on the IAFS. It drains into both main cells, but only once any external tanks that are switched on have run dry.

## Damage

A cell hit hard enough starts to leak, up to about 130 lb/h per cell, and faster the worse the damage. The IAFS shares its hitpoint with the ammunition bay. A leaking cell needs a repair to stop it. Move fuel out of a leaking cell with the transfer pump and crossfeed, or burn it first.

An external tank whose pylon is hit hard explodes and is gone from the wing. The fuller the tank, the bigger the explosion. A tank with less than about 200 lb left does not explode.

## Refuelling and defuelling

- **ACE refuelling** from a fuel truck or a fuel source fills the aircraft as Arma does. The fuel is shared out across the tanks.
- The **[mission planner]({{ '/mission/planner/' | relative_url }})** sets the fuel load precisely, with or without a fuel source nearby depending on the server settings.
- **Emergency jettison**, bound in **AH-64D Official Project**, drops everything on all four wing stations, external tanks included. It needs battery power.
