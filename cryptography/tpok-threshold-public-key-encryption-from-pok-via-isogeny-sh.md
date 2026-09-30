---
title: "TPOKÉ: Threshold Public-Key Encryption from POKÉ via Isogeny Sharing"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2243"
summary: "POKÉ, introduced by Basso and Maino, is one of the most efficient isogeny-based public-key encryption schemes. The generic parallel-encryption approach yields a (t,n)-threshold variant by running n in"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

POKÉ, introduced by Basso and Maino, is one of the most efficient isogeny-based public-key encryption schemes. The generic parallel-encryption approach yields a (t,n)-threshold variant by running n independent POKÉ instances and secret-sharing the message, but this multiplies the public-key and ciphertext sizes by roughly n. We present S-TPOKÉ, a POKÉ-based (t,n)-threshold construction for every 1le tle n, and Ch-TPOKÉ, an (n,n) variant that arranges the parties' secret isogenies differently. Both schemes avoid repeating part of the isogeny computation that appears in every independent POKÉ instance. Compared with the trivial construction, they reduce the number of degree-3^{b} isogenies computed during encryption from 2n to n+1 and reduce the ciphertext size by about a factor of two when n is large. The two schemes differ in how the parties' secret isogenies are arranged. S-TPOKÉ is our main construction: the dealer samples n independent secret isogenies, while encryption samples one sender-side secret isogeny and shares it across the parties. Ch-TPOKÉ instead arranges the parties' secret isogenies into a chain. For S-TPOKÉ, we prove SIM-CPA security under static corruption in the random oracle model from the (k,n)-S-C-POKE assumptions for all 1le kle t, which extend C-POKE to the threshold setting. For Ch-TPOKÉ, we prove only SIM-CPA security under static maximal corruption from the (j,n)-Ch-D-POKE assumptions for all jin{1,ldots,n}, which extend D-POKE to a chain-based threshold setting. This guarantee is strictly weaker than SIM-CPA security under static corruption. We also give asymptotic parameter choices targeting lambda-bit security and derive closed-form expressions for the public-key, ciphertext, and partial-decryption sizes in terms of lambda and n.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2243) | 2026-09-28
