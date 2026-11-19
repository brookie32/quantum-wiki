---
title: "Live Noise Fingerprints for Quantum Program Analysis"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.19143"
summary: "arXiv:2611.19143v2 Announce Type: replace-cross Abstract: Quantum programs are probabilistic in nature, and noisy execution due to current imperfect hardware further complicates their analysis. In thi"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.19143v2 Announce Type: replace-cross Abstract: Quantum programs are probabilistic in nature, and noisy execution due to current imperfect hardware further complicates their analysis. In this paper, we study abstract semantics for analysing quantum programs under these conditions. We introduce noise fingerprints, compact descriptions of the observable effects of noise relative to a finite interface of input states and output measurements. We use them to define our abstract domain with respect to the concrete noise-related behaviour. We relate the concrete and abstract domains through a probabilistic Galois connection, extending the Galois-connection framework to distribution-valued interpretations. We study the resulting abstraction in terms of observational soundness, conciseness, efficiency, and ability to adapt to changing noise. We show that polynomial-size interfaces yield exponentially smaller fingerprints than full noise models while preserving the chosen observations, and that fingerprint distance characterises the largest observational discrepancy over the chosen interface. Further, we develop ChanShadow, which reuses noise fingerprints of commonly used short program fragments to analyse noisy execution of whole programs and provides a uniform finite-sample error bound. We construct working examples showing how fingerprints support program analysis. We evaluate fingerprint precision, representation cost, measurement requirements, and behaviour under noise drift. On a synthetic benchmark, fingerprints retain (99 pm 1)% of the noise strength information of a full noise model. On simulated noise drift, reusing earlier measurements reduces the number of fresh measurement rounds needed to reach an error tolerance of 0.10 by a factor of 2.3 at 95% confidence and by a factor of 27 under the median-error criterion.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.19143) | 2026-11-19
