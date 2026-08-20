---
title: "Unified Strong-Field Dynamics Simulations from Atoms to Heterostructures"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.18472"
summary: "arXiv:2608.18472v1 Announce Type: new Abstract: We present extsc{TDSE-Z}, a high-performance open-source framework for strong-field quantum dynamics in atomic, molecular, and semiconductor effective-m"
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2608.18472v1 Announce Type: new Abstract: We present extsc{TDSE-Z}, a high-performance open-source framework for strong-field quantum dynamics in atomic, molecular, and semiconductor effective-mass systems. The core engine implements a weak-form Galerkin discretisation of the Hermitian BenDaniel-Duke operator, hat{T}_{BDD} = -frac{1}{2}nabladot(m^{-1}(mathbf{r})nabla), on geometry-adapted B-spline meshes, supporting arbitrary potentials and customisable laser configurations in one to three dimensions. We validate the static position-dependent-mass (PDM) eigensolver through two stringent benchmarks: a comparison to the analytical Quesne PDM model and a ext{GaAs/Al}_{0.3}ext{Ga}_{0.7}ext{As} double quantum well, where the exponential decay of computed tunnel splittings follows Wentzel-Kramers-Brillouin (WKB) theory at the sub-percent level. We further demonstrate the time-propagation engine on constant-mass systems, accurately reproducing high-harmonic generation (HHG) spectra in atomic benchmarks and confirming the importance of dimensionality in fully capturing the strong light-matter interaction. Our implementation demonstrates robust strong-scaling efficiency, maintaining performance across hundreds of CPU cores. While the static eigensolver currently supports optional GPU offloading, the time-propagation engine is CPU-optimised, providing a modular architecture for future expansion toward exascale quantum dynamics.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.18472) | 2026-08-20
