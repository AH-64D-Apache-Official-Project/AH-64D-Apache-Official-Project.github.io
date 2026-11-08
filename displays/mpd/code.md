---
title: Laser codes (CODE, CHAN and FREQ pages)
lead: The laser code table, the codes used by the LRFD and LST, and the missile channels used by SAL Hellfires.
keywords: [code, freq, chan, laser code, prf, lrfd, lst, channel, 1688, 1111, sal, buddy lase]
seats: [PLT, CPG]
---

The aircraft holds a table of sixteen laser codes, each identified by a letter from A to R (excluding I and O). The laser systems refer to a letter, not to the code number:

- the **LRFD** (laser rangefinder/designator) fires on one letter's code;
- the **LST** (laser spot tracker) searches for one letter's code;
- the four **missile channels** each hold a letter; a SAL Hellfire's priority and alternate channels are selected on the [WPN page]({{ '/displays/mpd/wpn/' | relative_url }}#sal-missiles).

The three pages present the same 16 code buttons, each with its letter and code. They are selected from the WPN page: `T1`{: .vab} CHAN and `T4`{: .vab} CODE. The FREQ page is selected from the CODE page, `T5`{: .vab}. `B1`{: .vab} returns to the WPN page.

## Defaults

| | Letter | Code |
|---|---|---|
| LRFD | A | 1111 |
| LST | B | 1112 |
| Missile channel 1 (priority) | A | 1111 |
| Missile channel 2 (alternate) | B | 1112 |
| Missile channels 3 and 4 | C, D | 1113, 1114 |

With the defaults, the LRFD and the priority missile channel are both on 1111, and the aircraft designates for its own missiles. For a remote designation, or to designate for another aircraft, the codes are set to match.

## FREQ: setting the codes {#freq}

A code button is pressed and its code entered on the [KU]({{ '/displays/ku/' | relative_url }}). A code is four digits from 1111 to 1788: first digit 1, second digit 1 to 7, last two digits 1 to 8. The codes are the ACE laser codes and operate with other ACE laser designators and laser-guided weapons.

## CODE: LRFD and LST {#code}

`T2`{: .vab} SET selects LRFD or LST. Pressing a code button then sets that code as the LRFD (or LST) code. The current letter is boxed.

## CHAN: missile channels {#chan}

The CHANNEL buttons, `T2`{: .vab} to `T5`{: .vab}, select missile channel 1 to 4. Pressing a code button then sets that code on the channel. The channel's current letter is boxed.

> The Hellfire guides on its priority channel's code; the laser fires on the LRFD code. Designating for the aircraft's own missile requires the same letter, or two letters holding the same code.
{: .note}
