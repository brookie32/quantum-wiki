---
title: "A Single-Trace Side-Channel Attack on the KpqC Digital Signature Scheme AIMer v3"
date: "2026-11-10"
updated: "2026-11-13"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2859"
summary: "The Korean Post-Quantum Cryptography (KpqC) competition selected AIMer, a post-quantum digital signature scheme based on the MPC-in-the-Head paradigm, as one of its final algorithms in 2025. However, "
last_verified: "2026-11-13"
review_by: "2027-02-11"
stale: false
---

The Korean Post-Quantum Cryptography (KpqC) competition selected AIMer, a post-quantum digital signature scheme based on the MPC-in-the-Head paradigm, as one of its final algorithms in 2025. However, detailed side-channel analysis (SCA) of AIMer remains limited, particularly for its latest version, AIMer v3. In this paper, we present, to the best of our knowledge, the first side-channel attack on AIMer v3. Specifically, we demonstrate a single-trace power analysis attack using deep learning to exploit power leakage from bits of the secret preimage during the computation of AIM3's input affine layer. Using a ChipWhisperer-HuskyPlus, we recover the full secret key from a single signature on an ARM Cortex-M4 processor with a success rate of 100%. We further evaluate the attack performance under different noise levels and propose potential countermeasures.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2859) | 2026-11-10
