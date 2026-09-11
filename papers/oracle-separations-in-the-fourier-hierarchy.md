---
title: "Oracle Separations in the Fourier Hierarchy"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.11830"
summary: "arXiv:2609.11830v1 Announce Type: new Abstract: The Fourier hierarchy FH_0subseteqFH_1subseteqFH_2subseteqdots, introduced by Shi (TCS 2005), measures a quantum computation by the number of Hadamard l"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.11830v1 Announce Type: new Abstract: The Fourier hierarchy FH_0subseteqFH_1subseteqFH_2subseteqdots, introduced by Shi (TCS 2005), measures a quantum computation by the number of Hadamard layers it uses. Between two layers the circuit may permute basis states and attach phases, but it may not create superposition; the layers are its only source of interference. The first level is exactly BPP, while the second already solves Simon's problem and, through phase estimation, factors integers. Shi conjectured that every additional layer strictly increases computational power, and asked, as a first step, for oracle separations between consecutive levels. To our knowledge, the question was open at every level kge2. We prove that for every constant kge2 there is an oracle relative to which FH_ksubsetneqFH_{k+1}. The separating problem is built from Forrelation (Aaronson and Ambainis, STOC 2015): the level above solves it with a constant number of queries, whereas at level k it stays hard even for circuits making exponentially many queries. This holds for both of the usual ways of giving a circuit access to an oracle, the phase oracle and the standard oracle, which writes its answer into a register. The two are not interchangeable: relative to an oracle, the standard oracle is strictly more powerful at the same number of layers. We also separate the union of all the levels from BQP relative to an oracle. The lower bounds rest on a structural property of the hierarchy: the number of Hadamard layers limits how adaptively a circuit can query its oracle. With a phase oracle, a circuit with k layers is reproduced exactly by an algorithm making only k-1 rounds of parallel queries, which brings known lower bounds for such algorithms to bear. The standard oracle lets a circuit branch on earlier answers, and that case needs a separate argument.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.11830) | 2026-09-11
