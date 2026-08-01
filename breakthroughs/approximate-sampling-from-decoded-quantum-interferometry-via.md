---
title: "Approximate sampling from decoded quantum interferometry via Markov chain Monte Carlo methods"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.28120"
summary: "arXiv:2607.28120v1 Announce Type: new Abstract: Optimization problems are among the leading candidates for industrially relevant quantum advantage. Decoded quantum interferometry (DQI) has been propos"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2607.28120v1 Announce Type: new Abstract: Optimization problems are among the leading candidates for industrially relevant quantum advantage. Decoded quantum interferometry (DQI) has been proposed to tackle approximate optimization, establishing a connection to classical decoding problems. While previous work has primarily focused on the theoretical complexity of DQI, comparatively little is known about its empirical performance relative to classical algorithms. In this work, we shed further light on the complexity of DQI and investigate numerically whether classical sampling methods can emulate the optimization capabilities of DQI. We first present a simplified analytical characterization of DQI that connects its expected performance to binomial statistics, and we identify concrete obstacles in further studying the complexity of DQI. Exploiting the fact that DQI output probabilities are efficiently computable, we apply Markov chain Monte Carlo (MCMC) techniques, particularly block-Gibbs sampling, to sample from the induced distribution. We study the runtime scaling of these methods for two optimization problems called max-XORSAT, where we reach beyond 1000 effective qubits; and OPI, where we reach beyond 150 effective qubits. Our results show that MCMC algorithms can reliably attain the approximation ratios expected from DQI across a broad range of problem sizes. In OPI, in the regime where a super-polynomial advantage is claimed for DQI, we observe an empirical runtime for MCMC that scales approximately as 1.1^{n}, indicating exponential growth with a comparatively small base. Our findings do not refute existing quantum advantage claims but provide new empirical evidence that classical sampling algorithms can closely match DQI's optimization performance, offering a more nuanced perspective on the practical advantage of DQI.



## Related
- [[hardness-and-complexity-transition-of-noisy-random-circuit-s|Hardness and Complexity Transition of Noisy Random Circuit Sampling]]
- [[matrix-product-state-approach-to-lossy-boson-sampling-and-no|Matrix product state approach to lossy boson sampling and noisy IQP sampling]]
- [[the-impact-of-qubit-connectivity-on-quantum-advantage-in-noi|The Impact of Qubit Connectivity on Quantum Advantage in Noisy IQP Circuits]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.28120) | 2026-07-31
