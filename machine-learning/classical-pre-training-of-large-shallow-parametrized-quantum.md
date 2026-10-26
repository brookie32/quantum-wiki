---
title: "Classical Pre-Training of Large Shallow Parametrized Quantum Circuits through Pauli Propagation and deployment on Quantum Hardware"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.32571"
summary: "arXiv:2610.32571v1 Announce Type: new Abstract: Scaling parametrized quantum circuits to a larger number of qubits is a central challenge in Quantum Machine Learning: gradient estimation via the param"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2610.32571v1 Announce Type: new Abstract: Scaling parametrized quantum circuits to a larger number of qubits is a central challenge in Quantum Machine Learning: gradient estimation via the parameter-shift rule quickly becomes prohibitively expensive, while gradient-free optimizers offer limited convergence guarantees. We apply the Pauli propagation framework to a broad class of Quantum Machine Learning problems in which the loss is expressed as a function of expectation values of the circuit's observables, while keeping the relevant quantity of interest, such as the quantum state or its samples, classically intractable to compute. By propagating the observables backward through the circuit, we obtain an explicit parametric expression for the loss that can be minimized entirely on classical hardware. We also present complementary strategies to make propagation tractable at large scale, including weight-based and degree-based truncations and pruning heuristics. We demonstrate the approach on two benchmarks run on 64-qubit circuits: Variational Quantum Eigensolver on a two-dimensional Ising model, and training of a discrete-type generative model for binary images. In both cases, the classically pre-trained parameters are deployed on the IBM quantum processor ibm_berlin. For generative learning, we additionally show that the circuits considered here require substantially fewer parametrized gates than IQP-style ansatze, reducing transpilation overhead and making deployment on current quantum hardware feasible.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.32571) | 2026-10-26
