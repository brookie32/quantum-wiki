---
title: "zk-BAN: An efficient anonymous blocklisting system with signature-based revocation"
date: "2026-09-30"
updated: "2026-10-01"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2274"
summary: "Anonymous blocklisting enables services to revoke malicious users while preserving anonymity for honest users. Signature-based revocation supports revocation from past authentications, but existing sy"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

Anonymous blocklisting enables services to revoke malicious users while preserving anonymity for honest users. Signature-based revocation supports revocation from past authentications, but existing systems incur substantial overhead at large scale and for users returning after long offline periods. Window-based alternatives reduce this overhead but impose restrictive revocation-timing policies. This work presents zk-BAN, a signature-based anonymous blocklisting system that reduces proof-generation and verification costs through two design improvements: constructing a carefully filtered revocation list and partially unifying PRF tags to reduce repeated zero-knowledge computations. We formalize zk-BAN and prove that it satisfies blocklistability and unlinkability. Under modeled large-scale real-world workloads, zk-BAN generates proofs in approximately 600 ms and verifies them in approximately 2 ms. We show zk-BAN displays 54.4 times faster proving than our naive baseline and 136-fold faster proving and 32-fold faster verification than prior work.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2274) | 2026-09-30
