---
title: "Provable dual attack on LWE via lattice projection"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2117"
summary: "The Learning with Errors (LWE) problem is a cornerstone of post-quantum cryptography, and the dual attack is a central tool for evaluating its concrete hardness. In provable dual attacks, a major bott"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

The Learning with Errors (LWE) problem is a cornerstone of post-quantum cryptography, and the dual attack is a central tool for evaluating its concrete hardness. In provable dual attacks, a major bottleneck is the large number of discrete Gaussian samples required over the dual lattice. While recent works have focused on accelerating the guessing step via modulus switching, the sampling bottleneck has remained largely unoptimized. In this paper, we address this issue from a new perspective. First, we observe that Banaszczyk's inequality can be significantly improved when the first minimum of the lattice is suitably large. This yields a refined distinguishing inequality, which provides sharper conditions for attack success. Second, we propose a new provable dual attack framework based on lattice projection. Instead of sampling over the entire dual lattice, we sample over a carefully chosen sublattice, whose dual is the projection of the primal lattice onto a lower-dimensional subspace. This reduces the lattice dimension and thus substantially accelerates discrete Gaussian sampling. We rigorously analyze the parameter conditions for the success of our framework, and by enumerating all feasible parameters we achieve an improvement of 26.1--43.7 bits over the original provable dual attack framework.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2117) | 2026-09-20
