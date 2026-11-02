---
title: "Testing hardware quantum machine learning claims with a null circuit: fill prediction on Binance futures with 129 qubits of an IBM Heron processor"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41268"
summary: "arXiv:2610.41268v1 Announce Type: new Abstract: Quantum processors are now used as feature generators for classical models on tabular data. A circuit encodes each record, the device returns expectatio"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41268v1 Announce Type: new Abstract: Quantum processors are now used as feature generators for classical models on tabular data. A circuit encodes each record, the device returns expectation values, and a classical model learns from them. A recent report claimed large gains from such features, gains that appeared only on noisy hardware. These claims are hard to check, because a quantum device is not a static function. Its state changes from job to job and from one calibration to the next, and that drift can leak information about the outcome into the features. We propose a five-step protocol for testing claims of this kind. It runs a circuit that carries no data in the same jobs as the real one. It checks whether the hardware leaves a recognizable mark on each job. It compares random and natural assignments of records to jobs, replays the null results under other submission orders, and closes the leak with a job-purged backtest. We apply it, pre-registered, to the HSBC and IBM study of fill probabilities in bond trading, which reported a large hardware-only gain. We use a public analog task and run the study's circuit on a 129-qubit chain of an IBM Heron processor. Under controlled assignment the hardware features give no gain over classical features, and the device reproduces the ideal features about as well as shot noise allows. Yet every job carries a distinct fingerprint. A circuit with no data at all predicts fills well above chance when records are batched by outcome and the same job sits on both sides of the train/test split. Removing that overlap removes the effect. The protocol costs under an hour of processor time and is designed for any hardware feature or kernel pipeline on tabular data.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41268) | 2026-11-02
