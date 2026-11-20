---
title: "QuasiStim: Scalable Accurate Non-Pauli Noise Simulation for Fault-Tolerant Quantum Circuits"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.15975"
summary: "arXiv:2610.15975v2 Announce Type: replace Abstract: Fault-tolerant quantum computer design relies on simulating noisy quantum error correction (QEC) circuits with hundreds to thousands of physical qub"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2610.15975v2 Announce Type: replace Abstract: Fault-tolerant quantum computer design relies on simulating noisy quantum error correction (QEC) circuits with hundreds to thousands of physical qubits and large circuit depths. High-throughput stabilizer simulators, such as Stim, are the de facto tools for this regime. However, these simulators typically support only Clifford gates and stochastic Pauli noise. As a result, more realistic device noise models, such as coherent control errors and thermal relaxation, are often approximated using Pauli twirling. This replacement offers speed but can introduce substantial inaccuracies. To address this, we propose QuasiStim for scalable, accurate QEC simulation of realistic noise, with QuasiFold as a compiler frontend and DeltaFrame as a sampling backend. QuasiFold lowers sampling overhead by opportunistically merging non-Pauli noise sites in the quantum circuit without changing the circuit output. DeltaFrame samples the resulting stabilizer trajectories by reusing precomputed predicted references instead of resimulating the full tableau for each shot. In our evaluation, QuasiFold can reduce the number of shots by over 1000imes on bivariate-bicycle (BB) codes under coherent R_{ZZ} noise. Compared to a per-shot tableau simulator, DeltaFrame is 190imes to 1479imes faster on rotated surface-code memory as d grows from 5 to 35. QuasiStim also makes the PTA bias measurable: the gap is non-trivial and varies with noise strength, decoder, and circuit schedule.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.15975) | 2026-11-20
