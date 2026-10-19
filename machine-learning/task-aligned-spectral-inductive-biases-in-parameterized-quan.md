---
title: "Task-aligned spectral inductive biases in parameterized quantum circuits"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.23834"
summary: "arXiv:2610.23834v1 Announce Type: new Abstract: Parameterized quantum circuits are widely investigated in quantum machine learning, yet how their architecture can provide task-aligned inductive biases"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2610.23834v1 Announce Type: new Abstract: Parameterized quantum circuits are widely investigated in quantum machine learning, yet how their architecture can provide task-aligned inductive biases remains poorly understood. We study data reuploading quantum circuits with two distinct inputs: a signal that varies between samples and a fixed, task-defined spectral query that specifies how the signal should be probed. We show that encoding the query can change the circuit's hypothesis class over the signal by modulating how its existing signal frequencies are combined, without introducing new sample-dependent information. This mechanism matches tasks built on nonuniform Fourier transforms, whose evaluation frequencies specify the query and whose sampling positions guide its encoding. We examine this connection in a classification task inspired by synthetic aperture radar, where acquisition geometry determines a query for classifying unfocused spectral patches before image formation. Across small-scale spectral and radar-like tasks, aligned queries improve learning from limited data over parameter-matched circuits with mismatched or absent queries. These results provide a route from known spectral task structure to the design and validation of inductive biases in parameterized quantum circuits.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.23834) | 2026-10-19
