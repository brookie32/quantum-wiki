---
title: "Unique Signature Schemes with Tight Security in the Random Oracle Model via Hash-and-Subset-Sign"
date: "2026-11-02"
updated: "2026-11-04"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2720"
summary: "Unique signatures are digital signature schemes, where each message has exactly one valid signature. The uniqueness property typically comes at a price: Most unique signature schemes are known to have"
last_verified: "2026-11-04"
review_by: "2027-02-02"
stale: false
---

Unique signatures are digital signature schemes, where each message has exactly one valid signature. The uniqueness property typically comes at a price: Most unique signature schemes are known to have a security loss at least linear in the number of signature queries when aiming for existential unforgeability under chosen message attacks (EUF-CMA) security, which was shown to be inherent in the standard model by Coron (EUROCRYPT 2002) for signature schemes where public keys are verifiable (i.e., where it can be efficiently checked whether a public key has unique signatures). The only known tight unique signature schemes in the literature that support verifiable public keys are variants of chain-based signatures (CRYPTO 2017, FC 2018, EUROCRYPT 2022), which achieve tight security in the random oracle model. To achieve constant security loss, however, these schemes require log q calls of the random oracle to sign and verify, where q is an upper bound on the number of signatures generated using the scheme. In this work, we provide the first tight unique signature scheme with verifiable public keys which requires only a constant number (namely, six) random oracle queries to sign and verify. Specifically, we provide a general transformation akin to hash-and-sign which transforms a signature scheme with much weaker security (a variant of random unforgeability) into an EUF-CMA secure scheme. Signatures of our resulting scheme consist of at most 3 sub-signatures in parallel. Furthermore, we consider tightness in the multi-user setting, where the adversary may query signatures relative to many public keys, before deciding for which to forge. In this setting, we provide two constructions which achieve (1) a tight signature scheme, secure against semi-adaptive corruptions (i.e., where the adversary has to decide whether to corrupt a public key *before* making any signature queries relative to this key), and (2) a tight few-time signature scheme, secure against adaptive corruptions, where the scheme's setup is allowed to depend on an a-priori polynomial bound on the number of queries that the adversary has access to. These are the first unique signature schemes which are tightly secure in the multi-user model.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2720) | 2026-11-02
