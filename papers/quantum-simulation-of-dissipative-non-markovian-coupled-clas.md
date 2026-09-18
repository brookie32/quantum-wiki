---
title: "Quantum Simulation of Dissipative Non-Markovian Coupled Classical Oscillators"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.20721"
summary: "arXiv:2609.20721v1 Announce Type: new Abstract: We present a quantum algorithm for simulating classical oscillator networks characterized by non-Markovian dissipation and time-varying material propert"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.20721v1 Announce Type: new Abstract: We present a quantum algorithm for simulating classical oscillator networks characterized by non-Markovian dissipation and time-varying material properties, extending recent speedups for undamped harmonic systems to viscoacoustic and viscoelastic media. We embed the history-dependent dynamics into a Markovian state space governed by a non-Hermitian operator by approximating memory kernels through a Prony series. We then use linear combination of Hamiltonian simulation to estimate the instantaneous kinetic and potential energy for a subset of oscillators at time t within error epsilon using a number of queries to the oscillator system that scales as widetilde{O}(alpha_{rm tot} t/epsilon), where alpha_{rm tot} is polynomial in the strength of the dissipation, spring constants, inverse masses, and sparsity of the connections in the network. We further show that this energy estimation task is in the worst-case classically hard (i.e., a corresponding decision problem is mathsf{BQP}-complete), even in the presence of strong dissipation. For time-dependent materials, we show that changes in material properties appear as effective dissipation or growth in the energy representation. Additionally, we prove the infeasibility of exponential quantum advantages in locally coupled topologies through a novel form of Lieb-Robinson-like bounds that apply to differential equations. This allows our quantum algorithms to provide quartic speedups for locally coupled damped oscillator systems in three dimensions, raising the possibility of practical quantum speedups for realistically damped oscillator networks and approximated wave equations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.20721) | 2026-09-18
