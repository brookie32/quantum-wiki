---
title: "On the Formal Verification of Polynomial Commitments: two KZG constructions and the Algebraic Group Model"
date: "2026-07-21"
updated: "2026-07-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1490"
summary: "We formalize the notion of polynomial commitment schemes (PCSs) in the proof assistant Isabelle/HOL and formally verify the security proofs of two variants of the widely popular Kate, Zaverucha, and G"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

We formalize the notion of polynomial commitment schemes (PCSs) in the proof assistant Isabelle/HOL and formally verify the security proofs of two variants of the widely popular Kate, Zaverucha, and Goldberg (KZG) construction. Moreover, we formalize the Algebraic Group Model (AGM) by Fuchsbauer, Kiltz, and Loss using a novel constraint-programming-inspired approach. We formalize a reusable abstract definition of polynomial commitment schemes and define games for correctness, binding, hiding, and knowledge soundness/extractability. Based on this, we verify all applicable security proofs for two concrete PCS constructions: the standard (DL-)KZG and a batched KZG, using our AGM formalization in the knowledge-soundness proofs. Our proofs follow Shoup’s sequence-of-games approach, with machine-checked transitions, and are carried out in the CryptHOL framework for formal verification of cryptography in Isabelle. To our knowledge, this work is the first formalization of polynomial commitment schemes, the first formalization of the AGM, and the first formal verification of the security proofs for any concrete polynomial commitment scheme. This work lays the foundation for the formal verification of advanced cryptographic constructions, such as pairing-based zero-knowledge proofs (ZKPs) and succinct arguments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1490) | 2026-07-21
