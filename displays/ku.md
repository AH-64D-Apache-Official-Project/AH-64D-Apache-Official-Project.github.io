---
title: Keyboard unit
lead: The keyboard on the front panel, beside the left MPD. Whenever a page asks you to type something, you type it here, on your own keyboard.
keywords: [ku, keyboard unit, keyboard, input, type, prompt, enter, scratchpad]
seats: [PLT, CPG]
---

The KU is how you type into the aircraft: point names, idents, grids, altitudes, laser codes. Buttons that open a prompt have a `>` after their label, such as `POINT>`{: .mpd} or `IDENT>`{: .mpd}.

## Typing

1. Press a button with a `>`. The KU's display shows the prompt, for example `POINT:`, with any current value already filled in.
2. Click the middle of the KU (**Activate Keyboard Unit**). From now on your keyboard types into the aircraft.
3. Type the value, then press <kbd>Enter</kbd>.
{: .steps}

- <kbd>Backspace</kbd> deletes the last character.
- If the aircraft cannot use what you typed, the display shows an error. Press <kbd>Enter</kbd> to clear it and type again.
- <kbd>Esc</kbd> stops the KU taking your keyboard, so your keys fly the aircraft again. Click the KU again to carry on with the same prompt.
- A prompt can lead to the next one. Adding a point asks for its ident, free text, grid and altitude in turn.
- Pressing any MPD button cancels the prompt.

Letters, numbers, space, and `/ - + . *` can be typed. Up to 44 characters fit; the display shows the last 22.

> Use the number keys along the top of your keyboard. The numeric keypad does not type digits correctly.
{: .caution}

> While the KU has your keyboard, your normal key bindings do nothing for the keys it uses. If the aircraft stops responding to your keys, press <kbd>Esc</kbd>.
{: .tip}

## What the prompts accept

| Prompt | Accepts |
|---|---|
| **POINT** | A stored point: a letter and two digits, such as `W01`, `C55` or `T03`. |
| **IDENT** | An ident that suits the point type, such as `WP`, `LZ`, or a SAM number such as `8`. See [Points and routes]({{ '/mission/points/' | relative_url }}#idents). |
| **FREE** | Up to three characters, anything. |
| **GRID** | A map grid reference, up to eight digits. |
| **ALTITUDE** | Whole feet, as your barometric altimeter reads. |
| **CODE** | A laser code: four digits starting with 1, the second 1–7 and the last two 1–8 (1111 to 1788). See [COM pages]({{ '/displays/mpd/com/' | relative_url }}). |
