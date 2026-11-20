---
title: "Generalizing and Combining Check Constructions: Design-Space Exploration for Fault-Tolerant Quantum State Preparation"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.25107"
summary: "arXiv:2611.25107v1 Announce Type: new Abstract: Fault-tolerant quantum computing needs logical states prepared such that single faults cannot spread into uncorrectable errors. Post-selection achieves "
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2611.25107v1 Announce Type: new Abstract: Fault-tolerant quantum computing needs logical states prepared such that single faults cannot spread into uncorrectable errors. Post-selection achieves this with added checks that detect dangerous faults and discard the run. How the checks are measured sets the depth and operation count of the circuit, and the best trade-off depends on the hardware. Existing automated methods, however, each use one check construction and yield fixed trade-offs. We first introduce Block Checks, in which several checks share one fault-tolerantly prepared auxiliary block, which places them and existing constructions in a single design space. Second, to explore that space, we propose a Pareto tree search that adds checks and auxiliary blocks, merges auxiliaries, and edits the circuit. On quantum codes of distance up to seven, the search finds best-known circuits for many new operation--depth trade-offs and surpasses existing methods. The code is open source as part of the Munich Quantum Toolkit (MQT) at https://github.com/munich-quantum-toolkit/qecc, and all circuits are available in the QECirc library at https://qecirc.com.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.25107) | 2026-11-20
