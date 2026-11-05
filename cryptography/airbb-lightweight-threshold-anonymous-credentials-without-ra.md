---
title: "AirBB: Lightweight Threshold Anonymous Credentials without Random Oracles from BB Signatures"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2762"
summary: "Anonymous credentials are a well-studied cryptographic primitive enabling users to prove statements about their identity and selectively present personal information in an unlinkable manner. The issue"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Anonymous credentials are a well-studied cryptographic primitive enabling users to prove statements about their identity and selectively present personal information in an unlinkable manner. The issuer, however, is often a single point of failure. Threshold issuance addresses this by distributing the issuer across several parties such that a quorum of them must cooperate to issue credentials. Numerous constructions of single-issuer and threshold issuance anonymous credentials have been proposed. However, existing schemes each have at least one of the following weaknesses: (1) their presentations depend on the number of attributes, (2) they are not concretely efficient, or (3) they rely on the random oracle model (ROM) for non-interactive presentations. In this work, we present a new construction of threshold anonymous credentials that has a constant presentation size of 240 bytes, rivals the efficiency of BBS, and does not rely on the random oracle model. We achieve this by combining techniques from set commitments with Boneh-Boyen (BB) signatures (Eurocrypt'04) and prove our scheme's security in the algebraic group model. This is on par with the tight security proofs of existing schemes, which typically rely on the AGM or GGM, or on assumptions justified in those models. Since signing uses linear operations, the scheme is easily thresholdizable, without requiring interaction between the issuers or preprocessing.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2762) | 2026-11-04
