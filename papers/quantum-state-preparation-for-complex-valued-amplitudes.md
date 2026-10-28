---
title: "Quantum State Preparation for Complex-Valued Amplitudes"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.36680"
summary: "arXiv:2610.36680v1 Announce Type: new Abstract: We present a state preparation procedure that takes binary registers containing the real and imaginary parts of a complex number z=x+iy and prepares an "
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2610.36680v1 Announce Type: new Abstract: We present a state preparation procedure that takes binary registers containing the real and imaginary parts of a complex number z=x+iy and prepares an amplitude approximating z/alpha, where alpha is a normalization constant. The magnitude and argument are computed using the Coordinate Rotation Digital Computer (CORDIC) algorithm. We then encode the magnitude into an amplitude, and apply phase gates to introduce the argument. A reversible in-place multiplier allows the coordinate updates to use fixed precision while clearing their temporary workspace. The procedure uses O(n^2) T gates and O(n) additional qubits. Compared with separately encoding the real and imaginary parts and combining them through LCU, the construction can allow a smaller normalization and reduce amplitude-amplification costs. The computed polar representation also remains available for further arithmetic before amplitude-encoding.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.36680) | 2026-10-28
