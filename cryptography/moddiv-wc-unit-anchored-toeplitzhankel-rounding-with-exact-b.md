---
title: "MODDIV-WC: Unit-Anchored Toeplitz/Hankel Rounding with Exact Binary-LWE Masking and an IND-CCA Security Route"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2747"
summary: "egin{abstract} We present MODDIV-WC, a public-key encryption and key-encapsulation candidate based on a widened Hankel linear map followed by deterministic integer division, together with an implicit-"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

egin{abstract} We present MODDIV-WC, a public-key encryption and key-encapsulation candidate based on a widened Hankel linear map followed by deterministic integer division, together with an implicit-rejection Fujisaki--Okamoto wrapper, MODDIV-WC-FO. The construction uses a secret vector whose first coordinate is fixed to one and whose remaining coordinates are sampled from a positive interval. This unit anchor makes the Hankel map surjective for every admissible secret, a property that is central to the proof. The security analysis has four layers. First, we give an exact embedding of binary-secret LWE into the widened Hankel map using a parity mask that reproduces the MODDIV-WC secret distribution without statistical loss. Second, in an ideal public-key hybrid, a strong leftover-hash argument hides the challenge key. Third, adapting the Renyi-divergence boundary method of prior LWR and MP-LWR work, we prove a transfer lemma for the unit-anchored MODDIV-WC secret distribution. This avoids the earlier requirement that the probability of crossing a rounding boundary be negligible and instead preserves one-way success probabilities with a multiplicative Renyi loss. Fourth, we combine one-way chosen-plaintext security with the implicit-rejection modular Fujisaki--Okamoto analysis of Hofheinz, Hovelmanns, and Kiltz to derive IND-CCA security in the classical random-oracle model. For an explicit asymptotic family, the correctness, Renyi, leftover-hash, binary-secret-LWE, and random-oracle losses are simultaneously negligible, while the source LWE noise remains inverse-polynomial. Together with classical worst-case-to-LWE reductions and the binary-secret/modulus transformations of Brakerski, Langlois, Peikert, Regev, and Stehle, this yields an internally audited candidate route from polynomial-factor worst-case lattice hardness to IND-CCA security. No practical 128-bit parameters, QROM proof, or deployment claim is made. end{abstract}

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2747) | 2026-11-03
