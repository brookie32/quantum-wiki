---
title: "Kaiburr: ML-KEM at (much) higher security"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2730"
summary: "With deployment of standardized post-quantum cryptography well on the way, discussions continue about concrete choices of schemes and parameter sets. For example, while NIST standardized structured-la"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

With deployment of standardized post-quantum cryptography well on the way, discussions continue about concrete choices of schemes and parameter sets. For example, while NIST standardized structured-lattice-based ML-KEM, European agencies like BSI and ANSSI favor unstructured-lattice-based FrodoKEM. Another discussion revolves around different approaches to hybrid deployments – either combining post-quantum schemes with "traditional" elliptic-curve cryptography (or RSA) or combining multiple different post-quantum schemes. The typical question for systems engineers to ask is what the "best" or "most conservative" approach is within a certain performance budget. In this paper we add a data point to this discussion by investigating how to scale ML-KEM to (much) higher security levels of the underlying MLWE problem. We first observe that increasing security simply by increasing the module rank k quickly reaches a limit imposed by decryption failure probability. We then propose a generalization of the noise distribution, which enables scaling to much larger module rank and MLWE hardness, while preserving the essence of ML-KEM, most notably arithmetic in the ring Z_{3329}[X]/(X^{256}+1) and a simple and constant-time secret / noise generation. We select three concrete parameter sets of this high-security variant of ML-KEM, which we call Kaiburr. We present benchmarking results for optimized implementations of Kaiburr on 64-bit Intel CPUs and on the Asymmetric Cryptography Coprocessor (ACC) of the Pavona open-source silicon framework. Based on these benchmarks, we argue that, for example, a hybrid of FrodoKEM-976 and Kaiburr-1792 not only offers better performance than FrodoKEM-1344, it also offers protection against a broader range of hypothetical future attacks against (M)LWE.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2730) | 2026-11-03
