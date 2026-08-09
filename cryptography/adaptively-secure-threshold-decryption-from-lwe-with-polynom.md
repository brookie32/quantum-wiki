---
title: "Adaptively Secure Threshold Decryption from LWE with Polynomial Modulus"
date: "2026-08-06"
updated: "2026-08-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1627"
summary: "Threshold Decyption (TD) enables a set of decryptors, each holding a secret key share, to collaboratively decrypt ciphertexts. Lots of TD schemes consider only CPA security under static corruptions, b"
last_verified: "2026-08-09"
review_by: "2026-11-07"
stale: false
---

Threshold Decyption (TD) enables a set of decryptors, each holding a secret key share, to collaboratively decrypt ciphertexts. Lots of TD schemes consider only CPA security under static corruptions, but a stronger and more reasonable security notion in practice is CCA security under adaptive corruptions, which enhances the ability of adversaries to obtain partial decryptions of chosen ciphertexts and adaptively corrupt decryptors during the protocol. There are many works on TD from lattices, seeking for post-quantum security. However, none of these TD schemes achieves both adaptive security (i.e., security under adaptive corruptions) and polynomially-bounded modulus in lattices. Given the fact that polynomial modulus provides more post-quantum confidence than super-poly modulus, Devevey et al. [PKC 2021] left constructing an adaptively secure TD with polynomial modulus from lattices as an open problem. In this paper, we resolve the above open problem by proposing three adaptively secure (t,N)-TD schemes based on the LWE assumption, all with polynomial modulus under appropriate settings. - TD0: an adaptively CPA-secure scheme in the asynchronous setting in the standard model, whose modulus is polynomial for small number of users N. - TD1: an adaptively CCA-secure scheme in the asynchronous setting in the standard model, whose modulus is polynomial for small N and bounded decryption queries. - TD2: an adaptively CCA-secure scheme in the synchronous setting in the random oracle (RO) model, whose modulus is polynomial for bounded decryption queries. The main technical challenge is to limit the leakage of secret key shares arising from decryption queries, while keeping the modulus a polynomial. To overcome this barrier, we develop a refined polynomial noise flooding technique based on a detailed min-entropy analysis of secret shares conditioned on linear matrix hints, leveraging recent advances on Matrix-Hint LWE. Based on our new technique, we build TD1 using the replicated secret sharing (RSS) scheme, hence supporting only small N. To enable larger N, we design TD2 using the Shamir secret sharing scheme, in which we further integrate our new technique with the zero-sum masking technique [Katsumata et al., CRYPTO 2024] to restrict the secret key leakage. To the best of our knowledge, our TD1 and TD2 are the first non-interactive lattice-based threshold decryption schemes achieving adaptive CCA security and polynomial modulus, simultaneously. Moreover, they achieve the strongest notion of adaptive CCA security among those compared in [Brzuska et al., PKC 2026]. We further establish robustness for both TD0 and TD1 via publicly verifiable partial decryptions, ensuring that the combination either outputs the correct plaintext or aborts.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1627) | 2026-08-06
