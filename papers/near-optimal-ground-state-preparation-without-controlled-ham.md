---
title: "Near-Optimal Ground-State Preparation without Controlled Hamiltonian Evolutions"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.00520"
summary: "arXiv:2610.00520v1 Announce Type: new Abstract: Ground-state preparation, energy estimation, and property estimation are fundamental tasks in quantum simulation. Existing ground-state preparation algo"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.00520v1 Announce Type: new Abstract: Ground-state preparation, energy estimation, and property estimation are fundamental tasks in quantum simulation. Existing ground-state preparation algorithms achieve near-optimal complexity using block encodings or controlled Hamiltonian evolution, raising a natural question: is controlled Hamiltonian evolution necessary, or can the same scaling be attained in the weaker access model that provides access to only uncontrolled Hamiltonian evolution? We resolve this question by giving two algorithms that access the input Hamiltonian H only through queries to U_H and its inverse U_H^agger, where |H|lealpha_H and au=Theta(1/alpha_H). Given an input state with ground-state weight at least eta and a spectral gap of H of at least gamma, our first algorithm uses fresh copies of the input state and requires widetilde O(alpha_H/(gammaeta)) queries to U_H and U_H^agger, while our second algorithm uses coherent access to the input-state preparation unitary and its inverse to improve this complexity to widetilde O(alpha_H/(gammasqrt{eta})). The latter bound matches the known lower bound up to logarithmic factors, showing that algorithms with additional access to controlled Hamiltonian evolution cannot improve the query complexity for ground-state preparation beyond logarithmic factors. Both algorithms are based on a simple mechanism that we call the spectral descent principle, in which the algorithm starts from the input state |psirangle and progressively descends through the energy spectrum, moving closer to the ground state until the desired fidelity is reached. We also extend this framework to ground-state property and energy estimation and give explicit complexity guarantees for both tasks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.00520) | 2026-10-02
