---
title: Contributing to the docs
lead: How this manual is built, the conventions its pages follow, and how to draw a figure.
keywords: [contributing, docs, documentation, jekyll, markdown, figures, pull request, conventions]
redirect_from:
  - /dev-docs-contributing.html
---

The manual lives in its own [GitHub repository]({{ site.links.docs_repo }}). GitHub Pages builds the site from the `master` branch with Jekyll. To contribute, fork the repository, make your changes on a branch, and open a pull request against `master`.

## What to write

- **Describe the mod as it is.** Write about the current `master` of the [mod]({{ site.links.github }}), and check what you write against its code. If the code cannot confirm something, leave it out.
- **Write for players.** Plain words, short sentences, "you" for the reader. Say what a control does and when you would use it.
- **Say what is missing.** A button that the aircraft shows but the mod does not simulate gets "not simulated", nothing more.
- Describe things in your own words rather than quoting outside publications.

## Building it locally

With Docker, from the repository folder:

```
docker run --rm -v "$PWD:/srv/jekyll" jekyll/jekyll:pages jekyll build
python -m http.server 4000 --directory _site
```

Then open `http://localhost:4000`. Move `Gemfile` and `Gemfile.lock` aside while the build runs; the image brings its own GitHub Pages gems.

## Writing a page

Pages are Markdown in the folder of their section, such as `weapons/cannon.md`. Each starts with front matter:

```yaml
---
title: M230 cannon
lead: One sentence under the title.
keywords: [words, the, search, should, match]
seats: [PLT, CPG]          # the crew stations it applies to
redirect_from:
  - /weapons-m230.html     # an old address that should land here
---
```

Add the page to the menu in `_data/nav.yml`.

| To show | Write |
|---|---|
| A key binding | `{% raw %}{% include key.html id="fza_ah64_wasGun" %}{% endraw %}`. The bindings are in `_data/keybinds.yml`; Arma's own have `vanilla: true`. |
| An MPD button | `` `L3`{: .vab} `` |
| Text on a display | `` `FUEL`{: .mpd} `` |
| A procedure | A numbered list followed by `{: .steps}` |
| A tip, note, caution or warning | A blockquote followed by `{: .tip}`, `{: .note}`, `{: .caution}` or `{: .warning}` |
| A wide table | Wrapped in `<div class="table-wrap" markdown="1">` and `</div>`, with blank lines inside |
| The UFD | `<div class="ufd"><pre>...</pre></div>` |
| A figure | `{% raw %}{% include fig.html id="mpd-fuel" %}{% endraw %}` |

Links to other pages and images go through `relative_url`:

```
{% raw %}[TADS]({{ '/targeting/tads/' | relative_url }})
<img class="sym" src="{{ '/assets/icons/fcr/mpd/nts.png' | relative_url }}" alt="Next to shoot">{% endraw %}
```

A heading gets an anchor from its text, or set one with `## Heading {#id}`. Inside a table cell or list item, `{#id}` does not work: use `<span id="id"></span>`. An include used in a table cell must not end with a line break.

## Figures

The MPD and IHADSS figures are drawn from the mod's own source by the scripts in `_tools/figures`, so they match what the aircraft shows. Each figure is a spec in `_data/figures/<id>.yml` with its page state, caption and numbered callouts; the build writes the picture to `_includes/figures/`. The callout lines stop at the edge of what they point to.

See `_tools/figures/README.md` for what to install and how to write a spec. Rebuild only the figures you change: rebuilding the others moves their callouts by a pixel or two.

## Developer pages

The [developer pages]({{ '/developer/guidelines/' | relative_url }}) are archived from the 2.x manual. Each says at the top which parts no longer match the mod.
