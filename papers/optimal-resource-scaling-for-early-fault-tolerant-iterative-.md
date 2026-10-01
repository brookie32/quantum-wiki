---
title: "Optimal Resource Scaling for Early Fault Tolerant Iterative Quantum Phase Estimation under Cost Error Tradeoffs"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40128"
summary: "arXiv:2609.40128v1 Announce Type: new Abstract: The iterative quantum phase estimation algorithm (IPEA) is better suited for NISQ and early fault-tolerant hardware compared to the original algorithm, "
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40128v1 Announce Type: new Abstract: The iterative quantum phase estimation algorithm (IPEA) is better suited for NISQ and early fault-tolerant hardware compared to the original algorithm, which requires the inverse quantum Fourier transform. However, current error mitigation and correction implementations lead to imperfect unitaries, causing erroneous phase feedback in IPEA. To improve the reliability of phase bits is to repeat the k^th iteration for the 2^k-th power of the unitary N_k^* times, followed by a majority decision. However, due to variations in their circuit complexities, different iterations incur varying resource costs (w_k) and different per-shot error probabilities (q_k). Given tight resource constraints, we ask what the optimal number {N_k^*: 1le k le L} of shots per bit is: $arg max_{{N_k}} P(ext{all } L ext{ bits correct}) ext{ s.t.} sum_{k=1}^L w_k N_k le W We obtain closed-form expressions for N^*_k under the conditions: W gg sum_k w_k (enough for at least one shot per iteration), w_k increases with k, q_k are small enough and L is large. We do so by analyzing tractable upper and lower surrogate problems derived via tight concentration and anti-concentration bounds and showing that their solutions converge when q_kll 1. We observe that when Wgg sum_k w_k ln! left(sum_k w_kright), the optimal N_k^* is proportional to frac{ln! left(sum_k w_kright)}{c_k} and does not depend on individual w_k, where c_k=-lnleft(2sqrt{left(1-frac{q_k}{2} right) frac{q_k}{2}}right) propto lnfrac{1}{q_k}. However, when sum_k w_k ll Wllsum_k w_k ln! left(sum_k w_kright), the allocation is also (additively) influenced by frac{1}{c_k}lnfrac{1}{w_k} for larger values of k$, i.e., higher powers of unitary. These results lead to simple rules of thumb for resource allocation that may benefit the design of practical systems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40128) | 2026-10-01
