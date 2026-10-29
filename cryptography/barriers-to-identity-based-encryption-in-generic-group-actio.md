---
title: "Barriers to Identity-Based Encryption in Generic Group-Action Models"
date: "2026-10-28"
updated: "2026-10-29"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2670"
summary: "Identity-based encryption (IBE) is required to support a superpolynomial-size identity space using only polynomial-size public parameters. This compression requirement underlies known barriers to IBE "
last_verified: "2026-10-29"
review_by: "2027-01-27"
stale: false
---

Identity-based encryption (IBE) is required to support a superpolynomial-size identity space using only polynomial-size public parameters. This compression requirement underlies known barriers to IBE in the generic (pairing-free) group model. Cryptographic group actions, motivated prominently by isogeny-based cryptography, support many advanced primitives beyond public-key encryption. However, no generic construction of IBE from the basic group-action interface is known. Existing generic-group barriers do not resolve this question as they do not translate to generic group-action models. We establish the first tight barriers to IBE in two variants of the generic group-action model. In the type-safe generic group-action model, we prove that an IBE scheme with negligible correctness error and n non-origin action-set element-handles in its public parameters can support at most n identities, even for a weak notion of fully selective security. We show that this bound holds irrespective of the number of action-set element-handles in identity secret keys. We further establish that this bound is tight by demonstrating a matching construction. We then extend this tight characterization to a natural class of IBE schemes in the random-representation generic group-action model (including against representation-sensitive adversaries) under conditions ensuring that identity keys retain no hidden action-set encodings and discarded private encodings leave no residual information. We give a natural syntactic condition for the latter property. For actions additionally equipped with an inversion-like twist, we obtain a more general upper bound (including the same tight bound for odd-order actions). Our results provide the first formal evidence that IBE is likely to require additional algebraic structure or non-black-box techniques beyond the generic group-action interface. More broadly, we provide a new framework for proving lower bounds in generic group-action models.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2670) | 2026-10-28
