---
title: "Concrete Security Assessment of Isogeny-based Cryptography with the new Isogeny-Path algorithm"
date: "2026-08-27"
updated: "2026-08-28"
source: "agent"
category: "networking"
tags: [networking, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1821"
summary: "Very recently, Wesolowski (ePrint 2026/1486) proposed a heuristic algorithm for solving the supersingular isogeny-path problem in time and memory (p^{1/3+o(1)}), where (p) is the characteristic of the"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

Very recently, Wesolowski (ePrint 2026/1486) proposed a heuristic algorithm for solving the supersingular isogeny-path problem in time and memory (p^{1/3+o(1)}), where (p) is the characteristic of the underlying field. Although this constitutes an asymptotic improvement over the previous best-known complexity of (p^{1/2}log^{O(1)}(p)), its concrete impact on the security of isogeny-based cryptographic schemes, particularly SQIsign, remains unclear due to the superpolynomial overhead hidden in the (p^{o(1)}) factor and the algorithm's exponential memory requirement. In this work, we assess the concrete cost of Wesolowski's attack, study its time--memory tradeoffs, and investigate optimizations based on the van Oorschot--Wiener (vOW) technique. Our analysis shows that, over the practical memory ranges considered, neither the optimized full-list attack nor its vOW variants outperform the previous state-of-the-art low-memory algorithm for computing supersingular endomorphism rings. We further study quantum claw-finding improvements. While Grover search can essentially remove the large memory requirement, it offers little improvement in running time, whereas Tani's algorithm provides a stronger gate--memory tradeoff at the cost of substantial coherent quantum memory. Overall, our results show that the asymptotic (p^{1/3+o(1)}) improvement does not directly translate into a comparable reduction in concrete security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1821) | 2026-08-27
