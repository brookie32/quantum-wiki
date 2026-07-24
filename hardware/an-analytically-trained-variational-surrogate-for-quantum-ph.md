---
title: "An Analytically Trained Variational Surrogate for Quantum Phase Estimation on NISQ Hardware"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.20943"
summary: "arXiv:2607.20943v1 Announce Type: new Abstract: Quantum Phase Estimation (QPE) is a foundational algorithm for molecular ground-state energy estimation, but its deep circuit requirements make direct h"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.20943v1 Announce Type: new Abstract: Quantum Phase Estimation (QPE) is a foundational algorithm for molecular ground-state energy estimation, but its deep circuit requirements make direct hardware execution impractical on Noisy Intermediate-Scale Quantum (NISQ) devices. We present an analytically grounded variational surrogate framework in which a shallow Variational Quantum Circuit (VQC) is trained to reproduce the QPE measurement distribution without any quantum circuit simulation. The training target is computed entirely classically via the Dirichlet kernel, evaluated directly from the Full Configuration Interaction (FCI) ground-state energy, the ancilla qubit count, and the time evolution parameter, eliminating the exponentially scaling simulation bottleneck of prior surrogate approaches. We apply this framework to the hydrogen molecule (H_2) with a symmetry-tapered Hamiltonian, conducting a four-stage experimental investigation on IBM Quantum hardware. Stage 1 compares linear and full entangler topologies for the R_Y-R_Z-CZ ansatz, with and without XpXm Dynamical Decoupling (DD), across four distributional metrics (Hellinger distance, fidelity error, total variation distance, Jensen-Shannon divergence), identifying the linear entangler as optimal. Stage 2 varies VQC layers (p=1 to 5) for the linear-entangler ansatz, identifying single-layer depth as optimal under hardware noise. Stage 3 applies this configuration to the reduced R_Y-CZ ansatz, comparing ideal and noisy simulator-trained parameters. A supplementary noise analysis at p in {8,64} characterizes the depth-dependent interplay between circuit depth and DD effectiveness. The framework enables faithful QPE mimicry using a linearly scaling VQC, recovering the ground-state energy within the chemical accuracy threshold (1 kcal/mol), constituting a scalable, hardware-efficient paradigm for QPE-based molecular energy estimation on NISQ devices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.20943) | 2026-07-24
