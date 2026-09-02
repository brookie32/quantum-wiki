---
title: "Wagner's k-Tree Revisited: Memory-Time Costs of Preimage Attacks on Incremental Hashes"
date: "2026-08-30"
updated: "2026-09-02"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1835"
summary: "Wagner's k-tree algorithm solves the generalized birthday problem and underlies preimage attacks on randomize-then-combine incremental hashes (EUROCRYPT '97) such as iSHAKE, LtHash, and AdHash. In its"
last_verified: "2026-09-02"
review_by: "2026-12-01"
stale: false
---

Wagner's k-tree algorithm solves the generalized birthday problem and underlies preimage attacks on randomize-then-combine incremental hashes (EUROCRYPT '97) such as iSHAKE, LtHash, and AdHash. In its full-index execution, the 2^{k-1} index entries dominate peak memory at large k, and index trimming narrows each entry but leaves their number intact. Tang et al. (TCHES '26) introduced post-retrieval for the single-chain algorithm and left the 2^k exponent of the k-tree setting as an open problem. We resolve it by extending post-retrieval to the k-tree algorithm. This cuts the peak working memory to P_kell N = O(k^2 ell N), removing the 2^{k-1} index entries from the forward pass at the cost of a Theta(k) time overhead. Free elta-level caching shrinks this time factor at no memory cost. The trade-off is starkly asymmetric: it removes an exponential number of index entries for only a linear recovery-time overhead. As a practical application, we revisit the list-item-reduction landscape for the k-tree algorithm under the memory-time product metric, mathsf{MT} = M dot T. The gain is regime-dependent: for small k the index entries do not yet dominate, so the recovery overhead outweighs the saving. For large k the saving dominates, lowering the optimized log_2 mathsf{MT} from 4sqrt{n} to 2sqrt{2n} at leading order. For fixed-size iSHAKE preimage attacks, we save approximately 51 and 122 bits over state-of-the-art index trimming for iSHAKE-128 and iSHAKE-256, respectively, in the unlimited-block setting, narrowing to roughly 6 and 8 bits under block-count caps.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1835) | 2026-08-30
