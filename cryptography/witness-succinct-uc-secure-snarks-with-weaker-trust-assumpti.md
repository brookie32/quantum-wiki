---
title: "Witness-Succinct UC-Secure SNARKs with Weaker Trust Assumptions"
date: "2026-10-10"
updated: "2026-10-12"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2434"
summary: "Zero-knowledge Succinct Non-Interactive Arguments of Knowledge (zkSNARKs) are foundational cryptographic primitives enabling privacy-preserving and verifiable computation. However, most existing zkSNA"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

Zero-knowledge Succinct Non-Interactive Arguments of Knowledge (zkSNARKs) are foundational cryptographic primitives enabling privacy-preserving and verifiable computation. However, most existing zkSNARK constructions rely on strong trust assumptions—typically a fully trusted setup—which undermines their applicability in adversarial or decentralized environments. Although transparent zkSNARKs remove this assumption, they typically do not satisfy strong composability guarantees such as Universal Composability (UC). In this work, we present the first framework for constructing UC-secure zkSNARKs under weaker trust assumptions, based on a new primitive called Key-Updatable Polynomial Commitments (KU-pCom). This primitive enables publicly verifiable commitment-key updates, requiring only one honest update rather than a fully trusted setup. Our compiler transforms any Simulation-Extractable zkSNARK into a UC-secure variant by composing it with a KU-pCom scheme. We instantiate our framework in two settings: (1) using the structured, trusted setup of the KZG commitment scheme, and (2) an instantiation based on the lattice-based commitment scheme of Hwang et al. (Crypto 2024). We implement both instantiations and provide an end-to-end benchmark of UC-secure zkSNARKs with succinctness. Compared to prior UC-secure NIZKs that sacrifice succinctness (e.g., Abdolmaleki et al., CSF 2024), our work demonstrates that UC security, succinctness, and practical efficiency can be simultaneously achieved, establishing a new foundation for succinct, composable proof systems under weaker trust assumptions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2434) | 2026-10-10
