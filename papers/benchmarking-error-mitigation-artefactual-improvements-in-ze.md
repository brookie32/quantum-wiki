---
title: "Benchmarking Error Mitigation: Artefactual Improvements in Zero-Noise Extrapolation"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.09360"
summary: "arXiv:2607.09360v2 Announce Type: replace Abstract: Reliable benchmarking of Quantum Error Mitigation (QEM) requires distinguishing genuine improvements from artefacts of the post-processing arithmeti"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2607.09360v2 Announce Type: replace Abstract: Reliable benchmarking of Quantum Error Mitigation (QEM) requires distinguishing genuine improvements from artefacts of the post-processing arithmetic. In this paper, we expose a failure mode in Richardson Zero-Noise Extrapolation (ZNE), a widely used technique routinely (and often implicitly) relied upon in benchmarks and experiments. When noise amplification operates beyond usable signals - a regime that is quickly reached on current hardware for non-trivial circuits - we show that the extrapolation no longer reflects the underlying physics, but collapses into a fixed rescaling of a single noisy measurement, producing a bogus apparent improvement that is independent of noise amplification. This poses a rarely considered threat to the validity of many empirical evaluations in quantum computing. Measurements on real hardware (IQM Euro-Q-Exa) confirm this collapse with ordinary folding alone: as circuit depth erodes the signal, the reported estimate decouples from the truth and overshoots the ideal by up to 21%. We further introduce a matched-cost "garbage-folding" negative control that carries no usable signal yet reports a larger apparent improvement than genuine folding - showing that the magnitude of an improvement is not evidence of its correctness - alongside a zero-cost check flagging the artefact from data a benchmark already holds. We distil both into a short reporting checklist for ZNE benchmarks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.09360) | 2026-08-04
