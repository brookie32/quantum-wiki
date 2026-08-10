---
title: "Quantum Feature Amplification Network (QFAN) as An Autoregressive Quantum Generative Model"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.16044"
summary: "arXiv:2605.16044v3 Announce Type: replace Abstract: Simulating calorimeter showers is one of the largest computing costs in high-energy physics, and quantum generative models have been proposed as com"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2605.16044v3 Announce Type: replace Abstract: Simulating calorimeter showers is one of the largest computing costs in high-energy physics, and quantum generative models have been proposed as compact alternatives. Their progress is blocked by a resource problem: in existing gate-model proposals the register must grow with the image, so benchmark geometries with thousands of cells are out of reach. We introduce the Quantum Feature Amplification Network (QFAN), which breaks the link between register size and image size. QFAN splits an image into consecutive blocks of b pixels and generates them one at a time, every block produced by the same small circuit conditioned on a fixed-length summary of the pixels already generated, so the qubit count is set by the block size rather than the image dimension. The circuit is used as a sampler: each block is decoded from a finite set of Born measurement records, so the stochasticity of the generated shower is measurement randomness rather than classical noise, and a trained fraction of records is shared between the pixels of a block to control their correlation. Training minimizes a characteristic-function maximum mean discrepancy with exact analytic gradients. Using three qubits and 12 to 18 shared parameters, QFAN reproduces per-pixel spectra, inter-pixel correlations and total deposited energy at d=12 and d=25 pixels, on a noiseless simulator and on IBM hardware. Removing one element of the pipeline at a time locates what the quantum component contributes. Replacing the sampled records by their conditional means, which removes only the measurement randomness, does not degrade the model but collapses it to a single deterministic image. Freezing the circuit at its untrained initialization, with every classical stage refitted, leaves a model reproducing neither observable: it transports under a tenth of the inter-pixel correlation of the data and its per-pixel spectra degrade twofold.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.16044) | 2026-08-10
