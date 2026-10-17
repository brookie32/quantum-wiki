---
title: "Eﬃcient Fixed-Point Implementation of Mitaka"
date: "2026-10-17"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2521"
summary: "The Mitaka signature scheme is a variant of Falcon (FN-DSA). It has a considerably simpler signing procedure that can be parallelized while retaining Falcon's efficiency advantage. Mitaka offers two d"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

The Mitaka signature scheme is a variant of Falcon (FN-DSA). It has a considerably simpler signing procedure that can be parallelized while retaining Falcon's efficiency advantage. Mitaka offers two different signing approaches: a default one relying on floating-point arithmetic and an alternative, called MitakaZ, avoiding floating-point arithmetic at the cost of more Gaussian samples. Despite its better portability, MitakaZ has not previously been implemented in practice. This work presents an efficient fixed-point implementation of the Mitaka signing algorithm. We optimize the MitakaZ Gaussian sampler to make it suited to fixed-point arithmetic while achieving higher efficiency. Specifically, we replace the wide integral Gram root decomposition used in MitakaZ with a fixed-point square Cholesky decomposition, which substantially reduces the cost of integer Gaussian sampling. We prove bounds on intermediate values and representation errors without empirical assumptions on their magnitudes. The distributional analysis models each integer Gaussian call as exact at its represented inputs. We provide a fixed-point implementation of the new Mitaka signing algorithm in C. On an Intel Core~i7-1360P, our native AVX2 implementation generates signatures in an average of 361 kcycles for Mitaka-512 and 707 kcycles for Mitaka-1024, measured with Linux hardware performance events. On an ARM Cortex-M4F STM32F411, the corresponding measured costs are 4.0 and 7.8 Mcycles.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2521) | 2026-10-17
