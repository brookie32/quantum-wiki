---
title: "Access Cost Tradeoffs in Mixed-Mode Oblivious RAM"
date: "2026-11-09"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2847"
summary: "A mixed-mode oblivious RAM (ORAM) lets each memory request be marked public or private: public requests disclose their addresses, private requests hide them. We ask how much work such a scheme must do"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

A mixed-mode oblivious RAM (ORAM) lets each memory request be marked public or private: public requests disclose their addresses, private requests hide them. We ask how much work such a scheme must do, and which requests must do it, in the cell-probe model—with a passive server that only reads and overwrites addressed words. We examine the expected amortized per-request cost on randomized workloads with independent modes and uniformly random addresses. For array size n and client memory mle n^{1-arepsilon} words, let H=log_2(2+n/(m+1)). Our main result is a tight tradeoff between the cost of public reads and private writes. We show that if a request is private with probability 0<ple1/2 and private requests cost at most Q probes on average, then every scheme with mle n^{1-arepsilon} has expected public-read cost[ Omega!left(maxleft{1, frac{H}{log_2(2+1/p+Q/H)}right}right), ]even when the server learns the kind (read/write) of each private request. For polynomial m, we provide constructions that match this bound whenever Q exceeds a threshold that we identify for both Q treated as an expectation over the workload and as the average cost for the worst-case workload. In particular, at constant private frequency p a logarithmic private budget forces logarithmic public-read cost, and constant public-read cost requires private cost (n/(m+1))^{Omega(1)}. This answers, for passive servers, the question posed by Zhang, Wang, and Weng, whose PIR-based scheme achieves constant public and logarithmic private bandwidth with server computation. Our lower bound proof fixes the public query and changes its private history; crucially, we charge them separately. Our constructions combine a public cache with linear merges of hash tables. Two further groups of results concern public writes and total work. Firstly, we give a cost tradeoff between public writes and private reads. Secondly, for workloads mixing private operations, public reads, and public writes with probabilities p,r,a, we show that every scheme with mle n^{1-arepsilon} has total cost per request Omega(max{1,H/log_2(2+1/p)}) when private request kinds are hidden, and a construction with polynomial client memory matches this bound with a constant independent of p,r,a. We also separately bound the costs of reads and writes in this workload. Lastly, public requests can in some cases be made cheaper by offloading their cost to preparation in earlier requests or cleanup in later ones. For both public reads and writes, we show localized tradeoffs constrained to a subset of requests, which demonstrate some of the limitations of such offloading.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2847) | 2026-11-09
