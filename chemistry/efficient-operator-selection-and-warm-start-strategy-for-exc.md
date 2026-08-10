---
title: "Efficient Operator Selection and Warm-Start Strategy for Excitations in Variational Quantum Eigensolvers"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.10776"
summary: "arXiv:2602.10776v3 Announce Type: replace Abstract: We present a novel approach for efficient preparation of electronic ground states, leveraging the optimizer ExcitationSolve [Jager et al., Comm. Phy"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2602.10776v3 Announce Type: replace Abstract: We present a novel approach for efficient preparation of electronic ground states, leveraging the optimizer ExcitationSolve [Jager et al., Comm. Phys. (2025)] and established variational quantum eigensolver-based operator selection methods, such as Energy Sorting (ES). By combining these tools, we demonstrate a computationally efficient protocol that enables the construction of an approximate ground state from a unitary coupled cluster ansatz via a single sweep over the operator pool. Utilizing efficient classical pre-processing to select the majority of relevant operators, this approach reduces the computational complexity associated with traditional variational quantum eigensolver (VQE) optimization methods. We further show that second-order Epstein-Nesbet (EN2) perturbation theory emerges as the first-order Taylor expansion of our protocol in terms of a correlation measure, clarifying why our approach provides a more robust initial guess for the ground state in strongly correlated regimes. We also find that second-order M{o}ller-Plesset perturbation (MP2) theory, which is widely used for unitary coupled cluster (UCC) initialization, performs worse than both EN2 and our protocol. Furthermore, we show that our method can be seamlessly integrated with one-variational-parameter couple exchange operators, thereby further reducing the number of required CNOT operations. Overall, we empirically observe a quadratic convergence speedup beyond state-of-the-art methods, advancing the preparation of high-fidelity electronic ground states - one of the cornerstones of meaningful electronic structure calculations in the noisy intermediate-scale quantum computing (NISQ) era, and a prerequisite for fault-tolerant quantum computing (FTQC) algorithms such as quantum phase estimation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.10776) | 2026-08-10
