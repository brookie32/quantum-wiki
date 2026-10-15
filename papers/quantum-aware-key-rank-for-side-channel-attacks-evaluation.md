---
title: "Quantum-Aware Key Rank for Side-Channel Attacks evaluation"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.20537"
summary: "arXiv:2610.20537v1 Announce Type: new Abstract: Side-channel attacks on block ciphers rarely recover the key outright: they leave a residual key space ordered by subkey posteriors, and evaluation labo"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2610.20537v1 Announce Type: new Abstract: Side-channel attacks on block ciphers rarely recover the key outright: they leave a residual key space ordered by subkey posteriors, and evaluation laboratories report the key rank of the true key against thresholds near 2^48 and 2^60. No evaluation framework models an adversary who collects traces classically and finishes the search on a quantum computer, although quantum search with advice provides exactly that. We give such an adversary a cost model and a metric. For a device whose key has rank r, any quantum algorithm with classical access to the posteriors needs Omega(sqrt(r)) cipher evaluations, and block search achieves O(sqrt(r)); the per-instance advantage is exactly quadratic, and the super-quadratic exponents reported for search with advice are averages over the prior that apply to no single device. Under the NIST MAXDEPTH budget D and a Grover iteration of g gates and depth d, the quadratic advantage holds only for ranks up to (4D/(pi d))^2 and collapses to a constant factor beyond; with the best published AES-128 oracle and D = 2^40 the window closes near rank 2^58.6. We define the quantum-aware key rank, the classical rank of equal cost, computable from the rank estimators laboratories already run, and derive the classical rank a device must retain to keep a given threshold against each depth budget. Block search and amplitude amplification from the product-form posterior state are within a factor of two to four of each other on Hamming-weight posteriors, so the cost of coherent indexing decides between them. Experiments on simulated leakage and a toy cipher confirm the predicted window: at SNR 0.125 a depth-limited quantum adversary is worth about 22 traces to a classical one, however large its gate budget.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.20537) | 2026-10-15
