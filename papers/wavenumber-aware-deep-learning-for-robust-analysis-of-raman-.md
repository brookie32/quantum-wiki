---
title: "Wavenumber-Aware Deep Learning for Robust Analysis of Raman Spectra"
date: "2026-10-23"
updated: "2026-10-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.30746"
summary: "arXiv:2610.30746v1 Announce Type: cross Abstract: Machine-learning models for spectroscopy usually treat a spectrum as a fixed-grid intensity vector, leaving the physical coordinate implicit in the ar"
last_verified: "2026-10-23"
review_by: "2027-01-21"
stale: false
---

arXiv:2610.30746v1 Announce Type: cross Abstract: Machine-learning models for spectroscopy usually treat a spectrum as a fixed-grid intensity vector, leaving the physical coordinate implicit in the array index. Such models are tied to a single sampling grid, spectral range and resolution, which limits their use when measurement conditions change. Here we represent each spectral point as a pair of intensity and wavenumber and compute Transformer positional encodings from the wavenumber itself. On Raman spectra of three bacterial species and their synthetic mixtures, this representation remained robust to noise, sparser sampling and partial spectral coverage across convolutional, residual and Transformer networks. In controlled comparisons, wavenumber-based encoding outperformed index-based and learned encodings under partial observation and retained its performance on sampling grids never seen during training, where index-based encoding degraded. These findings were reproduced on a public 30-isolate bacterial benchmark. Explicit physical coordinates offer a simple route to robust spectral analysis under variable measurement conditions.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.30746) | 2026-10-23
