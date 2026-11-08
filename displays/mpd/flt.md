---
title: Flight (FLT) page
lead: The MPD FLT page presents the flight instrument symbology required for flight.
keywords: [flt, flight, flight instruments, attitude indicator, waterline, pitch ladder, airspeed, barometric altitude, radar altitude, heading scale, command heading, fly-to cue, flight path vector, rate of climb, turn rate, skid slip, navigation data]
seats: [PLT, CPG]
redirect_from:
  - /mpd-flt.html
---

The FLT page is selected from the top row of any aircraft page, from the MENU page, or with {% include key.html id="fza_ah64_symbologySelectPress" %}, which presents it on the left MPD.

{% include fig.html id="mpd-flt" %}

## Buttons

| Button | Label | Function |
|---|---|---|
| `T2`{: .vab} | `FLT`{: .mpd .box} | This page; pressed again, the ENG page |
| `T3`{: .vab} | `FUEL`{: .mpd} | FUEL page |
| `T4`{: .vab} | `PERF`{: .mpd} | PERF page |
| `T6`{: .vab} | `UTIL`{: .mpd} | A/C UTIL page |
| `R6`{: .vab} | `ACQ`{: .mpd} | [Acquisition source]({{ '/targeting/sights/' | relative_url }}#acq) list |
| `B1`{: .vab} | | MENU page |

The -W- (waterline) button, the BIAS buttons and the FLT SET button are not simulated.

## Navigation data status window

With a destination point selected, the navigation data status window in the lower left area of the page presents the destination point, distance to go, ground speed and time to go. The command heading and the navigation fly-to cue provide steering to the destination point. The seconds digits of the time to go are presented only when the time is less than 5 minutes; time to go is not presented at a ground speed of 15 kt or less. Points and routes are set on the [TSD]({{ '/displays/mpd/tsd/' | relative_url }}).

## Sensor bearings

The FCR centerline bearing and the alternate sensor bearing are presented along the bottom of the heading scale. The FCR centerline bearing represents the azimuth of the current FCR scan centerline. The alternate sensor bearing, a triangle, represents the line of sight azimuth of the other crewmember's selected sight.
