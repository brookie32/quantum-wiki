---
title: "Risk-aware neural pulse compilation of continuously parameterized single-qubit gates with optimal-control benchmarking and NMR hardware validation"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.11314"
summary: "arXiv:2604.11314v3 Announce Type: replace Abstract: Pulse-level compilation can reduce the depth and calibration overhead associated with decomposing continuously parameterized quantum operations into"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2604.11314v3 Announce Type: replace Abstract: Pulse-level compilation can reduce the depth and calibration overhead associated with decomposing continuously parameterized quantum operations into fixed gate libraries, but conventional optimal control requires a new optimization for each target and can be sensitive to hardware uncertainty. We introduce a physics-informed neural compilation framework that learns a reusable map from continuously parameterized single-qubit gate targets directly to experimentally admissible control waveforms. The compiler is trained end-to-end through differentiable quantum dynamics without precomputed optimal-pulse labels, and its robustness is improved by first diagnosing physically relevant failure modes and then applying tail-risk-aware fine-tuning. On a three-qubit liquid-state nuclear magnetic resonance (NMR) model, the learned compiler generalizes across Haar-distributed single-qubit targets with mean nominal fidelity above 0.99 and generates new pulses in submillisecond inference time. Matched benchmarks reveal complementary advantages: robust gradient ascent pulse engineering (GRAPE) achieves the highest per-target fidelity, whereas the trained neural compiler amortizes the optimization cost across the target family, enabling substantially faster online pulse generation. Risk-aware training substantially broadens tolerance to radio-frequency (RF)-amplitude errors, including perturbations beyond the training range. Experiments on a three-spin NMR processor reproduce the predicted broadening of the RF-tolerance response, although the absolute experimental correlations are lower than the simulated values. These results establish a general workflow combining amortized machine learning, physical sensitivity diagnosis, risk-aware control, optimal-control benchmarking, and hardware testing, providing a route toward fast and robust pulse-level compilation for repeatedly varying quantum operations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.11314) | 2026-10-19
