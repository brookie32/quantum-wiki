---
title: "A quantum annealing approach to the minimum distance problem of quantum codes"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2404.17703"
summary: "arXiv:2404.17703v4 Announce Type: replace Abstract: Quantum error-correcting codes (QECCs) are at the heart of fault-tolerant quantum computing. As the size of quantum platforms is expected to grow, o"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2404.17703v4 Announce Type: replace Abstract: Quantum error-correcting codes (QECCs) are at the heart of fault-tolerant quantum computing. As the size of quantum platforms is expected to grow, one of the open questions is to design new optimal codes of ever-increasing size. A related challenge is to certify the quality of a given code by evaluating its minimum distance, a quantity characterizing code's capacity to preserve quantum information. This problem is known to be NP-hard. Here we propose to harness the power of contemporary quantum platforms to address this question, and in this way help design quantum platforms of the future. Namely, we introduce an approach to compute the minimum distance of quantum stabilizer codes by reformulating the problem as a Quadratic Unconstrained Binary Optimization (QUBO) problem and leveraging established QUBO algorithms and heuristics as well as quantum annealing (QA) to address the latter. The reformulation as a QUBO introduces only a logarithmic multiplicative overhead in the required number of variables. We demonstrate the formulation using the D-Wave Advantage 4.1 quantum annealer and the hybrid quantum-classical algorithm Qbsolv, and benchmark the resulting QUBO-based implementations against specialized classical distance-finding methods. The QA- and SA-assisted implementations show broadly comparable performance, while the classical comparison clarifies the relative strengths of heuristic optimization and exact distance certification. Our results establish a solver-independent QUBO formulation with only a logarithmic multiplicative overhead in the number of variables and characterize connectivity and minor embedding as central limitations of its present implementation on quantum-annealing hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2404.17703) | 2026-10-15
