---
title: "A Note on the Security of ECDSA with Presignatures or Biased Nonces"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2545"
summary: "Over the years, several ECDSA security experiments have been proposed to enable faster distributed ECDSA signing. These experiments are not known to reduce to the standard ECDSA game, and recent work "
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Over the years, several ECDSA security experiments have been proposed to enable faster distributed ECDSA signing. These experiments are not known to reduce to the standard ECDSA game, and recent work (Groth and Shoup, Eurocrypt 2022) shows that some are vulnerable, especially when combined with raw signing (signing hash digests directly, rather than pre-hashed messages) and additive key derivation. Furthermore, several of these variants are implemented in public libraries and used by companies, sometimes in commercially deployed products, yet lack sound security foundations. In this note, we revisit the security landscape of these alternative modes of operation for ECDSA. As our main result, we show that the security of some of these variants, which are used in the wild, is equivalent in the generic group and random oracle model to a standard conjecture from fine-grained complexity on the average-case hardness of the k-SUM problem. We complement our study by proving lower bounds, conditioned on fine-grained complexity conjectures, on the running time of generic group model attacks against other standard modes of operation analyzed in (Groth and Shoup, Eurocrypt 2022). Overall, our results provide a complete picture of the security landscape of ECDSA variants, and reveal an elegant connection with (old and new) conjectures from the field of fine-grained complexity.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2545) | 2026-10-19
