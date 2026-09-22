---
title: "SAK: Sparse Arguments of Knowledge, from Sparse Lookup Arguments"
date: "2026-09-21"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2143"
summary: "We formalize and construct sparse arguments of knowledge, where given a length N witness that contains n non-zero values the prover time is O(n) irc o(N). In particular, we achieve a sparse argument o"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

We formalize and construct sparse arguments of knowledge, where given a length N witness that contains n non-zero values the prover time is O(n) irc o(N). In particular, we achieve a sparse argument of knowledge for the customizable constraint system relation, which generalizes circuit-satisfiability. We achieve this by first utilizing sublinear lookup arguments to provably select only the subset of the constraint system that touches the non-zero entries of the variable assignment, and then running a standard argument of knowledge with mild qualifications. Our resulting sparse argument of knowledge is publicly verifiable and supports a universal and updatable setup. It features an O(N log N) preprocessing phase, an O(n log n) prover time, and an O(1) verifier time, improving on the prior O(n log^2 n) and O(n log N) prover time.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2143) | 2026-09-21
