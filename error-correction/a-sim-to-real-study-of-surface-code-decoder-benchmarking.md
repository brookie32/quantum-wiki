---
title: "A Sim-to-Real Study of Surface-Code Decoder Benchmarking"
date: "2026-09-07"
updated: "2026-09-07"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.04557"
summary: "arXiv:2609.04557v1 Announce Type: new Abstract: Quantum error-correction decoders are typically benchmarked against synthetic circuit-level noise, under the assumption that a decoder's ranking under s"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

arXiv:2609.04557v1 Announce Type: new Abstract: Quantum error-correction decoders are typically benchmarked against synthetic circuit-level noise, under the assumption that a decoder's ranking under such noise transfers to hardware and improves as the noise model becomes more realistic. The Willow processor, the first to operate below the surface-code threshold, allows us to test this assumption. We rank a panel of six decoders using a four-rung ladder of noise models with increasing fidelity, evaluated against real data across three code distances, two bases, and fifteen round counts. Rank agreement with hardware appears once the noise model gives each operation type its own error rate. Calibrating the model to the device improves absolute error rates but not rank agreement. We additionally provide the first independent evaluation of NVIDIA's Ising pre-decoder on hardware, at code distances below its training receptive field and via a mapping onto the lattice on which it was trained. Under these conditions, it holds no accuracy-latency advantage: another panel decoder matches or improves on it in both per-cycle error rate and decode latency in 278 of the 280 evaluations. We release the full pipeline and the per-shot outcome of every evaluation, so future decoders and devices can be compared.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.04557) | 2026-09-07
