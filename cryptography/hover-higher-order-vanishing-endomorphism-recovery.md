---
title: "HOVER: Higher-Order Vanishing Endomorphism Recovery"
date: "2026-08-22"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1778"
summary: "Higher-Order Vanishing (HOV) is a technique for distinguishing Goppa codes, introduced by Hemmert and Wiemers at CRYPTO 2026 and recently extended to McEliece key recovery. We introduce a new variant "
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

Higher-Order Vanishing (HOV) is a technique for distinguishing Goppa codes, introduced by Hemmert and Wiemers at CRYPTO 2026 and recently extended to McEliece key recovery. We introduce a new variant of HOV, HOVER (Higher-Order Vanishing Endomorphism Recovery) that replaces the costly low-rank direction-search phase of HOV with a much faster linear algebra step. Our attack is based on the observation that the first catalecticants of the public HOV kernel define a contraction tensor; HOVER computes the coefficient endomorphisms that preserve all relations of this tensor. In the clean case, this public algebra is F_{2^m}, and the eigenspaces of a field generator are exactly the hidden HOV directions, already ordered by Frobenius. We give a basis-invariant construction, a structural classification of its possible matrix-algebra outputs, and explicit fail-closed acceptance conditions. During our end-to-end public-only experiments, we broke five TII challenge keys, including TII-252, which was the ``highest'' unbroken challenge (by the brute-force labeling metric of the challenge) when discovered. However, our analysis does not indicate HOVER would threaten Classic McEliece parameters in its present form. Lastly, we note that HOVER's main cryptanalytic shortcut was discovered with a large language model, underscoring the strong potential of AI cryptanalysis.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1778) | 2026-08-22
