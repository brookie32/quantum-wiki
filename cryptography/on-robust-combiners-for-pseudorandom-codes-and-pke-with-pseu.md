---
title: "On Robust Combiners for Pseudorandom Codes and PKE with Pseudorandom Ciphertexts"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2650"
summary: "Robust combiners are a standard way to hedge cryptographic assumptions: given several candidate constructions, they produce one construction that remains secure as long as one candidate is secure. In "
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

Robust combiners are a standard way to hedge cryptographic assumptions: given several candidate constructions, they produce one construction that remains secure as long as one candidate is secure. In favorable cases, such combiners also yield universal constructions. We ask whether this paradigm applies to cryptographic primitives whose public outputs must be both pseudorandom and sparse. Our first result gives a negative answer for pseudorandom codes (PRCs), i.e., error-correcting codes whose codewords are computationally indistinguishable from uniform strings. We prove that secret-key PRCs admit no black-box robust combiner. The impossibility holds even for the weakest meaningful guarantee, where the combined scheme is required to be secure when all but one candidate PRC are secure. We then show that the obstruction is not specific to error correction. In the sparse ciphertext regime, public-key encryption with pseudorandom ciphertexts also admits no black-box robust combiner. This stands in contrast to ordinary IND-CPA encryption, for which robust combiners are easy to obtain. Thus the requirement that public outputs look uniformly random introduces a genuine barrier to black-box assumption hedging, and rules out the standard combiner route to universal constructions for these primitives.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2650) | 2026-10-26
