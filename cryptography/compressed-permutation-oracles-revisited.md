---
title: "Compressed Permutation Oracles Revisited"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.28469"
summary: "arXiv:2609.28469v1 Announce Type: new Abstract: The compressed permutation oracle has been used to analyze the quantum security of a number of cryptographic constructions which resisted prior techniqu"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2609.28469v1 Announce Type: new Abstract: The compressed permutation oracle has been used to analyze the quantum security of a number of cryptographic constructions which resisted prior techniques. However, these analyses were fundamentally limited by the poor soundness of the method: the technique was proven sound only up to O(N^{1/12}) queries to permutations on N elements. We revisit this analysis, improving the soundness bound to a tight Omega(N^{1/2}). In addition to being tighter, our proof is conceptually simpler and more direct, and gives the same bound in the ideal cipher model. The main technical idea is to construct the compression isometry from a simple POVM on the naive purification, a technique which may find wider applications. As immediate applications, our results yield tight, concrete collision and pre-image lower bounds for the sponge hash construction underlying SHA3 and the Davies--Meyer compression function used in SHA1 and SHA2. More broadly, the improved soundness theorem provides a general-purpose tool for analyzing quantum security in settings where random permutations or ideal ciphers serve as the underlying primitive.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.28469) | 2026-09-24
