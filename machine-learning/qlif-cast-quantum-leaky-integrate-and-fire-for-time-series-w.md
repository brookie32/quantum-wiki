---
title: "QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Weather Forecasting"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.18333"
summary: "arXiv:2605.18333v3 Announce Type: replace Abstract: Accurate and efficient time-series forecasting remains a challenging problem for both classical and quantum neural architectures, particularly in mu"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2605.18333v3 Announce Type: replace Abstract: Accurate and efficient time-series forecasting remains a challenging problem for both classical and quantum neural architectures, particularly in multivariate environmental settings. This work adapts the Quantum Leaky Integrate-and-Fire (QLIF) spiking neural network for time-series regression tasks, specifically short-term multivariate weather forecasting. We extend QLIF beyond classification and demonstrate its applicability to continuous-valued prediction problems. The QLIF-CAST model encodes neuron excitation states as single-qubit quantum superpositions, driven by R_x rotation gates and T1 relaxation decay, and is embedded within a hybrid quantum-classical recurrent architecture. We conduct two distinct evaluations. First, a controlled comparison against a parameter-matched classical LIF baseline on a multivariate weather dataset shows that QLIF-CAST achieves 15.4% lower MSE and 4.4% lower MAE, demonstrating that quantum neuronal dynamics reduce prediction error over classical equivalents. Second, a cross-domain comparative analysis with state-of-the-art quantum LSTM (QLSTM) and quantum neural network (QNN) models on air quality and wind speed benchmarks reveals that QLIF-CAST converges in up to 94% less training time, occupying a distinct position in the speed-error trade-off space. Hardware verification on IBM Marrakesh (156-qubit QPU) confirms reliable circuit execution with only 1.2% average deviation from simulation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.18333) | 2026-10-08
