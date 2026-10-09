---
title: "Large-Scale Benchmarking of Quantum Neural Network Configurations for Financial Time Series Forecasting"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.12148"
summary: "arXiv:2610.12148v1 Announce Type: cross Abstract: Quantum machine learning, and quantum neural networks (QNNs) in particular, are advancing fields with growing potential. Although systematic compariso"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.12148v1 Announce Type: cross Abstract: Quantum machine learning, and quantum neural networks (QNNs) in particular, are advancing fields with growing potential. Although systematic comparisons of QNN configurations have been explored primarily for classification tasks, comparatively little attention has been given to regression problems, particularly financial time series forecasting. This study presents a large-scale systematic comparative evaluation of QNN component configurations for financial time series forecasting, using the GBP/USD spot exchange rate as a case study. A grid search across encoding methods, ansatz designs, qubit counts, layer depths, and cost functions yields 1,368 distinct model configurations, each evaluated in terms of prediction accuracy, computational cost, and convergence behaviour. The results reveal unique insights into how the choice of methods influences performance, such as that gate selection and arrangement are more critical to model success than raw parameter count, and that entanglement is a system-level property of the full circuit rather than solely at the ansatz level. The best-performing QNN configuration achieves an R^2 score of 0.985, outperforming a classical BiLSTM baseline. Additionally, the impact of real quantum hardware noise is assessed through execution on the IQM Emerald device, revealing that gate errors and decoherence represent a significant barrier to practical deployment, with gate selection and circuit depth identified as key determinants of hardware noise resilience. Overall, the findings provide practical architectural guidance for QNN design and establish a baseline characterisation of QNN noise sensitivity on near-term quantum devices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.12148) | 2026-10-09
