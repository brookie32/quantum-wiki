---
title: "Rerandomizable Garbling Beyond BHHO-KMHE and a Construction from LWE"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2664"
summary: "Rerandomizable garbling schemes (RGS) are a fundamental primitive enabling advanced cryptographic constructions such as multi-hop homomorphic encryption (Gentry, Halevi, Vaikuntanathan, CRYPTO 2010), "
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

Rerandomizable garbling schemes (RGS) are a fundamental primitive enabling advanced cryptographic constructions such as multi-hop homomorphic encryption (Gentry, Halevi, Vaikuntanathan, CRYPTO 2010), iO-combiners (Ananth, Jain, Naor, Sahai, Yogev, CRYPTO 2016), and YOSO-style MPC (Acharya, Hazay, Kolesnikov, Prabhakaran, TCC 2022 and CRYPTO 2024). All known RGS instantiations rely on discrete-logarithm-type assumptions, concretely via the BHHO scheme (Boneh, Halevi, Hamburg, Ostrovsky, CRYPTO 2008) and its recent pairing-based variant (Heitjohann, von der Heyden, Jager, CRYPTO 2025). This reliance stems from the use of key-and-message homomorphic encryption (KMHE) that supports rerandomization and strong "key-privacy under leakage", which hides the applied homomorphic transformations and is currently only achievable using BHHO-style bitwise encryption in combination with permutation-based homomorphisms. Our first main contribution is a new garbling technique that shifts the burden of hiding homomorphic transformations from the encryption scheme to the garbling itself. This allows us to construct RGS from KMHE schemes with substantially weaker properties, avoiding the need for bitwise encryption and permutation-based homomorphisms, and enabling the construction of RGS from KMHE with other homomorphisms, such as additively-homomorphic ones. As a second contribution, we give a concrete lattice-based instantiation of the required KMHE primitive, based on LWE. This construction is a variant of the GSW FHE scheme (Gentry, Sahai, Waters, CRYPTO 2013), which uses new techniques for rerandomization and is tailored to the requirements of our new garbling scheme by supporting a "homomorphic"/"lossy" mode. This yields the first RGS construction that does not rely on discrete-logarithm assumptions and may provide post-quantum security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2664) | 2026-10-28
