---
title: "Forging Encrypted Linear Checksums in Verifiable FHE: A Cryptanalysis of DataSeal"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3047"
summary: "DataSeal (IEEE S&P 2025) gives an FHE evaluator encrypted secret linear checksums. We study whether it can use them to make an incorrect output pass verification. Each of DataSeal's two published matr"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

DataSeal (IEEE S&P 2025) gives an FHE evaluator encrypted secret linear checksums. We study whether it can use them to make an incorrect output pass verification. Each of DataSeal's two published matrix checks separately admits substitution of a different public function without ciphertext multiplication. Even when both checks are enforced, two independent authenticated input columns yield a nonzero checksum-preserving error with probability 1-q^{-2} over a uniform key, provided the forged circuit decrypts correctly. This attack has multiplication depth one when the input columns are encrypted; public basis columns permit depth-zero attacks. We then analyze a natural repair: adding independent checksum rows. For tge2 rows, we bound the success probability of fixed-coefficient affine attacks and give nearly matching public-vector constructions of order q^{-(t-1)}. Extra rows reduce success in this class, but exposing encrypted tags costs approximately one row of protection relative to blind rank-one errors. With t+1 independent authenticated vectors, a cofactor attack succeeds with probability at least 1-1/(q(q-1)) if its circuit decrypts. Its depth is lceillog_2(t+1)rceil for encrypted vectors. For public vectors, depth lceillog_2trceil is necessary and sufficient for universal polynomial cancellation in our fixed-coefficient model and field range; partial cofactors characterize intermediate attacks. Independent SEAL/BGV runs execute the DataSeal forgeries and selected multi-row circuits, including a depth-two three-row cofactor. A parameter study finds settings where honest workloads decrypt but an added depth-one forgery fails, while depth-zero public-basis forgeries still execute. Independent MNIST models show forgeries that pass verification and change predictions. These experiments measure feasibility for our layouts and modulus chains; the authors' unpublished implementation and settings remain untested.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3047) | 2026-11-25
