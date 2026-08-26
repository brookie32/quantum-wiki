---
title: "Quantum Algorithm for Elliptic Curve Discrete Logarithms with Space-Efficient Point Addition"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.13816"
summary: "arXiv:2607.13816v2 Announce Type: replace Abstract: The Elliptic Curve Discrete Logarithm Problem (ECDLP) is a fundamental problem in cryptography, and reducing the resource requirements of quantum al"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2607.13816v2 Announce Type: replace Abstract: The Elliptic Curve Discrete Logarithm Problem (ECDLP) is a fundamental problem in cryptography, and reducing the resource requirements of quantum algorithms for solving ECDLP is an important goal. In this work, we present a space-efficient quantum algorithm for solving the ECDLP over prime fields, achieving an implementation with only 3n+6lfloor log_2 n rfloor+O(1) logical qubits and 1008n^3/log_2 n+O(n^2) Toffoli gates, where n is the bit-length of the prime. For a 256-bit prime-field curve, our construction requires only 835 logical qubits, reducing the previous best estimates of 1098 and 1175 logical qubits by Chevignard et al. [EUROCRYPT 2026] and Babbush et al. [ArXiv Preprint 2026], respectively. The key to our improvement is a new space-efficient reversible modular inversion circuit, which addresses the dominant space bottleneck in affine-coordinate point addition. Starting from the extended Euclidean algorithm (EEA), we refine the register-sharing technique of Proos and Zalka by introducing length registers and location-controlled arithmetic to compactly store and update intermediate variables. We further optimize the reversible update procedures and construct the corresponding controlled arithmetic circuits, resulting in a modular inversion circuit implemented by only 2n+6lfloor log_2 n rfloor+O(1) logical qubits and 217n^2+O(nlog_2 n) Toffoli gates. This modular inversion circuit together with mid-circuit measurements and classical feed-forward operations provides a space-efficient controlled affine point-addition circuit and a complete implementation of Shor's algorithm for ECDLP.



## Related
- [[unconditional-correctness-of-recent-quantum-algorithms-for-f|Unconditional correctness of recent quantum algorithms for factoring and computing discrete logarithms]]
- [[capability-adaptive-cryptanalysis-with-reduced-space-quantum|Capability-Adaptive Cryptanalysis with Reduced-Space Quantum Verification]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.13816) | 2026-08-11
