---
title: Up-front display (UFD)
lead: The UFD provides warning, caution, advisory, communications, fuel and time information within the crew's instantaneous field of view.
keywords: [ufd, up-front display, warnings, cautions, advisories, radios, fuel, clock, acre]
seats: [PLT, CPG]
redirect_from:
  - /ufd.html
---

The UFD provides warning, caution, advisory, communications, fuel and other information within the instantaneous field of view of the crew. Each crew station has its own UFD. The UFD operates on battery power.

<div class="ufd" role="img" aria-label="Example UFD with a caution, two advisories, the radio lines, fuel and clock">
<pre>         |FWD FUEL LO  |ATT HOLD
         |             |TW LOCK SEL
         |             |
         |             |
         |             |
..VH 139.500* GLBL-      L1 149.500
.>UH 240.500* SIDE- C3   L2 249.500
..F1  39.075  -CMD- C5 H T1  45.500
..F2  49.500  GROUP C2   L3  69.525
3700    XP 1200 B NORM   14:32:07 L</pre>
</div>

## Warnings, cautions and advisories

The first five lines are divided into warning (left), caution (centre) and advisory (right) areas. A total of 5 warnings/cautions/advisories may be displayed. The full text of each message, and its corrective action, is listed on the [WCA page]({{ '/displays/mpd/wca/' | relative_url }}) and on [Emergency procedures]({{ '/flying/emergency/' | relative_url }}).

When a new warning or caution is displayed, one MPD in each crew station changes to the [ENG page]({{ '/displays/mpd/eng/' | relative_url }}): the left MPD, or the right MPD if the left is displaying the FLT page. No MPD changes if either MPD is already displaying the ENG page.

## Radios

The next four lines present radio status: VHF (VH), UHF (UH), FM1 (F1) and FM2 (F2).

- **Without ACRE**, the radios represent the Arma chat channels: VH Global, UH Side, F1 Command and F2 Group. The arrow marks the active channel. The displayed frequencies are static.
- **With ACRE**, the lines display the aircraft's racked radios: each radio's frequency, preset channel and label, and the push-to-talk key assigned to it.

## Bottom line

Total fuel quantity in pounds, internal and external, is displayed on the left. The transponder (XP) status in the centre is static. Local time is displayed on the right.
