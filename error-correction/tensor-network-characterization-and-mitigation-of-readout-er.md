---
title: "Tensor network characterization and mitigation of readout errors"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.25974"
summary: "arXiv:2606.25974v2 Announce Type: replace Abstract: Readout errors are a major bottleneck to extracting reliable information from near-term quantum processors, especially when spatial correlations are"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2606.25974v2 Announce Type: replace Abstract: Readout errors are a major bottleneck to extracting reliable information from near-term quantum processors, especially when spatial correlations are non-negligible. We present a unified tensor-network framework that models the readout process as a matrix product operator (MPO), enabling efficient characterization and mitigation beyond uncorrelated approximations. The MPO model is trained via likelihood optimization on calibration data and applies to multiple tasks, including nonlocal observable estimation, random circuit sampling, and random-measurement protocols, such as classical shadows and learning-based tomography. Experiments on a superconducting processor and numerical simulations up to 20 qubits show that the MPO model captures correlated readout errors that uncorrelated models miss, with a sample cost that grows only near-linearly with system size. When extended to two-dimensional systems, the framework can also be integrated with tensor-network quantum error-correction decoders by performing joint inference over data and readout errors. These results establish tensor-network readout error mitigation as a scalable and versatile approach for noise-aware quantum data processing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.25974) | 2026-07-24
