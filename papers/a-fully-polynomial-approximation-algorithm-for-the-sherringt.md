---
title: "A Fully Polynomial Approximation Algorithm for the Sherrington-Kirkpatrick Model"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.05446"
summary: "arXiv:2611.05446v1 Announce Type: cross Abstract: Montanari's incremental approximate message passing (IAMP) algorithm [FOCS 2019; SIAM J. Comput., 2025] and the zero-temperature formulation of El Ala"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.05446v1 Announce Type: cross Abstract: Montanari's incremental approximate message passing (IAMP) algorithm [FOCS 2019; SIAM J. Comput., 2025] and the zero-temperature formulation of El Alaoui, Montanari and Sellke (AMS) [Ann. Probab., 2021] find a (1-arepsilon) approximation to the maximum Sherrington-Kirkpatrick (SK) energy in C(arepsilon)N^2 operations for fixed accuracy, with probability tending to one as Noinfty, under their respective full-support and access-model assumptions. However, it was unknown whether this approximation could be achieved with work polynomial in both N and 1/arepsilon, together with quantitative guarantees at finite dimension. Under the same assumptions as AMS, we introduce grouped IAMP with exact Gaussian query outputs (GEG-IAMP), which is the first SK approximation algorithm with total work polynomial in N and 1/arepsilon and a finite-size guarantee above a dimension threshold polynomial in 1/arepsilon and log(1/alpha). More precisely, for every alphain(0,1/2), it returns a (1-arepsilon) approximation with probability at least 1-alpha whenever Nge mathsf{K}arepsilon^{-2}log^2(e/arepsilon)log(mathsf{K}/alpha), using O(N^2/arepsilon) work and O(N^2) storage. GEG-IAMP replaces the Onsager correction by Reeves's coupling construction [arXiv:2508.10782] and groups Euler-Maruyama steps into O(1/arepsilon) matrix-vector products. We also prove a relative guarantee for AMS IAMP with O(N^2arepsilon^{-3}log^2(e/arepsilon)) work but a sufficient dimension exponential in inverse accuracy. By returning a fixed configuration below its dimension threshold, GEG-IAMP also provides an asymptotic fully polynomial randomized approximation scheme (AFPRAS), with an additive error independent of dimension.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.05446) | 2026-11-05
