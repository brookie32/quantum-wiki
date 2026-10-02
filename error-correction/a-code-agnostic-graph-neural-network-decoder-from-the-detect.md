---
title: "A Code-Agnostic Graph Neural Network Decoder from the Detection Error Model"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01683"
summary: "arXiv:2610.01683v1 Announce Type: new Abstract: We present POLYMECHANON, a graph neural network (GNN) decoder for quantum error correction whose only input is the detection error model (DEM) of a quan"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01683v1 Announce Type: new Abstract: We present POLYMECHANON, a graph neural network (GNN) decoder for quantum error correction whose only input is the detection error model (DEM) of a quantum code under a given noise model. We represent the DEM as a tripartite graph of detectors, error mechanisms and logical observables, where every input feature is computed by using the quantum code as data rather than design choice. In this way, the same architecture decodes in principle any stabiliser code, under any noise model that can be expressed as a detection error model, once trained on the DEM. We test this approach along four directions. Firstly, on the rotated surface code the decoder outperforms correlated MWPM under both phenomenological and circuit-level noise, with up to 25% fewer logical failures. Secondly, on a family of high-rate qLDPC codes it matches BP+OSD on the smaller codes and surpasses it on the larger ones, with up to 16% fewer logical failures on [![130,4,6]!]. Thirdly, its decoding time does not depend on the physical error rate, whereas that of BP+OSD grows with it: on [![130,4,6]!] its effective cost per shot is of the order of a few ms on a single GPU against a few tens of milliseconds for BP+OSD on a single CPU core, and its fixed computational graph makes it a candidate for real-time decoding on neutral-atom processors. Finally, a single model trained across codes of different families outperforms uncorrelated MWPM on the graph-like codes seen during training and stays within 10% of BP+OSD on the others, while it tends to fail to generalize to unseen codes, particularly larger ones. Its probabilistic output enables confidence-based post-selection, lowering the logical error rate by more than an order of magnitude on the surface code while keeping more than 90% of the shots. Since only the DEM changes, new codes and noise models can be decoded without redesigning the decoder.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01683) | 2026-10-02
