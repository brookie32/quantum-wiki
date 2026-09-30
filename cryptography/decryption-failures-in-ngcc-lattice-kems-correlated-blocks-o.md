---
title: "Decryption Failures in NGCC Lattice KEMs: Correlated Blocks, Omitted Compression Noise, and Failure Boosting under a Query Cap"
date: "2026-09-28"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2250"
summary: "The Chinese NGCC post-quantum competition received a family of lattice KEMs whose decryption failure rates (DFRs) are certified by their designers with models that differ in detail. We recompute the f"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

The Chinese NGCC post-quantum competition received a family of lattice KEMs whose decryption failure rates (DFRs) are certified by their designers with models that differ in detail. We recompute the failure probability of the first-round lattice KEMs whose claimed DFR, or a simple recomputation of it, lies near or below the nominal level, and we estimate the offline search for weak ciphertexts under a cap of 2^{64} or 2^{80} decapsulation queries. Three distinct mechanisms are relevant. (i)~Correlated decoding blocks. DTRU decodes 16-coefficient DoubleE_8 blocks; in the tricyclotomic ring Z_q[x]/(x^n-x^{n/2}+1) and the LPPNF ring, the two octets of a block are ring-paired and the repetition code places the same bit on both. Our covariance-aware estimates raise the DFR of six of the seven sets by roughly 50--110 bits. Their estimated uncapped first-failure costs are 2^{85}--2^{111} decapsulations. Under a fitted ciphertext-tail model, DTRU-648, DTRU-768, and DTRU-Prime fit within 2^{64} expected queries after 2^{22}--2^{26} estimated offline encapsulations. (ii)~Omitted compression noise. Cheetah compresses its public key and both ciphertext components. Section~2.2 of the specification omits the public-key term langle e_b,rrangle, while the v-compression error can be treated as a known, ciphertext-dependent shift. Under the coefficient-independence model, exponentially tilted one-dimensional FFTs give DFR estimates of 2^{-79.1} and 2^{-51.8} for Cheetah128 and Cheetah256, rather than the claimed 2^{-129} and 2^{-176}. Their expected random-query waiting times are below 2^{80}. We check the noise model at observable rates on a scaled-down instance and against full-size shallow-tail samples. (iii)~Bounded noise in two-dimensional codes. Rudraksh2 and Scabbard decode coefficient pairs with B2-Minal codes and already evaluate their joint distribution by two-dimensional FFT. We rederive the two-dimensional atoms and evaluate one-dimensional projections onto failure radii of the real decoder. The resulting projected-tail estimates are 2^{-103.9} for Rudraksh2-128-I and 2^{-102.1} for Scabbard-128, a few bits below the claimed 2^{-100} and 2^{-99}. Under a 2^{80} query cap, the estimated classical totals are 2^{112} and 2^{188}, respectively. No attack described here recovers a key. Under the first-failure DFR metric, several estimated costs lie below their nominal levels; the formal far-tail figures remain subject to the modelling, extrapolation, and geometric limitations stated in the paper.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2250) | 2026-09-28
