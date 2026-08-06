---
title: "Distributed Monotone Policy Encryption with Stronger Security for DNFs and Threshold Policies from Lattices"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1609"
summary: "Distributed monotone-policy encryption (DPE) lets each user sample and publish its own key, after which anyone can encrypt to a list of published keys under a monotone access policy that determines wh"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Distributed monotone-policy encryption (DPE) lets each user sample and publish its own key, after which anyone can encrypt to a list of published keys under a monotone access policy that determines which coalitions can decrypt. Silent threshold encryption is the t-out-of-N special case. What makes the primitive non-trivial is compactness, where the ciphertext stays sublinear in the policy description. Every post-quantum DPE scheme so far settles for selective security, fixing the challenge policy and the corrupted positions before setup, and complexity leveraging cannot close the gap without giving up compactness. The one DPE scheme known in the stronger static model, where the policy and the placement of malicious keys are chosen adaptively, relies on witness encryption (Devadas-Jain-Waters-Wu, Asiacrypt'25). We give the first statically secure DPE schemes from falsifiable lattice assumptions. For DNF policies, ciphertexts are of size mathsf{poly}(lambda, log N), independent of the number and widths of the clauses, and public keys, secret keys, and partial decryptions are of size mathsf{poly}(lambda). For t-out-of-N threshold policies, ciphertext of size au^6 dot mathsf{poly}(lambda) for au = min(t^2, N - t), improving to au^2 dot mathsf{poly}(lambda) given a common reference string. We prove security under decomposed LWE, and the improved threshold parameters under succinct LWE, in the random oracle model. Our constructions generalize the equivocal encryption framework of Goyal-Yadugiri to policies. We define equivocal DPE, which simulates public keys and partial decryptions and withholds the equivocation trapdoor while releasing the public coins that accompany a ciphertext, and compiles to static DPE with no loss in parameters.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1609) | 2026-08-04
