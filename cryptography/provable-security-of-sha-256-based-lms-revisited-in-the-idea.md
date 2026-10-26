---
title: "Provable Security of SHA-256-Based LMS Revisited in the Ideal-Cipher Model"
date: "2026-10-24"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2624"
summary: "The hash-based Leighton-Micali Signature (LMS) has been standardized by IETF, NIST and ISO. State-of-the-art non-quantum security proofs for LMS have been given by Katz (SSR 2016) and Fluhrer (Eprint "
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

The hash-based Leighton-Micali Signature (LMS) has been standardized by IETF, NIST and ISO. State-of-the-art non-quantum security proofs for LMS have been given by Katz (SSR 2016) and Fluhrer (Eprint 2017/553). However, the actual structure of SHA-256(/192) is the (chopped) Merkle-Damg{aa}rd construction using a blockcipher-based Davies-Meyer function, and precise security bounds of SHA-256-based LMS_SHA256_M32 and SHA-256/192-based LMS_SHA256_M24 should be derived in the {it ideal-cipher model (ICM)}. This was {it not} considered in Katz and Fluhrer's proofs. In fact, by leveraging structural properties of (chopped) Merkle-Damg{aa}rd, we exhibit forgery attacks against LMS_SHA256_M32 and LMS_SHA256_M24 that expose the inapplicability of Katz's and Fluhrer's random-oracle bounds to the concrete SHA-256 constructions. The precise security guarantees of LMS_SHA256_M32 and LMS_SHA256_M24 thus remain unknown (and are also missing in the standards). To bridge the structural gap, we provide ICM-based security proofs for the additive-Davies-Meyer abstractions of LMS_SHA256_M32 and LMS_SHA256_M24. The security level of LMS_SHA256_M32 is roughly 256-log_2 widehat{B} bits, where widehat{B} is the number of blocks in SHA-256 calls internally made by LMS_SHA256_M32 and widehat{B}ll2^{128}. The security level of LMS_SHA256_M24 is roughly min { 192 - log_2 widehat{Gamma} , 256-log_2 widehat{B} } bits, where widehat{Gamma} is the number of SHA-256/192 calls internally made by LMS_SHA256_M24 and widehat{B} is the number of blocks in them, and widehat{B}ll2^{128} and widehat{B} widehat{Gamma} ll 2^{192}. In conclusion, LMS_SHA256_M32 and LMS_SHA256_M24 ensure a moderate (yet not ``full'') level of security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2624) | 2026-10-24
