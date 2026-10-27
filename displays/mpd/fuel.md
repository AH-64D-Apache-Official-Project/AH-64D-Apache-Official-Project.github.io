---
title: FUEL page
lead: Fuel quantity, flow and endurance, and the controls for the transfer pump, boost pump, crossfeed and external tanks.
keywords: [fuel, crossfeed, boost, transfer, xfer, aux, tanks, endurance, sfr, check]
seats: [PLT, CPG]
redirect_from:
  - /mpd-fuel.html
---

Open it from the MENU (`B1`{: .vab} then **FUEL**) or from the top row of any other aircraft page. Both crew stations share the same fuel system, so a change made on one seat's FUEL page shows on the other's.

{% include fig.html id="mpd-fuel" %}

## Buttons

| Button | Label | Action |
|---|---|---|
| `T2`{: .vab} | `FLT`{: .mpd} | Opens the FLT page. |
| `T3`{: .vab} | `FUEL`{: .mpd .box} | This page. |
| `T4`{: .vab} | `PERF`{: .mpd} | Opens the PERF page. |
| `T6`{: .vab} | `UTIL`{: .mpd} | Opens the aircraft UTIL page. |
| `L1`{: .vab} | `L AUX`{: .mpd} | Left external tanks on or off. Shown with tanks on station 1 or 2. Can only be turned on while one of them holds fuel. |
| `L2`{: .vab} | `C AUX`{: .mpd} | Internal auxiliary tank transfer on or off. Shown with the tank fitted. |
| `L4`{: .vab} | `XFER`{: .mpd} | Opens the transfer pump menu on `L1`{: .vab} to `L4`{: .vab}: **FWD**, **OFF**, **AFT**, **AUTO**. |
| `R1`{: .vab} | `R AUX`{: .mpd} | Right external tanks on or off (stations 3 and 4). |
| `R2`{: .vab} | `BOOST`{: .mpd} | Boost pump on or off. Turning it on also sets crossfeed to **AFT**; turning it off returns crossfeed to **NORM**. |
| `R3`{: .vab}–`R5`{: .vab} | `FWD`{: .mpd} `NORM`{: .mpd} `AFT`{: .mpd} | Crossfeed mode. Locked while the boost pump is on. |
| `B1`{: .vab} | | MENU. |
| `B6`{: .vab} | `CHECK`{: .mpd} | Opens or closes the fuel check. |

## Fuel cells and feed

The aircraft carries fuel in a forward and an aft cell. With crossfeed in **NORM**, engine 1 draws from the forward cell and engine 2 from the aft cell, and the feed lines are drawn bold while fuel is flowing.

**FWD** and **AFT** crossfeed feed both engines from one cell. Use them to balance the cells, or to keep an engine running from the other cell after damage.

> A cell quantity turns yellow below 240 lb (forward) or 260 lb (aft), and is replaced by a white **E** when the cell is empty. Low fuel also raises the `FWD FUEL LO`{: .mpd} or `AFT FUEL LO`{: .mpd} caution.
{: .caution}

## Transfer pump

`L4`{: .vab} replaces the left-side labels with the transfer menu. Pick a mode to close it:

- **FWD** and **AFT** pump fuel from one cell into the other. The line between the cells animates in the direction of flow.
- **AUTO** keeps the two cells balanced, moving fuel towards whichever cell is lighter.
- **OFF** stops transfer.

## External and auxiliary tanks

External tanks are fitted to the wing stations from the pylon loadout (see [Rearm and refuel]({{ '/mission/rearm/' | relative_url }})). When any are fitted the page draws them on the wings, adds the `L AUX`{: .mpd} and `R AUX`{: .mpd} switches and shows a **TOT** line for total fuel and total endurance. A side's switch turns itself off when its tanks run dry.

## Fuel check

`B6`{: .vab} **CHECK** opens the fuel check. It measures your real burn rate over a set time and works out when you will run out.

1. Choose the length of the check: `R2`{: .vab} 15, `R3`{: .vab} 20 or `R4`{: .vab} 30 minutes.
2. Press `R5`{: .vab} **START**. The start time is recorded in local time.
3. Close the check with `B6`{: .vab} if you need the page. A running check carries on in the background.
4. When the time is up, or when you press `R5`{: .vab} **STOP**, the page shows the elapsed time, burn rate in pounds per hour, the burnout time, and the times by which you must land to keep a 20 minute (VFR) or 30 minute (IFR) reserve. If neither crew station has the check open when it finishes, a `FUEL CHECK`{: .mpd} advisory tells you the results are ready.
{: .steps}

Starting a new check clears the previous results.
