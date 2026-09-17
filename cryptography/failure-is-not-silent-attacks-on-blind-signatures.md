---
title: "Failure Is Not Silent: Attacks on Blind Signatures"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2043"
summary: "Blind signatures and OPRFs are widely used to build anonymous tokens and privacy-preserving protocols. This paper shows that several prior claims of blindness and request-privacy for such primitives a"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Blind signatures and OPRFs are widely used to build anonymous tokens and privacy-preserving protocols. This paper shows that several prior claims of blindness and request-privacy for such primitives are false under the standard security definitions. In particular, we give explicit malicious-signer/evaluator adversaries showing that the theorems claimed for several existing constructions, including the blind ECDSA scheme of Qin et al. and the verifiable Dark Matter OPRF, do not hold. The attacks exploit a simple but previously overlooked channel: a malicious signer can craft its response so that the honest user's final verification aborts if and only if the user's hidden message satisfies a chosen predicate. The abort/no-abort outcome, therefore, becomes a one-bit testing oracle on the hidden message. Importantly, this is not a failure of the standard blindness definition: our attacks win the standard blindness/request-privacy games. Rather, the flaw is that prior proofs implicitly used encryption hiding or commitment hiding in settings where the adversary also learns an input-dependent abort event. Our main attack applies to a general pattern of homomorphic-encryption-based blind signatures and OPRFs, in which the user encrypts its input, then decrypts and verifies the signer's homomorphic response. We also present two additional case studies, based on derandomization and selective use of signer components, which illustrate the same proof pitfall in other constructions. We identify a positive design criterion: schemes with publicly checkable signature derivation, in the sense of Fischlin-Schröder, do not leak extra information through such selective aborts. Finally, we discuss mitigations. Generic protection requires publicly verifiable honest evaluation, e.g., via zero-knowledge proofs. For random-token use cases of some HE-based blind signatures, we give a partial mitigation based on random unknown-message blindness RUMBL and a random-oracle transformation to standard blindness.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2043) | 2026-09-15
