---
title: Keybind reference
lead: Every binding the mod adds, with its default, and the game bindings the Apache takes over.
keywords: [keybinds, bindings, controls, keys, defaults, hotas, cockpit controls, keyboard, reference]
---

Bindings are in **Options → Controls**. For which to set up first, and the cockpit cursor and flight controls, see [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}).

## AH-64D Official Project

{% assign groups = "Sights|Night vision|IHADSS|TADS|Laser|Fire control radar|Weapons|Countermeasures|Radial menu" | split: "|" -%}
{%- for g in groups %}
### {{ g }}

<div class="table-wrap"><table>
<thead><tr><th>Binding</th><th>Default</th><th>What it does</th></tr></thead>
<tbody>
{%- for pair in site.data.keybinds -%}{%- assign k = pair[1] -%}{%- if k.group == g %}
<tr><td><b>{{ k.name }}</b></td><td style="white-space:nowrap">{% if k.keys %}{% for key in k.keys %}<kbd>{{ key }}</kbd>{% unless forloop.last %}+{% endunless %}{% endfor %}{% else %}unbound{% endif %}</td><td>{{ k.desc }}</td></tr>
{%- endif -%}{%- endfor %}
</tbody></table></div>
{% endfor %}

## AH-64D MPD Minigames

<div class="table-wrap"><table>
<thead><tr><th>Binding</th><th>Default</th><th>What it does</th></tr></thead>
<tbody>
{%- for pair in site.data.keybinds -%}{%- assign k = pair[1] -%}{%- if k.group == "MPD games" %}
<tr><td><b>{{ k.name }}</b></td><td style="white-space:nowrap">{% if k.keys %}{% for key in k.keys %}<kbd>{{ key }}</kbd>{% unless forloop.last %}+{% endunless %}{% endfor %}{% else %}unbound{% endif %}</td><td>{{ k.desc }}</td></tr>
{%- endif -%}{%- endfor %}
</tbody></table></div>

See [MPD games]({{ '/displays/mpd/games/' | relative_url }}).

## Game bindings the Apache uses

These are Arma's own bindings, in their usual categories. In the Apache they do this:

<div class="table-wrap"><table>
<thead><tr><th>Binding</th><th>What it does in the Apache</th></tr></thead>
<tbody>
{%- for pair in site.data.keybinds -%}{%- assign k = pair[1] -%}{%- if k.group == "Game controls" %}
<tr><td><b>{{ k.name }}</b></td><td>{{ k.desc }}</td></tr>
{%- endif -%}{%- endfor %}
</tbody></table></div>

## Cockpit controls

**AH-64D Official Project: Cockpit Controls** has a binding for each of these, named `system: control`, such as `left mpd: left mpd t1`. All are unbound by default.

| System | Bindings |
|---|---|
| **Left MPD**, **Right MPD** | Every button: `L1`–`L6`, `R1`–`R6`, `T1`–`T6`, `B1`/MENU–`B6`, and the FCR, WPN, TSD, A/C and VID page buttons. |
| **Engine panel** | APU, battery, rotor brake; each engine's start switch, and its power lever to OFF, IDLE or FLY. |
| **Fire panel** | Select engine 1, the APU or engine 2; discharge the primary or reserve bottle; test. |
| **Armament panel** | ARM/SAFE, ground override. |
| **Warning/caution panel** | Acknowledge master caution, master warning. |
| **Others** | Emergency hydraulics, NVS mode, floodlight, anti-collision light, keyboard unit, monocle, canopy door. |

**AH-64D HeliSim Cockpit Controls** has one binding per switch position, for switch panels: **Battery** Off and On, **APU** Off and On, each **Engine Start** switch at Ignition Override, Off and Start, the **Rotor Brake** at Off, Brake and Lock, and each **Power Lever** at Off, Idle and Fly.

The flight controls are in **HeliSim Flight Controls**; see [Controls and bindings]({{ '/getting-started/controls/' | relative_url }}#2-flying).
