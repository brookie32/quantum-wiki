---
title: "Robust ECDSA Threshold Signing at Scale"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2493"
summary: "This work presents an efficient, scalable, and robust threshold ECDSA signing protocol for the tleq (n-1)/3 scenario, making it suitable for e.g., bridging consensus from one Blockchain to another. Ou"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

This work presents an efficient, scalable, and robust threshold ECDSA signing protocol for the tleq (n-1)/3 scenario, making it suitable for e.g., bridging consensus from one Blockchain to another. Our construction allows to batch-compute pre-processing material for efficient online signing. While our protocol is based on established ideas for (Verifiable) Secret Sharing, we optimize it to scale efficiently both in terms of computation and communication with a large number of signers. We therefore combine efficient batching techniques for sharing (Fitzi & Hirt, PODC 2006), randomness extraction (Beerliova-Trubiniova & Hirt, TCC 2008) and share opening (Damgård & Nielsen, CRYPTO 2007) with recent advances in efficient Zero-Knowledge proofs (Attema & Cramer, CRYPTO 2020). We implement and evaluate the protocol experimentally and show that it is practical for large number of parties n.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2493) | 2026-10-15
