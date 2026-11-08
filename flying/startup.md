---
title: Start-up
lead: The normal procedures from the interior check to the before takeoff check.
keywords: [startup, start, interior check, apu, battery, fire test, engine, power lever, idle, fly, rotor brake, rotor lock, before takeoff, checklist, abort]
seats: [PLT, CPG]
redirect_from:
  - /startup.html
---

{% capture P %}<span class="seat seat-plt">PLT</span>{% endcapture %}
{% capture C %}<span class="seat seat-cpg">CPG</span>{% endcapture %}
{% capture B %}<span class="seat">PLT/CPG</span>{% endcapture %}

In the following checks, {{ P }} denotes the pilot (back seat), {{ C }} the copilot/gunner (front seat), and {{ B }} both crew stations. Items marked (not simulated) are not implemented.

## Interior check

1. {{ P }} RTR BRK switch – OFF.
2. {{ B }} HDU – On.
{: .steps}

## Before starting APU

1. {{ P }} MSTR IGN switch – BATT.
2. {{ P }} Searchlight – As required.
3. {{ P }} TAIL WHEEL button – Lock (not simulated).
4. FIRE DET/EXTG panel TEST switch – Test as follows:
   1. {{ P }} Position 1 – MSTR WARN, ENG 1, APU and ENG 2 FIRE buttons are illuminated, a DECK FIRE warning is displayed on the UFD and the voice warning system is activated.
   2. {{ C }} Position 2 – MSTR WARN, ENG 1, APU and ENG 2 FIRE and DISCH buttons are illuminated, a DECK FIRE warning is displayed on the UFD and the voice warning system is activated.
{: .steps}

## Starting APU

1. Fire guard (if available) – Posted.
2. {{ P }} APU exhaust area – Clear.
3. {{ P }} APU – Start as follows:
   1. APU button – Press and release.
   2. UFD – Monitor for APU advisories.
{: .steps}

## After starting APU

Not simulated.

## Before starting engines

1. {{ B }} NVS MODE switch – As desired.
2. {{ P }} Control sweep and trim check – Perform.
{: .steps}

## Starting engines

1. {{ P }} Area – Clear.
2. Fire guard (if available) – Posted.
3. {{ P }} RTR BRK switch – OFF or LOCK.
4. {{ P }} EXT LT – As required.
5. {{ P }} First engine – Start as follows:
   1. ENG START switch – START.
   2. Power lever – IDLE, at first indication of Ng increase.
   3. Engine oil PSI – Monitor.
   4. TGT – Monitor.
   5. Ng – Monitor.
   6. MSTR WARN, MSTR CAUT and UFD – Monitor.
6. {{ P }} Second engine – Start as for the first engine.
7. {{ P }} RTR BRK switch – OFF.
8. {{ P }} Power levers – Advance both power levers smoothly to FLY and ensure that both torque indications increase simultaneously.
9. {{ P }} Np and Nr – Verify 101%.
10. {{ P }} MSTR WARN, MSTR CAUT and UFD – Monitor.
11. {{ P }} APU – Off.
{: .steps}

> With the rotor brake in the LOCK position, a rotor lock start may be performed; with the rotor brake in LOCK, there is no increase in Np or Nr.
{: .note}

### Abort start {#aborting-a-start}

1. Power lever (affected engine) – OFF.
2. ENG START switch (affected engine) – IGN ORIDE for 30 seconds and until TGT is below 540 °C.
{: .steps}

## Before taxi check

Not simulated.

## Taxi check

Not simulated.

## Before takeoff check

1. {{ B }} Weapons subsystem – Check as follows:
   1. A/S button – SAFE.
   2. GND ORIDE button – OFF.
   3. Weapons not actioned – Verify.
2. {{ P }} TAIL WHEEL button – Lock (not simulated).
3. {{ P }} PARK BRAKE – As desired (not simulated).
4. {{ P }} Power levers – FLY.
5. {{ B }} Systems – Check as follows:
   1. FUEL page options – As desired.
   2. Fuel quantity – Check.
   3. UFD – Check.
   4. Engine and flight instruments – Check.
   5. ASE – As required.
   6. Avionics – As desired:
      1. Transponder – As desired (not simulated).
      2. COMM – As desired (not simulated).
      3. NAV – As desired.
6. {{ B }} Power check – Perform; validate the PERF page (not simulated).
{: .steps}

The before landing, after landing and shutdown checks are given in [Shutdown]({{ '/flying/shutdown/' | relative_url }}).
