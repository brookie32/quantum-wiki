---
title: "Ultra-high-distance quantum memories from amplified qLDPC codes"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.37231"
summary: "arXiv:2609.37231v1 Announce Type: new Abstract: A large code distance does not by itself guarantee a well-protected quantum memory, as faults during syndrome extraction can propagate into correlated d"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.37231v1 Announce Type: new Abstract: A large code distance does not by itself guarantee a well-protected quantum memory, as faults during syndrome extraction can propagate into correlated data errors. Certifying circuit distance becomes demanding as circuits grow. In this work, we introduce distance amplifiers, a modular approach to increasing both code distance and certified circuit-level protection in quantum low-density parity-check codes. The construction tensors a base code with an amplifier, adapting their syndrome-extraction circuits to the amplified code. To certify the resulting memory, we develop a fault-response certificate that yields rigorous lower bounds on circuit distance. Suitable gate ordering and flag qubits control correlated errors, allowing us to establish explicit conditions under which the amplified circuit distance equals the product of the constituent circuit distances. We prove this multiplicative relation for three types of amplifiers: the flagged [[4,2,2]], hypergraph-product, and rotated surface codes. The certificate extends recursively, so the circuit distance multiplies exactly at every amplification step. For example, four successive applications of the flagged [[4,2,2]] amplifier to a [[18,4,4]] seed yield a [[13320,64,64]] code with the circuit distance d_{circ} geq 48 and check weights w leq 14. We further show how individual logical qubits can be tracked explicitly through amplification. By enabling high-distance quantum memories to be built and certified from smaller building blocks, our framework offers a systematic route toward scalable fault-tolerant quantum computing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.37231) | 2026-09-30
