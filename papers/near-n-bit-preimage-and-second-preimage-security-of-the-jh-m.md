---
title: "Near-n-Bit Preimage and Second-Preimage Security of the JH Mode"
date: "2026-11-27"
updated: "2026-11-27"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3071"
summary: "Existing direct bounds on preimage and second-preimage resistance for the JH mode remain at the birthday scale. We revisit this mode in the ideal-permutation model, with a (2n)-bit state and permutati"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Existing direct bounds on preimage and second-preimage resistance for the JH mode remain at the birthday scale. We revisit this mode in the ideal-permutation model, with a (2n)-bit state and permutation, (n)-bit message blocks, and an (n)-bit digest. Each permutation query supplies one edge into every column of the state graph. We use Menger's theorem to bound which endpoints those edges can connect through the residual graph, and a potential to bound the growth of the states on either side. For messages of at most (2^{64}) bits and padding with (ell(M)leqlceil |M|/nrceil+1) blocks, the resulting bounds give negligible advantage up to (2^{n-2sqrt{2n}-O(log n)}) queries. For the widths of JH-512, the unweighted certificates bound success probability below (1/2) up to (2^{431}) queries for preimages and (2^{416}) for second preimages. Both budgets include candidate evaluation. Our Lean 4 development covers the fixed-target preimage proof and the second-preimage bound with a common occupancy threshold.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3071) | 2026-11-27
