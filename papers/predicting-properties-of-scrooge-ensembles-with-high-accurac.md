---
title: "Predicting properties of Scrooge ensembles with high accuracy and low sample complexity"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39992"
summary: "arXiv:2609.39992v1 Announce Type: new Abstract: The Scrooge ensemble associated with a density matrix rho is the maximally random ensemble whose average density matrix is rho. It has attracted growing"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39992v1 Announce Type: new Abstract: The Scrooge ensemble associated with a density matrix rho is the maximally random ensemble whose average density matrix is rho. It has attracted growing interest for its applications to quantum many-body dynamics and quantum information. The intrinsic statistical properties of the Scrooge ensembles are encoded in their higher-order moments, yet they are nontrivial to analyze and prepare for they feature a non-polynomial Haar integrand, blocking direct use of Haar integration machinery. Existing physical mechanisms to sample multiple copies of states from the Scrooge ensembles, meanwhile, typically require costly postselection, rendering them inefficient for large system size. In this work, we develop efficient and accurate methods for analyzing and implementing Scrooge moments. We first introduce a polynomial approximation to the Scrooge k-th moments whose error is tunable down to a threshold that improves from inverse polynomial to exponential in 1/||rho||_infty over previous results. Building on our approximation, we then give the first efficient quantum algorithm that estimates observable expectation values using widetilde{O}(k^3/epsilon^5) copies of rho for any target error epsilon above this threshold. We further provide a construction of a block encoding of the Scrooge k-th moment when the preparation circuit of rho is known. Of independent interest could be a key subroutine in our algorithms, which efficiently implements projection onto the k-fold symmetric subspace for rho^{otimes k} using O(k^3/epsilon^2) samples of rho, avoiding the naive k! postselection cost of such a projection. These results provide new tools for both the theoretical analysis and practical prediction of properties of Scrooge ensembles, with potential applications to quantum many-body dynamics and quantum information processing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39992) | 2026-10-01
