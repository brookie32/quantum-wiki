---
title: "Quantum space-depth tradeoffs for coherent block encodings"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.01843"
summary: "arXiv:2607.01843v2 Announce Type: replace Abstract: Block encodings are a basic interface between quantum algorithms and linear algebra. Standard LCU constructions achieve optimal circuit depth but ty"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2607.01843v2 Announce Type: replace Abstract: Block encodings are a basic interface between quantum algorithms and linear algebra. Standard LCU constructions achieve optimal circuit depth but typically require logarithmically many ancilla qubits. We ask how much quantum workspace can be reduced without sacrificing circuit depth, and study this tradeoff from both algorithmic and lower-bound perspectives. For a Hermitian decomposition A=sum_{j=1}^L alpha_j H_j, with |H_j|=1 and alpha=sum_j|alpha_j|, we give two coherent arepsilon-approximate block-encoding constructions. The first uses one ancilla qubit and has depth widetilde O(L(alpha/arepsilon)^{o(1)}), while the second uses O(loglog(alpha/arepsilon)) ancillas and achieves depth widetilde O(L). For a broad Suzuki-based coherent simulation architecture, we prove an ancilla-depth tradeoff. In the polynomial-resource regime and for a constant number of coherent rounds, log(1/arepsilon)le O((log Q)^2+2^alog Q), where Q is depth normalized by the number of Hamiltonian terms and a is the ancilla count. Thus polylogarithmic dependence on 1/arepsilon requires more than constantly many ancillas within this architecture. In a separate repeated-query LCU model, for balanced coefficients 1/L and error arepsilon=eta/L with fixed 0<eta<1, we prove 2^a=Omega_eta(L^2/(T+L)), where T is the number of oracle queries. Hence a=Omega(log L) when T=O(L^alpha) for some alpha<2. Moreover, in the exact case, age log L regardless of T. We also extend this tradeoff to arbitrary nonnegative coefficients. Finally, we apply our low-ancilla constructions to normalized trace estimation in DQC1, obtaining an optimal algorithm linear in the approximate degree together with a matching query lower bound. Together, these results establish quantitative space-depth and space-query tradeoffs in two natural circuit models.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.01843) | 2026-10-01
