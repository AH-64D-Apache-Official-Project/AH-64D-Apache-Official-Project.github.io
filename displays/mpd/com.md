---
title: COM pages
lead: Laser codes. Which code your laser fires on, which one the spot tracker looks for, and which ones your SAL Hellfires are set to.
keywords: [com, code, freq, chan, laser code, prf, lrfd, lst, channel, 1688, 1111, sal, buddy lase]
seats: [PLT, CPG]
---

The aircraft keeps a table of sixteen laser codes, each with a letter **A** to **R** (there is no I or O). Everything else refers to a letter, not to the number:

- the **LRFD**, your laser rangefinder/designator, fires on one letter's code;
- the **LST**, the laser spot tracker, looks for one letter's code;
- the four **missile channels** each hold a letter, and a SAL Hellfire's primary and alternate channels are chosen on the [WPN page]({{ '/displays/mpd/wpn/' | relative_url }}#sal-missiles).

All three pages show the same table, each letter beside its button with its code. They are reached from the WPN page: `T1`{: .vab} **CHAN** and `T4`{: .vab} **CODE**. **FREQ** is on the CODE page's `T5`{: .vab}. `B1`{: .vab} returns to WPN. The **COM** button on the bezel is not simulated.

## Defaults

| | Letter | Code |
|---|---|---|
| LRFD | A | 1111 |
| LST | B | 1112 |
| Missile channel 1 (primary) | A | 1111 |
| Missile channel 2 (alternate) | B | 1112 |
| Missile channels 3 and 4 | C, D | 1113, 1114 |

Out of the box, then, your own laser and your primary Hellfire channel are both on 1111, so you can lase for your own missiles straight away. To fire for someone else's laser, or to lase for another aircraft, set the codes to match theirs.

## FREQ: setting the codes {#freq}

Press a letter's button and type its code on the [KU]({{ '/displays/ku/' | relative_url }}). A code is four digits from 1111 to 1788: the first digit 1, the second 1 to 7, the last two 1 to 8. This is the same code ACE uses for lasers, so it works with other ACE laser designators and Hellfire-type weapons.

## CODE: LRFD and LST {#code}

`T2`{: .vab} **SET** chooses what you are setting, **LRFD** or **LST**. Then press a letter: that letter's code becomes the LRFD's (or LST's) code. The boxed letter is the current one.

## CHAN: missile channels {#chan}

`T2`{: .vab} to `T5`{: .vab} choose missile channel **1** to **4**. Then press a letter to put that code on the channel. The boxed letter is the channel's current code.

> The Hellfire looks for its **primary channel's** code. The laser fires on the **LRFD's** code. Lasing for your own missile needs both to be the same letter, or two letters holding the same code.
{: .tip}
