---
title: "Truncated hybrid tensor networks for distributed quantum simulation"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.16520"
summary: "arXiv:2609.16520v1 Announce Type: new Abstract: Simulation of quantum many-body systems is a principal application of quantum computing, but available devices remain limited by the number of qubits an"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2609.16520v1 Announce Type: new Abstract: Simulation of quantum many-body systems is a principal application of quantum computing, but available devices remain limited by the number of qubits and cannot accommodate systems of the desired size. One approach is to host a large evolution across several modest distributed systems that exchange classical information alone. Current protocols such as circuit knitting incur a quasi-probability sampling cost that grows exponentially with the number of remote gates across the cut, even when physical correlations across the cut are actually bounded. In this work, we present a truncated hybrid tensor network (THTN) framework in which a remote two-body gate is applied as a sum of local unitaries on the subsystems, linked by a classical connecting tensor, and an interface truncation retains Schmidt modes across the cut. Remote gates between the same subsystems can be merged on one connector, so non-one-dimensional models, such as layered partitions with strong intra-layer and weaker interlayer couplings, may be cast onto a one-dimensional cut. The retained non-negative Schmidt coefficients also define a sampling rule for local observables. We validate this distributed protocol by classical simulation against time-evolving block decimation (TEBD) at the same bond dimension. The truncated dynamics track the TEBD references on chains and ladders, with the clearest gain on a layered model.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.16520) | 2026-09-16
