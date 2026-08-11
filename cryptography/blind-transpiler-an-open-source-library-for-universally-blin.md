---
title: "Blind Transpiler: An open-source library for universally blind and homomorphic quantum computations"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.17131"
summary: "arXiv:2607.17131v2 Announce Type: replace Abstract: Blind quantum computation is a cryptographic primitive that allows a limited-capability client to delegate its complex computation to a remote serve"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2607.17131v2 Announce Type: replace Abstract: Blind quantum computation is a cryptographic primitive that allows a limited-capability client to delegate its complex computation to a remote server without revealing its data and/or computation. This branch of quantum cryptography has been bifurcated into two distinct primitives, quantum homomorphic encryption (concerning the security of only data) and universal blind quantum computation (concerning the security of data and the computing algorithm). These primitives have immense applicability in problems like secure cloud computing, secure quantum variational algorithms, quantum federated learning, and secure multiparty computation. However, no software tools exist for the rapid prototyping of such protocols, hindering the academic interrogation for potential applications. In this paper, we describe the development of the first such library for transpiling circuits written in Qiskit to its blind counterpart, which can then be delegated in a client-server architecture without revealing the client's data and/or computation. The proposed library is designed in modular and reusable component layers, enabling easier scalability to newer BQC primitives and robustness against changes in underlying primitives. We show the implementation of these primitives to a blind variational quantum classifier for the IRIS dataset.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.17131) | 2026-08-11
