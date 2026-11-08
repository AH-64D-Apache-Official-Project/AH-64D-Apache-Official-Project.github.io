---
title: Radial menu
lead: Mod feature. A single binding that opens a ring of selections for the sight, TADS, radar, laser spot tracker and symbology.
keywords: [radial menu, radial, wheel, sight select, quick menu, dwell, gamepad]
seats: [PLT, CPG]
---

The radial menu is bound with {% include key.html id="fza_ah64_radialMenu" %} in **AH-64D Official Project**. It opens around the center of the screen.

## Selection

| Input | Function |
|---|---|
| Mouse | Point at a sector and left-click. Right-click returns, or closes the top menu. |
| Stick, hat or keys | Hold a **Radial Menu: Up / Down / Left / Right** binding toward a sector. The sector is selected after the **Stick dwell time** (0.8 s default). |
| Menu binding | In a sub-menu, returns; in the top menu, closes it. |
| Esc | Closes the menu. |

Only the direction bindings select by holding. The aim input and head tracking do not select, so the view can be moved with the menu open.

The hub in the center displays the current selection; selecting it returns, or closes the top menu. Selected items are green; items not currently available are gray.

The menu closes after a selection unless **Keep open after selecting** is on in [Addon settings]({{ '/getting-started/settings/' | relative_url }}).

Each item operates the same binding as the corresponding control; the [sights]({{ '/targeting/sights/' | relative_url }}), [TADS]({{ '/targeting/tads/' | relative_url }}) and [radar]({{ '/targeting/fcr/' | relative_url }}) pages apply.

## Top menu

| Position | Items |
|---|---|
| Top two thirds | The sights available to the crew station, left to right: TADSL, TADS, HMD, FCR, FCRL. Selecting one also sets or clears Link as required, then opens that sight's menu. |
| Bottom third | NVS TADS or NVS PNVS: exchanges the night vision sensor. Gray with the NVS MODE switch OFF. |

The pilot's menu contains HMD and, with the radar installed, FCR.

## Sub-menus

| Menu | Top half | Bottom half |
|---|---|---|
| TADS (CPG) | Sensor: DVO, DTV, FLIR, and LST for the spot tracker menu | Field of view: W, M, N, Z |
| FCR | Mode: GTM, RMAP, ATM, TPM | Scan size: W, M, N, Z |
| HMD | TRANS or CRUS (the other of the two) | HVR or BOB (the other of the two) |
| LST (CPG) | AUTO, or OFF when in AUTO | MANUAL, or OFF when in MAN |

The TADS and FCR menus list only the options that can be changed to; the current sensor, mode or size is omitted. FCR options require ownership of the radar. TADS options are gray while the TADS is a night vision sensor, and the sensor options are gray under the A3 Thermal Improvement FLIR.

> The radial menu can share a binding with the Hatchet cockpit cursor, for example a mouse side button. With both bound to the same input, the radial menu opens and the cursor is restored afterward.
{: .note}
