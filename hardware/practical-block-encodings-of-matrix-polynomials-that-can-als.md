---
title: "Practical block encodings of matrix polynomials that can also be trivially controlled"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.18767"
summary: "arXiv:2601.18767v2 Announce Type: replace Abstract: Quantum circuits naturally implement unitary operations on input quantum states. However, non-unitary operations can also be implemented through 'bl"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2601.18767v2 Announce Type: replace Abstract: Quantum circuits naturally implement unitary operations on input quantum states. However, non-unitary operations can also be implemented through "block encodings", where additional ancilla qubits are introduced and later measured. While block encoding underlies a host of well-established theoretical applications, its implementation in practice has been prohibitively expensive for current quantum hardware. In this paper, we present practical and explicit block encoding circuits implementing matrix polynomial transformations of a target matrix. With standard approaches, block-encoding a degree-d matrix polynomial requires a circuit depth scaling as d times the depth for block-encoding the original matrix alone. By leveraging the recently introduced Fast One-Qubit Controlled Select Linear Combination of Unitaries (FOQCS-LCU) framework, we show that the additional circuit-depth overhead required for encoding matrix polynomials can be reduced to scale linearly in d with no dependence on system size or the cost of block encoding the original matrix. Moreover, we demonstrate that the FOQCS-LCU circuits and their associated matrix polynomial transformations can be controlled with negligible overhead, enabling efficient applications such as Hadamard tests. Finally, we provide explicit hardware-efficient circuits for representative non-unitary operators, namely quantum spin models, together with detailed non-asymptotic gate counts and circuit depths.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.18767) | 2026-10-07
