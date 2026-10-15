---
title: "Shot- and Noise-Aware Pauli Correlation Encoding for Max-Cut Experiments on IBM Heron Quantum Processor"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.19544"
summary: "arXiv:2610.19544v1 Announce Type: new Abstract: Pauli correlation encoding (PCE) encodes m binary variables in the signs of k-body Pauli correlators of n=O(m^{1/k}) qubits, and trains a parameterized "
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2610.19544v1 Announce Type: new Abstract: Pauli correlation encoding (PCE) encodes m binary variables in the signs of k-body Pauli correlators of n=O(m^{1/k}) qubits, and trains a parameterized circuit on a relaxed loss of sharpness alpha. The strongest published schedules sharpen this loss aggressively and are benchmarked with exact expectation values, whereas a quantum computer estimates correlators from a finite number of shots. We show that the sharpness is a hidden shot budget. Since the expected sign of a correlator estimated from S shots, erf(csqrt{S/2}), agrees with anh(0.851sqrt{S},c) to within 0.019, the edge term of the relaxed loss at alpha=0.851sqrt{S} approximately equals, up to a constant, minus twice the cut expected from decoding S shots. This explains why schedules tuned with exact expectation values lose their advantage at realistic budgets, and yields a shot-aware schedule whose final sharpness is set by the shot budget. On five G-set graphs with 800 variables on 13 qubits, this schedule outperforms every published schedule at its target budget in all 150 paired comparisons of the decoded circuit output, owing to the sharpness at 1.6imes10^4 shots and mostly to switching off the regularization at 10^3; after a classical bit-swap search, it remains the best on average at 1.6imes10^4 shots. Device noise damps the correlators by a factor s, which amounts to a smaller shot budget s^2S. On the IBM Heron processor ibm_fez, an all-to-all ansatz of the type used for the best published G-set results compiles to 835 CZ gates and decodes to a random cut, while our 96-CZ hardware-native circuit, trained in simulation and sharpened to alphasimeq0.65,ssqrt{S}, retains up to 0.919 of the best-known cut. For new circuits, a damping and an offset calibrated on other circuits of the same graph predicted the decoded cuts at 10^3 shots to within 0.002.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.19544) | 2026-10-15
