---
title: "Fast Quantum-Circuit Superoptimization"
date: "2026-09-19"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2115"
summary: "Optimizing quantum circuits is critical: circuits must fit within the resource limits of a quantum computer, and every unnecessary operation increases their cost and probability of failure.We present "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Optimizing quantum circuits is critical: circuits must fit within the resource limits of a quantum computer, and every unnecessary operation increases their cost and probability of failure.We present a simple optimization algorithm for quantum circuits that (1) is very fast, (2) scales to millions of operations, and (3) matches or outperforms the optimization quality of the best existing optimizers and superoptimizers. Our key insight is that we can compactly represent circuit equivalence classes as a map which associates a projective unitary with a smallest representative circuit implementing it. We give a sound algorithm for synthesizing such maps, which we call minimal unitary representative maps (MURMs). Armed with a MURM, our optimizer inspects every bounded subcircuit in a linear pass and replaces it with a minimal variant. Incremental computation and symbolic arithmetic make every replacement fast and sound. Our evaluation shows that our approach achieves significantly greater circuit reductions than leading optimizers, runs orders of magnitude faster, and scales to circuits with millions of operations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2115) | 2026-09-19
