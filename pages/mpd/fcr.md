---
title: FCR Page
tags: [mpd]
sidebar: ah64d_sidebar
permalink: mpd-fcr.html
folder: mpd
---



{% include image.html file="mpd/MPD-FCR-GTM.png" alt="Image of the FCR Page" caption="Figure 1: FCR GTM." %}

{% include image.html file="mpd/MPD-FCR-ATM.png" alt="Image of the FCR Page" caption="Figure 2: The FCR page in ATM." %}

The FCR(Fire Control Radar) is the cheese wheel mounted ontop of the Rotor Mast.

The Fire control Radar is Capbable of Tracking up to 256 Target at a range of 8 KM at any one time, The FCR page itself will only display the 16 closest Targets to be scanned, as the Apache Only carries 16 Hellfires.

The Fire Control Radar has 4 Submodes ground targeting mode (GTM), radar map mode (RMAP), air targeting mode (ATM), or terrain profiles mode (TPM), of the 4 We currently Implement GTM & ATM.


## Operations
Cscope - This when enabled projects the FCRs 16 targets into your Ihadss.
{% include note.html content="The cscope only displays the icon on the Last scan position and does not predict the movement of targes." %}

The rest of the FCR can be operated via [keybinds](keybinds.html)

## Specifications
- Min Range 500M.
- Max Range Stationary targets 6km.
- Max Range Moving Targets 8km.
- Max Trackable Speed 1500 Km/h.

## GTM 
- Azimuth +-45°.
- Elevation +25° -35°.

## ATM
- Azimuth +-168°.
- Elevation +45° -22°.
- MIN Trackable Speed 6 Km/h.
{% include note.html content="In ATM, Only targets moving greater that 6km/h will be detected" %}
