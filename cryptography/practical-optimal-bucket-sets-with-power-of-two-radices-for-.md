---
title: "Practical Optimal Bucket Sets with Power-of-Two Radices for LFG-Based MSM Algorithms"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2750"
summary: "Fixed point multi-scalar multiplication (MSM) is a major computational component of pairing-based SNARK proof generation. The Luo--Fu--Gong (LFG) framework is a variant of Pippenger's bucket method th"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Fixed point multi-scalar multiplication (MSM) is a major computational component of pairing-based SNARK proof generation. The Luo--Fu--Gong (LFG) framework is a variant of Pippenger's bucket method that uses a multiplier set M and precomputed point multiples to reduce the number of buckets and online point additions. For radix q and a positive multiplier set M, covering all digit residues requires a bucket set of size at least q/(2|M|). Previous constructions approaching this bound based on primitive roots or power-residue classes impose radix restrictions that exclude q=2^c, thereby requiring additional binary-to-radix conversion in software implementations. We present two bucket set constructions for power-of-two radices q=2^c, using the multiplier sets M={1,2,3} and M={1,3}, respectively. Their cardinalities are q/6+O(log q) and q/4+2, respectively, so both asymptotically attain the counting bound q/(2|M|) while allowing efficient radix-digit extraction through shifts and masks. We also present scalar conversion and two methods for handling the leading digit, allowing both constructions to be used within the LFG framework.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2750) | 2026-11-03
