---
title: "Plateau-Constrained Selection of Commuting Phase-Term Orderings Under a Fixed Maintained-Parity Compiler Contract"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.27592"
summary: "arXiv:2608.27592v1 Announce Type: new Abstract: Ordering objectives for commuting phase terms can have many equal optima, yet prior methods do not characterize or exploit those ties. We use a classica"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2608.27592v1 Announce Type: new Abstract: Ordering objectives for commuting phase terms can have many equal optima, yet prior methods do not characterize or exploit those ties. We use a classical two-stage permutation search under fixed placement and maintained-parity quantum lowering: Stage 1 certifies the primary support optimum, and Stage 2 samples equal-cost tours and selects by a frozen routed score. On synthetic 16-qubit assignment-Ising instances, exact counting through 20 terms establishes instance-dependent multiplicity; when the support lower bound is attained, the reversal-reduced width equals the number of undirected Hamiltonian paths of the support line graph. A revised engineering analysis found 9.14% fewer routed controlled-NOT gates than unoptimized order, while the registered comparison found 11.10% fewer than prior stochastic search. Among 24 sampled minimum-support-cost orders at 36 terms, direct-depth selection reduced opposite-SABRE-seed depth by 12.83% in all 20 aggregates, whereas a matched 24-restart control changed depth by only -0.41% (unresolved). Candidate rankings persisted across SABRE routing seeds, explaining why selection survived routing re-randomization. The depth benefit transferred to a second generator and to 48 terms, but reversed under BasicSwap. On a prospective IBM Heron panel, raw generator error shifted by -0.0025 (-0.59%); fixed-panel shot uncertainty excluded zero, but term-seed inference remained unresolved. Equal-primary-cost tours are a useful router-conditioned compiler freedom, not a guaranteed hardware benefit.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.27592) | 2026-08-31
