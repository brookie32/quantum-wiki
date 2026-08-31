---
title: "Parallel Quantum Advantage with Limited Adaptivity Requires Structure"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.20297"
summary: "arXiv:2608.20297v1 Announce Type: new Abstract: Aaronson and Ambainis (Theory of Computing, 2014) conjectured that quantum query algorithms admit efficient almost-everywhere classical simulation: for "
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2608.20297v1 Announce Type: new Abstract: Aaronson and Ambainis (Theory of Computing, 2014) conjectured that quantum query algorithms admit efficient almost-everywhere classical simulation: for any T-query quantum algorithm, its acceptance probability can be approximated on a (1-elta) fraction of inputs, up to epsilon additive error, using poly(T, 1/epsilon, 1/elta) classical queries. At a high level, the conjecture suggests that exponential quantum speedups are possible only on sufficiently structured inputs. In this work, we make progress on this conjecture by proving it for quantum algorithms that make massively parallel quantum queries. In contrast, Yamakawa and Zhandry (Journal of the ACM, 2024) showed that quantum algorithms restricted to parallel queries can still achieve exponential speedups over classical algorithms for sampling problems. We establish our simulation theorem by proving the stronger statement that parallel-query quantum algorithms cannot distinguish the uniform distribution over oracles from oracles drawn from so-called "dense distributions". Our main technical contribution is a coupling theorem that relates the uniform distribution over oracles to oracles drawn from dense distributions. We further extend this approach beyond the purely parallel setting, obtaining simulation theorems both for algorithms with a bounded quantum-query prefix followed by a massively parallel quantum-query stage, and for hybrid algorithms that make an arbitrary polynomial number of adaptive classical queries before the massively parallel quantum-query stage. Finally, using the parallel-query simulation theorem as a base case, we obtain simulation theorems for quantum algorithms with constant rounds of adaptivity.



## Related
- [[algebraic-paradoxes-in-adaptive-quantum-computation|Algebraic paradoxes in adaptive quantum computation]]
- [[certified-randomness-without-structure-against-shallow-query|Certified Randomness without Structure Against Shallow-Query Adversaries]]
- [[quantum-advantage-with-adaptive-shallow-circuits|Quantum Advantage with Adaptive Shallow Circuits]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.20297) | 2026-08-21
