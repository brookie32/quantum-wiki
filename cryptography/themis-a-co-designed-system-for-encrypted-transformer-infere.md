---
title: "THEMIS: A Co-Designed System for Encrypted Transformer Inference"
date: "2026-09-29"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2264"
summary: "Secure Transformer inference can be made non-interactive under fully homomorphic encryption (FHE), but the computation is extremely expensive. Existing FHE-based systems reduce that cost by optimizing"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

Secure Transformer inference can be made non-interactive under fully homomorphic encryption (FHE), but the computation is extremely expensive. Existing FHE-based systems reduce that cost by optimizing individual stages in isolation, each within its own component rather than against the CKKS level budget they all share. A local gain therefore may not translate into an end-to-end speedup. We present THEMIS, a co-designed system for encrypted Transformer inference organized around two design principles, one bounding the depth each kind of stage may spend and one fixing where on the modulus chain it runs. THEMIS generalizes coefficient-encoded plaintext-ciphertext matrix multiplication (PCMM) to slot-encoded ciphertexts without format conversion, retaining the same accelerated coefficient-side backend and amortizing its nearly fixed cost through multi-batch packing. Two attention ciphertext-ciphertext matrix multiplication (CCMM) kernels combine the idle imaginary lane of each slot with baby-step giant-step accumulation and hoisting, so the attention multiplications issue far fewer key switches. For softmax, THEMIS conditions the first denominator with a calibrated row-wise offset and reserves high precision for the final normalization alone, which cuts the depth the reciprocal path consumes while keeping the precision of the returned probabilities. For a single stage, THEMIS accelerates PCMM and the attention CCMMs by 21.66imes and up to 7.39imes over MOAI (ICLR'26), and by up to 23.02imes and 16.49imes over Euston (S&P'26), while THEMIS's softmax runs 2.57imes faster than THOR (CCS'25) at higher precision. For the complete pipeline, THEMIS serves BERT-base on a CPU in 400.06 amortized seconds per input, with accuracy on GLUE tasks comparable to plaintext. Of that latency, the stages around bootstrapping account for only 10.83%, which is the lowest share among all works compared here.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2264) | 2026-09-29
