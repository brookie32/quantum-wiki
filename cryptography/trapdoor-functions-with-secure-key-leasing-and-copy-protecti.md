---
title: "Trapdoor Functions with Secure Key Leasing and Copy Protection"
date: "2026-09-07"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1913"
summary: "Inspired by the no-cloning theorem in quantum theory, a variety of quantum cryptographic primitives with unclonable functionalities, such as secure key leasing and copy protection, have been proposed "
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

Inspired by the no-cloning theorem in quantum theory, a variety of quantum cryptographic primitives with unclonable functionalities, such as secure key leasing and copy protection, have been proposed and attracted significant attention. However, trapdoor functions (TDFs), fundamental primitives in public-key cryptography, have not been extensively studied in these areas. In this work, we initiate a study of TDFs in both secure key leasing and copy protection settings. We first introduce the definition of TDFs with secure key leasing (TDF-SKL), which enables leasing and deleting of quantum trapdoors. We formalize TDF-SKL both with and without domain sampler, and give a construction of TDF-SKL without domain sampler based on the LWE assumption and a construction of TDF-SKL with domain sampler based on any standard PKE schemes combined with hinting pseudorandom generators [Koppula and Waters, CRYPTO 2019]. Next, we define TDFs with copy protection (TDF-CP), where the inversion functionality is copy protected by a quantum trapdoor. We establish a construction of TDF-CP assuming indistinguishability obfuscation and the LWE assumption, following a modular framework of copy protection proposed by Ananth and Behera [CRYPTO 2024]. We also present applications of TDF-SKL and TDF-CP. Existing constructions of public-key encryption with secure key leasing (PKE-SKL) and single-decryptor encryption (SDE) suffer from a critical vulnerability: quantum decryption keys may be destroyed after decrypting maliciously chosen ciphertexts. We construct PKE-SKL schemes and SDE schemes with robust quantum decryption keys that remain reusable after decrypting arbitrary ciphertexts from TDF-SKL and TDF-CP, respectively.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1913) | 2026-09-07
