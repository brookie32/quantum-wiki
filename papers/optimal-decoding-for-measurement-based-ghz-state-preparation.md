---
title: "Optimal Decoding for Measurement-Based GHZ State Preparation: The Maximum-Utility Decoder"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.00160"
summary: "arXiv:2608.00160v1 Announce Type: new Abstract: The meticulous preparation of macroscopic Greenberger-Horne-Zeilinger (GHZ) states provides a foundational resource for quantum technologies such as met"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.00160v1 Announce Type: new Abstract: The meticulous preparation of macroscopic Greenberger-Horne-Zeilinger (GHZ) states provides a foundational resource for quantum technologies such as metrology, cryptography, and fault-tolerant codes. While state-of-the-art measurement-based protocols offer efficient low-depth execution, their performance can be bottlenecked by conventional decoders, such as minimum weight perfect matching (MWPM) or even maximum-likelihood decoding (MLD), which optimize for binary logical recovery and fail to maximize the continuous long-range order characteristic of a GHZ state for two-dimensional geometries. Here we overcome this limitation by framing the decoding problem as minimum Bayesian risk inference, introducing a general paradigm that maximizes the expected {utility} of the decoded state. Implementing this maximum-utility approach, we construct an algorithm that achieves the highest possible per-shot decoded quantum order and thereby establish an optimal decoding strategy for measurement-based GHZ state preparation. To improve its computational efficiency, we design a scalable two-stage decoder, which first encodes the syndromes into the edge weights of MWPM and then refines the result with a convolutional neural network trained to maximize the expected utility, at a fraction of the cost of the optimal decoder. Remarkably, we find that the first stage alonenicode{x2014}which makes the matching aware of the gauge choice at no cost beyond bare MWPMnicode{x2014}already performs near-optimally up to the largest sizes we study, N=256imes256, closing up to 87% of the gap between the bare-MWPM and optimal decoding thresholds. Generalizing MWPM and MLD, the maximum-utility decoder (MUD) establishes a versatile framework that can be explicitly tailored to the operational demands of specific experiments by redefining the utility function.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.00160) | 2026-08-04
