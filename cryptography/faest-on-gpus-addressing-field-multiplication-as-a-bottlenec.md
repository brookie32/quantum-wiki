---
title: "FAEST on GPUs: Addressing Field Multiplication as a Bottleneck"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2489"
summary: "FAEST is a post-quantum signature scheme that combines VOLE-in-the-Head with QuickSilver to prove knowledge of a secret key. It relies on well-established symmetric primitives and offers small public "
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

FAEST is a post-quantum signature scheme that combines VOLE-in-the-Head with QuickSilver to prove knowledge of a secret key. It relies on well-established symmetric primitives and offers small public keys, but signing and verification are computationally expensive. We present an NVIDIA GPU implementation of the key-generation core and the QuickSilver procedures OWFProve and OWFVerify for the standard and EM constructions in both s and f variants. Profiling shows that once AES is accelerated by hardware, field multiplication in QuickSilver becomes the largest cost throughout this parameter grid. In FAEST-128f, field multiplication takes about 82% of signing time. To address this bottleneck in our GPU implementation of FAEST, we use PTX clmad for native carry-less arithmetic and Karatsuba to reduce the number of limb products. The clmad build improves throughput across all twelve OWFProve and OWFVerify paths, and its advantage grows with the field width. On an RTX A5000, PTX clmad raises standard OWFProve throughput to 1.99x, 2.45x, and 2.82x that of the software-multiplication build at 128, 192, and 256 bits, respectively. Together, PTX clmad and Karatsuba deliver 26.6x the throughput of the software-multiplication build in the field-multiplication-heavy kernel of standard 256-bit OWFProve. When all OWFProve stages are included, the combined build reaches 2.9x and 3.1x the software throughput for standard and EM at 256 bits, respectively. These results establish native carry-less arithmetic as a key design choice for GPU implementations of FAEST, with Karatsuba providing an additional improvement for 256-bit proving.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2489) | 2026-10-15
