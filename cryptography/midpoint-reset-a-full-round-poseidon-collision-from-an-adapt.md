---
title: "Midpoint Reset: A Full-Round Poseidon Collision from an Adaptively Chosen MDS Matrix"
date: "2026-08-21"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1760"
summary: "We give an explicit compression collision for all 28 rounds of the KoalaBear Poseidon instance with parameters (t,alpha,R_F,R_P)=(16,3,8,20), in the setting where the round constants are fixed before "
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

We give an explicit compression collision for all 28 rounds of the KoalaBear Poseidon instance with parameters (t,alpha,R_F,R_P)=(16,3,8,20), in the setting where the round constants are fixed before the MDS linear layer is chosen. The main problem is to construct a single linear layer that simultaneously controls two executions through both the full and partial rounds. We do this by tracking their midpoint and half-difference. In each two-round block, one prescribed image of the linear layer cancels the midpoint against the next round constant, so the following odd cubic S-box receives opposite states and resets the midpoint to zero. Two additional images are reused throughout the permutation to return the half-difference to the same one-dimensional subspace. The resulting trajectory constraints determine a linear layer, while a scalar recurrence closes the final difference under feed-forward. For the KoalaBear instance we obtain a collision in all sixteen output coordinates with an MDS matrix satisfying the prescribed linear-layer checks. The scalar construction reduces to low-degree equations and admits a family of parameter choices, so the collision is not an isolated instance. The result exposes an adaptive correlation between fixed round constants and a subsequently chosen linear layer that matrix-only checks do not capture.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1760) | 2026-08-21
