---
title: "FaultScope: A software package for fast error attribution in quantum error correction"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41528"
summary: "arXiv:2610.41528v1 Announce Type: new Abstract: We introduce FaultScope, a classical simulator for quantum error correction circuits, implemented in Rust with a Python interface. FaultScope estimates "
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41528v1 Announce Type: new Abstract: We introduce FaultScope, a classical simulator for quantum error correction circuits, implemented in Rust with a Python interface. FaultScope estimates logical error rates and their derivatives with respect to component error rates from the same sampled and decoded shots, without modifying or differentiating through the decoder. These derivatives enable error attribution to individual noisy components, helping identify noise hotspots for targeted noise reduction. FaultScope supports forward simulation of error propagation through circuits and direct sampling of detector and logical observable outcomes from detector error models. In our noiseless and noisy benchmarks, FaultScope has the lowest runtime among the tested simulators at every size. Computing all derivatives adds only 0.33--0.97% to the runtime of logical error rate estimation across five repetition code sizes with 7--2047 error locations. FaultScope can be used to benchmark large-scale quantum error correction schemes and guide targeted noise reduction efficiently, thereby facilitating the design and optimization of fault-tolerant quantum computing architectures.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41528) | 2026-11-02
