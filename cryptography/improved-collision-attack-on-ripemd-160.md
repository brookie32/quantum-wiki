---
title: "Improved Collision Attack on RIPEMD-160"
date: "2026-08-20"
updated: "2026-08-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1744"
summary: "RIPEMD-160 is an ISO/IEC hash function standard based on the Merkle-Damgård structure with a double-branch compression function. There have been many attempts at modular differential attacks on reduce"
last_verified: "2026-08-22"
review_by: "2026-11-20"
stale: false
---

RIPEMD-160 is an ISO/IEC hash function standard based on the Merkle-Damgård structure with a double-branch compression function. There have been many attempts at modular differential attacks on reduced RIPEMD-160, with the best previous result being a 40-step practical collision attack achieved in 2023. That attack constructs a simple local collision in round 2 of the left branch to minimize uncontrolled conditions. To achieve this, differences must be introduced into many message words, which constrains the maximum number of steps that can be attacked. To overcome this limitation and target more steps, we propose a new differential characteristic structure that abandons the sparse local collision in round 2 and instead uses a single continuous differential characteristic spanning rounds 1 to 2 for each branch. This structure allows us to inject a difference into only one message word. Using an automatic search tool based on the high-performance parallel SAT-solver PRS, we identify suitable differential characteristics by imposing more control over conditions, differences, and the probability of proper propagation. Based on the differential characteristics, we identify three colliding message pairs for 42-step RIPEMD-160 with theoretical time complexity of approximately 2^{47.4}, thereby improving the best practical collision attack by 2 steps on this hash function.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1744) | 2026-08-20
