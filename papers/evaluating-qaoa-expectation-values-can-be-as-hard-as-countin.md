---
title: "Evaluating QAOA expectation values can be as hard as counting optimal solutions"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.11385"
summary: "arXiv:2608.11385v1 Announce Type: new Abstract: Evaluating expectation values is a critical task for variational quantum eigensolvers, and for parameterized quantum circuits and other quantum algorith"
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2608.11385v1 Announce Type: new Abstract: Evaluating expectation values is a critical task for variational quantum eigensolvers, and for parameterized quantum circuits and other quantum algorithms more generally. We consider the well-studied case of the Quantum Approximate Optimization Algorithm (QAOA) for the MaxCut problem. Recent work of Wang et al. [arXiv:2511.20212] showed this task to be NP-hard in general for any QAOA depth pgeq 2, complementing past results showing efficiently computable formulas for p=1 with arbitrary problem graphs. We sharpen this dichotomy showing that for pgeq 2 exact or exponentially precise cost expectation value evaluation is #P-hard under deterministic polynomial-time Turing reductions. Hardness at pgeq 2 is shown to remain even for evaluating single pairwise correlators langle Zotimes Zrangle , as well as for highly restricted sets of algorithm parameters. Our proof refines the NP-hardness construction of Wang et al. that recovers the maximum cut value from the largest exponent of a QAOA Laurent polynomial, utilizing a distinct and simpler construction that extracts a value proportional to the total number of maximum cuts, in addition to the optimal cut value. Thus we show that the QAOA expectation value hardness transition from p=1 to p=2 is not only from tractability to optimization hardness, but to that of counting optimal solutions. As an application we show our results imply analogous hardness results for computing gradients and Hessians of QAOA circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.11385) | 2026-08-13
