---
title: "Nearly optimal algorithms to learn sparse quantum Hamiltonians in physically motivated distances"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.09813"
summary: "arXiv:2509.09813v2 Announce Type: replace Abstract: We study the problem of learning Hamiltonians H that are s-sparse in the Pauli basis, given access to their time evolution. Although Hamiltonian lea"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2509.09813v2 Announce Type: replace Abstract: We study the problem of learning Hamiltonians H that are s-sparse in the Pauli basis, given access to their time evolution. Although Hamiltonian learning has been extensively investigated, two issues recur in much of the existing literature: the absence of matching lower bounds and the use of mathematically convenient but physically opaque error measures. We address both challenges by introducing two physically motivated distances between Hamiltonians and designing a nearly optimal algorithm with respect to one of these metrics. The first, time-constrained distance, quantifies distinguishability through dynamical evolution up to a bounded time. The second, temperature-constrained distance, captures distinguishability through thermal states at bounded inverse temperatures. We show that s-sparse Hamiltonians with bounded operator norm can be learned in both distances with O(s log(1/epsilon)) experiments and O(s^2/epsilon) evolution time. For the time-constrained distance, we further establish lower bounds of Omega((s/n)log(1/epsilon) + s) experiments and Omega(sqrt{s}/epsilon) evolution time, demonstrating near-optimality in the number of experiments. As an intermediate result, we obtain an algorithm that learns every Pauli coefficient of s-sparse Hamiltonians up to error epsilon in O(slog(1/epsilon)) experiments and O(s/epsilon) evolution time, improving upon several recent results. The source of this improvement is a new isolation technique, inspired by the Valiant-Vazirani theorem (STOC'85), which shows that NP is as easy as detecting unique solutions. This isolation technique allows us to query the time evolution of a single Pauli coefficient of a sparse Hamiltonian--even when the Pauli support of the Hamiltonian is unknown--ultimately enabling us to recover the Pauli support itself.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.09813) | 2026-09-28
