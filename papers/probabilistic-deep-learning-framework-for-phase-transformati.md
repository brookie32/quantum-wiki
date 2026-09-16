---
title: "Probabilistic Deep Learning Framework for Phase Transformation Forecasting aided by In Situ High temperature Microscopy"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.16940"
summary: "arXiv:2609.16940v1 Announce Type: cross Abstract: The mechanical performance of structural materials is governed by their microstructure, which is itself set by the thermal history imposed during proc"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2609.16940v1 Announce Type: cross Abstract: The mechanical performance of structural materials is governed by their microstructure, which is itself set by the thermal history imposed during processing. Predicting how that microstructure evolves along an arbitrary thermal trajectory, however, remains a challenging problem. Conventional continuous-cooling-transformation diagrams, for instance, provide only a static description, and they do not exist for all materials, especially emerging and novel ones. Deep-learning approaches address this issue, but they treat image-based characterization, temporal prediction, and microstructure forecasting as separate tasks. Here, we introduce a probabilistic deep-learning framework that unifies these tasks for in situ high-temperature confocal laser scanning microscopy data. The initial surface image is compressed with a beta-variational autoencoder into a low-dimensional latent representation, which, together with the cooling rate and the full temperature history, is passed to a temporal fusion transformer that produces a quantile forecast of the Widmanstatten ferrite ratio. In parallel, a Gaussian process predicts the end-state Widmanstatten ferrite ratio and corrects the forecast equilibrium level, yielding probabilistic prediction intervals. We demonstrate the efficacy of our method on Widmanstatten ferrite evolution in S235 steel across five cooling regimes and showcase significant accuracy. This verifies the relevance of our framework and paves the way for a streamlined and highly accelerated investigation of material evolution under thermal treatment.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.16940) | 2026-09-16
