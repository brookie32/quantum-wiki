---
title: "Adaptively Secure (Threshold) Batched IBE from Static Assumptions"
date: "2026-11-09"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2843"
summary: "Batched identity-based encryption (batched IBE) lets a key authority release one short decryption key for a set of identities and a batch label/epoch. It has been used to mitigate maximal extractable "
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

Batched identity-based encryption (batched IBE) lets a key authority release one short decryption key for a set of identities and a batch label/epoch. It has been used to mitigate maximal extractable value (MEV) attacks on public blockchains. Existing constructions either use the generic-group and/or random-oracle models, or rely on q-type assumptions whose size grows with the batch-size bound. In this paper, we present the first adaptively secure batched IBE scheme from static assumptions. Our scheme supports an exponential identity space and an exponential epoch space, and its ciphertexts, digests, and batch keys consist of a constant number of group elements independent of the batch size. Our scheme relies on composite-order bilinear groups, and we prove its adaptive security assuming hardness of static subgroup decision assumptions and a static pairing assumption, with a security loss polynomial in the security parameter lambda and the number of key queries. Our proof does not rely on q-type assumptions, random oracles, generic-group arguments, or complexity leveraging. We also present a threshold version with adaptive challenge security under static corruption, and translate our scheme to prime-order bilinear groups under the static MDDH assumption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2843) | 2026-11-09
