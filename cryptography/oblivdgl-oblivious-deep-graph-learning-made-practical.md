---
title: "OblivDGL: Oblivious Deep Graph Learning Made Practical"
date: "2026-10-27"
updated: "2026-10-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2655"
summary: "The rapid deployment of Graph Neural Networks (GNNs) within Machine Learning as a Service (MLaaS) has opened up new privacy concerns. Both sensitive graph data and proprietary GNN models are submitted"
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

The rapid deployment of Graph Neural Networks (GNNs) within Machine Learning as a Service (MLaaS) has opened up new privacy concerns. Both sensitive graph data and proprietary GNN models are submitted to and processed in third-party MLaaS platform for training and inference. To alleviate those concerns, recent efforts have been made to design tailored secure computation protocols for GNNs. Unfortunately, existing designs cannot accomplish security, functionality, and scalability simultaneously. They leak a certain degree of graph information, offer limited support on secure training of GNNs, and can hardly scale to large graphs. In this paper, we design and implement OblivDGL, an oblivious deep graph learning framework for secure GNN inference and training. Our design is inspired by Deep Graph Library (DGL), an industrial practice for graph learning. At its core, we distill the secure computational patterns of GNNs into a generalized form, and empower both secure GNN training and inference through a novel oblivious message passing paradigm. To realize such a paradigm, we design a new oblivious graph representation, and realize it by function secret sharing (FSS), a lightweight secure computation technique with low latency. Compared to prior secure GNN systems, OblivDGL achieves the most stringent privacy guarantees, i.e., revealing no private information except for the total number of edges and nodes. One standout feature of OblivDGL is the scalability of processing encrypted graphs by carefully tailored parallelization designs. Extensive evaluations on four benchmark graph datasets demonstrate that, compared to state-of-the-art secure GNN frameworks, OblivDGL reduces communication cost by up to 1024x and achieves up to 14.3x speedup in runtime during secure training. For secure inference, OblivDGL achieves up to 754x lower communication and a 4.19x speedup.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2655) | 2026-10-27
