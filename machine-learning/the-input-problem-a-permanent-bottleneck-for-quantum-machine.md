---
title: "The Input Problem: A Permanent Bottleneck for Quantum Machine Learning"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.08433"
summary: "arXiv:2608.08433v1 Announce Type: new Abstract: Quantum algorithms are conventionally presented with their input state supplied for free. When the input is classical data, this convention conceals a c"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.08433v1 Announce Type: new Abstract: Quantum algorithms are conventionally presented with their input state supplied for free. When the input is classical data, this convention conceals a cost that is frequently larger than the algorithm it precedes. We review what the three standard encodings, such as basis encoding, amplitude encoding, and Grover--Rudolph distribution loading, actually cost once transpiled to a hardware gate set, and argue that the resulting Theta(N) bound is a counting theorem rather than an engineering limitation that improved hardware will remove. Measured gate counts for a representative loading task are reported: an optimal library implementation requires 247 CNOT gates at n=8 qubits and doubles with each additional qubit, while the classical preprocessing that produces the rotation angles requires reading the entire input vector. We show how this cost eliminates the quadratic advantage of quantum amplitude estimation for Monte Carlo integration, and argue that the same accounting constrains quantum machine learning more broadly: the strong input models that make quantum algorithms fast on classical data also enable classical dequantization, and quantum kernel methods carry a Theta(M^2) state-preparation cost for the Gram matrix that does not amortize. We explain that the efficiently preparable states, device-generated distributions, variationally learned loading, and amortized preparation are required to get advantage from quantum machine learning and close with a checklist for evaluating input-dependent advantage claims. Executable notebooks reproducing every construction and measurement discussed here are available.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.08433) | 2026-08-11
