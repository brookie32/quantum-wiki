---
title: "Elevator Codes: Concatenation for resource-efficient quantum memory under biased noise"
date: "2026-09-22"
updated: "2026-09-22"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.10786"
summary: "arXiv:2601.10786v2 Announce Type: replace Abstract: Biased-noise qubits, in which one type of error (e.g. X- and Y-type errors) is significantly suppressed relative to the other (e.g. Z-type errors), "
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

arXiv:2601.10786v2 Announce Type: replace Abstract: Biased-noise qubits, in which one type of error (e.g. X- and Y-type errors) is significantly suppressed relative to the other (e.g. Z-type errors), can significantly reduce the overhead of quantum error correction. Codes such as the rectangular surface code or XZZX code substantially reduce the qubit overhead under biased noise, but they still face challenges. The rectangular surface code suffers from a relatively low threshold, while the XZZX code requires twice as many physical qubits to maintain the same code distance as the surface code. In this work, we introduce a 2D local code construction that outperforms these codes for noise biases eta ge 7imes10^{4}, reducing the qubit overhead by over 50% at p_Z=10^{-3} and eta = 2 imes 10^6 to achieve a logical error rate of 10^{-12}. Our construction relies on the concatenation of two classical codes. The inner codes are repetition phase-flip codes while the outer codes are high-rate bit-flip codes enabled by their implementation at the logical level, which circumvents device connectivity constraints. These results indicate that under sufficiently biased noise, it is advantageous to address phase-flip and bit-flip errors at different layers of the coding scheme. The inner code should prioritize a high threshold for phase-flip errors, while the bit-flip outer code should optimize for encoding rate efficiency. In the strong biased-noise regime, high-rate outer codes keep the overhead for correcting residual bit-flip errors comparable to that of the repetition code itself, meaningfully lower than that required by earlier approaches.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.10786) | 2026-09-22
