---
title: "GAUGE: A Formal Framework for Measuring Cryptographic Security under Heterogeneous Adversary Cost Models"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.17281"
summary: "arXiv:2609.17281v1 Announce Type: cross Abstract: Standards bodies report cryptographic security as a single number of bits, but this value depends on the adversary cost model used to price time, memo"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2609.17281v1 Announce Type: cross Abstract: Standards bodies report cryptographic security as a single number of bits, but this value depends on the adversary cost model used to price time, memory, and quantum resources. Different conventions can therefore produce different rankings of cryptographic schemes. GAUGE represents security as a function over admissible cost models, called a security profile. Comparisons then become comparisons between profiles, and ranking reversals become an explicit structural property rather than a measurement error. We formalize price functionals over a cone of adversary cost models, show that security profiles are piecewise-linear and concave, and prove a rating trilemma: when two profiles cross, no rating can simultaneously be faithful to underlying costs, total over comparable pairs, and independent of the chosen cost model. We provide a polynomial-time linear-programming procedure that certifies whether the ranking of two schemes is robust, reverses under admissible models, or is genuinely incomparable. We extend GAUGE with a two-layer risk measure combining stochastic cryptanalytic decay with uncertainty over the appropriate cost model. We evaluate the framework on NIST post-quantum standards, classical anchors, and a 25-year chronology of cryptanalytic breaks. The analysis certifies a ranking reversal for ML-KEM-512 versus AES-128 from a 4-5% shift in memory pricing, and measures a lattice-sieving cost drift of 9.79 bits per year over eight years. A hybrid X25519 + ML-KEM-768 handshake reduces combined-break probability twenty-fold at a 2.3 kilobyte cost. The artifact reproduces all tables and figures in under seven seconds. GAUGE provides an explicit and auditable framework for reporting cryptographic security under competing cost models.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.17281) | 2026-09-16
