---
title: "MAMBA-Frost: A Lattice KEM from Learning With Quantization"
date: "2026-09-21"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2136"
summary: "The Learning With Errors (LWE) problem provides a conservative and well-established security foundation for lattice-based cryptography, while Learning With Rounding (LWR) improves bandwidth efficiency"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

The Learning With Errors (LWE) problem provides a conservative and well-established security foundation for lattice-based cryptography, while Learning With Rounding (LWR) improves bandwidth efficiency through deterministic rounding. However, the rounding noise in LWR is inherently correlated with the hidden linear term, preventing tight and sample-preserving reductions to standard LWE for polynomial moduli. Prior work on the Learning With Quantization (LWQ) problem established a tight security reduction from LWE, where standard additive noise is intrinsically replaced by quantization error. We specialize this framework by explicitly instantiating the quantization lattice as a scaled integer lattice. Under this geometric choice, specifically utilizing aligned power-of-two moduli, we derive the exact finite-support error distribution and construct an explicit bijection between transmitted split samples and normal-form LWE samples. These ingredients yield (mathsf{MAMBAext{-}Frost}), a plain LWQ-based key encapsulation mechanism that seamlessly pairs unstructured LWE security with quantization-based compression. Because its effective error stems entirely from public dithered quantization, (mathsf{MAMBAext{-}Frost}) operates strictly with hardware-friendly power-of-two arithmetic. Furthermore, the construction employs an (E_8)-coded message embedding to optimize the correctness margin without altering the underlying LWQ hardness argument. We instantiate (mathsf{Frost}) at NIST security levels 1, 3, and 5 and provide a complete software implementation. Its power-of-two design realizes the core arithmetic with shifts and masks, keeping the implementation simple and amenable to constant-time engineering. At level 1, (mathsf{Frostext{-}128}) reduces the combined public-key and ciphertext size by about (40%) compared with (mathsf{FrodoKEMext{-}640}) and by about (8%) compared with (mathsf{SCloud}^{+}ext{-}128). On an AVX2 platform, (mathsf{Frostext{-}128}) achieves speedups of (2.3imes), (1.8imes), and (1.5imes) for key generation, encapsulation, and decapsulation over (mathsf{FrodoKEMext{-}640}), and (2.1imes), (1.5imes), and (1.3imes) over (mathsf{SCloud}^{+}ext{-}128).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2136) | 2026-09-21
