---
title: "SM4th and uBlockith: VOLE-based Post-Quantum Signature Schemes from Chinese Block Ciphers"
date: "2026-07-23"
updated: "2026-07-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1506"
summary: "FAEST is a family of post-quantum signature schemes based on VOLE-in-the-Head, and is one of the nine candidates advanced to the third round of the NIST Additional Digital Signature process. FAEST rel"
last_verified: "2026-07-26"
review_by: "2026-10-24"
stale: false
---

FAEST is a family of post-quantum signature schemes based on VOLE-in-the-Head, and is one of the nine candidates advanced to the third round of the NIST Additional Digital Signature process. FAEST relies only on symmetric cryptographic primitives, including block ciphers and hash functions, and does not require structured number-theoretic assumptions. We propose two families of signature schemes, SM4th and uBlockith, targeting 128-bit and 256-bit classical security, respectively. SM4th and uBlockith follow the FAEST framework but instantiate it with Chinese-designed block ciphers, including SM4, uBlock, and Ballet. We further design constraint systems tailored to these block ciphers and provide instruction-set-aware optimized implementations. Our evaluation on two Intel platforms and a Hygon platform shows that the end-to-end performance of the proposed schemes is strongly platform dependent. On an Intel platform with native SM4 support, the SM4th variants achieve performance comparable to the corresponding FAEST-128 variants, with a gap of less than 1imes. On the Hygon platform with native CIS-SM4 support, the SM4th variants are within approximately 3imes of FAEST-128. The SM4th-EM-s (short) variant has a combined public-key and signature size of 3,850 bytes, compared with 3,938 bytes for FAEST-EM-128s. The uBlockith variants remain approximately 3--4imes slower than FAEST-256. These results demonstrate the feasibility and costs of instantiating VOLE-based signatures with the selected Chinese block ciphers.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1506) | 2026-07-23
