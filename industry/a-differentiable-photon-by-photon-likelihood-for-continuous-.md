---
title: "A differentiable photon-by-photon likelihood for continuous free-energy landscapes and diffusion coefficients from single-molecule FRET"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "industry"
tags: [industry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2608.21061"
summary: "arXiv:2608.21061v1 Announce Type: new Abstract: Single-molecule FRET probes the conformational dynamics of biomolecules by measuring the distance between two dyes. The experiment produces a stream of "
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2608.21061v1 Announce Type: new Abstract: Single-molecule FRET probes the conformational dynamics of biomolecules by measuring the distance between two dyes. The experiment produces a stream of coloured photons, which is only an indirect readout of these dynamics. Recovering the free-energy landscape and diffusion coefficient from such a photon stream is a difficult inverse problem. Existing approaches assume a small number of discrete states, bin the photons, or are computationally expensive. Here we derive an exact likelihood for the recorded photon stream under a model in which the dye distance diffuses on a continuous free-energy landscape. It uses the raw inter-photon times and colours at full time resolution, and analytically integrates out all hidden trajectories. The likelihood is differentiable, so automatic differentiation returns exact gradients with respect to all model parameters. This lets us jointly infer the free-energy landscape, the diffusion coefficient, and the photophysical parameters by gradient-based optimization. On simulated data, we recover free-energy landscapes, including ones with a short-lived intermediate, together with the diffusion coefficients. Uncertainties follow from the curvature of the likelihood, computed directly from the same gradients. The framework also guides experimental design. Before any data are recorded, we can evaluate how much a given acquisition setting reduces the resulting uncertainty. Evaluation on the GPU is fast, and independent traces are processed in parallel, so a single fit converges in minutes and scales to large datasets. The likelihood extends photon-by-photon analysis to continuous free-energy landscapes and diffusion coefficients, putting fast quantitative inference with uncertainties within reach of the smFRET community.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2608.21061) | 2026-08-24
