---
title: Up-front display
lead: The small display above the right MPD. Warnings, cautions and advisories at a glance, with the radios, total fuel and the clock.
keywords: [ufd, eufd, up-front display, warnings, cautions, advisories, radios, fuel, clock, acre]
seats: [PLT, CPG]
redirect_from:
  - /ufd.html
---

Each crew station has its own UFD. It works on battery power alone, so it is the first display to come on at start-up and the last to go off.

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

The top five lines have three columns: **warnings** on the left, **cautions** in the middle and **advisories** on the right, in their short form. The [WCA page]({{ '/displays/mpd/wca/' | relative_url }}) lists every message with its full text and what it means.

When a new warning or caution appears, one of your MPDs switches to the [ENG page]({{ '/displays/mpd/eng/' | relative_url }}) so you can see what is wrong: the left one, or the right one if the left is showing FLT. Nothing switches if either MPD already shows ENG.

## Radios

The next four lines are the radios, **VH**, **UH**, **F1** and **F2**.

- **Without ACRE**, they stand for Arma's chat channels: VH is Global, UH Side, F1 Command and F2 Group. The arrow marks the channel you are on. The frequencies are for show.
- **With ACRE**, they show the aircraft's own racked radios: each radio's frequency, preset channel and label, and which of your push-to-talk keys transmits on it.

## Bottom line

**Total fuel** in pounds on the left, internal and external together. The transponder text in the middle is for show. On the right is the clock, in local time.
