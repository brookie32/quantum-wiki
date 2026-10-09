---
title: "Merged amplitude encoding for Chebyshev quantum Kolmogorov-Arnold networks"
date: "2026-10-09"
updated: "2026-10-09"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.02818"
summary: "arXiv:2603.02818v4 Announce Type: replace Abstract: Quantum Kolmogorov--Arnold networks evaluate each edge activation function as a quantum inner product, creating a trade-off between qubit count and "
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

arXiv:2603.02818v4 Announce Type: replace Abstract: Quantum Kolmogorov--Arnold networks evaluate each edge activation function as a quantum inner product, creating a trade-off between qubit count and the number of circuit executions per forward pass. We introduce merged amplitude encoding for the Chebyshev-edge classical-to-classical QKAN (CCQKAN), which packs the element-wise products of all n input-edge vectors of an output node into a single amplitude state, reducing circuit executions by a factor of n while using no more qubits than the sequential SWAP-test baseline once its measurement registers are counted. The merged and original circuits compute the same quantity exactly; we characterize what this consolidation costs in trainability. Across 10 network configurations and 16 random seeds, the two circuits are indistinguishable under ideal conditions. Under finite-shot training with a hardware-standard SPSA optimizer at matched measurement budget, the merged circuit incurs a small systematic loss deficit that grows with network width (significant in 6 of 10 configurations), consistent with amplified estimator noise in the merged state; under depolarizing noise no systematic difference is detected. A parameter-matched single-qubit data re-uploading baseline reaches substantially higher loss on the same tasks while using fewer qubits and executions, delineating complementary resource regimes. No quantum advantage is claimed.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.02818) | 2026-10-09
