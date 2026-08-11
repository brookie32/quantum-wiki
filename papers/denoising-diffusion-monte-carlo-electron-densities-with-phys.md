---
title: "Denoising Diffusion Monte Carlo Electron Densities with Physically Informed Variance Stabilization: From Fourier Filters to 3D UNETs"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.08152"
summary: "arXiv:2608.08152v1 Announce Type: cross Abstract: Obtaining accurate electron densities is important for the fundamental description of molecular and condensed matter systems, as well as for the devel"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.08152v1 Announce Type: cross Abstract: Obtaining accurate electron densities is important for the fundamental description of molecular and condensed matter systems, as well as for the development of next-generation density functionals. Diffusion Monte Carlo (DMC), in particular, is known to produce benchmark-quality data; however, the predicted real-space electron densities contain substantial amounts of statistical noise. In this work, we study denoising approaches for DMC densities, judged on the basis of the information-theoretic Jensen-Shannon divergence. The denoising is facilitated by an approximate heteroscedastic to homoscedastic transformation leveraging the density functional theory density as a physical prior. We systematically compare a range of denoising techniques-including Fourier transform, regression, and 3D UNETs-on materials showing a wide range of density variations: carbon diamond, blue phosphorus, and rutile VO2. Our results indicate that simple flattened machine learning models and 2D image-based models introduce line artifacts and struggle to capture the full spatial correlation. In contrast, when using variance stabilization, regression methods outperform all others in both the high and low- noise limits across all materials considered. The best denoisers reduce the required cost of density-generating DMC simulations by 10-100x, providing a promising route forward for application in noise-sensitive tasks such as DFT functional inversion.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.08152) | 2026-08-11
