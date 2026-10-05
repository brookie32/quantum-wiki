---
title: "Trapdoor Projective Sampling and Identity-Based Anonymous Broadcast"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2334"
summary: "In anonymous broadcast encryption, a ciphertext hides both the message and the set of recipients. In the general case, a lower bound of Kiayias and Samari forces the ciphertext to grow linearly with t"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

In anonymous broadcast encryption, a ciphertext hides both the message and the set of recipients. In the general case, a lower bound of Kiayias and Samari forces the ciphertext to grow linearly with the number of recipients, a bound already met by the trivial per-recipient solution. The bounded universe is the setting where anonymous broadcast becomes concise, even asymptotically optimal and as efficient as the underlying public-key encryption. Far from a mere restriction, it is the building block for anamorphic communication against a dictator, where one must reach many (but boundedly many) recipients covertly, as put forth in the DPPY scheme at Eurocrypt '25. DPPY is, however, secret-key anamorphic encryption, where the broadcast layer itself must be hidden. Even a public-key variant does not suffice against a strong adversary, since a per-recipient public key lets a dictator ask for the matching secret key. This motivates hiding identities directly, with no recipient public key published, leading to identity-based anonymous broadcast in the bounded model, the focus of this paper. Technically, projective sampling (Ling, Phan, Stehlé and Steinfeld, LPSS, CRYPTO ’14), the tool underlying concise anonymous broadcast encryption, offers no key extraction: private keys cannot be produced from a projected key fixed in advance. We introduce trapdoor projective sampling that reverses the order of key generation in projective sampling: projected keys are fixed first as hashes of identities and compatible private keys are then preimage-sampled with a trapdoor. Adding a trapdoor is always a challenging objective, and we achieve it by showing that the LPSS projection space can be made far narrower - from m×(m−n) down to m×2n - without breaking the k-LWE security argument, and it is exactly at this width that the projection matrix can be generated with a trapdoor. We formalise the notion of trapdoor projective sampling with new security requirements, instantiate it from k-LWE, and obtain an identity-based anonymous broadcast whose ciphertext is as in LPSS, DPPY schemes. We also extend it to an unbounded identity universe under static corruption, with target sets kept bounded and adaptive.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2334) | 2026-10-04
