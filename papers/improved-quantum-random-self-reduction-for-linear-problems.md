---
title: "Improved Quantum Random Self-Reduction for Linear Problems"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39823"
summary: "arXiv:2609.39823v1 Announce Type: new Abstract: We study quantum random self-reductions for linear problems over finite fields. Let MinF^{nimes n} be an arbitrary matrix, and let O be an oracle that a"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39823v1 Announce Type: new Abstract: We study quantum random self-reductions for linear problems over finite fields. Let MinF^{nimes n} be an arbitrary matrix, and let O be an oracle that agrees with the linear map xmapsto Mx on an arepsilon-fraction of inputs xsimF^n. Given coherent access to O and coherent entry access to M, we give a uniform quantum reduction that computes Mx on any prescribed input x with probability at least 2/3 in time widetilde{O}(nT^{1/3}), for nle Tle n^{3/2} and constant field size and arepsilon, where T is the cost of one coherent query to O. In particular, when T=widetilde{O}(n), the reduction runs in time widetilde{O}(n^{4/3}), improving the widetilde{O}(n^{3/2}+T) reduction of Asadi, Golovnev, Gur, Shinkar, and Subramanian (SODA 2024). Our reduction uses the Bogolyubov--Ruzsa subspace guaranteed by additive combinatorics, but it avoids learning this subspace explicitly, which was computationally expensive for the previous reduction; in particular, it does not recover a basis for its orthogonal complement. The main technical step is to decompose the inputs into sparse pieces and find a vector that lies outside the Bogolyubov--Ruzsa subspace via a quantum search based on amplitude amplification. This yields a tunable tradeoff between the cost of querying the average-case oracle and the cost of verifying matrix-vector products.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39823) | 2026-10-01
