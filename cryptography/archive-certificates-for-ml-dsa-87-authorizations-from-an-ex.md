---
title: "Archive Certificates for ML-DSA-87 Authorizations from an Exact Bounded Relation"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2739"
summary: "A blockchain that signs every transaction with FIPS 204 ML-DSA-87 keeps 4,627 bytes of signature per transaction forever. We describe and measure an archive certificate: one hash-based proof, for a ra"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

A blockchain that signs every transaction with FIPS 204 ML-DSA-87 keeps 4,627 bytes of signature per transaction forever. We describe and measure an archive certificate: one hash-based proof, for a range of already validated blocks, of knowledge of canonical FIPS 204 signatures on exactly the recorded messages under the keys resolved from chain state. Fresh blocks keep native verification. The construction starts from an exact bounded relation for ML-DSA-87 verification once the high bits u = w_1' are fixed. The main certificate keeps u hidden and proves the SHAKE256 challenge hash inside the proof, by a GKR argument for Keccak-f[1600] over the same WHIR commitment as the lattice relation. For 65,536 signatures we measured 104.09 bytes per signature in a Johnson-regime family, which has a classical bound only, and 126.89 in a unique-decoding family, against 4,627 bytes raw. The price is a slow prover and a verifier slower than native verification. At 2^{64} queries and 2^{20} verification submissions, conditional on cited Reed–Solomon proximity theorems, the classical random-oracle extraction error is below 2^{-188.07} for the Johnson family and below 2^{-201.99} for unique decoding. In the quantum random oracle model we state, for the unique-decoding family only, an extraction-failure bound below 2^{-129.67} at 2^{64} quantum queries; it is not a work factor. An external review is outstanding, so certificate-only bootstrap stays disabled.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2739) | 2026-11-03
