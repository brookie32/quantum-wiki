---
title: "New IND-CPA-D Attacks on BFV and BGV"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2546"
summary: "IND-CPA-D security is an extension of IND-CPA security introduced in the context of Fully Homomorphic Encryption (FHE). It captures the situation where the computation result is known to the adversary"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

IND-CPA-D security is an extension of IND-CPA security introduced in the context of Fully Homomorphic Encryption (FHE). It captures the situation where the computation result is known to the adversary; it is in particular necessary for FHE with threshold decryption. This work presents three new attacks in this situation on the BFV and BGV FHE schemes, when their parameters are instantiated with heuristic assumptions commonly used to enable correctness. We first extend the bootstrapping failure attacks from Cheon et al. [CCS'24] on the DM/CGGI and CKKS schemes, to both BFV and BGV. We focus on BGV when instantiated with the so-called powerful-basis representation of ring elements. The second attack relies on skewing the ciphertext noise in BFV, making it outpace the heuristic noise bounds for plaintext-ciphertext multiplications. This is achieved by crafting plaintexts, for which the noise bounds do not hold. The third and last attack focuses on outpacing the noise growth in BFV ciphertext-ciphertext multiplications. For this purpose, we skew the mask part of the ciphertext by selecting a random encryption of zero, whose addition yields a ciphertext with a sufficiently large mask norm. While the first two attacks successfully recover the secret key, the last attack instead breaks the IND-CPA-D indistinguishability game. We report experiments on all these attacks, based on the HElib and OpenFHE libraries, respectively, for BGV and BFV. Notably, the second attack implemented in OpenFHE fully recovers the secret key in a few minutes to a few hours, depending on the parameters.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2546) | 2026-10-19
