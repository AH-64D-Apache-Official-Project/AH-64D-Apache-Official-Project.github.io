---
title: FUEL page
lead: Fuel quantity, flow and endurance, and the controls for the transfer pump, boost pump, crossfeed, auxiliary tanks and fuel check.
keywords: [fuel, crossfeed, boost, transfer, xfer, aux, tanks, endurance, sfr, check]
seats: [PLT, CPG]
redirect_from:
  - /mpd-fuel.html
---

The FUEL page is selected from the MENU page (`B1`{: .vab}, then FUEL) or with the FUEL page button on any aircraft page. The fuel system is aircraft common; a selection made on one crew station's FUEL page is displayed on the other's. The system is described in [Fuel system]({{ '/aircraft/fuel/' | relative_url }}).

{% include fig.html id="mpd-fuel" %}

## Buttons

| Button | Label | Function |
|---|---|---|
| `T2`{: .vab} | `FLT`{: .mpd} | FLT page |
| `T3`{: .vab} | `FUEL`{: .mpd .box} | This page |
| `T4`{: .vab} | `PERF`{: .mpd} | PERF page |
| `T6`{: .vab} | `UTIL`{: .mpd} | UTIL page |
| `L1`{: .vab} | `L AUX`{: .mpd} | L AUX fuel transfer on or off, from the left external tanks. Displayed with tanks on station 1 or 2; selectable only while one of them contains fuel. |
| `L2`{: .vab} | `C AUX`{: .mpd} | C AUX fuel transfer on or off, from the internal auxiliary fuel cell. Displayed with the IAFS installed. |
| `L4`{: .vab} | `XFER`{: .mpd} | Fuel transfer option buttons on `L1`{: .vab}–`L4`{: .vab}: FWD, OFF, AFT, AUTO |
| `R1`{: .vab} | `R AUX`{: .mpd} | R AUX fuel transfer on or off, from the right external tanks (stations 3 and 4) |
| `R2`{: .vab} | `BOOST`{: .mpd} | Boost pump on or off. On sets crossfeed to AFT; off returns crossfeed to NORM. |
| `R3`{: .vab}–`R5`{: .vab} | `FWD`{: .mpd} `NORM`{: .mpd} `AFT`{: .mpd} | CROSSFEED buttons. Inhibited while the boost pump is on. |
| `B1`{: .vab} | | MENU page |
| `B6`{: .vab} | `CHECK`{: .mpd} | CHECK format, present or remove |

## Fuel cells and feed

With CROSSFEED NORM, engine 1 feeds from the forward fuel cell and engine 2 from the aft fuel cell; the fuel lines are a graphic representation of fuel routing, displayed bold while fuel flows. CROSSFEED FWD or AFT feeds both engines from that cell.

A fuel cell quantity is displayed yellow below 240 lb (forward) or 260 lb (aft), and is replaced by a white **E** indicator when the cell is empty. Low fuel also raises the `FWD FUEL LO`{: .mpd} or `AFT FUEL LO`{: .mpd} caution.

## Fuel transfer

`L4`{: .vab} XFER replaces the left-side labels with the fuel transfer option buttons; selecting an option removes them.

- FWD transfers fuel from the aft fuel cell to the forward fuel cell, and AFT from the forward to the aft; the fuel transfer line is displayed and marquees to indicate the direction of transfer.
- AUTO selects automatic fuel leveling between the fuel cells, transferring toward the lighter cell.
- OFF stops fuel transfer.

## Auxiliary tanks

External tanks are installed on the wing stations from the pylon loadout (see [Rearm and refuel]({{ '/mission/rearm/' | relative_url }})). With tanks installed, the page displays tank icons on the aircraft icon, adds the L AUX and R AUX buttons, and displays the total (TOT) fuel quantity and total endurance (ENDR TOT) status. A side's transfer is deselected automatically when its tanks are empty.

## Fuel check {#fuel-check}

`B6`{: .vab} CHECK presents the CHECK format, which calculates burnout, VFR reserve and IFR reserve times, based on the fuel quantity change during the selected interval.

1. MINUTES – Select: `R2`{: .vab} 15, `R3`{: .vab} 20 or `R4`{: .vab} 30 minutes.
2. `R5`{: .vab} START – Press. The start time is recorded in local time.
3. `B6`{: .vab} – Press to remove the CHECK format if the page is required; the check continues in the background.
4. At the end of the interval, or on `R5`{: .vab} STOP, the status windows display the START time, RUN time and burn RATE, in pounds per hour, and the calculated BURNOUT, VFR RES (20 minute reserve) and IFR RES (30 minute reserve) times. If neither crewmember is viewing the CHECK format at the conclusion of the check, the `FUEL CHECK`{: .mpd} advisory is displayed.
{: .steps}

Starting a new check clears the previous results.
