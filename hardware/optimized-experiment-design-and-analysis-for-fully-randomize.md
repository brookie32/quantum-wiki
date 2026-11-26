---
title: "Optimized experiment design and analysis for fully randomized benchmarking"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2312.15836"
summary: "arXiv:2312.15836v2 Announce Type: replace Abstract: Randomized benchmarking (RB) is a widely used strategy to assess the quality of available quantum gates in a computational context. RB involves appl"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2312.15836v2 Announce Type: replace Abstract: Randomized benchmarking (RB) is a widely used strategy to assess the quality of available quantum gates in a computational context. RB involves applying known random sequences of gates to an initial state and using the statistics of a final measurement step to determine an effective depolarizing error per step of the sequence, which is a metric of gate quality. Here we investigate the advantages of fully randomized benchmarking, where a new random sequence is drawn for each experimental trial. The advantages of full randomization include smaller confidence intervals on the inferred step error, the ability to use maximum likelihood analysis without heuristics, straightforward optimization of the sequence lengths, and the ability to model and measure behaviors that go beyond the typical assumption of time-independent error rates. We discuss models of time-dependent or non-Markovian errors that generalize the basic RB model of a single exponential decay of the success probability. For any of these models, we implement a concrete protocol to minimize the uncertainty of the estimated parameters given a fixed time constraint on the complete experiment, and we implement a maximum likelihood analysis. We consider several previously published experiments and determine the potential for improvements with optimized full randomization. We experimentally observe such improvements in Clifford randomized benchmarking experiments on a single trapped ion qubit at the National Institute of Standards and Technology (NIST). For an experiment with uniform lengths and intentionally repeated sequences the step error was 2.42^{+0.30}_{-0.22}imes 10^{-5}, and for an optimized fully randomized experiment of the same total duration the step error was 2.57^{+0.07}_{-0.06}imes 10^{-5}. We find a substantial decrease in the uncertainty of the step error as a result of optimized fully randomized benchmarking.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2312.15836) | 2026-11-26
