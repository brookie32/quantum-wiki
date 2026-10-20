---
title: "Efficient and Compact High-order Masking Raccoon on Memory Constrained Devices"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2540"
summary: "Raccoon, presented at CRYPTO 2024, is a provably secure lattice-based signature scheme featuring an O(d log{d}) masking overhead. Although it did not advance beyond the first-round of NIST's additiona"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Raccoon, presented at CRYPTO 2024, is a provably secure lattice-based signature scheme featuring an O(d log{d}) masking overhead. Although it did not advance beyond the first-round of NIST's additional call for post-quantum digital signatures, Raccoon remains a promising candidate due to its low masking overhead and strong provable side-channel resistance. This paper proposes the first efficient and compact implementation of high-order Raccoon on the ARM Cortex-M4, with a focus on optimizing its polynomial multiplication, sampling, and memory consumption. 1) For polynomial multiplication, we present a consecutive 32-bit NTT/INTT implementation for the two moduli in Raccoon, enabling optimal 3+3+3 layer merging to reduce memory-access overhead, together with extensive lazy reduction to minimize modular reductions. As a side contribution, we propose a novel negative double Montgomery reduction technique to accelerate double modular reductions in multi-moduli NTT. 2) For polynomial sampling, we identify and resolve a previously overlooked performance bottleneck caused by frequent incremental SHAKE256 invocations for small data chunks on ARM Cortex-M4. By transitioning to the one-shot approach, we achieve speedups of at least 1.80imes across all sampling routines in Raccoon. 3) Finally, we explore memory-saving techniques to enable the practical deployment of high-order masked Raccoon (up to 32 orders) on resource-constrained IoT devices. The proposed implementations outperform the Raccoon reference implementation by 1.85imes-2.25imes. Notably, high-order masked Raccoon-192 outperforms masked Dilithium3 by 3.12imes, 8.07imes, and 2.71imes at masking orders d=2, 4, and 8, respectively. Finally, the leakage evaluations confirm that the second-order Raccoon implementation provides strong resistance to differential power analysis (DPA) once micro-architectural transitional leakages are mitigated.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2540) | 2026-10-19
