---
title: "Resource-Efficient QUBO Formulation for Anchored Currency Arbitrage"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.15889"
summary: "arXiv:2608.15889v1 Announce Type: new Abstract: Currency arbitrage (CA) involves trading currencies in cycles to exploit discrepancies in market valuations. Quadratic unconstrained binary optimization"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.15889v1 Announce Type: new Abstract: Currency arbitrage (CA) involves trading currencies in cycles to exploit discrepancies in market valuations. Quadratic unconstrained binary optimization (QUBO) involves minimizing a quadratic cost (energy) function of binary variables. Previous works have explored the use of QUBO to solve CA problems. We build on these previous works by introducing realistic constraints such as beginning cycles from a held currency and accounting for per-transaction trading fees. We show that this formulation requires fewer logical variables (qubits) than previous QUBO encodings in the literature. We derive provably sufficient penalty weights for its constraint terms. We also introduce an exact anchor-gauge reweighting of the exchange rates that compresses the QUBO coefficient range from the rate scale to the arbitrage scale, addressing the finite analog precision of annealing hardware. We demonstrate the efficacy of this formulation using classical simulated annealing against an exact Held-Karp baseline on the same CPU and show that it can effectively find profitable cycles and account for trading fees. Finally, we benchmark faithful implementations of five prior QUBO encodings at matched sampler budgets and show that the proposed encoding is the only one to recover the exact fee-adjusted optimum.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.15889) | 2026-08-18
