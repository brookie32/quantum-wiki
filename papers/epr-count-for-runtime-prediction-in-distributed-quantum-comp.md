---
title: "EPR Count for Runtime Prediction in Distributed Quantum Computing"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39851"
summary: "arXiv:2609.39851v1 Announce Type: cross Abstract: EPR-pair consumption is commonly used as a communication-cost objective in distributed quantum computing, but minimizing EPR cost does not necessarily"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39851v1 Announce Type: cross Abstract: EPR-pair consumption is commonly used as a communication-cost objective in distributed quantum computing, but minimizing EPR cost does not necessarily minimize distributed execution time. Despite its widespread use, the reliability of EPR count as a runtime surrogate has received limited direct characterization across different workloads and communication conditions. This work addresses this gap by systematically evaluating the relationship between EPR cost and runtime over all balanced two-QPU mappings of QFT, QAOA, and CDKM circuits. The results show that mappings with identical EPR cost can have substantially different execution times, lower-EPR mappings can be slower, and minimum-EPR mappings can be runtime-suboptimal. The reliability of EPR count is strongly workload dependent and also changes with the communication operating regime: increasing EPR-generation latency amplifies runtime differences hidden by equal EPR cost, while increased communication concurrency can reduce the ability of EPR count to preserve runtime ordering. These results show that EPR count and execution time are related but distinct optimization objectives, and identify regimes in which explicit communication-aware runtime modeling is necessary.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39851) | 2026-10-01
