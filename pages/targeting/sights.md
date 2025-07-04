---
title: Weapon Sights
tags: [weapons, targeting]
summary: Sight Selection and usage
permalink: targeting-sights.html
folder: weapons
---

A sight is a targeting system that the aircraft uses to train a weapons system on a target. The operator selects a sight, and then when they WAS a weapon that weapon will 'look down' that sight.

Alternatively, an acquisition source is some data source that you can use to help you acquire a target with your sight. An example would be the other crew-member's headset, so you could train your sight where they're looking.
{% include todo.html content="Acquisition sources are not implemented yet."%}

## Sights

* **HMD** - The HMD sight will sight whatever you are looking at with the IHADSS. It is selectable using {% include keybind.html name="sight-select-hmd"%}.
* **FXD** - The FXD sight will fix the weapon system to the nose of the aircraft (including the camera).. It is selectable using {% include keybind.html name="sight-select-fxd"%}.
{% include important.html content="in HMD or FXD, The ranging for weapons like rockets is always 1km away." %}
* **TADS** - The TADS sight will select what the TADS is aiming at.. It is selectable using {% include keybind.html name="sight-select-tads"%}.
* **FCR** - The FCR sight will sight whatever the Next-To-Shoot (NTS) target is from the FCR. It is selectable using {% include keybind.html name="sight-select-fcr"%}.

## Viewing selected sight

The selected sight can be viewed on the IHADSS symbology in the lower-left corner.

It is also visible on the WPN page.