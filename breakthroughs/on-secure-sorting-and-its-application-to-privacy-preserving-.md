---
title: "On Secure Sorting and Its Application to Privacy-Preserving Graph Pattern Matching"
date: "2026-10-13"
updated: "2026-10-14"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2457"
summary: "Sorting in secure computation has been studied almost as long as there have been implementations of multi-party computation (Wang et al., AsiaCCS'10). More recent advances include completely secure im"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Sorting in secure computation has been studied almost as long as there have been implementations of multi-party computation (Wang et al., AsiaCCS'10). More recent advances include completely secure implementations (revealing nothing other than the list size) that have used Quicksort (Araki et al., CCS'21) and radix sort (Asharov et al., CCS'22). For the first time, we extensively compare the two variants across a range of parameters and for both honest- and dishonest-majority computation. We then apply secure sorting to improve sparse matrix multiplication without oblivious RAM based on recent work by Damie et al. (CODASPY'26). Our main contribution here is to produce an output in the same format as the inputs to the multiplication. This is needed for repeated multiplication of graph adjacency matrices, which we use to find cycles in graphs. Such cycles have been associated with money laundering, and this also applies to another graph pattern dubbed scatter-gather, which we can detect with the same approach. Our work therefore can be applied to privacy-preserving anti-money laundering detection.



## Related
- [[truffle-maliciously-secure-three-party-shuffles-with-applica|Truffle: Maliciously Secure Three-Party Shuffles with Applications to Parsing]]
- [[fair-and-efficient-helper-aided-mpc-with-cheater-identificat|Fair and Efficient Helper-Aided MPC with Cheater Identification]]
- [[universally-composable-reverse-firewalls-for-oblivious-linea|Universally Composable Reverse Firewalls for Oblivious Linear Evaluation and Applications]]

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2457) | 2026-10-13
