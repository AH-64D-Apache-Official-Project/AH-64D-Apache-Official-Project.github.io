---
title: Radial menu
lead: One binding that opens a ring of choices for your sight, the TADS, the radar, the laser spot tracker and your symbology. Handy when you have not bound every key.
keywords: [radial menu, radial, wheel, sight select, quick menu, dwell, gamepad]
seats: [PLT, CPG]
---

Bind {% include key.html id="fza_ah64_radialMenu" %} in **AH-64D Official Project**. Press it to open the menu around the centre of your screen.

## Selecting

| With | Do |
|---|---|
| **Mouse** | Point at a sector and left-click. Right-click goes back, or closes the top menu. |
| **Stick, hat or keys** | Hold one of the **Radial Menu: Up / Down / Left / Right** bindings towards a sector. It selects after the **Stick dwell time** (0.8 s by default). |
| **The menu binding** | In a sub-menu, goes back. In the top menu, closes it. |
| **Esc** | Closes it. |

Only the direction bindings select by holding. Your aim input and head tracking never do, so looking around with the menu open is safe.

The hub in the middle shows what is currently selected; clicking it goes back, or closes the top menu. Selected items are green, items you cannot choose right now are grey.

After a selection the menu closes, unless **Keep open after selecting** is on in [Addon settings]({{ '/getting-started/settings/' | relative_url }}).

Each choice presses the same bindings you would press yourself, so everything on the [sights]({{ '/targeting/sights/' | relative_url }}), [TADS]({{ '/targeting/tads/' | relative_url }}) and [radar]({{ '/targeting/fcr/' | relative_url }}) pages applies.

## Top menu

| Where | Items |
|---|---|
| Top two thirds | The sights your crew station can select, left to right: **TADSL**, **TADS**, **HMD**, **FCR**, **FCRL**. Choosing one also sets or clears Link as needed, then opens that sight's menu. |
| Bottom third | **NVS TADS** or **NVS PNVS**: swaps your night vision sensor. Grey while your NVS mode switch is off. |

The pilot sees only HMD and, with the radar fitted, FCR.

## Sub-menus

| Menu | Top half | Bottom half |
|---|---|---|
| **TADS** (CPG) | Sensor: **DVO**, **DTV**, **FLIR**, and **LST** for the spot tracker menu | Field of view: **W**, **M**, **N**, **Z** |
| **FCR** | Mode: **GTM**, **RMAP**, **ATM**, **TPM** | Scan size: **W**, **M**, **N**, **Z** |
| **HMD** | **TRANS** or **CRUS**: the other of the two | **HVR** or **BOB**: the other of the two |
| **LST** (CPG) | **AUTO**, or **OFF** when in AUTO | **MANUAL**, or **OFF** when in MAN |

The TADS and FCR menus list only the options you can change to: the current sensor, mode or size is left out. FCR options need you to own the radar. TADS options are grey while the TADS is a night vision sensor, and the sensor choices are grey under A3 Thermal Improvement's FLIR.

> The radial menu shares a key easily with Hatchet's cockpit cursor, for example a mouse side button. When both are bound to the same press, the radial menu opens and the cursor comes back afterwards.
{: .tip}
