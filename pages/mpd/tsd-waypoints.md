---
title: TSD Waypoints
tags: [mpd, tsd]
sidebar: ah64d_sidebar
permalink: mpd-tsd-waypoints.html
folder: mpd
---

**VIDEO TUTORIALS**
1. [Waypoints](https://youtu.be/OVvo2ZsPwjo?si=p__8Eyz1hNDdyPUy)
2. [Route Planning](https://youtu.be/sw4tsiR0yHk?si=HqOyfo9tOAmHIoAL)

## Waypoint operations

In the NAV mode, the player can either edit a waypoint, add a waypoint, delete a waypoint or store the current position of the helicopter as a waypoint. All this can be done via clicking on the `WPT` button on the TSD page. That will show 4 options, ADD, DEL, EDT and STO. The different operations are explained in detail below.

Target Points cannot be created in the NAV mode of the TSD.

### Adding a waypoint (ADD)

1. The player has to selet the type of identification group for the waypoint. There are 3 choices, 
    1. WP
    2. HZ
    3. CM

To enter the details of the waypoint the player will need to use the KU. To start using the KU, the player will need to press the `IDENT` button. There are 4 text fields which will be present on the KU for population by the player.
1. IDENT : Identification or Type of waypoint depending upon the IDENT group selected on the TSD page. The possible IDENTS are defined [here](./mpd-dms).
2. FREE : Maximum of 3 letters for the waypoint. Used to describe the waypoint. Advised not to leave blank.
3. GRID : 8 digit grid reference for the waypoint
4. ALTITUDE : Height of the waypoint above MSL.

### Edit a waypoint (EDT)

This sub-mode is similar to the ADD submode, the main difference being the player has to select the waypoint to edit first and then change either the free text, grid reference or height above MSL.

1. Click on the POINT button for the KU to reflece POINT. Via the KU change the POINT value to the Waypoint IDENT which needs to be changed.
2. Then click on EDT for the following KU inputs from the player.
    1. FREE : Maximum of 3 letters for the waypoint. Used to describe the waypoint. Advised not to leave blank.
    2. GRID : Displays the current grid reference for the waypoint, can be changed or left as is.
    3. ALTITUDE : Displays the current height above MSL for the waypoint, can be changed or left as is.

### Deleting a waypoint (DEL)

This a simple submode which deletes a selected waypoint. The waypoint has to be selected by pressing the POINT button first and then entering the waypoint ident in the KU. After entering the waypoint press the `DEL` button which will display a sub-menu asking the player for a confirmation for deleting the waypoint, `YES` for deleting and `NO` for keeping the waypoint.

### Storing Current Position (STO)

The helicopter has the ability to store the current position of the helicopter as a waypoint via the TSD page. It only has one submenu option, `NOW`, which will upon pressing will store the current position of the helicopter as a waypoint.

### Creating a RTE(RTE)

This will allow the player to create a proper flightplan following a set of waypoints imported and/or created by the player. The RTE sub-page is accessed via the `RTE` button at the bottom of the TSD page.

It will display the following operations, ADD, DEL, DIR and RVM on the left side and END on the right side.

To add a waypoint to the route, press `ADD`, press `POINT` to enter the waypoint IDENT from the KU and then press END to add the waypoint to the route. All waypoints added to route are added serially, basically one after the other.

To delete a waypoint from the route, press `DEL` and select the waypoint from the route. This will delete the waypoint without any _confirmation message_. 

`DIR` works similar to ADD, the player can either choose a waypoint from the RTE list or enter a waypoint `IDENT` using the U after pressing `POINT`.

### Importing waypoints

To import waypoints, follow the guide present under the [DTU](/mpd-dms) page. 

## Adding Target Points (THRT)

This is similar to adding a normal waypoint in the NAV mode. This can be done from either mode. 

1. Click on `THRT` to bring up the submenu for adding, deleting, editing or storing a target point. This sub-menu is the same as the waypoint sub-menu for the NAV mode. The only difference is that the player is entering targets into the ATK database for the helicopter rather than waypoints, hazard points or control measures.
2. The possible IDENTs for the waypoints can be found [here](.mpd-dms).
3. The FREE text box, as above only takes 3 characters should be used to describe the type of threat. For example a `SA-6` site can be represented as a `SA6`. Advised not to leave blank.

## ABR
This is a sub page of the TSD page which can be accessed from the ABR button. This sub page lists all the possible identifications for a waypoint or control measure or target point along with an explanation for each identification. The identifications are also colour coded for differentiating  types of identifications for example, friendly is light blue (cyan) and enemy is red.