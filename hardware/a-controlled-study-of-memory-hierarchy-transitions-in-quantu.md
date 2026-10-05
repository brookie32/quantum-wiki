---
title: "A Controlled Study of Memory Hierarchy Transitions in Quantum Circuit Simulation on Apple M4 Pro Unified Memory Architecture"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.08792"
summary: "arXiv:2605.08792v3 Announce Type: replace-cross Abstract: State-vector quantum circuit simulation is memory-bandwidth bound, yet the interaction between memory hierarchy, access pattern, and hardware "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2605.08792v3 Announce Type: replace-cross Abstract: State-vector quantum circuit simulation is memory-bandwidth bound, yet the interaction between memory hierarchy, access pattern, and hardware parallelism remains incompletely characterized. We address this using the Apple M4 Pro Unified Memory Architecture (UMA), where CPU and GPU share identical physical LPDDR5X DRAM (sim224 GB/s STREAM bandwidth for both), eliminating memory-technology and interconnect confounds. Using a thermally isolated, multi-trial methodology across 11 simulation backends on GHZ and QFT circuits from 3 to 30 qubits, we make three central contributions. First, a Roofline analysis confirms all gate implementations have arithmetic intensity leq0.38 FLOP/byte, well below the ridge point for any plausible peak compute on modern hardware, establishing structural memory-boundedness. Second, we identify a reproducible 4.46imes timing discontinuity at the 28rightarrow29 qubit transition, confirmed under thermally isolated conditions and cross-validated across GHZ and QFT circuits; tensordot backends exhibit the full discontinuity while direct-index backends maintain sim2imes per-qubit scaling throughout. Third, despite STREAM predicting only 1.85imes GPU speedup (MLX CPU 119.9 GB/s vs. MLX GPU 221.9 GB/s), all three algorithm classes exceed this prediction: tensordot 3.1--4.1imes, flat-index 3.5--5.9imes, and direct-index 6--10imes, demonstrating that peak streaming bandwidth does not predict simulation speedup for non-contiguous memory access patterns, with the gap widening as access irregularity increases. These findings provide a hardware-characterization framework for quantum simulation workloads on UMA.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.08792) | 2026-10-05
