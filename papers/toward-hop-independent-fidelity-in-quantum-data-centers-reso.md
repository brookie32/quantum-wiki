---
title: "Toward Hop-Independent Fidelity in Quantum Data Centers: Resource Requirements for Entanglement Purification"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.05369"
summary: "arXiv:2605.05369v2 Announce Type: replace Abstract: Quantum data-center networks must distribute entanglement between QPUs over paths whose length grows with system scale, but each entanglement-swappi"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2605.05369v2 Announce Type: replace Abstract: Quantum data-center networks must distribute entanglement between QPUs over paths whose length grows with system scale, but each entanglement-swapping step reduces the quality of the raw end-to-end state. Topology, multiplexing, and repeated connection attempts can increase the number of raw end-to-end copies available for a request, yet they do not answer the central resource question: whether those copies are sufficient to remove, via entanglement purification, the fidelity loss caused by multi-hop distribution. We study this question through a topology-independent black-box model of the network. Each elementary link is modeled as a Werner state with parameter w_0, so ideal swapping over an ell-link path produces equal-quality raw copies with Werner parameter w_0^ell; purification succeeds if it outputs at least one state with Werner parameter at least w_0 with probability at least p_{th}. We compare recursive BBPSSW purification with higher-order r-to-1 bilocal-Clifford purification protocols of Jansen et al., using an all-in recursive schedule whose success probability is computed by exact dynamic programming. The resulting resource landscapes show a threshold structure governed by the Werner entanglement condition w_0^ell>1/3 and demonstrate that multi-copy purification substantially improves both feasibility and copy efficiency. Across the evaluated grid, the Jansen family requires fewer copies than BBPSSW at more than 96% of shared feasible points; at p_{th}=0.70, the median copy budget drops from 268 to 30. These results provide a quantitative purification-resource benchmark for assessing whether future quantum data-center architectures can practically support hop-independent end-to-end entanglement quality.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.05369) | 2026-07-31
