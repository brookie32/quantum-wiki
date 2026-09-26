---
title: "Multi-Key FHE Almost as Fast as Single-Key FHE"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2195"
summary: "Multi-key fully homomorphic encryption (MKFHE) supports homomorphic computation over ciphertexts encrypted under independently generated keys. Known constructions accommodate independent keys by expan"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

Multi-key fully homomorphic encryption (MKFHE) supports homomorphic computation over ciphertexts encrypted under independently generated keys. Known constructions accommodate independent keys by expanding every ciphertext under the concatenation of the participating secret keys, and then evaluating the circuit in that expanded dimension. A concatenated key is N times longer than an individual key, so the ciphertext on each wire and the running time of each gate grow with N, the number of users. Lopez-Alt, Tromer, and Vaikuntanathan, who introduced MKFHE, asked for a scheme in which all algorithms are independent of N. More than a decade later, no MKFHE scheme has a homomorphic evaluation whose cost is even sublinear in N. We construct the first MKFHE whose homomorphic evaluation asymptotically matches that of single-key FHE, while users still generate their keys and encrypt independently and the participating set is chosen only after encryption. We insert a public, deterministic, and non-interactive preprocessing phase between encryption and evaluation: key aggregation combines the selected public keys, and ciphertext preparation converts each independently encrypted input into a short single-key ciphertext under a virtual key, namely the sum of the participating secret keys. Evaluation then runs on ordinary single-key ciphertexts, so every wire ciphertext, every gate, and the decryptable output are independent of N. We give two instantiations, a leveled GSW-based scheme over Z_q from standard LWE and a leveled BFV-based scheme over cyclotomic rings from circular Ring-LWE. Both retain single-round distributed decryption with statistically simulatable partial decryptions, where the published key material grows with N. As a proof of concept, we implement our ring-based construction in Go. For 32 users, its multiplication is 275.13imes and 45.50imes faster than CDKS and KKLSS, and its ciphertexts are 16.5imes smaller than both.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2195) | 2026-09-23
