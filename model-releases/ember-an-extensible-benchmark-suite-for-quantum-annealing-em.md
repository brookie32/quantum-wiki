---
title: "Ember: An Extensible Benchmark Suite for Quantum Annealing Embedding Algorithms"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "model-releases"
tags: [model-releases, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25433"
summary: "arXiv:2604.25433v1 Announce Type: new Abstract: Minor embedding is a required compilation step for quantum annealing, mapping logical problem graphs onto sparse hardware topologies. Despite its centra"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25433v1 Announce Type: new Abstract: Minor embedding is a required compilation step for quantum annealing, mapping logical problem graphs onto sparse hardware topologies. Despite its central role in determining solution quality, no standardized benchmark exists for comparing embedding algorithms: prior studies use incompatible graph libraries, inconsistent metrics, and non-reproducible experimental setups, making cross-algorithm comparisons unreliable. We present Ember (Embedding Minor Benchmark for Evaluative Reproducibility), an open-source benchmarking framework addressing this gap. Ember provides a standardized algorithm interface with seeded, reproducible execution infrastructure; a diverse graph library of 24,016 instances spanning structured, random, and physics-motivated problem types not previously used in embedding benchmarks; and a unified analysis pipeline supporting all three current D-Wave hardware topologies (Chimera, Pegasus, Zephyr). We evaluate five algorithms across the full library on Chimera and find that no algorithm dominates universally: rankings vary systematically with graph structure, and the best algorithm depends on the family being embedded. We also examine the effects of hardware topology (including Pegasus and Zephyr), qubit error rates, and evaluate a reinforcement-learning approach (CHARME) within a narrower test set. Ember is available at https://github.com/zachmacsmith/ember and is installable via pip install ember-qc.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25433) | 2026-04-29
