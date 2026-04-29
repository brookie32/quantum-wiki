---
title: "INJEQT: Improved Magic-State Injection Protocol for Fault-Tolerant Quantum Extractor Architectures"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25094"
summary: "arXiv:2604.25094v1 Announce Type: new Abstract: Near-term FTQC system designs are constrained by limited error budgets and largely sequential execution of non-Clifford gates. As a result, reducing the"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25094v1 Announce Type: new Abstract: Near-term FTQC system designs are constrained by limited error budgets and largely sequential execution of non-Clifford gates. As a result, reducing the number of the most-error prone instructions becomes critical for successful program execution. In this work, we study the extractor architecture, a recently proposed FTQC design that enables universal quantum computation on spatially-efficient QEC codes such as the BB code family. In these architectures, over 90% of the total program error arises from the synthillation process, which involves lvert Trangle-state preparation and injection to implement non-Clifford gates. We observe that standard Rz synthillation requires multiple sequential lvert Trangle-state injections, each incurring an inter-module measurements, the most expensive instruction in the architecture, which cumulatively dominate the overall error budget. To address this bottleneck, we propose INJEQT, a 2-factory design that uses an auxiliary code capable of synthesizing Rz(heta) states with lower error rates. These states are then injected into the extractor modules using only a constant number of inter-module measurements. This approach reduces overall error rates by up to 22imes. We further reduce the time overhead by a pre-fetching strategy that prepares the Rz states and their correction states in parallel. This approach improves the wall-clock time by up to 13imes and reduces the space-time cost by up to 7.2imes, for an optimal choice of the number of INJEQT factories for each metric. We evaluate INJEQT for multiple state preparation techniques such as distillation, cultivation and STAR, and model the execution times for both lattice surgery-based and transversal CNOT based injections. Our results demonstrate that INJEQT is robust across factory choices and device technologies, enabling more efficient architectural designs for FTQC.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25094) | 2026-04-29
