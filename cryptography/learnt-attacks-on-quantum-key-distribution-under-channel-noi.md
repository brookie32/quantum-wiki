---
title: "Learnt Attacks on Quantum Key Distribution under Channel Noise and Device Drift"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01792"
summary: "arXiv:2610.01792v1 Announce Type: new Abstract: Quantum key distribution (QKD) links are provisioned from security analyses of stationary channels, whereas the devices that determine the channel drift"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01792v1 Announce Type: new Abstract: Quantum key distribution (QKD) links are provisioned from security analyses of stationary channels, whereas the devices that determine the channel drift between recalibrations. Whether an eavesdropper who cannot alter the channel's own noise gains by following that drift has not been quantified. Adaptive eavesdropping is posed here as a constrained Markov decision process in which the attacker selects one circuit per round while the noise level follows an Ornstein--Uhlenbeck process and the abort condition is a budget over each block of rounds. The value of adaptation is bounded by the best fixed circuit and a dynamic-programming upper bound. The actions are learnt attacks. Whereas Decker et al. trained a parametrised circuit on a fixed gate template against a fixed channel, here the gate structure and rotation angles are searched jointly. This yields circuits compact enough to form a discrete action set, extending the construction to noise models lacking a known template, including the amplitude damping channel. On device-independent E91 under bilateral depolarising noise, a reinforcement-learning attacker raises her Holevo information from 0.135 for the best fixed circuit to 0.348 at zero detection, 98% of the upper bound. On BB84 under a drifting bit-flip channel, she exceeds a conservative noise-indexed rule by 0.024 in fidelity, reaching 99% of the upper bound. Under stationary noise, the attacker's gain from basis asymmetry changes sign between an averaged and a per-basis error-rate constraint. The search, started from random gate sequences, recovers the analytical cloners and the collective-attack key rate, and meets the lower bound of the Winick--Lutkenhaus--Coles objective from above.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01792) | 2026-10-02
