---
title: "Zero- Versus Infinite-Temperature Damping in Variational Quantum Circuits: Feature Scale, Sampling Cost, and Frame Gauge"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01466"
summary: "arXiv:2610.01466v1 Announce Type: new Abstract: The Pauli twirl of amplitude damping (AD) is generalized amplitude damping at infinite temperature: it keeps the contraction of AD and removes its non-u"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01466v1 Announce Type: new Abstract: The Pauli twirl of amplitude damping (AD) is generalized amplitude damping at infinite temperature: it keeps the contraction of AD and removes its non-unital term, so comparing the two in variational circuits isolates the zero-temperature bias, which acts mainly through the scale of the features. For random parameters, features under AD settle on a floor, which at strong damping is set by the last layer, has a closed form, and at fixed T_1 falls with temperature as anh(hbaromega/2k_BT); under the twirls they shrink by a constant factor per layer, up to eight qubits. A trainable output scale removes most of the resulting accuracy differences, leaving AD ahead of its twirls by at most about three percentage points in our simulations; what it removes reappears as a cost in measurement shots: trained and tested with 10^3 shots per image, a four-qubit classifier under AD at p=0.3 stays within 1.5 points of noiseless accuracy, while the twirled classifiers lose up to 33. At weaker damping the separation depth grows roughly as (np)^{-1}ln(1/p). The damping direction is a gauge when the damping follows complete entangling layers and the circuit boundaries are trainable; in an eigensolver it becomes physical inside a decomposed two-qubit gate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01466) | 2026-10-02
