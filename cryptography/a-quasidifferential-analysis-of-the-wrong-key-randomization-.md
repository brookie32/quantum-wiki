---
title: "A Quasidifferential Analysis of the Wrong-Key Randomization Hypothesis"
date: "2026-08-31"
updated: "2026-09-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1848"
summary: "The Wrong-Key Randomization (WKR) hypothesis governs data-complexity estimates in differential cryptanalysis: wrong-key guesses are assumed to behave as a random permutation would. Exact computation o"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

The Wrong-Key Randomization (WKR) hypothesis governs data-complexity estimates in differential cryptanalysis: wrong-key guesses are assumed to behave as a random permutation would. Exact computation of fixed-key differential probabilities was, until recently, infeasible. We use quasidifferential trails to compute the exact wrong-key distribution for the key-recovery map (G_{k,k'} = F_{k'}^{-1}!irc F_k) in PRESENT-like SPNs. A mask-first reformulation exposes a Walsh--Hadamard structure; restricting the transform to the low-dimensional support, together with SMT-guided trail enumeration, reduces the cost: for a 16-bit toy cipher, from~(2^{80}) to~(2^{13}); for presentCipher, from~(2^{192}) to~(2^{30}); and for GIFT, from~(2^{192}) to~(2^{32}). For the toy cipher, PRESENT and GIFT, the computed distribution is a structured mixture: a large zero-probability class coexists with bottleneck classes orders of magnitude above the random-permutation mean, and nothing lies between them. Such a distribution is not unimodal, so no Poisson or binomial law fits it for any parameter and the hypothesis is formally false for all three targets. For PRESENT, however, we show that this deviation does not affect the security of Wang's 14-round differential attack. We cast the computed distribution as a structured composite hypothesis---the differential counterpart of the random-permutation/composite-hypothesis model used for wrong keys in linear cryptanalysis--and show that the shape of the wrong-key distribution, not merely its mean, governs how many wrong keys survive the key-recovery filter. For PRESENT with Wang's distinguisher, the structural signal is carried only by the right pairs, whose weight is too small for the deviation to surface; the hypothesis remains a safe heuristic in this case despite being formally false. Our SMT-based enumeration tool is publicly available.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1848) | 2026-08-31
