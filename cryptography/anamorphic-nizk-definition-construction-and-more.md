---
title: "Anamorphic NIZK: Definition, Construction and More"
date: "2026-11-11"
updated: "2026-11-13"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2866"
summary: "Anamorphic encryption enables covert communication despite disclosure of ordinary decryption keys~ite{PersianoPY22}. Work on anamorphic signatures extends this capability to settings permitting only a"
last_verified: "2026-11-13"
review_by: "2027-02-11"
stale: false
---

Anamorphic encryption enables covert communication despite disclosure of ordinary decryption keys~ite{PersianoPY22}. Work on anamorphic signatures extends this capability to settings permitting only authentication and shows that Fiat-Shamir preserves anamorphism~ite{kutylowski2023anamorphicSignatures,fiat1986prove}. However, this result assumes an already anamorphic protocol and does not by itself ensure witness privacy against the recipient, motivating anamorphism directly in non-interactive zero-knowledge proofs (NIZKs). We introduce anamorphic NIZK (ANIZK), in which publicly verifiable proofs carry covert messages recoverable with a double key. The framework formalizes anamorphic security, strong robustness, and recipient anamorphic zero knowledge and simulation extractability. A generic construction in the random oracle model combines suitable Sigma protocols with authenticated encryption with associated data through a salted Fiat-Shamir transform. Applying ANIZK within the Naor-Yung paradigm ite{NaorYung90} yields recipient anamorphic encryption satisfying STE-xCCA1, SIND-aCCA1, and SIND-nCCA security under the notions of~ite{choi2026unified}. Finally, an asymmetric variant of ANIZK, termed ASY-ANIZK, combines a labeled NIZK with public-key encryption satisfying ciphertext pseudorandomness and random ciphertext rejection. It separates public embedding from secret recovery and achieves weak robustness, as public embedding precludes strong robustness.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2866) | 2026-11-11
