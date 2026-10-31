---
title: "Quasi-polynomial time algorithms for block basis reduction of linear codes"
date: "2026-10-29"
updated: "2026-10-31"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2685"
summary: "The block code basis reduction algorithm (BKZ) proposed by Ghentiyala and Stephens-Davidowitz requires an exponential number of calls to the minimum weight codeword (MWC) oracle according to the weak "
last_verified: "2026-10-31"
review_by: "2027-01-29"
stale: false
---

The block code basis reduction algorithm (BKZ) proposed by Ghentiyala and Stephens-Davidowitz requires an exponential number of calls to the minimum weight codeword (MWC) oracle according to the weak complexity bounds established in the original paper. In almost all cases these bounds are worse than plain enumeration of codewords, despite the fact that in practice the algorithm works much better. In this work we propose block code basis reduction algorithms with polynomial and quasi-polynomial complexity for fixed eta. Our algorithms are relaxations and modifications of the original algorithm. First, we show that the truncated version of the BKZ algorithm requires heuristic quasi-polynomial time of calls to MWC-oracle with the same basis quality as in the full BKZ algorithm. Second, we add some weak restrictions on the code basis that enables the algorithm to run in polynomial number of calls to the oracle. Third, we introduce the DeepBKZ algorithm which is adapted from lattice reduction. Under some relaxations (analogs of PotBKZ from the lattices) it also runs in quasi-polynomial number of calls to the MWC-oracle. We provide an implementation of proposed algorithms which is capable to process block sizes 2-24 and more. Based on this implementation, we provide concrete complexity estimates and an analysis of the approximation factors achieved for the low-weight codeword problem on random linear codes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2685) | 2026-10-29
