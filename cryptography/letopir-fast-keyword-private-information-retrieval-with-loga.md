---
title: "LetoPIR: Fast Keyword Private Information Retrieval with Logarithmic Communication"
date: "2026-08-27"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1814"
summary: "Keyword private information retrieval (PIR) allows a client to retrieve a record associated with a keyword from a database without revealing any information about the keyword. In the standard single-s"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

Keyword private information retrieval (PIR) allows a client to retrieve a record associated with a keyword from a database without revealing any information about the keyword. In the standard single-server setting, existing hintless keyword PIR protocols incur substantial communication and computation costs. In this paper, we propose an efficient approach to generate k-hot vectors (i.e., vectors with exactly k non‑zero components) in homomorphic-encryption form, and present a bucket-merging technique to decrease the maximum size of buckets. Based on these techniques, we construct LetoPIR, a hintless keyword PIR protocol that outperforms previous PIR protocols in the same setting. Compared to the state-of-the-art hintless keyword PIR scheme, SparsePIR (USENIX'23), LetoPIR achieves a 12.4imes sim 17.0imes improvement in communication cost for databases ranging from 256 MB to 4 GB with records of 256 bytes, and more than 3.0imes improvement in computation cost for the 256 MB database. Compared to the state-of-the-art keyword PIR scheme with client hint, KPIR (USENIX'25), LetoPIR reduces the communication cost by 51.4imes sim184.8imes, while achieving a similar (even better) computation cost.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1814) | 2026-08-27
