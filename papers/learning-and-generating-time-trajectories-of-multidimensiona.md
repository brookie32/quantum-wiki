---
title: "Learning and Generating Time Trajectories of Multidimensional Stochastic Processes"
date: "2026-11-16"
updated: "2026-11-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.17711"
summary: "arXiv:2611.17711v1 Announce Type: cross Abstract: We present a multidimensional statistics-informed neural network (SINN) framework for learning and generating trajectories of multicomponent stochasti"
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

arXiv:2611.17711v1 Announce Type: cross Abstract: We present a multidimensional statistics-informed neural network (SINN) framework for learning and generating trajectories of multicomponent stochastic processes. SINN is built upon a deterministic recurrent neural network that takes streams of white-noise sequences as input and generates ensembles of stochastic trajectories whose statistical properties match those of the underlying stochastic dynamics. While SINN has been demonstrated for various one-dimensional non-Markovian processes, extending it to multidimensional processes is essential for real-world applications. Here, we present key developments toward this goal. First, because direct estimation of multivariate probability density functions (PDFs) becomes computationally challenging with increasing dimension, we represent joint-distribution information using collections of one-dimensional PDFs constructed from linear combinations of the process components. Second, to accommodate the larger set of statistical objectives required to characterize multidimensional processes, we adopt a self-adaptive loss-balancing strategy that dynamically weights the components of the total loss function. Third, we introduce a reference-normalized validation framework that interprets statistical discrepancies relative to the finite-sample variability between independent target ensembles. We also investigate the role of the input white-noise dimension in SINN performance. We evaluate the proposed approach using a Langevin benchmark based on two coupled Duffing oscillators and further demonstrate its applicability to the Langevin dynamics of the Fermi-Pasta-Ulam chain and kinetic Monte Carlo simulations of a lattice Lotka-Volterra model. Our results demonstrate that the multidimensional SINN framework provides a practical approach for modeling multidimensional stochastic dynamics.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.17711) | 2026-11-16
