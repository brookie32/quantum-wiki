---
title: "LUTune: Automated Lookup Table Optimization for Efficient TFHE-Based ML Inference"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3037"
summary: "TFHE evaluates quantized activation functions by programmable bootstrapping (PBS) using lookup tables (LUTs). The input precision of a LUT and the noise tolerance of its consumers affect PBS latency a"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

TFHE evaluates quantized activation functions by programmable bootstrapping (PBS) using lookup tables (LUTs). The input precision of a LUT and the noise tolerance of its consumers affect PBS latency and evaluation-key size. LUTune rewrites activation LUTs using the outputs permitted by Concrete ML's approximate rounding rule. It folds LUTs to reduce their input precision and decomposes plaintext weights into signed digits to reduce the output-noise variance predicted for dense layers. LUTune checks the circuit failure bound under Concrete's noise model at the selected parameters. On VGG6 it achieves a 5.2imes speedup and a 17.2imes reduction in evaluation-key size relative to the lowest-latency Concrete ML configuration, using the same frozen weights and quantizers.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3037) | 2026-11-25
