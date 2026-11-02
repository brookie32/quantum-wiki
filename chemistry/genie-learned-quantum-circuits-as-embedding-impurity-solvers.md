---
title: "GENIE: learned quantum circuits as embedding impurity solvers, and why compactness, not correlation strength, decides when they work"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41957"
summary: "arXiv:2610.41957v1 Announce Type: new Abstract: Sample-based quantum diagonalization has been used as an impurity solver in density matrix embedding theory (DMET), but always with fixed-form circuits "
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41957v1 Announce Type: new Abstract: Sample-based quantum diagonalization has been used as an impurity solver in density matrix embedding theory (DMET), but always with fixed-form circuits and without comparison to classical selection at the same subspace size. We introduce GENIE, a DMET impurity solver in which a generative transformer learns the sampling circuit, trained on the quantum-selected configuration interaction energy. On N2, hydrogen chains, water and a hydrogen ring, we compare GENIE at equal determinant budget with classical selected configuration interaction (CIPSI, ASCI, heat-bath CI) and with DMET combined with sample-based quantum diagonalization (SQD). GENIE selects: for N2 at 200 determinants it is within a factor of 1.7 of CIPSI and 25 to 1000 times more accurate than the determinants a fixed circuit actually samples, while standard SQD reaches good energies mainly by filling the subspace. GENIE does not beat the best classical selection, and its circuits require fault-tolerant hardware. Its failures are governed by the compactness of the wavefunction relative to the budget, not by correlation strength. A cheap estimate from coupled-cluster amplitudes predicts this compactness. A router built on it never recommended GENIE where it then failed, apart from seed-to-seed variance, and it transferred unchanged to a blind test on new systems. We also identify two benchmarking pitfalls that can create apparent quantum advantages of one to two orders of magnitude.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41957) | 2026-11-02
