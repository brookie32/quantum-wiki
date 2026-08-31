---
title: "A quantum-assisted framework for PDE-based Bayesian inverse problems"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.27028"
summary: "arXiv:2608.27028v1 Announce Type: cross Abstract: Quantum computing offers potential advantages for solving partial differential equations (PDEs). However, most existing quantum PDE solvers primarily "
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2608.27028v1 Announce Type: cross Abstract: Quantum computing offers potential advantages for solving partial differential equations (PDEs). However, most existing quantum PDE solvers primarily focus on preparing quantum states for solutions, while the efficient recovery of classical information from these states remains less explored. Motivated by the readout limitation, we propose a quantum-classical hybrid framework for Bayesian PDE inversion problems: The quantum processor evolves the PDE and evaluate the loss function with sampling noises, while the classical computer tunes the hyper-parameters in the Gaussian Process Regression to explore the next trial candidate. To match the quantum solvers for linear and semi-linear autonomous evolution PDEs, we suggest to use a normalized quantum-state loss as the data-misfit function and evaluate the new misfit by combining quantum PDE solvers with the Hadamard test, thereby allowing us to extract useful classical information using only a limited number of quantum state copies without reconstructing the full solution vector. The analysis of error propagation and overall complexity of loss evaluation under a prescribed accuracy shows that the new data-misfit function outperforms the conventional L2-loss under quantum measurements. Quantum circuit simulations of 1D and 2D linear convection diffusion equations under approximate and finite sampling loss evaluations, together with classical numerical experiments on a nonlinear forced viscous Burgers equation, demonstrate the feasibility of the proposed approach for parameter inversion even when the loss evaluations are affected by sampling noise. This framework may provide a viable quantum-assisted scheme for PDE-based inverse problems and elucidate the potential of quantum PDE algorithms in addressing a complete quantum-to-end optimization stack.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.27028) | 2026-08-31
