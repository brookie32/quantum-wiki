---
title: "Quantum Gaussian processes for prediction of channel observations"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.19306"
summary: "arXiv:2608.19306v1 Announce Type: new Abstract: Given a set of input states, we consider the task of predicting the expectation value of a Pauli observable at the output of an unknown quantum evolutio"
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.19306v1 Announce Type: new Abstract: Given a set of input states, we consider the task of predicting the expectation value of a Pauli observable at the output of an unknown quantum evolution, using only a limited number of measurements. Recently, quantum Gaussian process (QGP) regression was introduced for this task across various classes of unitary evolution. Here, we extend the QGP framework beyond unitary dynamics. In particular, we prove convergence of the channel's outputs to a QGP and derive the associated closed-form kernel under a uniform (Lebesgue measure) prior over quantum channels. The kernel's dimensional factor, however, dictates the required observation precision. While manageable when the channel and observable are restricted to small subsystems, exponential suppression precludes learning when the subsystem grows extensively with the system size. Since the Lebesgue prior is overly broad for many applications, we propose an empirical Bayes heuristic that replaces the dimensional factor with a learnable scale parameter while retaining the kernel's state-overlap correlation structure. In numerical simulations of up to 64 qubits, channel QGP regression with the Lebesgue kernel exhibits a strong inductive bias for local channels, enabling faithful extrapolation. For global 64-qubit channels, the rescaled kernel restores learnability, with predictions improving systematically with the shot budget. Results from a noisy quantum computer further demonstrate the robustness of QGP regression under experimental conditions. Beyond regression, we validate QGPs as Bayesian-optimization surrogates for state preparation under noisy XXZ dynamics.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.19306) | 2026-08-21
