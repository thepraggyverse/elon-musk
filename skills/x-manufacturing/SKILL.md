---
name: x-manufacturing
description: "Review production paths by treating the factory, delivery pipeline, operations process, or build system as the product. Use for manufacturing, software delivery, support, fulfillment, data pipelines, deployment flows, and any system where throughput, quality, constraints, suppliers, or rework matter."
---

# X Manufacturing

Use this skill when success depends on making the thing repeatedly, cheaply, quickly, and reliably.

## Covers

- Make real things: without production, supply does not exist.
- The real work is production, not only design.
- The factory is the product.
- Use twice-speed throughput as a capacity lens.
- Attack the bottleneck that controls the whole rate.
- Manufacturing is the moat.
- A supplier bottleneck or dependency can set the whole rate.
- Compete through speed, quality, and cost.

## Workflow

1. Map inputs, parts, tools, people, queues, inspections, rework, and outputs.
2. Identify the single constraint that limits throughput.
3. Find supplier, dependency, setup, tolerance, or quality bottlenecks.
4. Delete unnecessary parts, variants, steps, and checks.
5. Simplify the production path before automating.
6. Measure the experiment against throughput, speed, quality, and cost.
7. Choose the next throughput experiment.

## Output

```text
Manufacturing Review:
Production path:
Constraint:
Supplier/dependency risks:
Delete candidates:
Simplified path:
Quality/cost guardrails:
Throughput experiment:
```

## Completion Gate

Complete only when the end-to-end production path, active constraint, dependency risk, deletion candidates, quality and cost guardrails, and next throughput experiment are explicit.

## Example

Use `x-manufacturing` on a release process: "Treat our CI/review/deploy flow as the factory. What limits output?"
