---
title: "Schnorr Signatures and MuSig2 Are Jointly Secure, Even in Deterministic Wallets"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2128"
summary: "Modern cryptocurrency wallets use Schnorr signatures together with public, deterministic key derivation: by repeatedly rerandomizing a single master public key, an unlimited number of public keys for "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Modern cryptocurrency wallets use Schnorr signatures together with public, deterministic key derivation: by repeatedly rerandomizing a single master public key, an unlimited number of public keys for incoming payments can be derived without access to secret data. Moreover, some wallets support multi-signature schemes such as MuSig2 for optionally aggregating derived public keys from n distinct parties into "n-of-n" public keys, so that funds received on such aggregated keys can be spent only when authorized by all n parties. However, these advanced key-management techniques stretch the underlying cryptographic schemes beyond the guarantees provided by existing security proofs. Although deterministic Schnorr wallets and MuSig2 have each been proven secure in isolation, the provable security of their composition---despite its deployment in wallets---has not been established thus far. The goal of this work is to narrow this gap between theory and practice. We provide the first formal security analysis of the joint use of single-signer Schnorr signatures and MuSig2, both under rerandomization and in deterministic wallets. First, we introduce the notion of a (rerandomizable) joint-signature scheme, in which an honest signer uses the same secret key for single-signer signatures and multi-signatures. Within this model, we prove tight security of Schnorr signatures plus MuSig2 under the algebraic one-more discrete logarithm (AOMDL) assumption in the combination of the algebraic group model (AGM) and the random oracle model (ROM). Finally, we provide a formal model of deterministic wallets with joint-signature schemes and show that Schnorr plus MuSig2 remains secure under public, deterministic key derivation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2128) | 2026-09-20
