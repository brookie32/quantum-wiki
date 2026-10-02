---
title: "Unflattening by Flattening -- How Input Distributions Shape Output Variance in Angle-Encoded Circuits"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01446"
summary: "arXiv:2610.01446v1 Announce Type: new Abstract: Barren plateaus hinder training of parameterized quantum circuits by making loss gradients exponentially small in the number of qubits. For angle-encode"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01446v1 Announce Type: new Abstract: Barren plateaus hinder training of parameterized quantum circuits by making loss gradients exponentially small in the number of qubits. For angle-encoded product states, we show how the input distribution affects output variation through algebraic input purity, i.e. the input's overlap with the circuit's dynamical Lie algebra. With the specified readouts and Haar or exact group 2-design sampling, matchgate circuits on n qubits retain output variance of order 1/n for every pure product input. The off-diagonal family instead has zero output on computational-basis inputs at any depth and for every parameter choice. Independent uniform angles yield mean variance of the same order as matchgates. A count of diagonal Pauli strings identifies these zero-output endpoints. For any fixed dataset of nonzero inputs with at least 2n coordinates, we construct a classical preprocessing certificate. A shared random rotation is accepted only when the dataset's mean purity passes a computable threshold. This certifies mean output variance of order 1/n for the off-diagonal family before circuit execution, with a constant expected number of trials. Binary and ternary weighted encodings also recover the independent-angle mean purity from one uniform scalar input. Numerical experiments examine training behavior and extensions to larger algebras. The guarantee concerns output variance averaged over inputs, while successful learning also depends on the task and information preserved by the encoding.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01446) | 2026-10-02
