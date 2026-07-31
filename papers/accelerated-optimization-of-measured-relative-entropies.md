---
title: "Accelerated optimization of measured relative entropies"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2511.17976"
summary: "arXiv:2511.17976v2 Announce Type: replace Abstract: The measured relative entropy and measured Renyi relative entropy are quantifiers of the distinguishability of two quantum states rho and sigma. The"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2511.17976v2 Announce Type: replace Abstract: The measured relative entropy and measured Renyi relative entropy are quantifiers of the distinguishability of two quantum states rho and sigma. They are defined as the maximum classical relative entropy or Renyi relative entropy realizable by performing a measurement on rho and sigma, and they have interpretations in terms of asymptotic quantum hypothesis testing. Crucially, they can be rewritten in terms of variational formulas involving the optimization of a concave or convex objective function over the set of positive definite operators. In this paper, we establish foundational properties of these objective functions by analyzing their matrix gradients and Hessian superoperators; namely, we prove that these objective functions are eta-smooth and gamma-strongly convex / concave, where eta and gamma depend on the max-relative entropies of rho and sigma. A practical consequence of these properties is that we can conduct Nesterov accelerated projected gradient descent / ascent, a well known classical optimization technique, to calculate the measured relative entropy and measured Renyi relative entropy to arbitrary precision. These algorithms are generally more memory efficient than our previous algorithms based on semi-definite optimization [Huang and Wilde, arXiv:2406.19060], and for well conditioned states rho and sigma, these algorithms are notably faster.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2511.17976) | 2026-07-31
