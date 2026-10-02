---
title: "Regev's reduction as a candidate quantum algorithm for the discrete logarithm problem in finite abelian groups"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.03972"
summary: "arXiv:2605.03972v2 Announce Type: replace Abstract: In this article, we investigate whether combining Regev's reduction with the Cheng-Wan reduction can yield an alternative quantum algorithm for the "
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2605.03972v2 Announce Type: replace Abstract: In this article, we investigate whether combining Regev's reduction with the Cheng-Wan reduction can yield an alternative quantum algorithm for the discrete logarithm problem (DLOG) in finite abelian groups. Cheng and Wan reduce DLOG over finite fields to bounded-distance decoding of low-rate Reed-Solomon codes at a large decoding radius. Regev's reduction, in turn, exploits a decoder for the high-rate dual code with a lower noise level to obtain a quantum algorithm for decoding the original low-rate code at a larger radius. The Cheng-Wan instances therefore provide a natural setting in which to explore the power of Regev's framework. We first extend the Cheng-Wan reduction to the discrete logarithm problem in finite abelian groups, assuming access to embeddings of their cyclic factors. We also establish NP-hardness of Reed-Solomon bounded-distance decoding at asymptotically vanishing rate, reaching the rate regime relevant to Cheng-Wan, while the radius at which we establish hardness remains beyond the Cheng-Wan radius. We then instantiate Regev's reduction at the Cheng-Wan parameters and, under a conjecture on the performance of the induced BDD algorithm on the structured Cheng-Wan instances, characterize the noise threshold for the quantum decoding problem(QDP) sufficient to solve DLOG. We evaluate known decoders in this regime and show that a quantum decoder based on unambiguous state discrimination(USD) enables Regev's reduction to reach a strictly stronger decoding regime than the standard classical Reed-Solomon decoders we consider. Nevertheless, the QDP noise threshold required by the Cheng-Wan reduction is asymptotically 4/3 times that achieved by USD. Going beyond the USD framework, we show that every Cheng-Wan instance can be solved through Regev's reduction using a suitable Pretty Good Measurement and its inverse, although no efficient implementation of it is known.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.03972) | 2026-10-02
