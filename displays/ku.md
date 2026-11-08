---
title: Keyboard unit (KU)
lead: The KU provides data entry for points, idents, grids, altitudes and laser codes.
keywords: [ku, keyboard unit, keyboard, input, type, prompt, enter, scratchpad]
seats: [PLT, CPG]
---

The KU provides data entry when adding waypoints, hazards, control measures, targets and threats, and for laser codes. When data entry is required, the KU illuminates to indicate it is ready to accept input. Data entry pushbuttons are labeled with a `>`, such as `POINT>`{: .mpd} or `IDENT>`{: .mpd}.

> While the KU is active it captures the physical keyboard until data entry is complete. Mouse and keyboard users place the aircraft in a stable condition before entering data.
{: .caution}

## Data entry

1. Data entry pushbutton – Press. The KU scratchpad displays the prompt, for example `POINT:`, with any current value.
2. KU – Interact with (**Activate Keyboard Unit**). The keyboard now enters data into the aircraft.
3. Value – Enter, then <kbd>Enter</kbd>.
{: .steps}

- <kbd>Backspace</kbd> deletes the last character.
- An invalid entry displays an error; <kbd>Enter</kbd> clears it for re-entry.
- <kbd>Esc</kbd> releases the keyboard; interacting with the KU again resumes the same prompt.
- A prompt can lead to the next: adding a point requests ident, free text, grid and altitude in turn.
- Pressing any MPD button cancels the prompt.

Letters, numbers, space and `/ - + . *` can be entered, from the number row or the numeric keypad. The scratchpad accepts up to 44 characters and displays the last 22.

## Prompts

| Prompt | Accepts |
|---|---|
| POINT | A stored point: a letter and two digits, such as `W01`, `C55` or `T03` |
| IDENT | An ident valid for the point type, such as `WP`, `LZ`, or a SAM number such as `8`. See [Points and routes]({{ '/mission/points/' | relative_url }}#idents). |
| FREE | Up to three characters |
| GRID | A map grid reference, up to eight digits |
| ALTITUDE | Whole feet, barometric |
| CODE | A laser code: four digits, first digit 1, second 1–7, last two 1–8 (1111 to 1788). See [Laser codes]({{ '/displays/mpd/code/' | relative_url }}). |
