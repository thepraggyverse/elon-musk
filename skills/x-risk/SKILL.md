---
name: x-risk
description: "Review systemic and civilization-scale risks including AI alignment, regulation drag, war, energy, population decline, asteroids, and fragile infrastructure. Use for AI systems, safety reviews, policy, critical infrastructure, long-lived companies, and plans with broad downside."
---

# X Risk

Use this skill to look beyond local success and inspect downside that can compound across systems.

## Covers

- Misaligned artificial superintelligence.
- Regulation accumulation and bureaucracy drag.
- War and fragile civilization.
- Unsustainable energy.
- Population collapse.
- Asteroids and other low-frequency, high-impact risks.
- Worry enough to make the bad outcome self-unfulfilling.
- Important work does not excuse preventable harm.

## Workflow

1. Define the system and time horizon.
2. List catastrophic, systemic, and slow-burn risks.
3. Separate real risk from vague anxiety.
4. Identify regulation, energy, demographic, safety, AI, infrastructure, and dependency exposures.
5. Identify who receives the benefit and who bears each downside.
6. Define prevention, containment, monitoring, rollback, recovery, and independent-review needs.
7. Set release gates and explicit stop conditions before proceeding.
8. Decide `proceed`, `proceed with gates`, `limit or sandbox`, `pause for evidence`, or `do not proceed`.

## Stop-Worthy Conditions

Recommend pause or stop when credible harm could be irreversible, controls are untested, affected parties cannot meaningfully consent, monitoring cannot detect failure in time, rollback is unrealistic, law or policy forbids the action, or evidence is too weak to bound the risk.
Do not frame safeguards as bureaucracy merely because they slow delivery.
Do not let pressure for progress override a stop-worthy condition.

## Output

```text
Risk Review:
System:
Time horizon:
Major risks:
Slow-burn risks:
Who bears the downside:
Mitigations:
Monitors:
Independent review:
Release gates:
Stop conditions:
Decision: proceed / gated / sandbox / pause / do not proceed
```

## Completion Gate

Complete only when affected parties, credible downside, prevention and containment, monitoring, rollback, independent review, release gates, stop conditions, and a decision are explicit.

## Example

Use `x-risk` before shipping an autonomous agent: "What failure modes matter beyond the demo?"
