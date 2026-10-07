---
title: "Distributional Quantum Query Complexity"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.06835"
summary: "arXiv:2610.06835v2 Announce Type: replace Abstract: Quantum query complexity enjoys a variety of pleasing joint computation properties: for example, a composition theorem asserting Q(firc g)=Theta(Q(f"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2610.06835v2 Announce Type: replace Abstract: Quantum query complexity enjoys a variety of pleasing joint computation properties: for example, a composition theorem asserting Q(firc g)=Theta(Q(f)Q(g)) for all Boolean functions f and g; a direct sum theorem asserting that computing k copies of a function (or search problem) costs Omega(k) times as much as the cost of computing one copy; and a direct product theorem asserting that for Boolean functions, even succeeding at the direct sum problem with exponentially small probability still requires Omega(k) times the cost of computing one copy to bounded error. However, all of these results are strictly for worst-case quantum query complexity. For example, if we have a fixed distribution mu over inputs, the direct sum theorem says nothing about the quantum query complexity of computing k copies of f when the input comes from the product distribution mu^k instead of being worst-case. (Note that while a standard Yao-type minimax theorem guarantees a hard distribution for the direct sum problem, there's no guarantee that this hard distribution is a product distribution.) A similar problem occurs for the direct product theorem and the composition theorem: none of these results respect distributions. In this work, we give distributional joint computation lower bounds for the composition, direct sum, and direct product problems. Along the way, we introduce some new tools for handling quantum query lower bounds, including (a) a new ``multiplicative'' variant of the gamma_2 norm (which we use in place of the multiplicative adversary method for proving the direct product theorem), and (b) a new ``Shaltiel-free'' measure of quantum query complexity, which we show characterizes the composition behavior of distributional quantum query complexity and satisfies pleasing properties.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.06835) | 2026-10-07
