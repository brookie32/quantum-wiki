---
title: "QASPA-MaxCut on Unweighted Graphs: Edge Encoding and QAOA Restarts"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.06698"
summary: "arXiv:2611.06698v1 Announce Type: new Abstract: Max-Cut is a common testbed for near-term quantum optimization because it has a simple Ising Hamiltonian, established classical baselines, and a paramet"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.06698v1 Announce Type: new Abstract: Max-Cut is a common testbed for near-term quantum optimization because it has a simple Ising Hamiltonian, established classical baselines, and a parameterized quantum circuit whose performance depends on the outer classical optimizer. This paper develops QASPA-MaxCut, a shift-phase circuit for Max-Cut that encodes graph edges through controlled R_y rotations of the form CX_{ij}R_y(heta_{ij})CX_{ij}. We derive the exact two-qubit algebra of the edge block, trace an unweighted four-vertex example, and compare one-layer QASPA-MaxCut with depth-one QAOA by exact state-vector simulation. The protocol uses seed 42, evaluates connected backbone-augmented random graphs with additional-edge probabilities p_{edge}in{0.1,0.3,0.5,0.7}, and adds nineteen custom unweighted topologies. The QASPA-MaxCut score is reported after the algorithm's classical selection stage: the four leading QASPA bit strings are evaluated by the Max-Cut objective, and the best cut is retained. The QAOA score is the expected approximation ratio after local optimization, reported as a best-of-k curve over one to ten restarts. In these small exact simulations, fixed-angle QASPA-MaxCut produces reported group-mean selection ratios between 0.955 and 1.000, the topology-level readout is unchanged in the retained finite-shot checks under the rule lceil 0.03047dot 2^n+1016.2rceil, and depth-one QAOA improves with additional classical restarts while remaining lower than the QASPA selection score in the reported mean summaries. This comparison motivates further study of the classical search budget needed to obtain competitive Max-Cut samples at shallow circuit depth.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.06698) | 2026-11-05
