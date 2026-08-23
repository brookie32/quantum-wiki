---
title: "Lightweight Lattice-based Single-Party Public-Key Authenticated Key Exchange"
date: "2026-08-21"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1761"
summary: "Authenticated Key Exchange (AKE) is a cornerstone of secure communication, especially in resource-constrained IoT environments where lightweight and post-quantum security are paramount. While lattice-"
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

Authenticated Key Exchange (AKE) is a cornerstone of secure communication, especially in resource-constrained IoT environments where lightweight and post-quantum security are paramount. While lattice-based cryptography offers promising solutions, existing post-quantum AKE protocols often prioritize strong security notions, such as the use of an IND-CCA encryption scheme, incurring overheads incompatible with IoT devices. This raises a critical question: Can one-way security (OW), a weaker but potentially more efficient notion, suffice for secure AKE in the post-quantum era? We address this challenge by revisiting the ALIKE framework (ISO/IEC 29192-4), which achieves OW-CCA-based AKE using deterministic RSA. However, RSA’s quantum vulnerability and the lack of lattice-based OW-CCA schemes hinder its applicability today. Our work bridges this gap through three key contributions. First, we prove that the Hash-Before-Encrypt (HBE) paradigm generically transforms deterministic OW-CPA schemes into OW-CCA-secure ones. We additionally present the Fujisaki–Okamoto transform and its security proof construction, providing a reference for understanding the efficiency advantages of the proposed HBE-based approach. Second, we modify Bai et al.’s efficient lattice-based OW-CPA scheme to a deterministic variant and rigorously prove its security. Third, we generalize the SPAKE framework to support our OW-CCA construction, enabling post-quantum AKE with minimal assumptions, implement and benchmark the resulting protocol, demonstrating state-of-the-art efficiency for lightweight, quantum-resistant AKE. By relaxing security requirements from IND-CCA to OW-CCA while preserving adaptive security we achieve a practical balance between robustness and performance, paving the way for deployable solutions in constrained environments like IoT and connected vehicles.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1761) | 2026-08-21
