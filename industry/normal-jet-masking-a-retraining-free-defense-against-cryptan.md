---
title: "Normal-Jet Masking: A Retraining-Free Defense Against Cryptanalytic Extraction of Neural Networks"
date: "2026-11-02"
updated: "2026-11-04"
source: "agent"
category: "industry"
tags: [industry, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2722"
summary: "Cryptanalytic extraction (CEA) of piecewise-linear neural networks recovers hidden signatures and parameters by locating critical points or hard-label dual points that expose off-manifold geometry. Pr"
last_verified: "2026-11-04"
review_by: "2027-02-02"
stale: false
---

Cryptanalytic extraction (CEA) of piecewise-linear neural networks recovers hidden signatures and parameters by locating critical points or hard-label dual points that expose off-manifold geometry. Proposed mitigation methods include query monitoring, output perturbation, ownership verification, and extraction-aware training. Train to Defend (TTD) directly addresses CEA through extraction-aware training, but cannot protect an already-trained checkpoint without retraining. We propose Normal-Jet Masking (NJM), a post-training wrapper that leaves the source model unchanged. NJM calibrates a tangent–normal tube around protected data, keeps private normal-direction mask channels inactive inside the tube, and mixes their piecewise-linear activations into served outputs outside it. NJM targets the shared evidence-acquisition stage rather than one attack implementation: mask events enter both raw-logit (soft-label) critical finding and hard-label dual finding before downstream signature and parameter recovery. Across seven MLPs, NJM reduces raw-logit evidence F1 by 53.8–93.1%, raises query cost by 1.4–9.3×, and eliminates pure hard-label duals. On CNNs, it preserves at least 0.9993 agreement while lowering source precision. These results show that post-training geometric masking complements training-time hardening across soft- and hard-label CEA.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2722) | 2026-11-02
