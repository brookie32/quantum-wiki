---
title: "Local tensor-train surrogates for quantum learning models"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25631"
summary: "arXiv:2604.25631v1 Announce Type: new Abstract: A key bottleneck in quantum machine learning is the computational cost of repeated quantum circuit evaluations during the inference phase. To address th"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25631v1 Announce Type: new Abstract: A key bottleneck in quantum machine learning is the computational cost of repeated quantum circuit evaluations during the inference phase. To address this, we present a framework for constructing fast, cheap, provably accurate classical tensor-train surrogates of fully trained quantum machine learning models within local patches of their input data space. The approach combines Taylor polynomial approximation with a tensor-train (TT) representation and embeds it in a statistical learning paradigm via empirical risk minimization. In our analysis, the Taylor-TT construction serves as a deterministic error certificate proving that the TT hypothesis class contains a good approximation; empirical risk minimization then provably recovers a surrogate with controlled generalization error and explicit bounds. This translates into three independently controllable error sources: (i) Taylor truncation error controlled by the patch radius r and polynomial degree p, (ii) TT approximation error controlled by the bond dimension hi, and (iii) statistical estimation error. While the parameter count scales polynomially in the number of data dimensions N, i.e., d_{eff} = N(p+1)hi^2 rather than the naive (p+1)^N, the worst-case constants inherit an exponential factor through the tensor-product feature norm during Taylor polynomial embedding onto TT. This cleanly separates representation complexity from feature-induced constants. Our risk bounds and sample complexity depend explicitly on the local patch radius r.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25631) | 2026-04-29
