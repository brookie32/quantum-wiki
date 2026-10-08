---
title: "Quantum Optimization of the Color-of-Money Problem on IBM Quantum Hardware: A Proof-of-Concept Study"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.09798"
summary: "arXiv:2610.09798v1 Announce Type: new Abstract: The Color-of-Money (CoM) problem is a financial optimization challenge in which enterprises must determine how to allocate and route funds across multip"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.09798v1 Announce Type: new Abstract: The Color-of-Money (CoM) problem is a financial optimization challenge in which enterprises must determine how to allocate and route funds across multiple accounts, currencies, and time periods while satisfying regulatory, operational, and liquidity constraints. As the number of assets, obligations, and planning periods increases, the decision space grows rapidly, making large-scale optimization increasingly challenging for classical approaches. In this work, we present a proof-of-concept quantum implementation of the CoM problem using IBM Quantum hardware. The original optimization problem is formulated as a constrained Mixed-Integer Linear Programming (MILP) problem and transformed into a Quadratic Unconstrained Binary Optimization (QUBO) representation suitable for quantum execution. We employ a Variational Quantum Algorithm (VQA) with Pauli Correlation Encoding (PCE), a qubit efficient encoding technique and apply error-mitigation technique to improve solution fidelity on noisy quantum hardware. A prototype instance consisting of 3 assets, 3 obligations, and 2 time periods was executed on real IBM quantum hardware and benchmarked against classical exact solver SCIP. The quantum approach successfully reproduced the same optimal solution obtained classically, validating the correctness and feasibility of the proposed methodology. While current noisy quantum hardware does not outperform classical optimization on the evaluated small instance, the results demonstrate the feasibility of executing treasury optimization workloads on current quantum hardware and provide a foundation for future investigations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.09798) | 2026-10-08
