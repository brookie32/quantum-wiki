---
title: "Membership Inference in Privacy-Preserving Vector Search"
date: "2026-10-20"
updated: "2026-10-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2570"
summary: "Vector retrieval increasingly runs over sensitive embedding databases. Backend-compatible protections are desirable in such settings in that they transform the plaintext vectors while leaving the sear"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

Vector retrieval increasingly runs over sensitive embedding databases. Backend-compatible protections are desirable in such settings in that they transform the plaintext vectors while leaving the search algorithm itself unchanged. However, the protected database then leaks some geometry, that is, information about the distances between the stored vectors. We study membership-inference attacks on such leakage given a single database snapshot and known plaintexts. Our central finding is that membership privacy depends on how much geometry is revealed and on whether known plaintexts can be linked to positions in the snapshot, and that the effect of each of these depends on the other. We first break the prior Scale-and-Perturb (SAP) scheme of Fuchsbauer et al. (FGHO, SCN 2022) with no known plaintexts. Empirically, our attack achieves advantage 0.997 on MS-MARCO. We then introduce Rotate-and-Perturb (RAP), a special case of a scheme FGHO call SAP-I and leave unanalyzed. For uniform data on the sphere, we prove perfect membership privacy with no known plaintexts. For fixed noise parameter β ∈ (0, 2], achieving constant advantage requires a number of known plaintext-ciphertext pairs at least logarithmic in the database size, provided that number is below the embedding dimension. Empirically, our attack reaches advantage 0.5 with 3 such pairs at database size 100 and 7 at 100,000 on text embeddings. We also study two more approaches, namely ideal distance-comparison-revealing encryption (DCRE) and an encrypted HNSW index using function-hiding inner-product functional encryption. Ideal DCRE remains vulnerable to known plaintext-ciphertext pairs. On the tested MS-MARCO databases, our attack on the encrypted HNSW index requires knowing 19–32% of the database and their corresponding index vertices to reach advantage 0.5. Finally, we study augmentations to these schemes to mitigate our attacks, shuffling and secret projection. Together, they substantially increase the number of known plaintexts needed by our tested attacks on RAP and comparison-only leakage.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2570) | 2026-10-20
