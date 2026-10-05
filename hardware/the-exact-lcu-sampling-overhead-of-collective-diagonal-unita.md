---
title: "The exact LCU sampling overhead of collective diagonal unitaries: resonances and a continued-fraction dichotomy"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03595"
summary: "arXiv:2610.03595v1 Announce Type: new Abstract: We consider the cost of implementing the quadratic collective phase e^{-igamma K^2}, with K a collective observable of evenly spaced spectrum, such as t"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03595v1 Announce Type: new Abstract: We consider the cost of implementing the quadratic collective phase e^{-igamma K^2}, with K a collective observable of evenly spaced spectrum, such as the permutation-symmetric Hamming weight. This gate is the cardinality-penalty layer of constrained quantum optimization, the one-axis-twisting gate of spin squeezing and the Kerr phase of a bosonic mode. Instead of two-qubit gates, it can be sampled as a linear combination of single-qubit rotation layers (an LCU) at an overhead Gamma. We determine the minimal overhead. Ancilla-free sampling of the layers reproduces the target's outcome probabilities up to this factor, and no smaller factor works for every input; when K is permutation symmetric, arbitrary single-qubit gates do no better. The minimal overhead's growth with the register size n is set by the continued fraction of gamma/pi: rational angles pi p/q in lowest terms cost exactly Gamma=q for every nge2q-2; the cost is Theta(n) if and only if gamma/pi is badly approximable; and a master formula, proved two-sided near low-denominator rationals, reads it off the nearest one. Without the symmetry the cost over single-qubit gates can be exponential: for the binary-weighted K=sum_j2^jx_j the squaring phase of Fourier arithmetic on m qubits costs at least 2^{0.557m-O(1)}, beyond the 2^{m/2} ceiling of every cut bound, by a new certificate-lifting argument. The Fourier-based LCU of Carrera Vazquez, Egger and Woerner (2026), which guarantees Gammale n+1, is optimal up to a constant factor at typical angles at fixed n; at rational angles the unique optimizer is the fractional-revival decomposition of Kerr optics, a recipe independent of n. In bosonic simulation, the Kerr-gate phase-shifter decomposition of Upreti, Quesada and Chabaud (2026) is the unique optimum over phase shifters, and a finite-cost one exists only at rational gamma/pi.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03595) | 2026-10-05
