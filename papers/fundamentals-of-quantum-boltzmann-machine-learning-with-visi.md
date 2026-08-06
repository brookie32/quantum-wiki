---
title: "Fundamentals of quantum Boltzmann machine learning with visible and hidden units"
date: "2026-08-06"
updated: "2026-08-06"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.19819"
summary: "arXiv:2512.19819v2 Announce Type: replace Abstract: One of the primary applications of classical Boltzmann machines is generative modeling, wherein the goal is to tune the parameters of a model distri"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

arXiv:2512.19819v2 Announce Type: replace Abstract: One of the primary applications of classical Boltzmann machines is generative modeling, wherein the goal is to tune the parameters of a model distribution so that it closely approximates a target distribution. Training relies on estimating the gradient of the relative entropy between the target and model distributions, a task that is well understood when the classical Boltzmann machine has both visible and hidden units. For some years now, it has been an obstacle to generalize this finding to quantum state learning with quantum Boltzmann machines that have both visible and hidden units. In this paper, I derive an analytical expression for the gradient of the quantum relative entropy between a target quantum state and the reduced state of the visible units of a quantum Boltzmann machine. Crucially, this expression is amenable to estimation on a quantum computer, as it involves modular-flow-generated unitary rotations reminiscent of those appearing in my prior work on rotated Petz recovery maps. This leads to a quantum algorithm for gradient estimation in this setting. I then specialize the setting to quantum visible units and classical hidden units, and vice versa; I also provide analytical expressions for the gradients, along with quantum algorithms for estimating them. Finally, I replace the quantum relative entropy objective function with the Petz-Tsallis relative entropy; here I develop an analytical expression for the gradient and sketch a quantum algorithm for estimating it, as an application of an independent derivation of a formula for the derivative of the matrix power function, which also involves modular-flow-generated unitary rotations. Ultimately, this paper demarcates progress in training quantum Boltzmann machines with visible and hidden units for generative modeling and quantum state learning.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.19819) | 2026-08-06
