---
title: "Probing the Weak-Driving Quantum Speed Limit via Drift-Aware Shooting Methods"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.22212"
summary: "arXiv:2606.22212v2 Announce Type: replace Abstract: A central goal of quantum optimal control is to achieve high-fidelity and low-energy control pulses. When quantum optimal control methods optimize e"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2606.22212v2 Announce Type: replace Abstract: A central goal of quantum optimal control is to achieve high-fidelity and low-energy control pulses. When quantum optimal control methods optimize every point of a pulse discretized over small time steps independently this can yield high fidelity control but also results in broadband and energy-hungry waveforms. We extend MAGICARP, a shooting method inspired by Pontryagin's maximum principle on energy that generates an entire pulse from a small set of parameters, making it smooth and energy-efficient by construction, from driftless systems to closed systems with the constant drift Hamiltonian of two exchange-coupled spins in an external magnetic field. The optimization proceeds in stages: the dressed states of the drift Hamiltonian structure the target, an initial shooting optimization is performed in the rotating-wave frame, and an exact laboratory-frame refinement follows. Benchmarked against Krotov and GRAPE at matched gate infidelity, MAGICARP consistently achieves the lowest energy and a conserved pulse area, concentrates its spectral weight on the gate-relevant transitions, and is the most robust to fluctuations in the exchange coupling; GRAPE independently converges to essentially the same pulse while black-box Krotov meets the same error at an order-of-magnitude energy premium. This method-independence is what qualifies the bounded solver as a measurement instrument, and the central result follows: a large statistical survey of unselected optimization runs resolves a weak-driving quantum speed limit for two exchange-coupled electron spins: low-amplitude realizations of the two-qubit quantum Fourier transform cease to exist below a critical gate time, and the minimum control energy diverges on approach to this limit. The divergence obeys a simple two-parameter area--pole law, E_2^{law}(T)=A/T+B/(T-T^*).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.22212) | 2026-09-22
