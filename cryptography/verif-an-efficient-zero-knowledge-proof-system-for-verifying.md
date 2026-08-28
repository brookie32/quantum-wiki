---
title: "VERIF: An Efficient Zero-Knowledge Proof System for Verifying IVF-Flat Retrieval in RAG Services"
date: "2026-08-26"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1802"
summary: "Retrieval-augmented generation (RAG) services outsource vector search over proprietary corpora, yet clients cannot verify that returned context conforms to the promised index, parameters, and snapshot"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

Retrieval-augmented generation (RAG) services outsource vector search over proprietary corpora, yet clients cannot verify that returned context conforms to the promised index, parameters, and snapshot. We present VERIF, the first dedicated zero-knowledge polynomial interactive oracle proof (PIOP) for complete, service-consistent IVF-Flat retrieval. VERIF proves top-m centroid selection, authenticated routing, exact full-vector scoring of every routed candidate, final top-k selection, and context binding. Its commitment-eliding reduction keeps query-dependent scores virtual and reduces selection claims directly to inner products over authenticated data. A unified, permutation-free top-t relation with limb-decomposed range arguments handles both selection stages without sorting or score commitments. Against a matched, optimized implementation of the same retrieval relation using a general-purpose circuit-based zkSNARK (Plonky2), our prototype achieves up to an 86.5imes prover speedup and reduces peak memory by up to 99.1%. VERIF proves retrieval over authenticated SIFT and 768-dimensional Cohere indexes containing 32 million and 8 million vectors in 5.90 and 11.57 seconds, respectively; verification takes 0.62--1.48 seconds. These results demonstrate practical verifiable IVF-Flat retrieval for RAG-as-a-Service.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1802) | 2026-08-26
