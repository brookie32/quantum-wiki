---
title: "Explicit Separations for One-Query Unitary Synthesis"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.26478"
summary: "arXiv:2607.26478v1 Announce Type: new Abstract: The unitary synthesis problem (Aaronson-Kuperberg, CCC 2007) asks whether every n-qubit unitary U is computable by efficient quantum circuits relative t"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2607.26478v1 Announce Type: new Abstract: The unitary synthesis problem (Aaronson-Kuperberg, CCC 2007) asks whether every n-qubit unitary U is computable by efficient quantum circuits relative to some classical oracle f = f_U depending on U. Recently, Lombardi-Ma-Wright (STOC 2024) proved that Haar-random unitaries cannot be efficiently synthesized by algorithms that make 1 query (or poly(n) parallel queries) to an arbitrary classical oracle. In this work, we prove several results about the hardness (and easiness!) of variants of unitary synthesis. Our results include: (1) 1-query vs. 2-query unitary synthesis: we prove 1-query lower bounds for synthesizing random permutation unitaries Plvert xrangle = lvert pi(x)rangle, as well as random alternating-basis phase unitaries F_2 dot H^{otimes n} dot F_1. This gives 1-query lower bounds for "explicit" families of unitaries that have efficient (even 2-query) synthesis algorithms. (2) Upper bound for complex phase unitaries: we also consider complex phase unitaries lvert xranglemapsto alpha_x lvert xrangle, which have a clean 2-query synthesis algorithm with no obvious 1-query algorithm. In this case, we prove an upper bound: there are 1-query algorithms (relative to binary phase oracles) that constant-approximate these unitaries in diamond distance. In order to prove our lower bounds, we introduce and analyze two new cryptographic games: the oracle state search game and the oracle Choi state game. Compared to prior work, our framework is mathematically simple, more flexible in what it can prove, and more accurately captures the hardness of synthesizing unitaries that are not "fully random". Finally, we also use the search game to prove a new hardness-of-approximation result for quantum programs (synthesizing unitaries relative to quantum advice) for phase unitaries, giving a sharper separation between 1-query unitary synthesis and quantum programs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.26478) | 2026-07-30
