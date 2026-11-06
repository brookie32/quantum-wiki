---
title: "Field-aligned measurement removes the anisotropy barrier of sample-based quantum subspace solvers for magnetized-plasma heat conduction"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.07102"
summary: "arXiv:2611.07102v1 Announce Type: new Abstract: Sample-based quantum subspace methods construct a small subspace from measured basis states and solve the target problem classically within it. We study"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.07102v1 Announce Type: new Abstract: Sample-based quantum subspace methods construct a small subspace from measured basis states and solve the target problem classically within it. We study these methods for heat conduction in magnetized plasmas, where the anisotropy hi_parallel/hi_perp reaches 10^8 to 10^{10}. We prove two results for the energy-norm Galerkin solution. First, if the measurement basis is aligned with the flux surfaces and the subspace contains the poloidal-mode-zero block, the error is bounded by |r_0|_{L^+}(hi_parallel-hi_perp)^{-1/2}, where the numerator does not depend on hi_parallel. The bound is sharp, so the accuracy improves as the anisotropy grows. Second, in the computational basis, a subspace that misses a single node of a flux surface suppresses the flux-function component there as hi_parallel^{-1/2}, which gives an error floor when the limiting solution is nonzero on that surface. We verify both results on a shaped cross-section and on a KSTAR-like Miller equilibrium with ten qubits. At hi_parallel/hi_perp=10^9, the computational basis gives an error of order unity for every shot budget, whereas a quantum Fourier transform on the poloidal register gives 1.3imes10^{-5}. The same barrier limits sample-based quantum diagonalization. The aligned measurement needs no time evolution, so the circuit is only state preparation and a five-qubit quantum Fourier transform. On a ten-qubit superconducting processor, the aligned basis gives a median error of 7.0imes10^{-6} with 768 shots, whereas the computational basis gives errors above 0.94 up to 1.2imes10^4 shots. A trapped-ion processor shows the same behavior.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.07102) | 2026-11-06
