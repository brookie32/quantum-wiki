---
title: "Dealing with low-weight errors that lead BP OSD to fail"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.30305"
summary: "arXiv:2610.30305v1 Announce Type: new Abstract: Belief Propagation combined with Ordered Statistics Decoding (BP OSD) is an open-source decoding tool used widely within the community due to its versat"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.30305v1 Announce Type: new Abstract: Belief Propagation combined with Ordered Statistics Decoding (BP OSD) is an open-source decoding tool used widely within the community due to its versatility and ease of application to Quantum Low Density Parity Check (QLDPC) codes. However, the degeneracy of quantum codes has been observed to degrade the performance of BP OSD, particularly leading to error floors for low physical error rates. Here, we investigate the low-weight error configurations responsible for such failures in Bivariate Bicycle codes. We show that, at code capacity, BP OSD fails on errors whose weight is significantly smaller than d/2, arising from global symmetries of the decoding graph that prevent the convergence of parallel BP. Furthermore, our analysis reveals new pitfalls that can arise when analysing the performance of BP OSD in the rare events regime, such as loss of ergodicity in splitting methods and numerical instabilities in the decoder. We show how to mitigate these failure mechanisms by modifying the BP update rules and the decoder implementation, leading to substantial improvement in logical error rate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.30305) | 2026-10-23
