---
title: "A Heuristic for Matrix Product State Simulation of Out-of-Equilibrium Dynamics of Two-Dimensional Quantum Spin Systems"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.23438"
summary: "arXiv:2511.23438v2 Announce Type: replace Abstract: Out-of-equilibrium dynamics of non-integrable Hamiltonian many-body quantum systems are characterized by highly entangled wave functions. Near-maxim"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2511.23438v2 Announce Type: replace Abstract: Out-of-equilibrium dynamics of non-integrable Hamiltonian many-body quantum systems are characterized by highly entangled wave functions. Near-maximal entanglement arises in systems exhibiting thermalization or pre-thermalization, where the system converges to a steady state with a fixed energy density. Classical simulation of the time dependence of such wave functions requires exponential resources. However, typical computations aim to estimate expectation values of local operators and correlation functions to some expected precision. For thermalizing systems at sufficiently high energy densities, such computations can be done without storing the full wave function by instead simulating the evolution of the local operator, which requires significantly fewer resources. Nonetheless, constructing such resource-efficient classical algorithms remains a challenge for intermediate energy densities, where simulating both the wave function and operator evolution is costly. In this paper, we propose a heuristic approach to accelerate the convergence of Matrix Product State (MPS) simulations of expectation values, applicable across a broad range of energy densities. We estimate the desired observables by rescaling the MPS results at low bond dimensions with a factor that depends on the fidelity of the MPS wave function. Using this technique, we simulated the dynamics of the two-dimensional Transverse-Field Ising Model (TFIM) on a 7imes8 grid with periodic boundary conditions, using a maximum bond dimension of hi = 4096 on a single A100 GPU, as well as the dynamics of the two-dimensional XY model on grids of size up to 9imes9. We compare our TFIM results to similar simulations on a digital quantum processor [R. Haghshenas et al., Nature 653, 56 (2026)], demonstrating excellent agreement and confirming the predictive power of our method.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.23438) | 2026-08-11
