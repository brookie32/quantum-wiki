---
title: "Efficient Large-Integer Arithmetic for FHE"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1608"
summary: "Fully Homomorphic Encryption (FHE) has emerged as one of the key technologies for privacy-preserving computation, enabling arbitrary computation directly on encrypted data. Vectorized FHE schemes, suc"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Fully Homomorphic Encryption (FHE) has emerged as one of the key technologies for privacy-preserving computation, enabling arbitrary computation directly on encrypted data. Vectorized FHE schemes, such as Brakerski/Fan--Vercauteren (BFV), Brakerski--Gentry--Vaikuntanathan (BGV), and Cheon--Kim--Kim--Song (CKKS), are typically used in applications dealing with large datasets, for example, confidential database queries and private ML inference. These FHE schemes are based on the computational hardness of Ring Learning with Errors (RLWE) and share a common algebraic foundation: arithmetic over high-dimensional polynomial rings with coefficient moduli spanning hundreds or thousands of bits, far exceeding the native arithmetic capabilities of modern processors. This article surveys the evolution of large-integer arithmetic in RLWE-based FHE libraries, with a focus on the Residue Number System (RNS) techniques used in practically all modern implementations. We give a formal treatment of the two fundamental RNS building blocks --- basis extension and scaling --- that require information about the magnitude of a large value and are therefore incompatible with a purely residue-wise view of arithmetic. We contrast the two principal algorithmic approaches to these operations: the integer-only approach of Bajard, Eynard, Hasan, and Zucca (BEHZ), which tolerates approximation overflows and corrects them with auxiliary redundant moduli, and the floating-point approach of Halevi, Polyakov, and Shoup (HPS). We then show how these primitives compose into the higher-level RNS procedures used across all vectorized RLWE schemes and review how their adoption reshaped the architecture and performance of libraries such as HElib, SEAL, PALISADE/OpenFHE, HEAAN, and Lattigo. We give particular attention to the scaling error inherent in the original Full RNS variant of CKKS, and to the more recent techniques --- reduced-error scaling, composite scaling, and grafting --- that eliminate it or restore flexible, high-precision rescaling from within the residue representation. We also cover GPU-accelerated implementations and close by discussing a renewed, and so far exploratory, interest in positional (non-RNS) representations, raising the question of how such approaches might compare with the Full RNS variants that dominate FHE implementations today.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1608) | 2026-08-04
