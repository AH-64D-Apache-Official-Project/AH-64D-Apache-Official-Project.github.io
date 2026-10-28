# Figure tools

These scripts draw the manual's MPD and IHADSS figures from the mod's own source, so the pictures match what the aircraft shows.

- **MPD pages** are rendered from the mod's MFD config. The config is preprocessed with `pcpp`, parsed, and drawn to SVG in the BMK font, then set in the cockpit's MPD bezel texture.
- **IHADSS pages** run the mod's own HTML symbology code in headless Chromium, with flight data from the figure's spec.

Each figure is described by `_data/figures/<id>.yml`: its title, caption, the page state to draw, and the numbered callouts. The build writes `_includes/figures/<id>.svg`, and IHADSS figures also write `assets/figures/hud/<id>.png`. Pages include a figure with `{% include fig.html id="<id>" %}`.

## Requirements

- Python 3 with `pcpp`, `PyYAML` and `Pillow` (`pip install pcpp pyyaml pillow`)
- Node with Playwright and its Chromium (`npm i -g playwright && npx playwright install chromium`). To use an installed Chrome instead, set `FM_CHROME_CHANNEL=chrome`. With a global install, set `NODE_PATH` to the global `node_modules` folder.
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

Two layers the game draws over a page can be added to `state`:

```yaml
  tsd:                       # TSD points and lines (fza_mpd_fnc_uiDrawPoint, fza_mpd_fnc_pageTSDDrawCanvas)
    scale: 10000             # the TSD scale in metres
    lines: [[[-240, -2000], [500, 4630]]]           # metres from the aircraft, x right and y ahead
    points:
      - { ident: WP, id: 2, at: [500, 4630] }       # icon, size, colour and labels come from FzaIconTypes
      - { ident: AE, id: 57, text: T72, at: [3300, 7300] }
  video: { hd: true, fmt: wpn, ... }                # VIDEO page: an IHADSS model, drawn as the page's symbology layer
```

Callout `x`/`y` are page units (0–1000 across the screen). Point anywhere inside the element; the build moves the end of the line to the element's edge on the `side` its badge is on (`l`, `r`, `t` or `b`). Add `snap: false` to leave a point where it is.

## Writing an IHADSS figure spec

```yaml
title: IHADSS hover symbology
kind: hud
caption: Pilot's hover symbology at 40 ft.
crop: [30, -30, 640, 510]  # format units shown: x0, y0, x1, y1. Heads up needs this wider crop; the default suits heads down
model:                     # the JSON the page's fzaIhadss.update() takes; fza_ihadss_fnc_htmlModel builds it in game
  hd: false                # false: heads up, spread layout, clipped to the lens
  white: false
  fmt: flt                 # flt or wpn
  mode: hover              # trans, cruise, hover, bobup
  vel: [1.5, 2.5]
  forFov: [-10, -4]
  had: [P-HMD, "1.5", "", TADS, "", "", "", ""]
symbols:                   # symbols the game draws natively over the page, in format units
  - { sym: headtracker, x: 480, y: 176 }
callouts:
  - { n: 1, x: 350, y: 193, side: l, label: Velocity vector, text: "Drift over the ground." }
```

The format is 640 × 480 units, 16 to the degree, with the reticle at 320, 240. Callout `x`/`y` are format units. `symbols` takes `headtracker`, `fpv`, `flyto`, `cuedlos` and the `rkt` cursors from `hud_symbols/`, or an icon path under `assets/icons/` such as `fcr/mpd/nts`. Place them where the game would: the head tracker is the aircraft's nose seen from where `forFov` says the head points, and so on. A world symbol outside the format or the lens is not drawn in game, so leave it out.

## Icons

`python icons.py tsd` and `python icons.py fcr` convert the MPD's TSD and FCR symbol textures to the PNGs in `assets/icons/`. Re-running rewrites the files even when nothing changed, so only commit the ones you meant to change.

`labels.py states.json name` lists the text drawn next to each button for a page state, which helps when writing a button table. `run.py states.json name` renders a state on its own, without the bezel, to `.cache/out/`.
