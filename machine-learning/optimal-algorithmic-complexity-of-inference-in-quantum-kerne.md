---
title: "Optimal algorithmic complexity of inference in quantum kernel methods"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.15214"
summary: "arXiv:2604.15214v3 Announce Type: replace Abstract: Quantum kernel methods are among the leading candidates for achieving quantum advantage in supervised learning. A key bottleneck is the cost of infe"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2604.15214v3 Announce Type: replace Abstract: Quantum kernel methods are among the leading candidates for achieving quantum advantage in supervised learning. A key bottleneck is the cost of inference: evaluating a trained model on new data requires estimating a weighted sum sum_{i=1}^N alpha_i k(x,x_i) of N kernel values to additive precision arepsilon, where alpha is the vector of trained coefficients. The standard approach estimates each term independently via sampling, yielding a query complexity of O(NlVertalpharVert_2^2/arepsilon^2). In this work, we identify two independent axes for improvement: (1) How individual kernel values are estimated (sampling versus quantum amplitude estimation), and (2) how the sum is approximated (term-by-term versus via a single observable), and systematically analyze all combinations thereof. The query-optimal combination, encoding the full inference sum as the expectation value of a single observable and applying quantum amplitude estimation, achieves a query complexity of O(lVertalpharVert_1/arepsilon), removing the dependence on N from the query count and yielding a quadratic improvement in both lVertalpharVert_1 and arepsilon. We prove a matching lower bound of Omega(lVertalpharVert_1/arepsilon), establishing query-optimality of our approach up to logarithmic factors. Beyond query complexity, we also analyze how these improvements translate into gate costs and show that the query-optimal strategy is not always optimal in practice from the perspective of gate complexity. Our results provide both a query-optimal algorithm and a practically optimal choice of strategy depending on hardware capabilities, along with a complete landscape of intermediate methods to guide practitioners. All algorithms require only amplitude estimation as a subroutine and are thus natural candidates for early-fault-tolerant implementations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.15214) | 2026-11-20
