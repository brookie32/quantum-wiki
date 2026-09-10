---
title: "Pairing-based Succinct Half-Chosen VOLE"
date: "2026-09-08"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1922"
summary: "Succinct Non-Interactive Half-Chosen VOLE allows a sender with a vector oldsymbol x of length n and a receiver with a scalar y to establish a pair of additive shares of oldsymbol x dot y, by simultane"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

Succinct Non-Interactive Half-Chosen VOLE allows a sender with a vector oldsymbol x of length n and a receiver with a scalar y to establish a pair of additive shares of oldsymbol x dot y, by simultaneous exchange of succinct messages. Recent works construct NIHC-VOLE with O(n^{2/3} lambda) communication from various assumptions (Abram, Roy and Scholl, Eurocrypt 24) and poly-logarithmic communication from LWE (Abram, Malavolta and Roy, STOC 25). We explore how bilinear pairings can improve group-based NIHC-VOLE schemes. • In the public setup setting, our scheme has online communication of O(sqrt{n log n}) group elements. The scheme relies on a new BDDH-like assumption. • In the designated receiver setting, our scheme has online communication of only 3 group elements and reusable offline communication of O(n) group elements. The scheme relies on the bilinear power DDH assumption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1922) | 2026-09-08
