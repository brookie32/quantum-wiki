---
title: "Quantum score matching with applications to learning thermal states"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.28391"
summary: "arXiv:2609.28391v1 Announce Type: new Abstract: Score matching has driven major advances in classical generative learning by enabling models to learn from data without evaluating intractable normaliza"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2609.28391v1 Announce Type: new Abstract: Score matching has driven major advances in classical generative learning by enabling models to learn from data without evaluating intractable normalization constants, or partition functions. Yet, extending this principle to quantum learning requires rethinking its foundations, as quantum states are described by noncommuting density operators rather than scalar probabilities. The noncommutativity creates fundamental challenges not only in defining quantum scores, but also in developing a training framework with efficient circuit implementations and rigorous theoretical guarantees. In this work, we bridge this gap by establishing a general quantum score-matching framework with end-to-end theoretical guarantees. Applied to Gibbs-state learning, our approach avoids additional thermal-state preparation and achieves information-theoretically optimal sample complexity in the high-temperature regime for Hamiltonians with bounded locality and interaction degree. This positions score matching as a new route to state-of-the-art performance in learning quantum Gibbs states. Beyond these theoretical results, numerical simulations show that our method remains effective even when gradients are estimated inaccurately under limited measurement budgets. Experiments on IBM quantum hardware further demonstrate that quantum score matching is NISQ-friendly: without any error mitigation or correction, it reduces the relative Hamiltonian-parameter error from 64% to approximately 10%. Together, these results extend score matching into an experimentally realizable paradigm for quantum-state learning.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.28391) | 2026-09-24
