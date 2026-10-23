---
title: "Problem-aware sampling for bias and variance reduction in randomised Hamiltonian simulation"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.31515"
summary: "arXiv:2610.31515v1 Announce Type: new Abstract: Randomised quantum simulation algorithms such as qDRIFT reduce circuit depth by replacing deterministic product formulas with stochastic compilations, b"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.31515v1 Announce Type: new Abstract: Randomised quantum simulation algorithms such as qDRIFT reduce circuit depth by replacing deterministic product formulas with stochastic compilations, but achieving high accuracy can require many steps. In vanilla qDRIFT, Hamiltonian terms are sampled with probabilities proportional to their coefficient magnitudes. We propose StateDRIFT, a variant of qDRIFT which optimises its sampling distribution to estimate time-evolved quantities using knowledge of the initial state and target observable, with a provable truncation bound that keeps qDRIFT's guarantees. The distribution at each depth is chosen by solving an optimisation problem targeting bias and/or variance. StateDRIFT can significantly reduce the bias and variance of estimators, and hence circuit depth, which we test on short-time dynamics of lattice models and molecules under Jordan-Wigner up to 18 qubits. For example, with BeH2 StateDRIFT can reduce the number of two-qubit gates required to achieve a given accuracy from 11,201 to 983. StateDRIFT involves measuring observables and commutators on the initial state, so we propose two practical ways to estimate these: classical surrogates such as tensor networks, and classical shadows, which recover most or all of the saving from exact oracles in the systems tested.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.31515) | 2026-10-23
