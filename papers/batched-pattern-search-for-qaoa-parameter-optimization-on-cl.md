---
title: "Batched pattern search for QAOA parameter optimization on cloud-accessed quantum hardware"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.13669"
summary: "arXiv:2609.13669v1 Announce Type: new Abstract: On a cloud-accessed quantum processor the classical optimizer of a variational algorithm communicates with the device through submitted jobs, and each j"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.13669v1 Announce Type: new Abstract: On a cloud-accessed quantum processor the classical optimizer of a variational algorithm communicates with the device through submitted jobs, and each job carries a queueing and turnaround overhead that does not depend on how many circuits it contains. We study a simple consequence of this for the quantum approximate optimization algorithm (QAOA). An optimizer whose next set of trial parameters is known before any result returns can evaluate the whole set in one job, whereas a sequential optimizer such as COBYLA spends one job per function evaluation. We compare a batched pattern search with COBYLA on IBM's ibmfez processor for cardinality-constrained portfolio selection with six to twelve assets, giving both optimizers the same number of jobs and the same number of shots. At every size the batched search reaches, after its first job, a parameter quality that the serial optimizer takes several jobs to match, and the two methods converge to comparable final values; repeating the eight-asset comparison from four starting points gives the same ordering each time. The instances are small enough to be solved exactly, which lets us check that the device's output distribution is correlated with the true ranking of portfolios and is clearly separated from a control circuit of the same depth with the cost layer removed. A short scan over circuit depth at classically optimal parameters shows that on this device the measured solution quality peaks at two or three QAOA layers. The protocol is described in enough detail to be reproduced, and the notebooks and raw counts are released.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.13669) | 2026-09-15
