---
title: "Analytic scGW nuclear gradients with the resolution-of-identity approximation"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.33536"
summary: "arXiv:2611.33536v1 Announce Type: new Abstract: We present the first fully analytic derivation and implementation of nuclear gradients for the finite-temperature scGW method. The derivation is formula"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2611.33536v1 Announce Type: new Abstract: We present the first fully analytic derivation and implementation of nuclear gradients for the finite-temperature scGW method. The derivation is formulated within the Phi-derivable framework of scGW, using a Lagrangian formulation to obtain the analytic gradients. With the resolution-of-identity approximation, the computational cost of evaluating the gradients scales as O(N_{au}N_ext{aux}^{2}N_ext{AO}^{2}), exhibiting the same asymptotic scaling as the parent scGW method. Using the newly implemented analytic gradients, we perform geometry optimizations for several molecular systems and benchmark the resulting structures against those obtained with Hartree--Fock, G_{0}W_{0}, MP2, CCSD, and CCSD(T). We find that scGW generally yields reasonable molecular geometries, with its performance being comparable to that of CCSD for several systems. Overall, these results demonstrate the potential of analytic scGW gradients for reliable geometry optimizations for molecular systems while retaining the favorable O(N_{au}N_ext{aux}^{2}N_ext{AO}^2) scaling of the underlying method.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.33536) | 2026-11-26
