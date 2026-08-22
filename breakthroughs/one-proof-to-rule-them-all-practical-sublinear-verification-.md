---
title: "One Proof to Rule Them All: Practical, Sublinear Verification for Actively Secure MPC on Z_{2^k} with Dishonest Majority and a Dealer (Full Version)"
date: "2026-08-19"
updated: "2026-08-22"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1741"
summary: "Towards bridging the gap between passively and actively secure multiparty computation (MPC), the use of sublinear distributed zero-knowledge (DZK) proofs gained popularity. Such proofs enable extendin"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

Towards bridging the gap between passively and actively secure multiparty computation (MPC), the use of sublinear distributed zero-knowledge (DZK) proofs gained popularity. Such proofs enable extending a passively secure protocol by adding a verification step whose communication is sublinear in the circuit size. For arbitrarily many parties and a dishonest majority, adding a trusted dealer enables efficient computation, as recently shown by Asterisk (IEEE S&P'24) without requiring DZK. This setting is also compatible with DZK, as shown by Boyle et al. (CRYPTO'21). Unfortunately, their approach is not tailored to computation over a ring Z_{2^k}, often favored for concrete efficiency and practicality, resulting in high computational overhead. In the honest majority setting with few parties, Li et al. (CCS'24) optimized DZK to rings, achieving significant performance improvements. In this work, we propose the first sublinear verification protocol that is both, designed for the n-party dishonest majority setting with a dealer, and tailored to computation over a ring Z_{2^k}, combining and improving upon both approaches above. Previous approaches used n DZK proofs to check correct behavior for each individual party. Instead, we show how to verify in a single, novel DZK proof that all parties together behave correctly. This decreases the communication complexity for verification from O(n dot log m) to O(n + log m) ring elements per party for m multiplications. Hence, for the first time, active security using DZK scales well with the number of parties n. We provide the first public implementation for DZK with arbitrary n and a dealer and show its practical efficiency. For m=10^6 multiplications across 30 layers, communication increases by only 0.7% over the passively secure base protocol with only moderate computation overhead. This becomes especially useful in a WAN setting, where we achieve active security at only 34% run time overhead over the passive variant. Compared to Asterisk (IEEE S&P'24), our protocol has 1.8x better communication and improves run time by 2.5x in WAN and 11.9x in LAN.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1741) | 2026-08-19
