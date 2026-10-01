---
title: "Transducer-based linear combination of unitaries: theory and applications"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40073"
summary: "arXiv:2609.40073v1 Announce Type: new Abstract: Linear combination of unitaries (LCU) is a fundamental primitive in quantum algorithms, whose cost is typically governed by the most expensive unitary a"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40073v1 Announce Type: new Abstract: Linear combination of unitaries (LCU) is a fundamental primitive in quantum algorithms, whose cost is typically governed by the most expensive unitary appearing in the combination. We develop a transducer-based LCU framework that reduces this worst-case dependence to a weighted average query complexity, when the constituent unitaries share access to a common set of primitive oracles. Consider A=sum_j c_j U_j, where c_j>0 and each unitary U_j can be implemented using C_j primitive queries. Given an upper bound ageq |A|, our algorithm implements a block-encoding of A/alpha with rescaling factor alpha=O(a), using widetilde{O} (C_{max}+overline{C} {lambda}/{a} ) primitive queries, where lambda=sum_j c_j, C_{max}=max_j C_j, and overline{C}= {sum_j c_j C_j}/{lambda}. By comparison, the standard LCU construction requires widetilde{O} (C_{max} {lambda}/{a} ) primitive queries. The improvement can therefore be substantial when costly unitaries have small weights and lambda/a is large. As applications, we obtain improved block-encodings of sparse matrices, leading to quantum algorithms for sparse Hamiltonian simulation and quantum linear systems with near-optimal query complexity up to polylogarithmic factors in all relevant parameters. Our main technique is the transducer framework developed by Belovs, Jeffery, and Yolcu [Quantum, 8:1444 (2024)]. Here we develop a complementary operator-level theory tailored to block-encodings. We identify the resolvent norm K as a key complexity measure for transducer implementation besides the existing catalyst complexity. We show that the transducer action can be converted into an epsilon-approximate block-encoding using only Oleft(K log(1/epsilon)right) queries to the transducer, improving the precision dependence from polynomial to logarithmic.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40073) | 2026-10-01
