---
title: "High-order splitting of non-unitary operators on quantum computers"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.19659"
summary: "arXiv:2511.19659v4 Announce Type: replace Abstract: Dissipation and irreversibility are central to many physical systems, yet they lead to non-unitary dynamics that are challenging to realise on quant"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2511.19659v4 Announce Type: replace Abstract: Dissipation and irreversibility are central to many physical systems, yet they lead to non-unitary dynamics that are challenging to realise on quantum processors. High-order operator splitting is an attractive approach for simulating unitary dynamics, yet conventional product formulas introduce negative time steps at high orders that are ill-conditioned for dissipative dynamics. We show how block encodings of complex-coefficient product formulas can be constructed by a sequence of simple Hamiltonian evolutions in real and imaginary time with high-order accuracy. The unitary substages use positive real coefficients, while the dissipative substages use complex coefficients with positive real parts; the real parts preserve the contractive evolution, and the imaginary parts are additional unitary evolutions. We use known formulas of orders 4 and 6 and give a new symmetric formula of order 8 in this restricted class. We apply the approach to the classical problem of lossy mechanical wave propagation in statevector simulations and on a trapped-ion quantum processor. Orders 4 and 6 require comparable CNOT gates to orders 1 and 2 at large error tolerances, but quickly become more efficient as the tolerance is reduced. On the quantum hardware, a single step of order 4 achieves lower error than order 1 and comparable error to order 2, while order 6 is noise-limited. Our results show that operator splitting can combine practical circuit constructions with high-order convergence for non-unitary dissipative dynamics.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.19659) | 2026-08-19
