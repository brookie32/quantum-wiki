---
title: "A Quantum Algorithm for Solving the Poisson Equation for Free Field Conditions via the Hockney Method"
date: "2026-08-12"
updated: "2026-08-12"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.10809"
summary: "arXiv:2608.10809v1 Announce Type: new Abstract: For the often encountered problem of the Poisson equation, this work presents a quantum algorithm solving it based on the quantum Fourier transform (QFT"
last_verified: "2026-08-12"
review_by: "2026-11-10"
stale: false
---

arXiv:2608.10809v1 Announce Type: new Abstract: For the often encountered problem of the Poisson equation, this work presents a quantum algorithm solving it based on the quantum Fourier transform (QFT) for periodic boundary conditions as well as free field conditions, where the latter is realized via the Hockney method. Besides the QFT and an initialization procedure for amplitude encoding, the algorithm just uses a procedure for multiplying the state vector by a diagonal matrix w.r.t. amplitude encoding. For the latter, two alternative implementations are considered here. The first variant is a version of the LCU method and the second is a sequence of multi-controlled rotation gates that represents a factoring of the multiplied values into absolute values and complex phase factors. The functionality of the algorithm is verified via comparing the results obtained from state vector simulations for one- and two-dimensional test examples with their analytical solutions. For the considered test examples, it is found that the success probability for obtaining the desired ancilla qubit subspace in the LCU version is a factor of around two higher than that for the sequence of multi-controlled rotation gates. However, the LCU version requires a number of ancilla qubits up to the number of qubits that is set to store the discretized source term of the Poisson equation in amplitude encoding, whereas the sequence of multi-controlled rotation gates demands only one ancilla qubit. Computations of the success probabilities for both variants furthermore indicate that the success probability converges for a specific problem with increasing resolution. Concerning the required computational resources for the quantum algorithm, the conclusion is drawn that while the QFT is a more efficient procedure than its classical counterpart, the current implementations of the other necessary steps in the algorithm diminish the efficiency w.r.t. the runtime.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.10809) | 2026-08-12
