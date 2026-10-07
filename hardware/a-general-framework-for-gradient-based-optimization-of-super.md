---
title: "A General Framework for Gradient-Based Optimization of Superconducting Quantum Circuits using Qubit Discovery as a Case Study"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2408.12704"
summary: "arXiv:2408.12704v2 Announce Type: replace Abstract: Engineering the Hamiltonian of a quantum system is fundamental to the design of quantum systems. Automating Hamiltonian design through gradient-base"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2408.12704v2 Announce Type: replace Abstract: Engineering the Hamiltonian of a quantum system is fundamental to the design of quantum systems. Automating Hamiltonian design through gradient-based optimization can dramatically accelerate this process. However, computing the gradients of eigenvalues and eigenvectors of a Hamiltonian--a large, sparse matrix--relative to system properties poses a significant challenge, especially for arbitrary systems. Superconducting quantum circuits offer substantial flexibility in Hamiltonian design, making them an ideal platform for this task. In this work, we present a comprehensive framework for the gradient-based optimization of superconducting quantum circuits, leveraging the SQcircuit software package. By addressing the challenge of calculating the gradient of the eigensystem for large, sparse Hamiltonians and integrating automatic differentiation within SQcircuit, our framework enables efficient and precise computation of gradients for various circuit properties or custom-defined metrics, streamlining the optimization process. We apply this framework to the qubit discovery problem, demonstrating its effectiveness in identifying qubit designs with superior performance metrics. The optimized circuits show improvements in a heuristic measure of gate count, upper bounds on gate speed, decoherence time, and resilience to noise and fabrication errors compared to existing qubits. While this methodology is showcased through qubit optimization and discovery, it is versatile and can be extended to tackle other optimization challenges in superconducting quantum hardware design.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2408.12704) | 2026-10-07
