---
title: "NTPIR: Efficient Silent-Preprocessing PIR using NTR"
date: "2026-09-07"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1910"
summary: "Private Information Retrieval (PIR) enables a client to query a database without revealing the requested index. In the silent preprocessing model, existing protocols typically adopt a two-layer pipeli"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

Private Information Retrieval (PIR) enables a client to query a database without revealing the requested index. In the silent preprocessing model, existing protocols typically adopt a two-layer pipeline: a first-layer retrieval based on LWE, followed by an RLWE ring-packing stage and a second-layer homomorphic column retrieval, with ring packing being the primary performance bottleneck. We observe that NTRU supports the homomorphic operations required by this pipeline while representing each ciphertext with a single ring element, suggesting its potential to replace RLWE for a more compact intermediate representation. However, NTRU lacks RLWE's public randomness component, which is required in the offline/online separation of most existing PIR schemes. We introduce NTPIR to address this challenge through three techniques: (1) Pack-then-switch: we perform ring packing in the RLWE domain and transform the result to NTRU via a single key switch, preserving the offline preprocessing structure while yielding compact, single-element packed intermediates. (2) Split-point picking: this method integrates second-layer column selection with response packing, reducing automorphism complexity from linear to square-root complexity in the number of packed second-layer inputs. (3) Optimized arithmetic: we employ FFT-based polynomial multiplication and approximate gadget decomposition to improve the computational efficiency of the underlying homomorphic operations, with concrete correctness error at most 2^{-40}. On databases ranging from 1 to 8GB, NTPIR achieves up to a 1.81imes server-side online speedup over InsPIRe^{(2)} (S&P'26). At 8,GB, preprocessing step is 7--41imes faster than InsPIRe^{(2)}. In addition, at the highest-throughput configuration, NTPIR sustains 8,609MB/s on an 8GB database, corresponding to a 1.38imes speedup over InsPIRe^{(2)}, 1.8imes over SimpleYPIR, and 2.0imes over HintlessPIR.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1910) | 2026-09-07
