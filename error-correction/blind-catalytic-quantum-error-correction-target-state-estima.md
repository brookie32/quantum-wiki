---
title: "Blind Catalytic Quantum Error Correction: Target-State Estimation and Fidelity Recovery Without A Priori Knowledge"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.11857"
summary: "arXiv:2604.11857v4 Announce Type: replace Abstract: Catalytic quantum error correction (CQEC) amplifies residual coherence with a reusable catalyst, giving threshold-free recovery whenever the target "
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2604.11857v4 Announce Type: replace Abstract: Catalytic quantum error correction (CQEC) amplifies residual coherence with a reusable catalyst, giving threshold-free recovery whenever the target coherent modes survive in the noisy state; its original protocol, however, requires complete knowledge of the ideal target, which fails for variational and iterative algorithms whose output is unknown to the correction module. Here we show that this requirement can be removed by estimating the target from the noisy output alone, in a two-stage protocol we call blind CQEC. At the density-matrix level studied here the recovery map is the mode-inclusion-restricted projection of the estimate, so recovery fidelity obeys F_rec >= 1 - 2||rho_est - rho_target||_1 - 2 Delta_mode: the design of blind CQEC reduces to a classical estimation problem under a recovery ceiling set by mode survival. We benchmark five estimation strategies across three noise channels, four quantum algorithms (d = 4-64), Haar-random states, and mixed targets, assuming oracle access to the noisy density matrix. With exactly calibrated noise, channel inversion coincides with the oracle and both are capped by the mode-survival ceiling (F_rec = 0.77 at d = 64 with the 10^-10 mode threshold); noise-model-free coherence maximization matches the ceiling to within 1.5% at d <= 16; the choice between them is set by calibration accuracy, with the dephasing rate exponentially dominant. Unlike error-mitigation methods, blind CQEC returns the state itself rather than corrected expectation values. A noisy-VQE demonstration for H2 yields a 3.4x energy-error reduction. These results chart the estimator design space for blind, threshold-free recovery and identify the two open problems, an operational measurement model and a circuit-level catalytic map, that remain before deployment.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.11857) | 2026-10-08
