---
title: Frequently Asked	Questions
tags: [getting_started]
sidebar: ah64d_sidebar
permalink: faq.html
folder:	root
---
## Getting Started

###	How	do I interact with cockpit switches? {#cockpit-switches}

Use	the	keybind	{% include keybind.html	name="cockpit-interact"	%} with	the	crosshair over the switches.

###	How	do I map inputs	to my HOTAS	{#hotas}
Starting with v2.1, mapping inputs to HOTAS works the same as mapping normal keyboard switches.

###	How	do I start the aircraft? {#aircraft-startup}

1. Set the Rotor Brake Switch to OFF.
2. Turn	the	Battery	Switch ON.
3. Set Eng 1 Start Switch to Start.
4. Wait	for	Ng to reach	23%.
5. Move the Power Lever to Idle (Wait until Ng stabilizes at approximately 67.9%).
6. Repeat steps 3–5 for engine	2.
7. Advance	the	Power Levers to Fly	once ENG OIL PSI reaches 70 (approximately 1 minute	after the second engine	stabilizes).

## Weapons
###	How	do I change	the	aircraft loadout/re-arm? {#rearm}
The legacy re-arming menu has been replaced with the ARMA 3 pylon system:
- In Eden: Right-click the helicopter, select Attributes, and navigate to Pylon Settings.
- In-game: Use an ammo truck or any valid Ace ammo container. Ace-interact with the aircraft to configure the pylons.
- Using Zeus Enhanced: Zeus can edit loadouts and pylons through its interface.

###	What happened to the ATAS-92 Stinger? {#stinger}
The ATAS-92 Stinger was removed due to limited open-source information. Testing integrations were initially done on the AH-64A model, but these implementations were experimental and not continued past the A model. Although later versions of the AH-64D in Japan and Korea adapted the Stinger, no detailed integration data is available.
- The system will not be re-added.
- Please refrain from sharing confidential information about these systems (This is not warthunder).

###	Why	can't I	assign weapons to the pilot? {#pilot-weapons}
- Currently, all weapons are coded for the CPG (Co-pilot/Gunner) due to ARMA’s limitations. If weapons are assigned to the PLT (Pilot), they will automatically revert to the CPG. 
- While technically possible to make weapons available to the PLT, the current system does not support it and may behave incorrectly. Proceed at your own risk—it’s unsupported. 
- Recent ARMA updates may allow for a multi-seat weapon system in the future, but this is still a long-term goal.

## Interaction
### Keyboard Unit(KU) has extra letters
1. This is a byproduct of disabling keyboard input from the user so that it can be used with the in-game KU. It is suggested to backspace at least once before inputting any other keys.

## Targeting
###	How	do I turn on the radar.	{#radar-salute}
The radar offers two modes: single scan and continuous scan.
- Continuous scan: Use ARMS's default Binding (LCTRL + R)
- Single scan: Use the mod's custom binding (LSHIFT + R)

###	How	do I zoom when using the Pilot Night Vision	System (PNVS) camera? {#pnvs-zoom}
The sensor systems on the nose of the Apache include the TADS and PNVS. The pilot only has access to the PNVS, which does not have zooming capabilities. It is solely used for flying the aircraft.

## IHADSS /	UI
###	How	do get the Helmet Display Unit (HDU)? {#attach-hdu}
The HDU is stored in a container located on the right panel, below the cockpit door handle, and just behind the COM panel. Click on the container to "attach" (turn on) the HDU.

###	My HDU has no symbology	being displayed. {#power-hdu}
The IHADSS is powered by AC and DC power. To activate it:
1. Turn on the battery.
2. Start the APU. Once the APU is powered up, the IHADSS will display symbology.

###	How	do I prevent the cursor	(green x) from moving {#headtracking-cursor-move}
The curor movement is attached to a keybind "U".
To stop the cursor from moving:
1. Go to Options > Addon Options.
2. De-select the option: "Allow cursor movement while in head-tracking mode."
or alternately if you accidentaly activating it you can unbind the keybind

## Flight model

### Will there be a separate model for SFM+/SFM/AFM
1. No, the mod will only contain HeliSim as the flight model. There are multiple uploads which have older versions, or you can build from souce via GitHub.

###	I can't	Fly	the	aircraft but the engine	page is displaying values. {#cannot-fly}
Due	to the nature of Arma inputs and how we are	handling the throttle it might need	to be set up correctly
#### HOTAS Users:
1. Bind your controls to "Collective Raise (Analog)" and "Collective Lower (Analog)."
2. Select the HOTAS FM option in Addon Options.

#### Keyboard and Mouse Users:
1. Bind your collective to the normal "Raise" and "Lower" settings.
2. Select the "Mouse" or "Keyboard" FM option in Addon Options.
Although improvements to the control input system are planned, this is the current setup.

### With HOTAS my inputs get exaggerated:
1. Reduce the sensitivity curves of your HOTAS. A recommended value is 25%. The initialisation document has a picture with the standard curves required.
