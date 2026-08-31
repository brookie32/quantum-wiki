---
title: "Evidence for effectively constant shot complexity in the quantum approximate optimization algorithm without per-instance optimization"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.19035"
summary: "arXiv:2509.19035v3 Announce Type: replace Abstract: We study a modified fixed-point version of the Quantum Approximate Optimization Algorithm (fpQAOA), where parameters are trained classically on smal"
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2509.19035v3 Announce Type: replace Abstract: We study a modified fixed-point version of the Quantum Approximate Optimization Algorithm (fpQAOA), where parameters are trained classically on small instances and then transferred to larger problems. Our scheme combines three ingredients: (i) targeting approximate solutions via a prescribed approximation ratio (AR), (ii) scaling the circuit depth linearly with the problem size using a two-parameter sin-cos angle encoding, and (iii) normalizing QUBO Hamiltonians by their Frobenius norm. Noiseless numerical simulations (for system sizes up to 30 qubits) across a variety of random QUBO ensembles show that with these modifications the median number of quantum circuit runs ("shots") required to achieve AR=0.95 counterintuitively decreases towards a nearly constant value as the problem size increases, while the per-shot time remains polynomial. Extrapolation of this finite-size behavior is consistent with an effectively constant sampling complexity. Moreover, removing any single component of the scheme restores rapid growth of the required number of shots, highlighting the synergistic nature of the three modifications. These empirical findings suggest that fpQAOA, equipped with the proposed protocol, may achieve scalable approximate performance with polynomial-depth circuits for the considered problem classes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.19035) | 2026-08-31
