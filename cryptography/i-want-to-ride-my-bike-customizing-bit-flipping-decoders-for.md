---
title: "I Want to Ride My BIKE:  Customizing Bit-Flipping Decoders for Ephemeral Key KEMs"
date: "2026-10-16"
updated: "2026-10-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2511"
summary: "Large public keys and ciphertexts remain a major obstacle to the deployment of post-quantum cryptosystems in applications currently relying on compact classical schemes. In code-based post-quantum key"
last_verified: "2026-10-17"
review_by: "2027-01-15"
stale: false
---

Large public keys and ciphertexts remain a major obstacle to the deployment of post-quantum cryptosystems in applications currently relying on compact classical schemes. In code-based post-quantum key encapsulation mechanisms, reducing the Decoding Failure Rate (DFR) generally requires larger parameters, further increasing communication and storage overheads. Ephemeral key-pair scenarios allow a different trade-off: ideally, each secret key is used for a single decapsulation, limiting the opportunities to observe and exploit decryption failures. We investigate how this setting can be used to reduce the public-key and ciphertext sizes of code-based key encapsulation mechanisms such as BIKE. We present the first optimized implementation of the extsf{BF-max} decoder: compared with conventional parallel bit-flipping decoders currently used by BIKE, extsf{BF-max} provides better error-correction capability, but its computational structure makes an efficient implementation less straightforward. Combining extsf{BF-max} with other decoders from the literature, we introduce decoding strategies that offer different trade-offs among DFR, execution time, public-key size, and ciphertext size. Experimental results show that the proposed design reduces both public-key and ciphertext sizes by 7.8% compared with LeanBIKE, a BIKE variant specifically designed for ephemeral-key use, while retaining similar execution time and DFR. For additional context, the selected parameter set yields a combined public-key and ciphertext size that is 22% smaller than that of BIKE and smaller by a factor of 2.79 than that of HQC. Note that BIKE and HQC, unlike LeanBIKE and our design, target the long-term-key setting. As a concrete application, we show that the solutions we propose make it possible to incorporate BIKE into constrained protocols, such as Internet Key Exchange version 2 (IKEv2), in which no code-based KEM would otherwise fit.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2511) | 2026-10-16
