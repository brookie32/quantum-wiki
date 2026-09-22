---
title: "CKKS Bootstrapping in less than 10ms"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2119"
summary: "Bootstrapping enables deep homomorphic computation in CKKS by replenishing multiplicative levels. It remains one of the scheme's most expensive operations. HEAAN reports a bootstrapping latency of 6.9"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Bootstrapping enables deep homomorphic computation in CKKS by replenishing multiplicative levels. It remains one of the scheme's most expensive operations. HEAAN reports a bootstrapping latency of 6.97ms, substantially faster than other publicly documented alternatives. However, the algorithmic and implementation techniques underlying this result have not been disclosed, leaving it unclear how such performance is achieved. In this work, we present a fully specified CKKS bootstrapping construction that achieves performance comparable to that reported by HEAAN. Building on SHIP (presented in Eurocrypt 2025), we introduce several algorithmic innovations that reduce communication and computational overhead while enabling efficient parallel execution. Our implementation bootstraps a single complex-valued ciphertext in 8.2ms and achieves an amortized latency of 4.6ms per ciphertext for a batch of 64. These results demonstrate practical sub-10ms CKKS bootstrapping.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2119) | 2026-09-20
