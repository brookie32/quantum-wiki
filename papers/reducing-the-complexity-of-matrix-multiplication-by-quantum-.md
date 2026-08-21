---
title: "Reducing the Complexity of Matrix Multiplication by Quantum Computing"
date: "2026-08-21"
updated: "2026-08-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.05541"
summary: "arXiv:2602.05541v3 Announce Type: replace Abstract: Matrix multiplication is a fundamental operation in compute-intensive tasks and a key component of modern quantum acceleration frameworks. Here we p"
last_verified: "2026-08-21"
review_by: "2026-11-19"
stale: false
---

arXiv:2602.05541v3 Announce Type: replace Abstract: Matrix multiplication is a fundamental operation in compute-intensive tasks and a key component of modern quantum acceleration frameworks. Here we present a quantum matrix multiplication algorithm based on quantum kernels (QKMM), achieving an elementary gate complexity of (O(N^2log_2N)), with amplitude encoding overhead explicitly included and without assuming a QRAM oracle. This scaling is asymptotically lower than that of the best-known classical matrix multiplication algorithm (O(N^{2.371339})). Building upon QKMM, we establish a family of quantum linear algebra operators, including Quantum Vector Inner Product (V{scriptstyle 2}V), Quantum Vector-Matrix Multiplication (V{scriptstyle 2}M), QKMM (M{scriptstyle 2}M), Quantum One-to-Many Matrix Multiplication(O{scriptstyle 2}M) and Quantum Sequential Matrix Multiplication (SMM), providing a unified framework from vector operations to parallel and sequential matrix transformations. Through noiseless simulations, realistic noise modelling and experiments on a superconducting quantum processor, we systematically characterize the numerical accuracy, resource requirements and hardware execution limits of this operator framework. Furthermore, we integrate SMM into deep neural-network inference, enabling intermediate features to propagate coherently across layers without repeated measurement and re-encoding. These results establish a pathway from quantum circuit-level algorithm design to end-to-end coherent computation, providing a quantum computing framework for matrix-centric compute-intensive applications.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.05541) | 2026-08-21
