---
title: "Verifiable Quantum Advantage via Optimized DQI Circuits"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2510.10967"
summary: "arXiv:2510.10967v2 Announce Type: replace Abstract: Recently, a quantum algorithm called Decoded Quantum Interferometry (DQI) was introduced that achieves an apparent exponential speedup for Optimal P"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2510.10967v2 Announce Type: replace Abstract: Recently, a quantum algorithm called Decoded Quantum Interferometry (DQI) was introduced that achieves an apparent exponential speedup for Optimal Polynomial Intersection (OPI) problem, which has previously been studied in the contexts of cryptography and error correcting codes. However, this left open the question of how many logical gates and logical qubits would be needed to solve a classically intractable instance of OPI. Here, we develop optimized implementations of DQI which greatly reduce its resource requirements. We establish that DQI for OPI is the first known candidate for verifiable quantum advantage with optimal asymptotic speedup: solving instances with classical hardness O(2^N) requires only widetilde{O}(N) quantum gates, matching the theoretical lower bound. To realize this, we overcome the primary bottleneck of reversible Reed-Solomon decoding by introducing novel quantum circuits for the Extended Euclidean Algorithm (EEA) on degree-n polynomials with b-bit coefficients that reduce the leading-order space complexity to 2nb qubits. These improvements are broadly applicable, including to Shor's algorithm for the discrete logarithm. We analyze OPI over binary extension fields GF(2^b), assess hardness against new classical attacks, and identify resilient instances. Our resource estimates show that classically intractable OPI instances (requiring >10^{23} classical trials) can be solved with approximately 5.72 million Toffoli gates per shot and 1885 logical qubits. This is roughly 100 times fewer gates than required for factoring RSA-2048 and, remarkably, is also less than the leading interactive protocol for computational proof of quantumness, positioning DQI as a compelling candidate for practical, verifiable quantum advantage.



## Related
- [[from-simple-sources-to-quantum-advantage-homomorphic-polynom|From Simple Sources to Quantum Advantage: Homomorphic Polynomial Transduction via Relative Decoding]]
- [[approximate-sampling-from-decoded-quantum-interferometry-via|Approximate sampling from decoded quantum interferometry via Markov chain Monte Carlo methods]]
- [[a-provable-quantum-advantage-for-approximate-optimization-vi|A provable quantum advantage for approximate optimization via decoded quantum interferometry]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2510.10967) | 2026-11-20
