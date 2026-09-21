---
title: "Set-Packing and Sequence-Pair QUBOs for the 2D Cutting Stock Problem on Quantum Annealing Hardware"
date: "2026-09-21"
updated: "2026-09-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.20853"
summary: "arXiv:2609.20853v1 Announce Type: new Abstract: The two-dimensional Cutting Stock Problem (2D-CSP) is an NP-hard problem with direct economic and environmental impacts on manufacturing and logistics. "
last_verified: "2026-09-21"
review_by: "2026-12-20"
stale: false
---

arXiv:2609.20853v1 Announce Type: new Abstract: The two-dimensional Cutting Stock Problem (2D-CSP) is an NP-hard problem with direct economic and environmental impacts on manufacturing and logistics. We encode its fixed-plate variant, with free piece repetition and full non-overlap and containment constraints, as a Quadratic Unconstrained Binary Optimization (QUBO) problem for quantum annealing and compare two formulations from opposite encoding paradigms. The first was a coordinate-based set-packing model with one binary variable per candidate placement. Its variable count grows linearly with plate area and resolution, but its ground state is, by construction, a geometrically feasible maximum-area packing. The second is a coordinate-free sequence-pair model whose variable count is independent of plate resolution and size. We prove that this compactness has a structural limit: no coordinate-free QUBO of bounded interaction degree whose penalties vanish on every geometrically feasible layout can have a geometrically feasible ground state for 2D containment, because containment is a longest-path constraint that bounded-degree penalties cannot enforce on chains longer than their interaction order. We evaluate both formulations under multi-seed simulated annealing, simulated quantum annealing, and an exact integer-programming baseline. Hardware experiments include D-Wave minor embedding, a calibrated direct-QPU sweep, and Leap hybrid solvers in both penalty and constraint-native form, across a six-instance campaign with per-instance calibration. The hybrid solver returns our certificate configuration, tying its energy to thirteen decimal places while overflowing the plate. We claim no quantum speedup. Our contribution is an impossibility result characterizing the limits of compact packing QUBOs, and a practical rule for choosing between the two formulations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.20853) | 2026-09-21
