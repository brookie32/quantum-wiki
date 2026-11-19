---
title: "Quantum Simulation of First-Quantised Chemistry with a Sum-of-Squares Representation"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.24885"
summary: "arXiv:2611.24885v1 Announce Type: new Abstract: Calculating molecular energies is expected to be an important application of quantum computers, but the most efficient algorithms to achieve this typica"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.24885v1 Announce Type: new Abstract: Calculating molecular energies is expected to be an important application of quantum computers, but the most efficient algorithms to achieve this typically have significant space requirements. Scaling quantum processors to thousands of logical qubits is a daunting engineering challenge, so developing algorithms that run with reduced qubit requirements is of particular importance. Moreover, most algorithms are benchmarked on active spaces with about as many orbitals as electrons, missing dynamical correlation which is necessary to describe real chemistry. Capturing this correlation requires several times more orbitals than electrons, even in compact atomic-orbital basis sets. This low-filling regime favours first quantisation, where each electron is represented by a number of qubits that grows only logarithmically with the number of orbitals. Whether this approach translates into a practical advantage in orbital basis sets of realistic size, however, has been unclear. Here, we develop a first-quantised phase estimation algorithm for generic orbital basis sets, based on a non-convex sum-of-squares representation of the Hamiltonian and spectral-gap amplification. We compare it with the state-of-the-art second-quantised algorithm, compiling both with the same techniques at the logical level. For six molecules with 4 to 24 electrons in 5 to 14 times as many orbitals, our first-quantised method needs up to 16 times fewer Toffoli gates than the second-quantised algorithm in the low-qubit regime, where only a few hundred logical qubits are available. It stays cheaper up to between several hundred and about 1,400 qubits, and its smallest qubit count is 1.4 to 2 times lower than in second quantisation. In the low-qubit and low-filling regime, our algorithm is therefore the method of choice for chemistry in orbital basis sets.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.24885) | 2026-11-19
