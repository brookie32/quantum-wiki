---
title: "ANSA-IBS: Identity-Based Signatures from Annular NTRU Trapdoors and Bimodal Fiat-Shamir with Aborts"
date: "2026-09-21"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2134"
summary: "We give a lattice identity-based signature scheme from annular NTRU trapdoors and Fiat--Shamir with aborts (FSwA). Countered hashing maps each identity to its first invertible DLP/NTRU syndrome a. Ext"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

We give a lattice identity-based signature scheme from annular NTRU trapdoors and Fiat--Shamir with aborts (FSwA). Countered hashing maps each identity to its first invertible DLP/NTRU syndrome a. Extraction returns a short witness to s_0+s_1h=amod q, and signing normalizes this relation to a fixed-target two-response equation with public commitment recovery. Gärtner's iterative rejection method fits naturally into this signing layer: processing the challenge monomials separately reduces the Gaussian mask width and expected signing attempts, yielding shorter signatures. We report three parameter sets whose signing layer is calibrated against NIST security categories 2, 3, and 5, with fixed signature sizes of 8486, 11309, and 12727 bytes, respectively.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2134) | 2026-09-21
