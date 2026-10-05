---
title: "Single-Shot Error Correction at Optimal Spacetime Cost"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03684"
summary: "arXiv:2610.03684v1 Announce Type: new Abstract: Recent work established that, for independent erasures, storing K logical qubits for S time steps with error at most arepsilon requires a spacetime cost"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03684v1 Announce Type: new Abstract: Recent work established that, for independent erasures, storing K logical qubits for S time steps with error at most arepsilon requires a spacetime cost of Omega(S(K+log(S/arepsilon))). A matching construction was also given, but assumes ideal error correction. Here we show that the same scaling can be achieved with an explicit noisy error-correction circuit and efficient decoding, counting all state-preparation, gate, measurement, and wait locations, provided that the hardware supports long-range qubit connectivity and fast, reliable classical processing. Thus, reliability adds only a logarithmic overhead shared by all stored qubits. The construction works for sufficiently weak but otherwise general circuit noise, including faults during syndrome extraction and correlated faults, and for independent erasures it matches the best known lower bound up to constant factors. We attain this scaling using quantum Tanner codes, with each memory step consisting of one round of syndrome extraction followed by a fixed number of parallel classical decoder steps that reduce the residual error enough to keep later faults correctable, regardless of memory size, storage time, or target accuracy. Together, this gives exponentially small failure probability per step while keeping the cost of each memory step linear in the code size. The same analysis also extends to certain constant-depth logical Clifford operations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03684) | 2026-10-05
