---
title: "Accelerating Quantum-Classical Auxiliary-Field Quantum Monte Carlo with Shadow-Trained Neural Quantum States"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.08129"
summary: "arXiv:2611.08129v1 Announce Type: new Abstract: Quantum-classical auxiliary-field quantum Monte Carlo (QC-AFQMC) uses a trial state prepared on a quantum computer to improve the accuracy of the classi"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.08129v1 Announce Type: new Abstract: Quantum-classical auxiliary-field quantum Monte Carlo (QC-AFQMC) uses a trial state prepared on a quantum computer to improve the accuracy of the classical AFQMC algorithm. State-of-the-art QC-AFQMC represents this state with matchgate shadows, so every trial-walker overlap and local energy must be averaged over many snapshots, making this classical computation a bottleneck. Here we distill the matchgate shadow data into a symmetry-constrained, noise-aware, autoregressive transformer neural quantum state (NQS). Used as the AFQMC trial state, the NQS evaluates overlaps, force biases, and local energies without repeatedly summing over the matchgate shadows. For a nickel-catalyzed oxidative-addition reaction, the noise-awareness of our NQS design successfully recovers the ideal-upCCD AFQMC barrier and reaction energy within statistical uncertainty, while standard QC-AFQMC execution with the same shadow data yields qualitatively inaccurate results as a result of hardware noise. Since the shadow data are needed only for training, the estimated classical cost for the nickel system falls by approximately 99% relative to our previous QC-AFQMC implementation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.08129) | 2026-11-06
