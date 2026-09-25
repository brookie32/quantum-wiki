---
title: "Trading Circuit Depth for Pulse Sparsity in Chromatic Dynamical Decoupling"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.30175"
summary: "arXiv:2609.30175v1 Announce Type: new Abstract: Suppressing decoherence and crosstalk systematically across large networks of qubits is a pressing concern as qubit counts increase rapidly. General mul"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.30175v1 Announce Type: new Abstract: Suppressing decoherence and crosstalk systematically across large networks of qubits is a pressing concern as qubit counts increase rapidly. General multi-qubit dynamical decoupling (DD) has historically been based on Hadamard matrices and orthogonal arrays, with instantaneous-pulse sequences whose circuit depth scales linearly with the number of qubits. Chromatic-Hadamard DD (CHaDD) improves upon these methods by properly coloring the hardware graph and assigning to each color a row of a Hadamard matrix, resulting in a circuit depth that scales linearly with the number of colors C, which can be as low as the chromatic number of the graph. Here, we explore the tradeoff between circuit depth and the pulse repetition rate (PRR), the average fraction of time steps in which a qubit is pulsed, i.e., a measure of pulse density. We introduce two single-axis sequences based on binary and Gray matrices, Chromatic-Binary DD (CBDD) and Chromatic-Gray DD (CGDD), which, for C>2, are special cases of non-minimum-depth CHaDD and achieve PRR <2/C and PRR =1/C, respectively, compared with a PRR above 1/4 for CHaDD, at the price of a circuit depth of 2^C. In state preservation experiments on a 127-qubit IBM processor with C=3, the less dense sequences outperform CHaDD at short times when the pulses are not robust; this advantage is largely eliminated by robust versions designed to compensate for coherent pulse errors, and among the robust sequences, CGDD uses the fewest pulses over a fixed protection time. Across non-robust C=3 and C=5 schedules, equal PRR on a fixed qubit subset is empirically associated with similar state preservation. Thus, the PRR serves as a practical figure of merit for chromatic DD whenever coherent pulse errors dominate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.30175) | 2026-09-25
