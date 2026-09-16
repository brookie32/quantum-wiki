---
title: "The Role of Symmetry in Quantum Query-to-Communication Simulation"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2012.05233"
summary: "arXiv:2012.05233v3 Announce Type: replace Abstract: Buhrman, Cleve and Wigderson (STOC'98) showed that for every Boolean function f : {-1,1}^n to {-1,1} and G in {AND_2, XOR_2}, the bounded-error quan"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2012.05233v3 Announce Type: replace Abstract: Buhrman, Cleve and Wigderson (STOC'98) showed that for every Boolean function f : {-1,1}^n to {-1,1} and G in {AND_2, XOR_2}, the bounded-error quantum communication complexity of the composed function f o G equals O(Q(f) log n), where Q(f) denotes the bounded-error quantum query complexity of f. This is achieved by Alice running the optimal quantum query algorithm for f, using a round of O(log n) qubits of communication to implement each query. This is in contrast with the classical setting, where it is easy to show that R^{cc}(f o G) is at most 2R(f), where R^{cc} and R denote bounded-error communication and query complexity, respectively. We show that the O(log n) overhead is required for some functions in the quantum setting, and thus the BCW simulation is tight. We note here that prior to our work, the possibility of Q^{cc}(f o G) = O(Q(f)), for all f and all G in {AND_2, XOR_2}, had not been ruled out. More specifically, we show the following. - We show that the log n overhead is *not* required when f is symmetric, generalizing a result of Aaronson and Ambainis for the Set-Disjointness function (Theory of Computing'05). - In order to prove the above, we design an efficient distributed version of noisy amplitude amplification that allows us to prove the result when f is the OR function. - In view of our first result above, one may ask whether the log n overhead in the BCW simulation can be avoided even when f is transitive, which is a weaker notion of symmetry. We give a strong negative answer by showing that the log n overhead is still necessary for some transitive functions even when we allow the quantum communication protocol an error probability that can be arbitrarily close to 1/2. - We also give, among other things, a general recipe to construct functions for which the log n overhead is required in the BCW simulation in the bounded-error communication model.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2012.05233) | 2026-09-16
