---
title: "On the Expressive Power and Capacity of Quantum Data Reuploaders"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.09947"
summary: "arXiv:2610.09947v1 Announce Type: new Abstract: Data reuploading---repeatedly encoding classical inputs at multiple layers of a parameterized quantum circuit---is a central mechanism for enhancing the"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.09947v1 Announce Type: new Abstract: Data reuploading---repeatedly encoding classical inputs at multiple layers of a parameterized quantum circuit---is a central mechanism for enhancing the expressivity of quantum neural networks (QNNs). Building on the Fourier-theoretic framework of Schuld et al.~ite{schuld2021fourier}, we study the frequency spectrum of the general multivariate, R-reupload architecture (QDR). (i) We make explicit that the accessible frequencies form the set K_R=S^{(R)}-S^{(R)}, which equals the R-fold sumset T^{(R)} of the difference set T=S-S of the encoding spectrum, and we characterise it exactly: K_R={kinmathcal L: ell_T(k)le R}, where mathcal L=span_{mathbb Z}(T) is an integer lattice and ell_T is word length in T. (ii) We show that the directions of the spectrum stabilise already at R=1 (the real span of K_R equals that of mathcal L), whereas the spectrum itself never saturates: the maximal frequency grows linearly in R and the number of frequencies grows polynomially, as Theta(R^{m}) with m=rank,mathcal L. (iii) Using the spectrum size, we give a Rademacher-complexity bound on the capacity of QDRs of order sqrt{|K_R|/n}. (iv) We report experiments on function approximation and classification with train/test splits, several seeds and parameter-matched classical baselines. The simulated spectra match the theory exactly. A single-qubit QDR beats a matched MLP on several smooth or periodic univariate targets and on the spiral task, but it is clearly worse on multivariate regression (dge4), where it is highly sensitive to the input-encoding scale; it beats the MLP only on equations with dle3 inputs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.09947) | 2026-10-08
