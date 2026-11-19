---
title: "Covering the Pauli Observables: Sampling Thresholds and the Design Effect of a Measurement Setting"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.23827"
summary: "arXiv:2611.23827v1 Announce Type: new Abstract: Quantum state tomography and shadow-based estimation rely on measuring Pauli observables. An experiment does not measure them one at a time: it chooses "
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.23827v1 Announce Type: new Abstract: Quantum state tomography and shadow-based estimation rely on measuring Pauli observables. An experiment does not measure them one at a time: it chooses a measurement setting that assigns one of the bases X, Y or Z to each qubit, and a single run in that setting yields estimates of every Pauli observable compatible with it. We say that the setting covers those observables. We determine how many random settings cover a prescribed fraction of all Pauli observables. As the number of settings grows exponentially with the number of qubits, the covered fraction has a sharp threshold at a growth rate of 3^{3/4} per qubit, set by the rate-distortion function of covering at zero distortion. We give an explicit expression for the number of settings needed to reach a target fraction, accurate up to a remainder that reduces to a small oscillation for many qubits, and show that random sampling is asymptotically optimal up to a factor of less than 1.69. Coverage does not determine what a setting contributes to an estimator. Observables covered by one setting are estimated from the same outcomes, so their estimates are correlated. We quantify this correlation through the design effect of a setting, which equals the squared Pauli expectation that the setting captures and depends on the target state. We derive its mean over settings in closed form for every state and show that it can be estimated without bias from the measurement data. In simulations on six qubits, measuring settings needs 7.6 to 38 times fewer circuit runs than measuring the same number of observables independently. At high coverage, fitting the outcome histograms instead of averaged estimates roughly halves the reconstruction error, mainly because the fit counts how many settings cover each observable. The correlation itself costs such a fit about a factor of two, and a larger design effect signals more to gain from modeling it.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.23827) | 2026-11-19
