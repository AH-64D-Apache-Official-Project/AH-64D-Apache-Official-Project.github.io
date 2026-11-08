---
title: Shutdown
lead: The before landing check, the after landing check and the aircraft shutdown.
keywords: [shutdown, stop, engines off, before landing, after landing, rotor brake, battery, checklist]
seats: [PLT, CPG]
redirect_from:
  - /shutdown.html
---

{% capture P %}<span class="seat seat-plt">PLT</span>{% endcapture %}
{% capture C %}<span class="seat seat-cpg">CPG</span>{% endcapture %}
{% capture B %}<span class="seat">PLT/CPG</span>{% endcapture %}

In the following checks, {{ P }} denotes the pilot (back seat), {{ C }} the copilot/gunner (front seat), and {{ B }} both crew stations. Items marked (not simulated) are not implemented.

## Before landing check

1. {{ B }} Weapons systems – Safe:
   1. A/S button – SAFE.
   2. GND ORIDE button – OFF.
   3. Weapons not actioned in the HAD – Verify.
2. {{ B }} ASE – Safe.
3. {{ P }} TAIL WHEEL button – Locked, light off (not simulated).
4. {{ P }} PARK BRAKE – Released, handle in (not simulated).
5. {{ B }} Power – Sufficient for the approach.
{: .steps}

## After landing check

1. {{ P }} TAIL WHEEL button – As desired (not simulated).
2. {{ P }} Exterior lights – As required.
3. {{ B }} Avionics – As required (not simulated).
{: .steps}

## Aircraft shutdown

1. {{ P }} APU – Start as follows:
   1. APU button – Press.
   2. UFD – Monitor for APU advisories.
2. {{ P }} TAIL WHEEL button – Lock (not simulated).
3. {{ P }} PARK BRAKE – Set (not simulated).
4. {{ B }} NVS MODE switch – OFF.
5. {{ P }} Power levers – OFF, after the engines have cooled at IDLE for 2 minutes.
6. {{ P }} TGT – Monitor.
7. {{ P }} RTR BRK switch – BRK, below 50% Nr.
8. {{ P }} Stabilator – Set to zero (not simulated).
9. {{ P }} Searchlight – OFF.
10. {{ P }} RTR BRK switch – OFF, when the rotor stops.
11. {{ P }} EXT LT/INTR LT panel switches – OFF.
12. {{ P }} APU – OFF.
13. {{ P }} MSTR IGN switch – OFF.
{: .steps}
