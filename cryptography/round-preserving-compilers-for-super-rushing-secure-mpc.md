---
title: "Round-Preserving Compilers for Super-Rushing Secure MPC"
date: "2026-08-20"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1745"
summary: "Practical implementations of synchronous MPC protocols typically require each party to advance to the next round as soon as they have received all expected messages. This deviates from the theoretical"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

Practical implementations of synchronous MPC protocols typically require each party to advance to the next round as soon as they have received all expected messages. This deviates from the theoretical synchronous round-based model, where instead each party advances in the next round after a timeout. To capture this gap between theory and practice, Asharov, Chandramouli, Cohen and Ishai in Eurocrypt 2025 proposed a new model where the adversary is super-rushing. In this, the adversary can see future messages of some honest parties before delivering current-round messages to slower ones. In this work, we study super-rushing security in both the computational and statistical settings, and design round-preserving compilers that transform standard synchronous MPC protocols into ones secure against super-rushing adversaries. Ours is the first work to investigate the security of computational MPC protocols against a super-rushing adversary.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1745) | 2026-08-20
