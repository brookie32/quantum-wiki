---
title: "Succinct Arguments for QMA from Collapsing Hash Functions"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2040"
summary: "We prove the existence of succinct arguments for QMA, assuming only the existence of collapsing hash functions. This is the first scheme that relies only on unstructured ``Minicrypt'' assumptions, whi"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

We prove the existence of succinct arguments for QMA, assuming only the existence of collapsing hash functions. This is the first scheme that relies only on unstructured ``Minicrypt'' assumptions, which are not known to imply public-key encryption. Our main technical contribution is a quantum-succinct claw-state generation protocol that allows us to bootstrap a small number of quantum correlations into an arbitrarily large number of claw-state correlations, using classical communication only. This improves upon the work of [Zhang, STOC 2021], having better round complexity, a proof in the standard model, and being overall much simpler. This yields a quantum-succinct blind delegation of quantum computation protocol from one-way functions, which we plug into the communication-compression compiler of [Bartusek, Liu, and Malavolta, EUROCRYPT 2026] to obtain succinct arguments for QMA.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2040) | 2026-09-15
