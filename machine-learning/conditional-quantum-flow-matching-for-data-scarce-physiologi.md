---
title: "Conditional Quantum Flow Matching for Data-Scarce Physiological Signal Augmentation"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.14019"
summary: "arXiv:2609.14019v1 Announce Type: new Abstract: Generative augmentation is a standard remedy for label scarcity in physiological signal classification, but existing quantum generative models start fro"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.14019v1 Announce Type: new Abstract: Generative augmentation is a standard remedy for label scarcity in physiological signal classification, but existing quantum generative models start from uninformative noise, ignoring class structure that is already available. We propose Conditional Quantum Flow Matching (CQFM): a single 306-parameter circuit, conditioned on both flow time and class label, transports a compact class-conditional prior toward the target distribution. Quantum flow matching as published is unconditional, so this is to our knowledge the first conditional one, and the first EEG augmentation on a parameterized quantum circuit. A nonnegative spectral embedding removes the need for tomography at readout. On BCI Competition IV-2a, starting from a prior rather than noise is worth +5.1 accuracy points over QuDDPM (9/9 subjects), though at that operating point a class-conditional Gaussian matches CQFM. Where the prior fails the transport earns its keep: given one transferred from other subjects it regains +7.2 TSTR points (9/9).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.14019) | 2026-09-15
