---
title: "A Provable Oracle-Free Quantum Algorithm for Nonlinear Dynamics on Hybrid Oscillator-Qubit Processors"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.28541"
summary: "arXiv:2607.28541v1 Announce Type: new Abstract: We develop a hybrid qubit--qumode algorithm for nonlinear ordinary differential equations of the form ot{mathbf{x}}=mathbf{f}(mathbf{x}) with drift of p"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2607.28541v1 Announce Type: new Abstract: We develop a hybrid qubit--qumode algorithm for nonlinear ordinary differential equations of the form ot{mathbf{x}}=mathbf{f}(mathbf{x}) with drift of polynomial degree~L. Following the Fokker--Planck route of Tennie and Magri, the algorithm propagates the state density and returns the deterministic trajectory as the peak of that density in the small-noise limit. The discretised generator is carried into a parametrised family of Schrodinger equations by the warped-phase transformation of Jin, Liu, and Yu, and the Fourier-mode parameter of that family is placed on a single continuous-variable qumode. Our central structural result is that the Hermitian parts H_{1} and H_{2} of the discretised generator admit a bipartite Pauli decomposition that sorts the non-zero Pauli strings into O(log N) mutually commuting families and factorises each family into a diagonal of degree at most L tensored with a fixed rank-two bond operator. The factorisation renders each family exponential an exact product of O(n^{L}) monomial-controlled momentum displacements, with no intra-family Trotter error. On a d-dimensional grid of N=2^{n} points per axis the circuit costs O(d^{L+1}n^{L+2}) gates per Trotter step. No sparse-access oracle and no block encoding is invoked: every gate is fixed in closed form by the polynomial coefficients of the drift. We also prove a bound on the numerical abscissa lambda_{max}(H_{1}) that fixes the recovery domain of the warped-phase transform and the post-selection cost. A classical simulation on two nonlinear benchmarks confirms the structural theorems, the shifted recovery, and the accuracy-per-resource advantage of the continuous-variable coupling over a discretised mode register.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.28541) | 2026-07-31
