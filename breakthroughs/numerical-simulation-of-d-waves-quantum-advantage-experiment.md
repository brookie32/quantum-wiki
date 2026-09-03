---
title: "Numerical simulation of D-Wave's quantum advantage experiment with time-dependent variational Monte Carlo"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.01719"
summary: "arXiv:2609.01719v1 Announce Type: new Abstract: Programmable quantum annealers can realize real-time dynamics of frustrated transverse-field Ising models on large, nontrivial graphs. Recent work by Ki"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.01719v1 Announce Type: new Abstract: Programmable quantum annealers can realize real-time dynamics of frustrated transverse-field Ising models on large, nontrivial graphs. Recent work by King et al. argued that the classical simulation of such experiments would require exponential computational resources for classical methods such as tensor networks and neural quantum states. Here, we numerically simulate the D-Wave spin-glass annealing protocol with time-dependent variational Monte Carlo (t-VMC) using a correlator state tailored to spin-glass dynamics. For the two-dimensional cylinder, three-dimensional dimer, diamond, and biclique instances considered, at annealing times of 7 and 20 ns, we show that systematically increasing the variational ansatz size enables t-VMC to approximate the final two-spin correlation errors of the quantum processing unit (QPU). We also perform an accurate large-scale simulation of a challenging biclique instance for which no other variational method is known to work, and we find close agreement with the quantum annealer. Through ablation studies, we identify poor Markov-chain mixing, high-variance local-energy estimators, and stochastic Runge-Kutta error estimates as the principal numerical failure modes. We address these numerical issues by using parallel tempering, blurred sampling and an importance-weighted differential equation solver, thereby clarifying the numerical requirements for stable, large-scale t-VMC simulations. Our results extend the frontier of classical simulation while providing a realistic assessment of the computational costs of simulating quantum dynamics at this scale.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.01719) | 2026-09-03
