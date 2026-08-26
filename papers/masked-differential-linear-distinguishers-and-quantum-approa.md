---
title: "Masked Differential-linear Distinguishers and Quantum Approaches"
date: "2026-08-26"
updated: "2026-08-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.24799"
summary: "arXiv:2608.24799v1 Announce Type: new Abstract: We introduce masked auto-correlation, a new primitive for the cryptanalysis of symmetric-key primitives, together with a quantum attack pipeline built o"
last_verified: "2026-08-26"
review_by: "2026-11-24"
stale: false
---

arXiv:2608.24799v1 Announce Type: new Abstract: We introduce masked auto-correlation, a new primitive for the cryptanalysis of symmetric-key primitives, together with a quantum attack pipeline built on it. For a permutation f, output masks alpha,eta, and an input difference w, masked auto-correlation (MAC) measures the correlation between the masked outputs alphadot f(x) and etadot f(xoplus w). The associated masked differential-linear (MDL) approximations strictly generalize several classical techniques; ordinary linear cryptanalysis, differential-linear cryptanalysis, and the differential-linear connectivity table all arise as special cases. Our central object of study is the problem of finding mask pairs with large masked cross-correlation -- those that yield powerful distinguishers -- which we call MAC Fishing. We give a constant-query quantum algorithm that samples such pairs according to their squared correlation, and we prove an exponential classical lower bound of Omega(N/log N) queries, by adapting the hardness of Fourier Fishing. To our knowledge this is the first result pairing a quantum upper bound with a classical lower bound for the core task of identifying high-correlation approximations, making quantum algorithms an absolute necessity. Building on this, we analyse the distribution of masked auto-correlation for random permutations, and then construct capacity-based distinguishers and key-recovery attacks, both classically and with a quadratic quantum speed-up using amplitude estimation. We validate our claims with experiments on reduced-round mini-AES.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.24799) | 2026-08-26
