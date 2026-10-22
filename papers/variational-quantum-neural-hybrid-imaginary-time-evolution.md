---
title: "Variational quantum-neural hybrid imaginary time evolution"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2503.22570"
summary: "arXiv:2503.22570v3 Announce Type: replace Abstract: Numerous methodologies have been proposed to implement imaginary-time evolution (ITE) on quantum computers. Among these, variational ITE (VITE) meth"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2503.22570v3 Announce Type: replace Abstract: Numerous methodologies have been proposed to implement imaginary-time evolution (ITE) on quantum computers. Among these, variational ITE (VITE) methods for noisy intermediate-scale quantum (NISQ) computers have attracted much attention, as they use parameterized quantum circuits to mimic non-unitary dynamics. Although widely studied, conventional variational quantum algorithms face challenges in achieving high accuracy due to their strong dependence on the choice of ansatz quantum circuits. Recently, the variational quantum-neural hybrid eigensolver (VQNHE), which combines neural networks (NN) with a variational quantum eigensolver, has been proposed. This approach enhances the expressive power of variational states and improves the estimation of expectation values. Motivated by this idea, we explore the hybridization of VITE with an NN-based non-unitary operator. In this study, we propose a method named variational quantum-neural hybrid ITE (VQNHITE). By combining the NN with a parameterized quantum circuit, our proposal enhances the expressive power compared to conventional approaches, enabling more accurate tracking of imaginary-time dynamics. In addition, to mitigate the instability arising from randomly initialized NN parameters, we introduce an initial-parameter optimization procedure at a small imaginary-time step, which stabilizes the subsequent variational evolution. We tested our approach with numerical simulations on Heisenberg spin chains under both nearest-neighbor and all-to-all circuit connectivities. The results demonstrate that VQNHITE consistently achieves higher fidelity with the exact ITE state compared to VITE.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2503.22570) | 2026-10-22
