---
title: "Efficient Trotter-Suzuki Schemes for Long-time Quantum Dynamics"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.18756"
summary: "arXiv:2601.18756v2 Announce Type: replace Abstract: Accurately simulating long-time dynamics of many-body systems is a challenge in both classical and quantum computing due to the accumulation of Trot"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2601.18756v2 Announce Type: replace Abstract: Accurately simulating long-time dynamics of many-body systems is a challenge in both classical and quantum computing due to the accumulation of Trotter errors. While low-order Trotter-Suzuki decompositions are straightforward to implement, their rapidly growing error limits access to long-time observables. We present a framework for constructing efficient high-order Trotter-Suzuki schemes by identifying their structure and directly optimizing their parameters over a high-dimensional space. This method enables the discovery of new schemes with significantly improved efficiency compared to traditional constructions, such as those by Suzuki and Yoshida. Based on the theoretical efficiency and practical performance, we recommend two novel highly efficient schemes at 4^{extrm{th}} and 6^{extrm{th}} order. We also demonstrate the effectiveness of these decompositions on the Heisenberg model and the quantum harmonic oscillator, and find that for a fixed final time they perform better across the computational cost. Even when using large time steps, they surpass established low-order schemes like the Leapfrog. Finally, we investigate the in-practice performance of different Trotter schemes and find the decompositions with more uniform coefficients tend to feature improved error accumulation over long times. We have included this observation into our choice of recommended schemes.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.18756) | 2026-07-31
