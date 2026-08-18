---
title: "SQD-Enabled Circuit Compression for Resource-Efficient Quantum Chemistry"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.15076"
summary: "arXiv:2607.15076v3 Announce Type: replace Abstract: Sample-based Quantum Diagonalization (SQD) recovers ground-state energies by classically diagonalizing a Hamiltonian in the subspace spanned by quan"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2607.15076v3 Announce Type: replace Abstract: Sample-based Quantum Diagonalization (SQD) recovers ground-state energies by classically diagonalizing a Hamiltonian in the subspace spanned by quantum samples, requiring only bitstrings with sufficient ground-state overlap rather than an accurate variational energy. We reveal and exploit this underexplored robustness property: how much non-Clifford and variational expressivity can be removed from the sampling circuit before SQD accuracy degrades? We answer through two complementary compression techniques: gradient-based operator pruning, which discards low-impact excitation operators, and Clifford rounding, which snaps remaining parameters to the nearest Clifford angle. Both of these techniques can be applied to a VQE ansatz on a qubit-reduced Hamiltonian. A systematic ablation study across 21 molecules shows that median SQD error stays within chemical accuracy even at 50% compression on both axes, while simulation speedup reaches 33imes. Hardware validation on 6 molecules on IBM quantum hardware confirms up to 2.8imes transpiled-depth reduction with zero loss in SQD accuracy. Our implementation can be found at: https://github.com/zkysfls/cs-vqe-sqd

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.15076) | 2026-08-18
