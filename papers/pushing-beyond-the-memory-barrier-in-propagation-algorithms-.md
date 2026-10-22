---
title: "Pushing beyond the memory barrier in propagation algorithms with randomization"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.28845"
summary: "arXiv:2610.28845v1 Announce Type: new Abstract: Performant classical tools for simulating quantum circuits are important for benchmarking and supporting upcoming quantum devices. Pauli propagation off"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2610.28845v1 Announce Type: new Abstract: Performant classical tools for simulating quantum circuits are important for benchmarking and supporting upcoming quantum devices. Pauli propagation offers promising capabilities, but deep circuits usually cause a rapid growth in the number of Pauli strings and can quickly exhaust the available memory. In this work, we introduce a randomized protocol that combines a specialized resampling schedule, merging, and a controlled amount of bias to keep the propagating Pauli sum within any prescribed memory budget. Additional computational resources can then be spent on embarrassingly parallel repetitions that systematically improve the estimate. Building on the open-source library PauliPropagation.jl, we show that 1) increasing memory of each simulation reduces the error systematically more than outside averaging, 2) resampling just enough to apply the next gate delays variance accumulation and gives better error-per-time trade-offs than more aggressive resampling, and 3) a small, controlled bias is crucial in cutting down variance and pushing far beyond unbiased randomization. The resulting framework can reproduce deterministic calculations while requiring several orders of magnitude less memory.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.28845) | 2026-10-22
