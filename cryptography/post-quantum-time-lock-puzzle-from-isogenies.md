---
title: "Post-Quantum Time-Lock Puzzle from Isogenies"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2306"
summary: "We construct the first (conjectured) post-quantum Time Lock Puzzle (TLP) from isogenies. Our construction avoids setup/preprocessing and achieves non-trivial efficiency, where puzzle generation runs i"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

We construct the first (conjectured) post-quantum Time Lock Puzzle (TLP) from isogenies. Our construction avoids setup/preprocessing and achieves non-trivial efficiency, where puzzle generation runs in time sqrt{T} . We prove security in the quantum random oracle model (QROM) under a new conjecture about the sequentiality of isogeny pushforward computations, for which we provide a thorough justification. The only other (conjectured) post-quantum TLP constructions rely on heavy cryptographic machinery from lattice-based assumptions. We also provide, to the best of our knowledge, the first proof-of-concept implementation of a candidate post-quantum TLP. On an Apple M3 CPU, for a one-hour target delay, total puzzle generation, including setup, takes 2.9 minutes serially and 100.5 seconds with four generation workers. Our experiments demonstrate the practicality of the complete design and show that the quadratic gap between puzzle generation and solving in theory also translates into a meaningful concrete separation. As a stepping stone towards our main result, we provide a new TLP from isogenies in the preprocessing model from a combination of the sequentiality of isogeny walks in the F_{p^2} graph and the hardness of computational Diffie-Hellman (CDH) over cyclic prime-order groups. This improves the assumptions underlying the only known TLP from isogenies in the preprocessing model, which required pairing based assumptions instead of just discrete log. We further adapt this construction to achieve non-trivial efficiency of sqrt{T} in puzzle generation without setup/preprocessing.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2306) | 2026-10-02
