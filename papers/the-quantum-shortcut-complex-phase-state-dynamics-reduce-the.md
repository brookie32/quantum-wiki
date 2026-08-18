---
title: "The Quantum Shortcut: Complex Phase-State Dynamics Reduce the Optimization Steps of Sequence Models"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.14691"
summary: "arXiv:2608.14691v1 Announce Type: cross Abstract: Sequence models are conventionally distinguished by their backbone, the mechanism that routes information across positions, such as attention or recur"
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.14691v1 Announce Type: cross Abstract: Sequence models are conventionally distinguished by their backbone, the mechanism that routes information across positions, such as attention or recurrence. This paper varies a choice that is prior to the backbone and shared by nearly all current models: the substrate, the number system in which the hidden state is represented together with the form of the map from state to prediction. The prevailing substrate is a real-valued state with an affine--softmax readout; we study a complex-valued alternative drawn from the mathematics of quantum theory, in which information is carried by the phases of the state and scores are quadratic Born forms. Prior work proved an idealized version of this substrate representationally stronger than any real model with a linear readout; we ask whether it also trains faster. Relaxing the two properties that block deployment, exact unitarity and the Born vocabulary readout, we instantiate it in the Mamba state-space model and an attention-based Transformer. At 253M parameters, matched to within 0.02% and trained under one fixed protocol on three byte-level corpora, the complex models reach every measured validation loss in approximately one third (state-space) and one half (attention) of the optimization steps of their real counterparts. The two backbones then diverge. Once the learning-rate warmup ends, the state-space advantage continues to widen, from 0.321 to 0.354 bits per character on OpenWebText and from 0.368 to 0.396 on FineWeb, which an artifact of the warmup ramp would not do; the attention advantage instead decays toward zero on every corpus, and is therefore an effect of early training.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.14691) | 2026-08-18
