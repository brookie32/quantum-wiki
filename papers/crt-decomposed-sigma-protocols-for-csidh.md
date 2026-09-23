---
title: "CRT-Decomposed Sigma-Protocols for CSIDH"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.26258"
summary: "arXiv:2609.26258v1 Announce Type: cross Abstract: We construct a zero-knowledge proof of knowledge for the CSIDH group action that exploits the Chinese Remainder Theorem (CRT) structure of the ideal c"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.26258v1 Announce Type: cross Abstract: We construct a zero-knowledge proof of knowledge for the CSIDH group action that exploits the Chinese Remainder Theorem (CRT) structure of the ideal class group, available whenever the group structure is known exactly, as for CSIDH-512. We prove perfect completeness, perfect special honest-verifier zero-knowledge, and 2-special soundness, in which the secret is recovered from two accepting transcripts by one subtraction and one modular inversion per CRT component; no rewinding loop, lattice reduction, or heuristic sampling appears in the extractor. Because each round admits exactly two responses, Unruh's transform yields a non-interactive proof with straight-line extraction in the quantum random oracle model (QROM), removing the multiplicative forking-lemma loss. We instantiate the scheme on the CSIDH-512 class group, verify the algebraic layer by machine over the exact 258-bit modulus (10^4 random instances, all passing), and report protocol-level simulations in the exponent model: Monte Carlo soundness rates matching the proven 2^{-t} bound within 95% confidence at every tested t, serialized signature sizes within 1.6% of the formulas, instrumented action counts, and a scaled meet-in-the-middle attack whose measured cost follows the predicted sqrt{q} law. We further prove two delimiting results: CRT decomposition cannot enlarge the per-round challenge space, and publishing the CRT hop curves lowers classical key-recovery cost from about 2^{128.6} to about 2^{67.3} group action evaluations. The construction is therefore correct and structurally complete today, but quantitatively secure only on future parameters whose class number has large prime factors. We compare against CSI-FiSh, CSI-Otter, and Tanuki; a tightly secure blind signature from this proof of knowledge is left to future work.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.26258) | 2026-09-23
