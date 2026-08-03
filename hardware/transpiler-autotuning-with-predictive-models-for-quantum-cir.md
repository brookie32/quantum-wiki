---
title: "Transpiler Autotuning with Predictive Models for Quantum Circuit Optimization"
date: "2026-08-03"
updated: "2026-08-03"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.29145"
summary: "arXiv:2607.29145v1 Announce Type: new Abstract: Quantum software engineering is an emerging research field focusing on efficiently embedding the quantum programming paradigm into existing software eco"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

arXiv:2607.29145v1 Announce Type: new Abstract: Quantum software engineering is an emerging research field focusing on efficiently embedding the quantum programming paradigm into existing software ecosystems. A key aspect of this field is the realization of quantum algorithms using gate-based programming and the subsequent low-level optimization of the resulting quantum circuits, a process that is commonly performed by so-called transpilation pipelines. One significant challenge in these pipelines is determining which optimizations to apply to a given circuit. This decision is usually based on fixed default configurations that are uniformly applied to all circuits, frequently resulting in missed opportunities for more aggressive circuit optimization. In this work, we tackle this challenge by applying autotuning with supervised machine learning to develop an automated method for selection of transpiler passes. To train our machine-learning models, we employ feature-model based sampling to generate a representative dataset that examines how different combinations of Qiskit transpiler passes perform across thousands of circuits drawn from the state-of-the-art benchmarking suite MQT Bench. Using these data, we build a predictive model extension for the Qiskit transpilation pipeline that uses a machine learning model to automatically select combinations of transpiler passes aiming to achieve a maximum reduction in two-qubit gates. Our empirical evaluation shows that the combinations selected by our model are never outperformed by Qiskit's optimization levels, achieve on average an additional 19.1% - 32.4% reduction in two-qubit gates, and for some circuits finds reductions of up to 95.8% in cases where Qiskit achieves no reduction at all.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.29145) | 2026-08-03
