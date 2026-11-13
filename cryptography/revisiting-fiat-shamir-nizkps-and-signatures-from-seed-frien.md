---
title: "Revisiting Fiat-Shamir NIZKPs and Signatures from Seed-Friendly Sigma Protocols"
date: "2026-11-10"
updated: "2026-11-13"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2858"
summary: "Seed-friendly sigma protocols have a small challenge space, and when compiled into NIZKP, they require parallel repetition to reduce extraction error. Fiat-Shamir proofs obtained from seed-friendly Si"
last_verified: "2026-11-13"
review_by: "2027-02-11"
stale: false
---

Seed-friendly sigma protocols have a small challenge space, and when compiled into NIZKP, they require parallel repetition to reduce extraction error. Fiat-Shamir proofs obtained from seed-friendly Sigma protocols can be made more compact with fixed-weight parallel repetitions, and seed-tree compression. So far, these have been presented as compression techniques for the proof size, but standard analysis of the extraction property of NIZKP still relies on the Forking Lemma and rewinding. In this work, we show that not only fixed-weight parallel repetition and seed-tree compression improve the compactness of the proofs, but also improve their security. Interestingly, when the prover randomness is generated from a salted seed tree, interacting with a random oracle, the standard Fiat-Shamir compilation is straight-line extractable in the classical random-oracle model, without any additional proof field or proof-of-work. We further show that the Fiat-Shamir NIZKP from seed-friendly Sigma protocols satisfies multi-proof zero knowledge, and that its straight-line extractability does not require the underlying seed-friendly Sigma protocol to have unique responses.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2858) | 2026-11-10
