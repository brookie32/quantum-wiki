---
title: "Multi-qubit controlled gate synthesis without T-count overhead in the small-error limit"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.14202"
summary: "arXiv:2603.14202v2 Announce Type: replace Abstract: We study the Clifford+T synthesis of quantum multiplexers U=igoplus_{i=1}^{2^n}U_i: an n-qubit control register selects which single-qubit gate U_ii"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2603.14202v2 Announce Type: replace Abstract: We study the Clifford+T synthesis of quantum multiplexers U=igoplus_{i=1}^{2^n}U_i: an n-qubit control register selects which single-qubit gate U_iinSU(2) acts on the target qubit. For each block U_i, consider the minimum even T-count needed to approximate it within diamond distance arepsilon without ancillae, and let m be the largest of these costs. For arbitrary blocks, we construct an approximation of U within the same distance using at most m+O(sqrt{2^n(m+1)}) T gates. With one control qubit, the cost is m+O(1) and no ancillae are required. We also prove a lower bound that allows the approximating unitary to mix different control values and the circuit to use any number of clean ancillae initialized to zero and returned exactly to zero. For fixed n and independent Haar-random blocks, the minimum T-count among these circuits lies between (3-elta)L and (3+elta)L for every fixed elta>0, except with probability O(arepsilon^{c_{n,elta}}); here L=log_2(1/arepsilon), c_{n,elta}>0, and the bound holds for sufficiently small arepsilon. The optimal leading coefficient is therefore the same as for a single Haar-random SU(2) gate. In the lower-bound proof, unitarity forces pairs of off-diagonal blocks describing transitions in opposite directions to satisfy cancellation relations with residuals of order arepsilon^2. We combine these relations with the arithmetic of Clifford+T circuits to bound the Haar measure of targets compatible with each pair of off-diagonal blocks. As an application, we obtain ancilla-free approximations of Haar-random SU(4) gates within diamond distance arepsilon, using at most (9+elta)L T gates for every fixed elta>0, with failure probability polynomially small in arepsilon.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.14202) | 2026-10-01
