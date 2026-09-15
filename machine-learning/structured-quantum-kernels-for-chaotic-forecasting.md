---
title: "Structured Quantum Kernels for Chaotic Forecasting"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.13360"
summary: "arXiv:2609.13360v1 Announce Type: new Abstract: Quantum kernels promise exponentially large feature spaces, but expressive circuits render their Gram matrices uninformative, bandwidth tuning collapses"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.13360v1 Announce Type: new Abstract: Quantum kernels promise exponentially large feature spaces, but expressive circuits render their Gram matrices uninformative, bandwidth tuning collapses them toward classical RBF, and the practical consensus is that quantum kernels add nothing on classical data. We answer another productive question, an architectural one: whether the structure of an encoding circuit can carry an inductive bias that tuned classical kernels lack. We introduce AeRot, a quantum kernel fusing amplitude encoding of l2-normalized delay windows with a grouped single-qubit rotation layer that assigns contiguous temporal blocks to each qubit, making the circuit delay-window-aware. On Lorenz-63 kernel ridge regression with cross-validated bandwidths over 100 seeds, AeRot outperforms tuned RBF and Matern-5/2, the advantage emerging at physical horizons >= 0.15 tu and reaching +0.137 mean R^2 at 0.25 tu (5 qubits, window 32). Linear-stability analysis of the window tail localises the advantage to the unstable saddle-approach regime: AeRot wins 83% of windows in the most unstable decile, with the win rate rising monotonically with tail instability and a sign flip at the local stability boundary. The difficulty is fold-branch ambiguity: trajectories approaching the saddle are locally diverging, and Euclidean kernels struggle to resolve which lobe the trajectory will commit to. Structural diagnostics confirm Gram matrices structurally distinct from tuned RBF, with strictly higher target-kernel alignment at every horizon. The gain is architectural: a finite-sample inductive-bias effect of temporally structured encoding on a folded attractor, with no computational-separation claim attached. To our knowledge this is the first mechanistic localisation of quantum-kernel advantage to a specific dynamical regime of a classical system.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.13360) | 2026-09-15
