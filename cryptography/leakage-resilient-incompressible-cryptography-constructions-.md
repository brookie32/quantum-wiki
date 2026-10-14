---
title: "Leakage-Resilient Incompressible Cryptography: Constructions and Barriers"
date: "2026-10-13"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2461"
summary: "We introduce Leakage-Resilient Incompressible cryptography, which simultaneously addresses two variants of side-channel attacks that have been tackled in theoretical cryptography. Leakage-resilience s"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

We introduce Leakage-Resilient Incompressible cryptography, which simultaneously addresses two variants of side-channel attacks that have been tackled in theoretical cryptography. Leakage-resilience seeks to provide security against an adversary who learns a part of the secret-key and the entire ciphertext or signature; conversely, incompressible cryptography provides security against an adversary who learns the entire secret-key, but only a part of the ciphertext or signature. However, constructions in either of these security models can fail against an attack in the other model. In this work, we define a new model of security that subsumes both leakage-resilient cryptography and incompressible cryptography, and we present several non-trivial positive and negative results. On the positive side, first we present a transformation from incompressible symmetric-key encryption (SKE) to leakage-resilient incompressible SKE in the information-theoretic setting. Next, as one of our main results, we construct a leakage-resilient incompressible public-key encryption (PKE), combining an incompressible SKE and a new primitive that we call leakage-resilient non-committing key encapsulation mechanism (LR-NC-KEM). While an information-theoretic incompressible SKE suitable for use in both these constructions already exists in the literature (Dziembowski, CRYPTO 2006), we present a new construction achieving ciphertext-rate frac{1}{2} and compression-rate frac{1}{2}, using an appropriate notion of invertible extractors; this leads to corresponding improvements in the final parameters we obtain in these constructions. We also construct a leakage-resilient incompressible signature scheme in the classical random oracle model, assuming (mathsf{DCR}ext{ or }mathsf{LWE}) and the Decisional Linear assumption, with signature-rate and compression-rate 1-o(1) and leakage-rate 1. On the negative side, we show barriers to significantly improving the parameters we obtain, by showing impossibility of basing the security of such improved schemes on blackbox reductions. Apart from the general framework and the specific results we obtain, some of the intermediate tools that we define and instantiate, like LR-NC-KEM and invertible extractors, may be of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2461) | 2026-10-13
