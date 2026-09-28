---
title: "Removing nodal and support-mismatch pathologies in Variational Monte Carlo via blurred sampling"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.18148"
summary: "arXiv:2603.18148v2 Announce Type: replace-cross Abstract: Variational Monte Carlo (VMC) is a powerful and fast-growing method for optimizing and evolving parameterized many-body wave functions, especi"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

arXiv:2603.18148v2 Announce Type: replace-cross Abstract: Variational Monte Carlo (VMC) is a powerful and fast-growing method for optimizing and evolving parameterized many-body wave functions, especially with modern neural-network quantum states. In practice, however, the stochastic estimators that form the backbone of the method can become unstable or biased due to the presence of nodes, a ubiquitous feature of quantum wave functions. In the continuum, this results in heavy-tailed estimators with potentially divergent variances, while in discrete Hilbert spaces the sampling distribution can miss parts of the support needed to form unbiased estimators. These statistical pathologies lead to unreliable optimization trajectories in stochastic reconfiguration or incorrect variational dynamics in time-dependent Variational Monte Carlo (t-VMC), and severely limit the power of the numerical simulations. We introduce blurred sampling to address these difficulties. The method has a number of rigorous properties that make it well-behaved, effective and computationally efficient. Additionally, it is a post-processing approach that can be used without modifying the underlying sampler and incurs only minimal overhead. We demonstrate its effectiveness in a broad range of problems -- including ground state optimization in both continuum and discrete settings, as well as in time-dependent variational Monte Carlo, where it resolves previously identified failure modes -- and further apply it to large-scale problems in spin dynamics. This work establishes a broadly applicable framework for robust VMC and t-VMC calculations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.18148) | 2026-09-28
