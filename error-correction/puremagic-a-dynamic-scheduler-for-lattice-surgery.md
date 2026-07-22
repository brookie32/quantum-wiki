---
title: "PureMagic: A Dynamic Scheduler for Lattice Surgery"
date: "2026-07-22"
updated: "2026-07-22"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.06484"
summary: "arXiv:2512.06484v5 Announce Type: replace Abstract: Fault-tolerant quantum computation on surface codes requires magic states for universal computation. Traditional distillation factories deliver magi"
last_verified: "2026-07-22"
review_by: "2026-10-20"
stale: false
---

arXiv:2512.06484v5 Announce Type: replace Abstract: Fault-tolerant quantum computation on surface codes requires magic states for universal computation. Traditional distillation factories deliver magic states deterministically but consume large areas of logical qubits, forcing static, peripheral placement. Magic state cultivation reduces magic state preparation to a single logical qubit, but is inherently stochastic, making static scheduling infeasible. We introduce PureMagic, a dynamic scheduler that eliminates dedicated bus patches by repurposing all ancilla patches for both routing and cultivation. When a patch is needed for routing, cultivation is interrupted and restarted afterward, naturally cutting off the long tail of cultivation times and ensuring no ancilla is ever idle. We also introduce a weight limit on Tableau transpilation that trades gate count for parallelism, which PureMagic is particularly well-suited to exploit. Across 29 benchmark circuits, PureMagic achieves 40% to 150% efficiency improvement over bus routing, uses 19% to 80% fewer logical qubits, and reduces average magic state preparation time by 4.5x. Compared to DASCOT, a state-of-the-art static scheduler, PureMagic is up to 15x more efficient when magic state preparation costs are included. PureMagic's scheduled volumes fall between the conservative and optimistic FLASQ theoretical lower bounds, demonstrating near-optimal use of ancilla resources.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.06484) | 2026-07-22
