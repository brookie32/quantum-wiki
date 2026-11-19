---
title: "Ground-state energy estimation compiled on cat qubits: 6 808 qubits for FeMoco-54 in 23.6 hours"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.37840"
summary: "arXiv:2610.37840v2 Announce Type: replace Abstract: We provide a detailed resource estimate of the state-of-the-art sum-of-squares block encoding algorithm for electronic structure Hamiltonians of Low"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2610.37840v2 Announce Type: replace Abstract: We provide a detailed resource estimate of the state-of-the-art sum-of-squares block encoding algorithm for electronic structure Hamiltonians of Low et al. on superconducting cat qubits. To achieve this, we present compilations with closed-form costs of the dominant subroutines such as skew-tree Qrom, a Swap network and a Phaseup for both a repetition-cat and an LDPC-cat architecture. Our compilation represents algorithmic qubits in the X basis, taking advantage of the asymmetric cost of X and Z access that the concatenation of cat qubits with phase-flip classical code brings. Additionally, we provide a protocol for ert i rangle-state distillation and a two-level Toffoli-like ert ext{C}_Xext{C}_X X rangle magic state distillation protocol, including three factory layouts. To minimize the cost of Clifford corrections induced by magic state injections we tailor injection gadgets to each subroutine. Combining our compilation work with the adder compilation from the companion work Pappalardo et al., we provide global layouts for the block encoding in both architectures which we use to obtain resource estimates for ground-state energy estimation for the benchmarks of FeMoco-54 and FeMoco-76. Assuming a cycle time of 1mus, a reaction time of 10mus, a phase estimation precision of 1 mHa and circuit-level phase-flip noise with probability p_Z = 5 imes 10^{-4} with negligible bit-flip error, FeMoco-54 requires fewer than 7,000 cat qubits with an expected runtime of under one day for a single phase estimation run using an LDPC-cat architecture. Relaxing the bit-flip requirement to p_X = 10^{-11} with an additional layer of elevator codes raises this to an estimated 12,100 cat qubits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.37840) | 2026-11-19
