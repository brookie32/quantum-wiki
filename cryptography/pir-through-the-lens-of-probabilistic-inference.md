---
title: "PIR through the Lens of Probabilistic Inference"
date: "2026-10-28"
updated: "2026-10-29"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2669"
summary: "Private Information Retrieval (PIR) allows a client to retrieve an entry of a database while revealing no information about the requested index to the servers. Classic information-theoretic PIR protoc"
last_verified: "2026-10-29"
review_by: "2027-01-27"
stale: false
---

Private Information Retrieval (PIR) allows a client to retrieve an entry of a database while revealing no information about the requested index to the servers. Classic information-theoretic PIR protocols of Chor et al. (FOCS '95, JACM '98) and Ambainis (ICALP '97) achieve sublinear client computation and communication complexity with a constant number of servers, but require each server to perform computation linear in the database size. In this work, we ask for which classes of structured databases the server computation can be substantially reduced while preserving the communication complexity and privacy guarantees of these protocols. Our main contribution is a new connection between server computation in information-theoretic PIR and probabilistic inference. We show that the computation performed by every server in both the Chor et al. protocol and the recursive protocol of Ambainis can be viewed as computing a marginal probability of a product distribution. Consequently, efficient exact probabilistic inference algorithm immediately yields a faster server algorithm for PIR. We formalize this connection through the notion of inference complexity, which captures the complexity of evaluating these marginals. Using this framework, we obtain improved server computation for several broad classes of functions, including read-once arithmetic formulas, graphical models of bounded treewidth (and consequently arithmetic circuits of bounded treewidth), functions with low communication complexity, and functions with sparse Fourier representations. The resulting protocols preserve the communication complexity, client computation, and number of servers of the underlying PIR constructions while substantially reducing server computation for these structured function classes. Finally, we complement our algorithms with conditional lower bounds. Assuming the randomized Circuit Strong Exponential Time Hypothesis (rCSETH), we show that, for every constant (arepsilon>0), there exists a constant (c) such that no uniform algorithm can compute the first (virtual) server's response in the Chor et al. or Ambainis protocol on all (n)-input Boolean circuits of size at most (n^c) in time (O(N^{1-arepsilon})), where (N=2^n). Thus, under rCSETH, substantially sublinear server computation cannot be achieved uniformly for all polynomial-size Boolean circuits.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2669) | 2026-10-28
