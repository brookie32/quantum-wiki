---
title: "Prepared Episodes for Short Online Hash Based Signatures"
date: "2026-08-17"
updated: "2026-08-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1708"
summary: "SPHINCS+ provides stateless signing and self-contained verification, but its signatures are large: every message carries a FORS signature and a complete WOTS+/Merkle authentication chain to the long-t"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

SPHINCS+ provides stateless signing and self-contained verification, but its signatures are large: every message carries a FORS signature and a complete WOTS+/Merkle authentication chain to the long-term root. This cost is repeated even when messages arrive in a bounded episode whose maximum size is known in advance. We introduce prepared-episode signatures and instantiate them as SPHINCS-PE. The construction splits a globally addressed hypertree at an episode boundary into upper and lower trees. Preparation authenticates the boundary root through the upper tree, while each online signature traverses the lower tree back to that root. Because the upper tree is computed before messages arrive, it can use fewer, taller layers. This removes WOTS+ blocks from full signatures at the cost of more preparation work. Full signatures remain self-contained, while recurring verifiers may cache the upper certificate. Our fixed-count exposure analysis pools colliding preparations and bounds post-selection of the target episode. The end-to-end theorem reduces unforgeability to PE-ITSR and explicit PRF and hash-component games. Compared with the matched FIPS 205 SLH-DSA profiles, SPHINCS-PE reduces full-signature sizes by 3% to 12% for the short profiles and by 25% to 40% for the fast profiles. With the upper certificate cached, online signatures are 24% to 48% smaller for short profiles and 56% to 70% smaller for fast profiles. These results show that prepared episodes can shorten hash-based signatures without giving up self-contained verification.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1708) | 2026-08-17
