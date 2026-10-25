---
title: "Efficient Laconic Oblivious Transfer with Malicious Security"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2593"
summary: "Laconic Oblivious Transfer (OT) enables a receiver to compress a large database into a short digest, allowing a sender to generate a succinct ciphertext that reveals only a single indexed message. Whi"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Laconic Oblivious Transfer (OT) enables a receiver to compress a large database into a short digest, allowing a sender to generate a succinct ciphertext that reveals only a single indexed message. While prior works achieve efficient constructions in the semi-honest model, known solutions for malicious security rely on inherently heavy non-black-box techniques, such as garbled circuits or succinct arguments, resulting in impractical schemes. In this work, we present the first construction of maliciously secure laconic OT that makes fully black-box use of its underlying primitives. Our construction is based on a simple and widely used paradigm combining vector commitments with witness encryption, previously known to yield efficient semi-honest protocols. We show that this approach can in fact achieve malicious security by introducing two minimal yet powerful enhancements: equivocal vector commitments and maliciously secure witness encryption. We prove that these properties suffice to obtain laconic OT with security against malicious senders in the universal composability model and against malicious receivers in the context model. We instantiate our framework from standard assumptions, including LWE and bilinear Diffie-Hellman variants, obtaining schemes in the standard model. Notably, our constructions avoid heavy non-black-box tools mentioned before, and therefore achieve efficiency comparable to the state-of-the-art black-box constructions with merely semi-honest security. In particular, in certain settings, we obtain malicious security at essentially no additional asymptotic cost. Our results resolve a central question on the feasibility of practical, maliciously secure laconic OT, and provide a unifying pathway for efficiently achieving malicious security in laconic cryptography.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2593) | 2026-10-22
