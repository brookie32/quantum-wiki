---
title: "Properties of the Me Operation and Me-Scalar Multiplication on Elliptic Curves over Finite Fields"
date: "2026-09-11"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1976"
summary: "The M operation was introduced by Yura as an alternative to the max operation appearing in the box-ball system (BBS) to construct a BBS over finite fields. The Me operation is a version of the M opera"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

The M operation was introduced by Yura as an alternative to the max operation appearing in the box-ball system (BBS) to construct a BBS over finite fields. The Me operation is a version of the M operation for an elliptic curve E over a finite field {mathbb F}_p. As with the M operation, the Me operation satisfies the idempotent law and does not satisfy the associative law. Nevertheless, for P,Z in E({mathbb F}_p) and n in {mathbb N}, the 1st Me-scalar multiplication P_{n,Z}^{,I} with auxiliary element Z can be defined. Moreover, for P,Z in E({mathbb F}_p) and n in {mathbb Q}_+, the 2nd Me-scalar multiplication P_{n,Z}^{II} with auxiliary element Z can be defined. This paper shows the following properties that may be useful to construct cryptographic protocols: (P_{n_0,Z}^{,I})_{n_1,Z}^{,I}=(P_{n_1,Z}^{,I})_{n_0,Z}^{,I}, (P_{n_0,Z}^{II})_{n_1,Z}^{II}=(P_{n_1,Z}^{II})_{n_0,Z}^{II}=P_{n_0n_1,Z}^{II}; the 1st MeDLP and the 2nd MeDLP, which are Me versions of the ECDLP, are difficult to solve on classical computers under certain conditions; the 1st MeCDH and the 2nd MeCDH, which are Me versions of the ECCDH, are NOT difficult to solve; and the sequence { P_{n,Z}^{II}:n=1,2,3,ldots } is nonperiodic unless it is constant.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1976) | 2026-09-11
