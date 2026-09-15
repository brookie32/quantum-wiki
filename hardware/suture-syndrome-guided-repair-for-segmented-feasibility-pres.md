---
title: "SUTURE: Syndrome-Guided Repair for Segmented Feasibility-Preserving VQAs on Noisy Hardware"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.13935"
summary: "arXiv:2609.13935v1 Announce Type: new Abstract: Constrained binary optimization is a representative class of NP-hard problems in scheduling, resource allocation, and finance. Segmented feasibility-pre"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.13935v1 Announce Type: new Abstract: Constrained binary optimization is a representative class of NP-hard problems in scheduling, resource allocation, and finance. Segmented feasibility-preserving variational quantum algorithms (VQAs) are a promising approach that restricts ideal circuit evolution to feasible assignments and executes short measure-and-reseed segments. The existing boundary runtime enforces feasibility through purification, which discards measurements that violate the constraints. As problem size and noise increase, feasible measurements become rare; if no shot survives, the execution chain terminates. In our 72-qubit graph-coloring experiment on a real-device IBM Heron, 11 of 12 purification chains terminate before completing all segments. We propose SUTURE: syndrome-guided repair, a runtime that repairs infeasible measurements instead of discarding them and is deployable on current quantum devices. SUTURE exploits a parity-check-like structure induced by the problem constraints: violated constraints form a syndrome that detects and localizes corruption and, under suitable structural conditions, often identifies a correction. SUTURE combines three stages: (1) a compile-time profiler that uses the compiled constraints and feasible initialization samples to predict single-flip recovery, with a maximum error of 0.011 across four constraint families; (2) a bounded runtime decoder that replaces purification inside the segmented execution loop; and (3) a regime analysis that identifies when repair is preferable to purification. In simulation up to 120 qubits, SUTURE continues the execution chain far beyond the noise level at which purification collapses. In the same 72-qubit experiment on IBM Heron hardware, SUTURE completes all segments in all 12 runs, and hardware timing experiment, decoding adds 1.6% to execution-path latency and less than 1% to total pipeline latency.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.13935) | 2026-09-15
