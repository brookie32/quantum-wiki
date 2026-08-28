---
title: "Atom: Single-Server Private Information Retrieval with Low Communication and Fast Computation"
date: "2026-08-27"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1813"
summary: "Private information retrieval (PIR) enables a client to retrieve a record without revealing the index.Among existing PIR protocols with database-independent preprocessing, for each query, the protocol"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

Private information retrieval (PIR) enables a client to retrieve a record without revealing the index.Among existing PIR protocols with database-independent preprocessing, for each query, the protocols with low communication often take from several seconds to tens of seconds, while the faster protocols require hundreds of kilobytes for communication. In this paper, we propose three techniques for different-type ciphertext conversions: (1) the first one is to generate a two-orbit SIMD selector from encrypted bits; (2) the second one is to convert a packed mathsf{RLWE} ciphertext into an aligned monomial mathsf{RGSW} ciphertext; (3) the third one is to produce an arbitrary monomial mathsf{RGSW} ciphertext from encrypted bits. Building on these techniques, we design a new PIR protocol (called Atom), achieving the best of both worlds (i.e., having not only low communication but also fast computation). We implemented Atom and evaluated its performance for 256 B records and databases from 256 MB to 8 GB. Specifically, Atom takes 3.0 sim 3.8 KB of online communication (i.e., the total communication, excluding the setup phase that can be run only once and reused for multiple queries), and takes 0.4 sim 5.0 seconds per query. Compared to the state-of-the-art KsPIR (CCS'24), Atom reduces the online communication cost by a factor of 40.5imes sim 51.3imes, while its running time is comparable to KsPIR (0.2 sim 5.2 seconds per query).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1813) | 2026-08-27
