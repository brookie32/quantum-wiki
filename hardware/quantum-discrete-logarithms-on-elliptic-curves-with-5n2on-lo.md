---
title: "Quantum Discrete Logarithms on Elliptic Curves with 5n/2+o(n) Logical Qubits and widetilde O(n^2) Toffoli Gates"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "hardware"
tags: [hardware, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2014"
summary: "We give a quantum algorithm for the elliptic curve discrete logarithm problem over an (n)-bit prime field using (frac{5}{2}n+o(n)) logical qubits and (widetilde O(n^2)) Toffoli gates. Luo et al.'s exa"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

We give a quantum algorithm for the elliptic curve discrete logarithm problem over an (n)-bit prime field using (frac{5}{2}n+o(n)) logical qubits and (widetilde O(n^2)) Toffoli gates. Luo et al.'s exact space-efficient affine construction uses (3n+O(log n)) qubits with (O(n^3/log n)) Toffoli gates; ours lowers the leading qubit term from (3n) to (frac{5}{2}n) and the Toffoli count to near-quadratic. We construct an exact in-place modular inverter with (frac{3}{2}n+o(n)) logical qubits and (widetilde O(n)) Toffoli gates. For consecutive Euclidean remainders (R>r) and coefficient magnitudes (0le T<t), the invariant (Rt+rT=p) allows us to store only three of (R,r,T,t) in the persistent Euclidean state and reconstruct the fourth on demand. Temporary Euclidean data are recovered from the updated state and erased after each update. The arithmetic queries used in these steps are implemented in sublinear workspace using measurement-based uncomputation. We then use Hua's identity to reduce the variable-square multiplications needed for affine point addition to inversions, yielding exact controlled point addition within (frac{5}{2}n+o(n)) logical qubits and (widetilde O(n)) Toffoli gates.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2014) | 2026-09-14
