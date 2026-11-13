---
title: "Bulletproofs are Optimal: Lower Bounds for Vector Commitments from Fiat-Shamir in Pairing-Free Groups"
date: "2026-11-11"
updated: "2026-11-13"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2868"
summary: "Vector Commitments allow parties to commit to an (ordered) vector and to later succinctly open it at any desired position. In plain (i.e., known order and pairing-free) prime-order groups, all state-o"
last_verified: "2026-11-13"
review_by: "2027-02-11"
stale: false
---

Vector Commitments allow parties to commit to an (ordered) vector and to later succinctly open it at any desired position. In plain (i.e., known order and pairing-free) prime-order groups, all state-of-the-art constructions rely on the combination of a generalized Pedersen commitment and an inner product argument. This includes the celebrated constructions of Bootle et al. (EUROCRYPT 2016) and Bünz et al. (S&P 2018), and subsequent improvements. All of these achieve proofs consisting of Theta(log n) group elements, and further provide useful properties including malleability, subvector opening and transparent setup. However, breaking the O(log n) barrier in the plain discrete logarithm setting has proven to be a hard problem. This is in stark contrast with other settings, e.g. from pairing-friendly groups or groups of unknown order, where constructions with constant-size commitment and openings have been known for over a decade. In this work we investigate whether this limitation is inherent to constructions based on prime-order groups. Specifically we prove new lower bounds for any accumulator (a weaker object than vector commitments, thus making our result more general), with interactive public-coin membership proof in Maurer's Generic Group Model. An implication of our result is that in such setting at least one of the following must occur: (i) the commitment has super-constant size; (ii) the opening proof contains Omega(log n) group elements; (iii) the opening proof has length n^{1-o(1)}. Our bound further extends to primitives that directly imply accumulators/VCs including polynomial/functional commitments and inner product arguments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2868) | 2026-11-11
