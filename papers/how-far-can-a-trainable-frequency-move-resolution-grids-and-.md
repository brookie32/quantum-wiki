---
title: "How Far Can a Trainable Frequency Move? Resolution, Grids and Coupling in Trainable-FrequencyQuantum Models"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.23409"
summary: "arXiv:2602.23409v4 Announce Type: replace-cross Abstract: Trainable-frequency quantum models train the prefactors of their encoding gates so that the circuit's frequencies can move onto the target's. "
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2602.23409v4 Announce Type: replace-cross Abstract: Trainable-frequency quantum models train the prefactors of their encoding gates so that the circuit's frequencies can move onto the target's. From the unit start of prior work, training rarely reaches a target more than one resolution step away. We show that the target-driven part of the prefactor gradient is a weighted sum of slopes of the overlap sin u/u, where u is the model-target frequency distance scaled by the window half-width. This gives each frequency a reach: under gradient flow, an isolated real frequency whose coefficient adapts optimally reaches its target from within half a step, for every target at least one step from zero frequency; with a fixed coefficient, a phase-dependent barrier can stop it. A ternary prefactor grid places a model frequency within half a step of every band frequency, with logarithmically many encoding gates. Single-frequency circuits trained with Adam and jointly trained amplitudes behave as predicted: inside the first side lobe, a frequency starts toward its target exactly when in phase with it in 98% of runs, and only 11 of 768 frequencies starting beyond the lobe reached their target. With several frequencies, the grid start raised successful fits on synthetic targets from 69% to 84% against the best random start. With many target frequencies, least squares on the fixed grid fits near-perfectly, but the circuit does not reach the coefficients; training the prefactors narrows this shortfall, but with 8 and 24 target frequencies, training the fixed grid ten times longer fitted better. On real series, training the frequencies improved held-out R^2 at equal budget by 0.010--0.045 on four of seven series, but a classical screen did not separate these from the others. A classical model with independently trainable frequencies shows the same dependence on the start; our results describe how to train such models, not an advantage of the circuit.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.23409) | 2026-11-06
