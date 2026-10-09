---
title: "Quickly extracting fidelity decay rates in random circuit benchmarking experiments"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.11540"
summary: "arXiv:2610.11540v1 Announce Type: new Abstract: Randomized benchmarking (RB) with structured circuits is experimentally scalable, but gives biased short-depth fidelity estimates because incomplete ens"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2610.11540v1 Announce Type: new Abstract: Randomized benchmarking (RB) with structured circuits is experimentally scalable, but gives biased short-depth fidelity estimates because incomplete ensemble mixing introduces transient modes. Waiting for these transients to decay in deeper circuits can push the signal below the noise floor. This is a well-established obstacle, e.g. in linear cross-entropy benchmarking (LinXEB). Here we overcome this obstacle solely through classical post-processing. We introduce a one-parameter family of estimators that interpolate between the standard LinXEB-type post-processing and a new post-processing technique we call the trace filter function. Under practical assumptions, the trace filter function provably suppresses transient modes, exposing an interpretable fidelity decay at short depth, with theoretical guarantees comparable to standard RB, at the cost of an increased variance. We bound the variance, analyze the evaluation complexity of the new estimators, and develop practical post-processing algorithms. Experiments on a Rigetti superconducting processor validate the method for one-dimensional circuits of up to 12 qubits: where the standard estimator requires depth beyond a 40-layer experimental window, the trace filter function yields consistent estimates below 10 layers. Trace-filtered randomized benchmarking therefore extends reliable fidelity characterization to relevant structured circuit ensembles and short-depth regimes that are inaccessible to conventional estimators.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.11540) | 2026-10-09
