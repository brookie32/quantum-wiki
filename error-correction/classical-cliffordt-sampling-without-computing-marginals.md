---
title: "Classical Clifford+T Sampling without Computing Marginals"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.06119"
summary: "arXiv:2611.06119v1 Announce Type: new Abstract: We introduce a new exact classical sampling algorithm for Clifford+T circuits, called T-by-T sampling. For a circuit with T-count t, it reduces sampling"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.06119v1 Announce Type: new Abstract: We introduce a new exact classical sampling algorithm for Clifford+T circuits, called T-by-T sampling. For a circuit with T-count t, it reduces sampling to evaluating 2t amplitudes of circuits with successively increasing T-counts 1,2,...,t, without the need to compute costly marginal probabilities. Crucially, the number of amplitude evaluations is completely independent of the surrounding Clifford structure. This makes T-by-T sampling well suited for use together with low-rank stabiliser decompositions, which enable efficient amplitude evaluations as long as the T-count is not too high. In that sense, T-by-T sampling is an improvement over the gate-by-gate sampling technique introduced by Bravyi, Gosset, and Liu (Phys. Rev. Lett. 128, 2022), where the number of amplitudes instead scales with the number of non-monomial operations such as Hadamard gates, which can remain large even in circuits with low stabiliser rank. Concretely, T-by-T sampling offers significant speedups in regimes where T gates are embedded within large Clifford computations. This makes it well suited for applications such as simulating quantum error correction experiments, which typically have lower T complexity but involve extensive Clifford operations and measurements. In particular, we show how T-by-T sampling allows us to take samples from recent end-to-end magic state cultivation circuits with escape up to distance 19 in a couple of seconds.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.06119) | 2026-11-05
