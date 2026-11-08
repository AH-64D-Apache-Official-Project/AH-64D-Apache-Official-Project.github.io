---
title: Laser
lead: The laser rangefinder/designator (LRFD), which measures range and designates for laser-guided Hellfires, and the laser spot tracker (LST), which acquires a spot designated by another unit.
keywords: [laser, lrfd, designator, rangefinder, lase, lst, spot tracker, auto, manual, code, remote, buddy lase]
seats: [PLT, CPG]
---

The LRFD and LST are part of the TADS and point along the TADS line of sight. Their codes are set on the [laser code pages]({{ '/displays/mpd/code/' | relative_url }}).

## Laser rangefinder/designator (LRFD)

{% include key.html id="fza_ah64_laserDesig" %} fires the laser while held.

The laser fires only when:

- the aircraft is armed (A/S at ARM; see [Weapon action switch]({{ '/weapons/was/' | relative_url }}));
- AC power is available;
- the laser spot tracker is off; and
- for the CPG, the TADS is the selected sight.

The pilot can also fire the laser, along the TADS line of sight.

While lasing, the laser is the crew station's [range source]({{ '/targeting/sights/' | relative_url }}#range): the HAD displays the range preceded by `*`, for example `*3420`{: .mpd}. Ranges below 500 m are not displayed. When lasing stops, the last range is retained.

The laser fires on the LRFD code, and designates for any ACE laser-guided weapon on that code, from this or another aircraft.

> The LRFD is a designator: any weapon on the LRFD code guides on the spot.
{: .warning}

## Laser spot tracker (LST)

The LST is a CPG function. It searches for a laser spot on the LST code from another designator, such as a ground team or another aircraft, and slews the TADS onto it.

| Binding | Mode |
|---|---|
| {% include key.html id="fza_ah64_lstAuto" %} | AUTO: searches and, with no spot in view, scans the TADS for one |
| {% include key.html id="fza_ah64_lstManual" %} | MAN: searches along the TADS line of sight only |
| {% include key.html id="fza_ah64_lstOff" %} | OFF: returns control of the TADS |

Operation:

- The LST searches a 5° cone about the TADS line of sight, to 8 km, ten times per second.
- On detecting a spot, it tracks it and drives the TADS onto it. A spot not detected for one second is dropped, and the LST resumes searching.
- In AUTO with no spot, it scans the TADS 30° either side of the nose in four bars, 10° apart, from 5° above the horizon downward.
- The LST ignores the aircraft's own laser.

With the LST armed in either mode, the aircraft's own laser is inhibited; the two cannot operate together.

The LST does not operate without AC power, with the TADS turret or DTV damaged, or while the TADS is a night vision sensor.

## Messages

| HAD | Meaning |
|---|---|
| `LRFD CODE ?`{: .mpd} | LRFD set to a code letter with no code |
| `LST CODE ?`{: .mpd} | LST set to a code letter with no code |
| `REMOTE`{: .mpd} | Missiles actioned with the priority missile channel code different from the LRFD code: the missile guides on another designator |
| `LASE nn TRGT`{: .mpd} | A SAL Hellfire fired LOAL requires the target lased now, with *nn* seconds to impact. See [AGM-114 Hellfire]({{ '/weapons/hellfire/' | relative_url }}) |

## Coordination with other units

- **Designating for another unit**: the LRFD code is set to the code of that unit's weapon.
- **Engaging on another unit's designation**: the Hellfire priority channel is set to that unit's code. For the TADS to acquire the spot, the LST code is set to it and the LST armed.

With the default codes, the LRFD and the priority missile channel are both 1111, and the aircraft designates for its own missiles.
