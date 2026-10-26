---
title: "Cryptanalysis and Repair of 'Decentralized Multi-authority ABE for NC^1 from BDH'"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2642"
summary: "We present a plaintext-recovery attack on both the DBDH-based construction and the CBDH-based variant of Datta, Komargodski, and Waters (Journal of Cryptology, 2023). The attack succeeds with probabil"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

We present a plaintext-recovery attack on both the DBDH-based construction and the CBDH-based variant of Datta, Komargodski, and Waters (Journal of Cryptology, 2023). The attack succeeds with probability one in the claimed static security model using one corrupt authority and two users, each unauthorized even when granted the corrupt authority's attribute. The flaw is an invalid extension of the LSSS matrix-normalization lemma originating with Rouselakis and Waters (FC,~2015): preserving complete-share distributions does not preserve coordinate-wise ciphertext masks, which a corrupt authority can expose to remove identity binding from other users' shares. For both variants, replacing these masks with independent full linear sharings of zero preserves correctness and restores ciphertext-distribution invariance. We prove static security of both repaired variants in the random oracle model under their respective BDH assumptions, using the original hardcore-bit convention for the CBDH variant. Both proofs allow adaptive identity-hash queries. The modification retains the original matrix-width and row-labeling restrictions, keys, decryption, and ciphertext size, requiring only additional encryption randomness and finite-field arithmetic. We also attack both multi-authority attribute-based inner-product functional encryption constructions of Datta and Pal (PKC, 2023) and establish correctness and matrix-substitution invariance of the same repair. We prove static security of the repaired small-universe construction under asymmetric DBDH. For the large-universe construction, we identify a missing source-group encoding in the original reduction and give a complete static security proof under an augmented L-DBDH assumption, whose generic bilinear group hardness we establish.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2642) | 2026-10-26
