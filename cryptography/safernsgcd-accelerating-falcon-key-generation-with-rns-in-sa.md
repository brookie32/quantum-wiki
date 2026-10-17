---
title: "safeRNSgcd: Accelerating Falcon key generation with RNS in SafeGCD"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2507"
summary: "The deepest level of Falcon's NTRU solver needs only one Bézout coefficient from two large integer resultants already represented in a residue number system (RNS). We give mathtt{safeRNSgcd}, which co"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

The deepest level of Falcon's NTRU solver needs only one Bézout coefficient from two large integer resultants already represented in a residue number system (RNS). We give mathtt{safeRNSgcd}, which computes this coefficient while keeping the large states in RNS. Its central insight is that centered explicit CRT can recover the exact low bits needed by SafeGCD batches using single-word fixed-point arithmetic. Integrated into mathtt{ntrugen}, our C implementation reduces inversion and private-key basis-generation costs on a Raspberry Pi 5 and two x86-64 processors, compared with original mathtt{ntrugen} and a variant omitting the unused coefficient.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2507) | 2026-10-16
