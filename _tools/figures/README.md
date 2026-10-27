# Figure tools

These scripts draw the manual's MPD and IHADSS figures from the mod's own source, so the pictures match what the aircraft shows.

- **MPD pages** are rendered from the mod's MFD config. The config is preprocessed with `pcpp`, parsed, and drawn to SVG in the BMK font, then set in the cockpit's MPD bezel texture.
- **IHADSS pages** run the mod's own HTML symbology code in headless Chromium, with flight data from the figure's spec.

Each figure is described by `_data/figures/<id>.yml`: its title, caption, the page state to draw, and the numbered callouts. The build writes `_includes/figures/<id>.svg`, and IHADSS figures also write `assets/figures/hud/<id>.png`. Pages include a figure with `{% include fig.html id="<id>" %}`.

## Requirements

- Python 3 with `pcpp`, `PyYAML` and `Pillow` (`pip install pcpp pyyaml pillow`)
- Node with Playwright and its Chromium (`npm i -g playwright && npx playwright install chromium`)
- A checkout of the AH-64D mod at the commit being documented

## Use

```
export FM_MOD=/path/to/AH-64D          # the mod checkout
cd _tools/figures
python build_figs.py                   # every figure
python build_figs.py mpd-fuel mpd-eng  # just these
```

The first run preprocesses and parses the MPD config, which takes a minute or two. The result is cached in `_tools/figures/.cache/`. Delete that folder after changing `FM_MOD` to another commit.

## Writing a figure spec

```yaml
title: FUEL page
kind: mpd                  # mpd or hud
caption: FUEL page in flight, both engines feeding.
state:                     # mpd: which page, and the MFD user values and texts the page's draw script would set
  page: FUEL               # MPD_PAGE_<page> in mfdConstants.h
  u: { MFD_IND_FUEL_CROSSFEED: 2 }
  t: { MFD_TEXT_IND_FUEL_FWD: "1580" }
  src: { heading: 312 }    # engine sources: heading, altitudeAGL, horizonBank, horizonDive, speed
  pylons: { 5: fza_agm114k_base }  # WPN page: the magazine class (from the MPD addon's CfgMagazines) on each pylon
callouts:
  - { n: 1, x: 558, y: 214, side: r, label: Forward cell, text: "Fuel in the forward cell, in pounds." }
```

Callout `x`/`y` are page units (0–1000 across the screen). Point anywhere inside the element; the build moves the end of the line to the element's edge on the `side` its badge is on (`l`, `r`, `t` or `b`). Add `snap: false` to leave a point where it is.

`labels.py states.json name` lists the text drawn next to each button for a page state, which helps when writing a button table. `run.py states.json name` renders a state on its own, without the bezel, to `.cache/out/`.
