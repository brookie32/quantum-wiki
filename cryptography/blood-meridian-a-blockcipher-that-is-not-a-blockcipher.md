---
title: "Blood MERIDIAN: a blockcipher that is not a blockcipher"
date: "2026-08-27"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1818"
summary: "MERIDIAN is a 128-bit blockcipher proposed as a lightweight AES alternative. We show that its “Directional Substitution” layer is not injective by giving an explicit collision. This yields a full 12-r"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

MERIDIAN is a 128-bit blockcipher proposed as a lightweight AES alternative. We show that its “Directional Substitution” layer is not injective by giving an explicit collision. This yields a full 12-round collision for every key. Consequently, no keyed instance of MERIDIAN is a permutation, so no decryption function can invert encryption on all plaintexts, and its blockcipher and PRP security claims fail. We additionally identify a one-round differential that exceeds the claimed bound by a factor 13.37.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1818) | 2026-08-27
