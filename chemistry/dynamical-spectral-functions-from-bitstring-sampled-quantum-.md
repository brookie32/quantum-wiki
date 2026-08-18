---
title: "Dynamical spectral functions from bitstring-sampled quantum subspaces: entanglement, not one-body magic, tracks the sampling cost"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.16436"
summary: "arXiv:2608.16436v1 Announce Type: new Abstract: Sample-based quantum diagonalization (SQD) and quantum-selected configuration interaction (QSCI) are the electronic-structure methods with most hardware"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.16436v1 Announce Type: new Abstract: Sample-based quantum diagonalization (SQD) and quantum-selected configuration interaction (QSCI) are the electronic-structure methods with most hardware traction, yet their canonical target -- the ground-state energy -- is where classical methods have caught up. We move the target to dynamics and the resource question. From one bitstring-sampling primitive -- computational-basis measurements of a shallow real-time circuit, with no Hadamard or controlled unitaries -- we reconstruct, from sampled subspaces, the single-particle spectral functions A(omega) and A(k,omega) and the neutral-sector dynamical structure factors S(q,omega) and S^{zz}(q,omega), each built classically in the Lehmann representation from its own subspace. The reconstruction matches exact diagonalization on Hubbard chains and, for A(omega), across nineteen molecules (FCI-verified to <10^{-5} Ha), and runs on the IBM Heron processor. Second, we ask which resource controls the cost -- the determinant support |S| the sampler must populate. On number-conserving states the fermionic AntiFlatness collapses to one 1-RDM invariant, F_1 = 4,tr[gamma(1-gamma)] = 2N_u. An orbital-rotation (Gaussian) invariant while |S| is basis dependent, F_1 is provably decoupled from the cost; the cost is instead lower-bounded and tracked by the entanglement -- the minimal bond dimension hi (Spearman rho = 0.90). One-body magic is thus a faithful multireference diagnostic but an unreliable cost predictor; any genuine advantage lives in the non-Gaussianity of the higher-body cumulants. We prove moment exactness and a sampling bound polynomial in |S|, independent of Hilbert-space dimension. Self-consistent configuration recovery improves the subspace under device noise, while a learned generative model does not beat that classical baseline.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.16436) | 2026-08-18
