---
title: "Cross-Signature Signing-Key Recovery and Domain-Separation Repair for SDitH v2"
date: "2026-08-26"
updated: "2026-08-28"
source: "agent"
category: "industry"
tags: [industry, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1808"
summary: "We give the first cross-signature signing-key recovery attack on SDitH v2 from public chosen-message transcripts. Each hidden VOLE leaf exposes a commitment and a public endpoint A=mathsf{wit}oplus G_"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

We give the first cross-signature signing-key recovery attack on SDitH v2 from public chosen-message transcripts. Each hidden VOLE leaf exposes a commitment and a public endpoint A=mathsf{wit}oplus G_{rm wit}(s) that masks the permanent witness, and because share expansion uses s as the block-cipher key with an all-zero IV, one candidate stream block can be tested against all endpoints under the same public key. The attack shares nonlinear terms of the unary RSD predicates across endpoints, organizes public masks in tries, and updates the circuit along a Gray-code traversal, while a two-block leaf commitment validates each survivor before signing-key reconstruction. With q=2^{12} signatures, complete key recovery and forgery cost 11.23–11.67 bits less than matched AES-128/192/256 exhaustive search across six parameter sets, and the comparison includes target identification, commitment validation, signer-used keys, signature acquisition, witness reconstruction, and fresh signing. A multi-key experiment measures the generic gain from multiple targets, and executions over a reduced domain against the official C implementation recover the signing witness and produce a fresh accepted signature for every parameter set. We repair the shared stream domain by labelling each expansion with the signature salt, global leaf ordinal, and block position; this change preserves signature size and block-cipher call count and reduces the attack to generic multi-target search.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1808) | 2026-08-26
