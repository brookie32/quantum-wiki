---
title: "Dovetail: Group-Action Adaptor Signatures via a Heterogeneous Two-Block Construction"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3036"
summary: "Adaptor signatures bind the adaptation of a pre-signature into a valid signature to the disclosure of a witness, enabling atomic swaps, payment channels, and scriptless scripts. However, existing grou"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Adaptor signatures bind the adaptation of a pre-signature into a valid signature to the disclosure of a witness, enabling atomic swaps, payment channels, and scriptless scripts. However, existing group-action constructions face key limitations: O-IAS requires commutative actions with costly zero-knowledge proofs, Fast ORCAS incurs prohibitive communication on large group elements, and GATOR couples soundness amplification with pre-signing search cost. We present Dovetail, a group-action adaptor signature scheme built from a heterogeneous two-block construction over multiple public keys. By pairing a large non-cheating block with a small cheating block, Dovetail decouples soundness amplification from pre-signing search cost: the pre-signer fixes both commitments, searches over nonces until the challenge hits a target support, and uses its secret key to adjust the selected responses to the challenged public keys while preserving the ordinary signature format. Following Gerhart et al. (EUROCRYPT 2024), we prove Dovetail secure in the classical random oracle model under the Multiple Group Action Inverse Problem (mathsf{mGAIP}). Benchmarks across CSI-FiSh, LESS, MEDS, and ALTEQ at the 128-bit security level confirm these gains. On actions with large group elements, Dovetail outperforms both GATOR and Fast ORCAS in pre-signature size and pre-signing time, generating 15.39 kB pre-signatures in 16.25 ms on LESS (s=32, 4.6imes faster than Fast ORCAS) and 14.29 kB pre-signatures in 15.20 ms on ALTEQ (s=64, 121.7imes faster than GATOR). On compact-element actions such as CSI-FiSh (s=4), it produces 1.32 kB pre-signatures in 2.49 s, outperforming both GATOR and O-IAS.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3036) | 2026-11-25
