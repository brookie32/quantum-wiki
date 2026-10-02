---
title: "On the generic structures of the protocols for quantum auction and quantum summation and their relation"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.27693"
summary: "arXiv:2606.27693v2 Announce Type: replace Abstract: Secure multi-party computation (SMC) addresses the problem of jointly computing global functions of private inputs while revealing minimal informati"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2606.27693v2 Announce Type: replace Abstract: Secure multi-party computation (SMC) addresses the problem of jointly computing global functions of private inputs while revealing minimal information about individual data. Two prominent examples of SMC tasks are sealed-bid auction and secure multi-party summation. Existing schemes for quantum auction and quantum summation have largely been developed independently, motivated by distinct applications and employing different computational primitives. In this work, mutual reductions between the two tasks are established for single-item sealed-bid auctions with first-price payment. In one direction, an auction used as a black box computes a secure sum: each party bids a private random key drawn from its input, so the clearing price depends on the inputs only through their sum S. The reduction is perfectly private against colluding semi-honest parties and uses O(S^2log(1/elta)) auction rounds, which is optimal, or O(Slog(1/elta)) under coherent access. It can be instantiated with an existing auctioneer-free quantum auction after a one-line change to its disjunction subroutine, which as published leaks occupancy counts. In the other direction, summation with randomized inputs yields threshold disjunctions, and a single search over composite keys locates the highest bid and a winner, revealing nothing else. Because each query consumes the bidders' encodings, a bidder can adapt its effective bid undetected, while a fixed query set restores sealed bidding. Combinatorial auctions and general payment rules lie outside this framework. On a superconducting processor, one instance of each direction is executed, recovering the winner for four-bidder instances with ties and the sum of private inputs from repeated auctions.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.27693) | 2026-10-02
