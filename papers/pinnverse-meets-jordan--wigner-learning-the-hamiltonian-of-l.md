---
title: "PINNverse meets Jordan--Wigner: learning the Hamiltonian of long spin chains"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.14023"
summary: "arXiv:2611.14023v1 Announce Type: new Abstract: Inverse physics-informed neural networks (PINNverse) learn the parameters of a quantum Hamiltonian from measured expectation values, but the network out"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.14023v1 Announce Type: new Abstract: Inverse physics-informed neural networks (PINNverse) learn the parameters of a quantum Hamiltonian from measured expectation values, but the network output grows as 4^N with the number of qubits N. We show that, for spin chains with nearest-neighbor exchange interactions, the Jordan-Wigner transformation removes this exponential cost: the dynamics closes on an Nimes N one-body density matrix, so the network needs only N^2 outputs and the data are local observables measured in five global settings. Parasitic ZZ couplings (crosstalk) are included through a time-dependent Hartree--Fock closure. With synthetic data, the same network first solves the equation of motion and then recovers the Hamiltonian parameters of chains of up to 50 qubits, with couplings learned to better than 0.1%. Errors in the local frequencies of long chains are removed by a direct least-squares fit started from the network estimate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.14023) | 2026-11-11
