---
title: "Clifford-efficient sparse state preparation for molecular wavefunctions"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.20593"
summary: "arXiv:2608.20593v1 Announce Type: new Abstract: Sparse quantum state preparation concerns an n-qubit target state that is a superposition of only d ll 2^n computational basis states. Existing approach"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2608.20593v1 Announce Type: new Abstract: Sparse quantum state preparation concerns an n-qubit target state that is a superposition of only d ll 2^n computational basis states. Existing approaches exploit this sparsity by compressing these d basis states and their amplitudes onto a smaller set of qubits, called the dense register, before expanding the prepared state to the full register. Rather than relying on the permutation-based compression used in prior work, we exploit affine relationships among the binary configurations over the finite field operatorname{GF}(2) to reduce both the non-Clifford gate count and the ancillary qubit count. Invertible affine transformations over operatorname{GF}(2), comprising Gaussian elimination and all-ones-row removal, first reduce the dense register from n to the rank r using only Clifford gates and no ancillary qubits. An optional binary encoding stage then trades additional Toffoli gates and ancillary qubits for further compression to the minimum lceillog_2 drceil dense qubits needed to represent d distinct configurations. For chemically relevant wavefunctions, such as those obtained from selected configuration interaction calculations, shared electronic excitation patterns produce many of these affine relationships, enabling substantial Clifford-only compression before binary encoding. Across the molecular benchmarks, our method requires the fewest ancillary qubits among the evaluated sparse state preparation methods while maintaining comparable non-Clifford gate counts when using binary encoding.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.20593) | 2026-08-24
