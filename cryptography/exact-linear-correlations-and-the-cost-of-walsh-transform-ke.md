---
title: "Exact linear correlations and the cost of Walsh-transform key recovery, with application to SPEEDY"
date: "2026-08-21"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1765"
summary: "When two S-box layers of a round are separated by no key addition, the round correlation is a signed sum over all compatible intermediate masks, not a product of layer correlations, so the product rul"
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

When two S-box layers of a round are separated by no key addition, the round correlation is a signed sum over all compatible intermediate masks, not a product of layer correlations, so the product rule can fail in either direction. Our central finding is that evaluating this intra-round sum exactly changes the assessment of the published linear cryptanalysis of SPEEDY, whose two S-box layers are separated only by ShiftColumns. We first develop the linear cryptanalysis of this setting: an exact one-round algorithm with a decidable exactness condition for the product rule, a dependency-graph decomposition, a covering-number bound strengthening linear-trail weight bounds, and a Walsh-support criterion in which the affine dimension of that support, limited by the endpoint key masks, fixes the key-recovery transform cost. Potentials use the independent-round-key model; complexities are in equivalent encryptions. Applied to SPEEDY, these tools revise published results: a reported five-round mask sequence has exact correlation 2^{-90.0962}, not 2^{-93.0147}; the new bound raises the unrestricted five-round weight bound from 53.7714 to 62.2616 bits; and the full-round attack on SPEEDY-7-192 reported at time 2^{158.06} needs at least 2^{199.97} encryptions in the pruning class considered. For SPEEDY-6-192 we give a six-round known-plaintext attack (data 2^{169.84}, time 2^{170.20}, memory 2^{156}) and show that the attack class defined here contains no attack with data and time both at most 2^{128}, its time being at least 2^{136.302}. The same exact evaluation also revises a four-round differential-linear correlation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1765) | 2026-08-21
