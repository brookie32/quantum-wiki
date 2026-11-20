---
title: "Efficient XX Placement Strategies for Energy-Gap Enhancement in Quantum Annealing"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.20902"
summary: "arXiv:2611.20902v2 Announce Type: replace Abstract: Quantum annealing offers the prospect of a computational advantage over classical methods for certain classes of combinatorial optimisation problems"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2611.20902v2 Announce Type: replace Abstract: Quantum annealing offers the prospect of a computational advantage over classical methods for certain classes of combinatorial optimisation problems. Its performance, however, is fundamentally constrained by the minimum spectral gap between the ground state and the first excited state encountered during the annealing process. When this gap closes exponentially with problem size, the runtime required to maintain adiabatic evolution can likewise grow exponentially, severely limiting the practical efficiency of the annealer. For problems including the maximum weight independent set (MWIS), previous work has shown that introducing XX interactions along problem-graph edges can substantially enlarge the minimum energy-gap and thereby improve annealing performance. In practice, however, current quantum annealing hardware does not support these interactions natively and methods for implementing effective XX couplings come with hardware overhead and connectivity constraints. These limitations motivate the use of only a limited number of XX interactions. In this paper, we investigate XX placement strategies for MWIS instances under both resource and topological constraints, and demonstrate that careful selection of the placements can substantially increase the minimum energy-gap. We evaluate these strategies through a detailed statistical analysis of both deliberately constructed hard MWIS instances and random Erdos--Renyi graphs. Notably, these strategies are particularly effective for hard MWIS instances with initially small minimum gaps, where targeted placement yields the largest relative improvements.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.20902) | 2026-11-20
