---
title: "The Post-Quantum Cost of Garbled-Circuit Bitcoin Bridges"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2383"
summary: "Recent Bitcoin bridge designs rely on verification of succinct proofs to process withdrawals. This requires off-chain garbled circuit evaluation of a succinct proof, the input labels for which must be"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

Recent Bitcoin bridge designs rely on verification of succinct proofs to process withdrawals. This requires off-chain garbled circuit evaluation of a succinct proof, the input labels for which must be encoded on chain in a manner compatible with malicious security. We assess the post-quantum vulnerability of these cryptographic components, and examine the costs of secure alternatives. Circuit sizes for post-quantum proving systems can be made smaller than the current pairing-based baseline, but at the cost of significantly higher proof sizes that incur greater cost and require multiple Bitcoin blocks to encode. We suggest avenues of future research to improve efficiency of proofs, circuit representations, and input encodings.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2383) | 2026-10-06
