---
title: "Accelerating dynamic polarizability calculations of organic molecules using equivariant graph neural networks"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.09389"
summary: "arXiv:2610.09389v1 Announce Type: new Abstract: Predicting the dynamic polarizability tensor of organic molecules is essential for simulating light-matter interactions in optoelectronic devices, yet c"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.09389v1 Announce Type: new Abstract: Predicting the dynamic polarizability tensor of organic molecules is essential for simulating light-matter interactions in optoelectronic devices, yet conventional quantum-chemical methods such as time-dependent density functional theory (TD-DFT) are computationally expensive and limit large-scale screening. We present an equivariant graph neural network architecture that predicts frequency-dependent, complex-valued dynamic polarizability tensors directly from readily available molecular information, such as 3D geometry and UV-vis spectra. The model learns to approximate the shape and magnitude of the dynamic polarizability tensor, capturing both dispersive and absorptive features that define the molecular optical response. We evaluate the model on molecules from both the QM9 dataset and the Harvard organic photovoltaic dataset using various metrics, including the earth mover's distance, which is suitable for comparing spectral quantities. For both datasets, the model successfully reproduces the main features of the dynamic polarizability tensor and generalizes across diverse molecules. To assess the applicability, we further validated the model using a downstream workflow to calculate the optical properties of organic photovoltaic devices. We used the model-predicted polarizabilities to perform device-level optical simulations, yielding charge carrier generation rates in agreement with TD-DFT-based results (R^2 = 0.94). Our approach offers a promising complement, or even an alternative, to conventional methods such as TD-DFT, enabling faster and more efficient screening of photoactive organic molecules for optoelectronic applications.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.09389) | 2026-10-08
