---
title: "Superposition Key-Recovery Attacks on Dilithium and Fiat-Shamir Signature Schemes"
date: "2026-09-29"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2258"
summary: "In this work, we assess the security of the main signature scheme standardised by NIST, ML-DSA, and its precursor identification schemes under an extended quantum adversarial model, one in which the a"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

In this work, we assess the security of the main signature scheme standardised by NIST, ML-DSA, and its precursor identification schemes under an extended quantum adversarial model, one in which the adversary is allowed to use quantum resources to interact with a prover/signer. We begin our analysis by developing new techniques for superposition attacks that realise a relative phase oracle for the LSBs of a classical function evaluated in a quantum computer. We then extend these techniques to enable a relative phase oracle for arbitrary bits. Leveraging these techniques, we demonstrate full key-recovery attacks on several lattice-based identification schemes, exploiting the affine structure of the output. Finally, we extend these attacks to the corresponding Fiat-Shamir signature schemes and obtain key-recovery attacks under reasonable implementation assumptions. As a result, we are able to mount full key-recovery attacks in the Q2 model against the original CRYSTALS-Dilithium scheme, as well as the corresponding NIST Standardisation Rounds 1 and 2 proposals. However modifications introduced in the scheme during the NIST process preclude our superposition attacks against the final standardised version ML-DSA. We identify and discuss the specific aspects of the algorithm's execution that affect the applicability of our techniques. Overall, our work expands the body of research on superposition attacks and represents a further step towards establishing full quantum security for cryptographic constructions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2258) | 2026-09-29
