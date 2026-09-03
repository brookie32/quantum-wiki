---
title: "Open EM Side-Channel Dataset for ML-KEM (Kyber) Implementations"
date: "2026-09-01"
updated: "2026-09-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1851"
summary: "We present an open dataset of electromagnetic (EM) traces captured during the decapsulation operation of ML-KEM (Kyber), the key encapsulation mechanism standardised by NIST in FIPS 203. Each trace is"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

We present an open dataset of electromagnetic (EM) traces captured during the decapsulation operation of ML-KEM (Kyber), the key encapsulation mechanism standardised by NIST in FIPS 203. Each trace is windowed on a single pair-pointwise polynomial multiplication, in which the decapsulation key is one of the operands, making it a recurring target of published side-channel key-recovery attacks. The dataset covers three widely used implementations: the CRYSTALS reference implementation, the Cortex-M4 optimised pqm4 implementation, and the first-order masked mkm4 implementation, with 200k traces per implementation. For the masked implementation we release the traces of both shares, enabling first-order leakage assessment and share-wise analysis rather than attacks on unprotected code alone. All measurements were taken on an STM32F407 Cortex-M4 microcontroller using a near-field EM probe. Compared to previously published datasets targeting the same operation, which provide power measurements of the unprotected reference implementation only, this dataset contributes an EM modality and covers optimised and masked code. The traces and the associated sensitive variables are distributed as chunked NumPy arrays, so that researchers without access to measurement equipment can reproduce and extend side-channel analyses of ML-KEM.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1851) | 2026-09-01
