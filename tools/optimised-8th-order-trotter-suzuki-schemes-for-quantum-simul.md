---
title: "Optimised 8th-Order Trotter-Suzuki Schemes for Quantum Simulation"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "tools"
tags: [tools, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.27896"
summary: "arXiv:2611.27896v1 Announce Type: new Abstract: Simulating quantum dynamics in many-body systems is one of the most promising applications of quantum computers. Product formulas are a natural choice f"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2611.27896v1 Announce Type: new Abstract: Simulating quantum dynamics in many-body systems is one of the most promising applications of quantum computers. Product formulas are a natural choice for this task, since they map directly onto quantum gates, and increasing their order n could lead to reduced gate depths, provided the parameters are chosen efficiently. So far, schemes beyond 6^{extrm{th}} order have only been built as compositions of second-order schemes, while more general product formulas are known only up to 6^{extrm{th}} order. In this work, we extend our optimisation framework to order n = 8, and find both more efficient compositions and the first 8^{extrm{th}} order general schemes. Our formulas improve on the theoretical efficiency of the state-of-the-art schemes by Morales et al and we recommend two schemes explicitly. In simulations of the Heisenberg XZ chain one of our recommended schemes always outperforms those by Morales et al, though it is not always the same scheme that performs best. More generally, we observe that for Hamiltonians split into many non-commuting operators the uniformity of a Trotter decomposition becomes the main indicator of a scheme's performance. To assess the schemes' use on quantum hardware, we simulate noisy circuits with our new Qiskit plugin qiskit-omelyan. At current noise levels, the Leapfrog scheme remains the best choice, but as noise rates decrease toward fault tolerance, our recommended schemes become competitive.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.27896) | 2026-11-23
