---
title: "Anonymous Attribute-Based Signcryption: Definitions, Constructions, and Applications"
date: "2026-09-02"
updated: "2026-09-04"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1861"
summary: "We put forward a generalization of attribute-based signcryption, called anonymous attribute-based signcryption (A^2BSC). Beyond message confidentiality and ciphertext unforgeability, A^2BSC further re"
last_verified: "2026-09-04"
review_by: "2026-12-03"
stale: false
---

We put forward a generalization of attribute-based signcryption, called anonymous attribute-based signcryption (A^2BSC). Beyond message confidentiality and ciphertext unforgeability, A^2BSC further requires extit{ciphertext anonymity}: no information about the signcryptor's attributes or ciphertext-related attributes/policies is leaked, regardless of the decryption outcome. Specifically, we begin by establishing the syntax and security notions for A^2BSC within a extit{unified} framework, which encompasses various variants (key-policy, ciphertext-policy, dual-policy, and a hierarchical dual-policy variant called Special A^2BSC). Then, we construct a Special A^2BSC scheme for extit{general policies} (modeled as bounded-depth Boolean circuits) from the succinct learning with errors and the basis-augmented short integer solution assumptions in the standard model, hence achieving post-quantum security. This naturally yields lattice-based instantiations of both ciphertext-policy and dual-policy A^2BSC. Beyond its independent interest, we also show the expressiveness and generality of our A^2BSC by exploring its application to matchmaking encryption (ME) and arranged matchmaking encryption (AME) proposed by Ateniese et al. (Crypto '19). As a byproduct, we give generic constructions of both ME and AME for extit{arbitrary policies} against unbounded collusions, and strengthen the CPA-privacy of (A)ME to achieve CCA security. The latter is achieved for free in our construction, as A^2BSC natively provides CCA security. Overall, our new solution adds to the diversity of methods for building the advanced primitive (A)ME.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1861) | 2026-09-02
