---
title: "Scalable Clifford-Based Classical Initialization for the Quantum Approximate Optimization Algorithm"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.14327"
summary: "arXiv:2602.14327v2 Announce Type: replace Abstract: Variational Quantum Algorithms (VQAs), such as the Quantum Approximate Optimization Algorithm (QAOA), offer a promising route to tackling combinator"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2602.14327v2 Announce Type: replace Abstract: Variational Quantum Algorithms (VQAs), such as the Quantum Approximate Optimization Algorithm (QAOA), offer a promising route to tackling combinatorial optimization problems on near and intermediate-term quantum devices. However, their performance critically depends on the choice of initial parameters, and the limited expressiveness of the QAOA ansatz makes identifying effective initializations both difficult and unscalable. To address this, we propose a framework, Scalable Parameter Initialization for QAOA (SPIQ), that employs a relaxed QAOA ansatz to enable classical search over a set of Clifford-preparable quantum states that yield high-quality solutions. These states serve as superior QAOA initializations, driving rapid convergence while significantly reducing the quantum circuit evaluations needed to reach high-quality solutions and consequently lowering quantum-device cost. We present a scalable, application-agnostic initialization framework that achieves an absolute accuracy improvement of up to 80% over state-of-the-art initialization and reduces initial-state diversity by up to 10,000x across QUBO, PUBO, and PCBO problems spanning tens to hundreds of qubits. We further benchmark its performance on a wide range of problem formulations and instances derived from real-world datasets, demonstrating consistent and scalable improvements. Furthermore, we introduce two complementary strategies for selecting high-quality Clifford points identified by our search procedure and using them to seed multi-start optimization, thereby enhancing exploration and improving solution quality.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.14327) | 2026-08-25
