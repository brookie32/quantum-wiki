---
title: "Does the Readout Bypass Leak the Input? A Feature-Visibility Audit of Hybrid Quantum-Classical Models"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.38720"
summary: "arXiv:2609.38720v1 Announce Type: new Abstract: Readout-side residual hybrids concatenate raw inputs with measured quantum features. Under single-example gradient sharing, a biased first linear layer "
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.38720v1 Announce Type: new Abstract: Readout-side residual hybrids concatenate raw inputs with measured quantum features. Under single-example gradient sharing, a biased first linear layer admits standard analytic recovery of its input, so the bypass exposes raw coordinates without requiring inversion of the quantum circuit. We audit this mechanism using two tabular datasets, four architectures, and metrics conditioned on feature visibility. Iterative gradient matching gives median full-record PSNR of 73-96 dB for residual and input-only heads. Quantum-only heads score 8-11 dB on the full record but 54-96 dB on the six input coordinates they actually encode. These are reconstruction results for the tested six-input, six-observable circuits, not a general statement about quantum encodings. A loss-threshold membership attack remains near chance. The contribution is a visibility-conditioned privacy audit: omitted coordinates must not be credited as protection supplied by quantum processing, and near-exact PSNR differences must not be interpreted as meaningful privacy rankings. Our findings concern individual gradients and do not establish leakage under aggregation or multiple local training steps.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.38720) | 2026-10-01
