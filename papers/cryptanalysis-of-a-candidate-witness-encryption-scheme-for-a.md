---
title: "Cryptanalysis of a Candidate Witness Encryption Scheme for Aﬃne Determinant Programs"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1583"
summary: "At ITCS 2020, Bartusek, Ishai, Jain, Ma, Sahai, and Zhandry proposed a framework for witness encryption based on affine determinant programs, together with a concrete instantiation using their formula"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

At ITCS 2020, Bartusek, Ishai, Jain, Ma, Sahai, and Zhandry proposed a framework for witness encryption based on affine determinant programs, together with a concrete instantiation using their formula-based All-Accept encoding. Yao, Chen, and Yu later broke the separate ADP-based indistinguishability-obfuscation candidate, while noting that their attack did not apply to witness encryption. We give a deterministic polynomial-time attack that recovers the encrypted bit from the public ciphertext matrices of this concrete instantiation. It covers every qgeq1 in the theorem’s recovery range, including q(n)=lceil n^arepsilonrceil for all sufficiently large n. Outside a fixed finite set of primes, it applies to every SUBSET-SUM instance whose coefficient vector is nonzero modulo p and that has no Boolean solution modulo p. On an explicit efficiently generated family of integer NO instances, the encrypted bit is recovered with probability 1-negl(n) under the field-size convention of the original paper.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1583) | 2026-08-03
