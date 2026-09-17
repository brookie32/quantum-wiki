---
title: "Barely Doubly-Efficient PIR from Quadratic Residuosity"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2034"
summary: "A Private Information Retrieval (PIR) scheme allows a client to retrieve data from a database hosted on a remote server without revealing which location is being accessed. In Doubly-Efficient PIR (DEP"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

A Private Information Retrieval (PIR) scheme allows a client to retrieve data from a database hosted on a remote server without revealing which location is being accessed. In Doubly-Efficient PIR (DEPIR), the server preprocesses the database offline into a data structure that enables it to answer any client query in sublinear time with respect to the database size n. Lin, Mook, and Wichs (STOC 2023) presented the first DEPIR, from RLWE, and Lee (Crypto 2026) gave a barely doubly-efficient scheme from LWE in the CRS model, answering each query in o(n/log n) time. These are essentially the only constructions known, and both rest on lattices. Whether DEPIR could be realized from non-lattice-based foundations, particularly from number-theoretic assumptions, remained in doubt. In this work, we construct a DEPIR scheme from quadratic residuosity in the CRS model, answering each query in o(n/log n) time. As in Lee's LWE-based construction, our scheme leverages Williams's matrix-vector multiplication preprocessing (SODA 2007). Privacy follows from the pseudorandomness of Legendre symbols under quadratic residuosity, proved by Corrigan-Gibbs and Wu (TCC 2025). To cope with a new modulus at every query, we additionally develop a data structure that reduces a preprocessed integer modulo any modulus in sublinear time.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2034) | 2026-09-15
