---
title: "Vehicle-Routing Clustering by Sparse Quantum Relaxation"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.19575"
summary: "arXiv:2609.19575v1 Announce Type: new Abstract: This paper studies the cluster-assignment layer of a cluster-first-route-second decomposition for the capacitated pickup-and-delivery problem with time "
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.19575v1 Announce Type: new Abstract: This paper studies the cluster-assignment layer of a cluster-first-route-second decomposition for the capacitated pickup-and-delivery problem with time windows (CPDPTW), instead of a direct route-ordering quadratic unconstrained binary optimization (QUBO). Sample-based subspace diagonalization (SQD) degenerates to best-of-shots for any diagonal optimization Hamiltonian, so a useful transfer to routing requires non-diagonal relaxation. Quantum random access optimization (QRAO) provides this non-diagonality by encoding binary variables through non-commuting quantum random access code (QRAC) observables. CPDPTW-derived conflict graphs expose a routing-specific obstruction because dense objectives and penalty-encoded constraints destroy QRAO compression. We keep the Hamiltonian sparse by encoding only the sparsified objective and enforcing one-hot, capacity, and cluster time-budget feasibility by repair after rounding. We make no quantum-advantage claim. Under strong repair the classical pass alone reaches near-optimal cost at the tested sizes. The result is a regime map linking sparsification, achieved compression, linear-combination-of-unitaries (LCU) 1-norm, heavy-hex two-qubit depth, sampling drift, and final routing quality on Qiskit Aer, calibrated FakeTorino, and IBM Heron ibm_quebec. Across a 108-row ideal-calibrated-hardware evaluation grid spanning four to twelve pickup-delivery request pairs, the hardware slice has mean gap 0.0016 and mean device-vs-ideal total variation distance (TVD) 0.279; a decoder ablation at sizes six through twelve isolates the non-diagonal signal.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.19575) | 2026-09-18
