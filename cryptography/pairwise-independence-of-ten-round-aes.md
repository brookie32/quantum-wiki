---
title: "Pairwise Independence of Ten-Round AES"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2608"
summary: "We prove that ten rounds of AES{} with independent and uniform random round keys are arepsilon_{10}-close to pairwise independent, with [ arepsilon_{10}leqfrac{3017}{2^{141}}<2^{-129}. ] For every two"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

We prove that ten rounds of AES{} with independent and uniform random round keys are arepsilon_{10}-close to pairwise independent, with [ arepsilon_{10}leqfrac{3017}{2^{141}}<2^{-129}. ] For every two distinct plaintexts, the joint ciphertext distribution is therefore within this statistical distance of the uniform distribution on ordered pairs of distinct ciphertexts. The same sampled key tuple is used for both encryptions. The construction retains the AES{} round transformations, including the omission of MixColumns in the final round, with input and output whitening. Let E_{10} denote this random permutation and Omega the set of nonzero differences. We establish the result through the induced one-norm bound norm{Dten-U}_1leq3017/2^{140} on its averaged difference-distribution matrix restricted to Omega, where U projects onto the uniform distribution on Omega. The proof groups the ten rounds into five superbox layers and decomposes the deviation from uniformity into fourteen orthogonal subspaces according to the number of active words and residual factors. Local Gram moments and MDS code constraints control the dependencies between word differences. Bounds for the distributions produced by the first rounds preserve their common source variables, while joint estimates for the last four rounds retain the constraints across two linear layers. The final conversion to statistical distance uses the support size of each component. Exact rational evaluation of the resulting finite recurrence establishes the stated bound.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2608) | 2026-10-23
