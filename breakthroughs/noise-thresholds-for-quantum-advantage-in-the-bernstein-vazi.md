---
title: "Noise Thresholds for Quantum Advantage in the Bernstein-Vazirani and Deutsch-Jozsa Algorithms"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2508.01884"
summary: "arXiv:2508.01884v3 Announce Type: replace Abstract: We analytically investigate the robustness of the Bernstein-Vazirani and Deutsch-Jozsa algorithms against single-qubit Pauli noise, of which bit-fli"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2508.01884v3 Announce Type: replace Abstract: We analytically investigate the robustness of the Bernstein-Vazirani and Deutsch-Jozsa algorithms against single-qubit Pauli noise, of which bit-flip, phase-flip, and depolarizing noise are special cases, using the density-matrix formalism. For a general Pauli channel acting on each qubit after every gate, we derive exact closed-form expressions for the success probability of a single run as a function of the error probabilities and the number of qubits n, and validate them against Qiskit simulations. The noise enters only through the probability arepsilon with which each output bit is flipped. Under bit-flip noise with error probability p > 1/2 the most probable outcome of the Bernstein-Vazirani algorithm is the complement of the correct one, which classical post-processing corrects, whereas depolarizing and phase-flip noise never bias the output toward a wrong outcome. For the Deutsch-Jozsa algorithm, the success probability is the average over constant and balanced oracles, and the results are given for the single-variable balanced oracle, which is shown to be the least robust of all balanced oracles for arepsilon < 1/2. For a single run, the tolerable error probability of both algorithms decreases as 1/n. We then determine the minimum number of repetitions required for a given confidence and compare it with the number of queries of the classical algorithms. The threshold error probability below which the noisy Bernstein-Vazirani algorithm retains its query advantage increases with n, whereas that of the Deutsch-Jozsa algorithm with its standard readout decreases as 1/n. This contrast indicates that algorithms whose answer is encoded in many independently decodable output bits are considerably more robust to noise than algorithms whose verdict depends on a single global outcome.



## Related
- [[quantum-approximate-optimization-via-noise-directed-adaptive|Quantum Approximate Optimization via Noise-Directed Adaptive Warm-Starting]]
- [[the-impact-of-qubit-connectivity-on-quantum-advantage-in-noi|The Impact of Qubit Connectivity on Quantum Advantage in Noisy IQP Circuits]]
- [[verifiable-quantum-advantage-in-extremely-low-depth|Verifiable quantum advantage in extremely low depth]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2508.01884) | 2026-10-12
