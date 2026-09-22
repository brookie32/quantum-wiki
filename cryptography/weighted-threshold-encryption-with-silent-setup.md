---
title: "Weighted Threshold Encryption with Silent Setup"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2148"
summary: "We construct the first non-trivial weighted threshold encryption scheme with silent setup. The CRS and each public key consists of O(W) group elements, where W is the maximum committee weight. Both th"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

We construct the first non-trivial weighted threshold encryption scheme with silent setup. The CRS and each public key consists of O(W) group elements, where W is the maximum committee weight. Both the weight assignments and the threshold for decryption can be dynamically chosen at encryption time. Each partial decryption is a single G1 element computed non-interactively with one scalar multiplication, independent of the party's weight. The CPA ciphertext is two G_1 elements, improving upon the shortest known unweighted scheme, and CCA security costs two additional field elements. We prove security in the generic bilinear group model.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2148) | 2026-09-22
