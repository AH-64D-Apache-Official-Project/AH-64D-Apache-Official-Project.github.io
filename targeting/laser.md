---
title: Laser
lead: The TADS carries a laser rangefinder/designator, to measure range and guide laser Hellfires, and a laser spot tracker, to find a spot someone else is lasing.
keywords: [laser, lrfd, designator, rangefinder, lase, lst, spot tracker, auto, manual, code, remote, buddy lase]
seats: [PLT, CPG]
---

Both are part of the TADS turret, so they point wherever the TADS points. Their codes are set on the [COM pages]({{ '/displays/mpd/com/' | relative_url }}).

## Laser rangefinder/designator (LRFD)

Hold {% include key.html id="fza_ah64_laserDesig" %} to fire the laser. It stops when you let go.

It fires only when:

- the aircraft is **armed** (ARM/SAFE at ARM, see [Weapon action switch]({{ '/weapons/was/' | relative_url }})),
- there is AC power,
- the laser spot tracker is **off**, and
- for the CPG, the TADS is the selected sight.

The pilot can also fire it, wherever the TADS is pointing.

While you lase, the laser becomes your [range source]({{ '/targeting/sights/' | relative_url }}#range): the HAD shows the range with a `*` in front, for example `*3420`{: .mpd}. Ranges under 500 m are not shown. After you stop, the last range stays.

The laser fires on the **LRFD code**. It designates for any ACE laser-guided weapon on that code, yours or another aircraft's.

> The laser is a designator, not just a rangefinder: anyone with a weapon on your code can guide on your spot. Lase only what you want hit.
{: .warning}

## Laser spot tracker (LST)

The LST is the CPG's. It looks for a laser spot on the **LST code** made by someone else, such as a ground team or another aircraft, and turns the TADS onto it.

| Binding | Mode |
|---|---|
| {% include key.html id="fza_ah64_lstAuto" %} | **AUTO**: searches, and if there is no spot in view, scans the TADS for one. |
| {% include key.html id="fza_ah64_lstManual" %} | **MAN**: searches only where you point the TADS. |
| {% include key.html id="fza_ah64_lstOff" %} | **OFF**: gives the TADS back. |

How it works:

- It searches a 5° cone around the TADS line of sight, out to 8 km, ten times a second.
- When it finds a spot it **tracks** it, driving the TADS onto it. It loses a spot that has not been seen for a second and goes back to searching.
- In AUTO with no spot, it scans the TADS 30° either side of the nose in four bars, 10° apart, from 5° above the horizon down.
- It ignores your own aircraft's laser.

Arming the LST, in either mode, stops your own laser: the two cannot work at once.

The tracker's status shows in the centre of your helmet symbology, just above the HAD lines: `LST SEARCH`{: .mpd}, `LST AUTO SEARCH`{: .mpd}, `LST TRACK`{: .mpd}. `LST FAIL`{: .mpd} means it is armed but the TADS turret or day TV is damaged. It does not work without AC power, or while the TADS is a night vision sensor.

## Messages

| HAD | Meaning |
|---|---|
| `RFDCODE?`{: .mpd} | The LRFD is set to a letter with no code. |
| `LSTCODE?`{: .mpd} | The LST is set to a letter with no code. |
| `REMOTE`{: .mpd} | Missiles are actioned and the primary channel's code differs from your LRFD code: your Hellfire will guide on someone else's laser. |
| `LASE nn TRGT`{: .mpd} | A laser Hellfire fired lock-on after launch needs the target lased now, with *nn* seconds to impact. See [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}). |

## Working with other units

- **Lasing for someone else**: set your LRFD code to the code their weapon uses.
- **Firing on someone else's laser**: set your Hellfire's primary channel to their code. To have the TADS find their spot, set the LST code to it too and arm the LST.

The defaults put your LRFD and primary missile channel on the same code (1111), so out of the box you lase for your own missiles.
