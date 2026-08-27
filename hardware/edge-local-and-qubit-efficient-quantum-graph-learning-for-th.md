---
title: "Edge-Local and Qubit-Efficient Quantum Graph Learning for the NISQ Era"
date: "2026-08-27"
updated: "2026-08-27"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.16018"
summary: "arXiv:2602.16018v3 Announce Type: replace Abstract: Graph neural networks (GNNs) are a powerful framework for learning representations from graph-structured data, but their direct implementation on ne"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

arXiv:2602.16018v3 Announce Type: replace Abstract: Graph neural networks (GNNs) are a powerful framework for learning representations from graph-structured data, but their direct implementation on near-term quantum hardware remains challenging due to circuit depth, multi-qubit interactions, and qubit scalability constraints. In this work, we introduce a hybrid quantum graph learning architecture designed explicitly for unsupervised learning in the noisy intermediate-scale quantum (NISQ) regime. Our approach combines a variational quantum feature extraction layer with an edge-local and qubit-efficient quantum message-passing mechanism inspired by the Quantum Alternating Operator Ansatz (QAOA) framework. The message-passing operation is decomposed into pairwise interactions along graph edges using standard single- and two-qubit gates. For a graph with N nodes and n-qubit feature registers, this reduces the number of qubits required at one time from Nn to at most 2n. We train the model using the Deep Graph Infomax objective to perform unsupervised node representation learning. The external class labels are not used during graph construction or training and are used only to evaluate the learned embeddings. Experiments on the Cora citation network and the Phase 3 release of the 1000 Genomes Project show that the quantum edge interaction contributes to the quality of the learned node representations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.16018) | 2026-08-27
