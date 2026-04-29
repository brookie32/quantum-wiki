---
title: "Networked Realization of Quantum LDPC Codes"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25026"
summary: "arXiv:2604.25026v1 Announce Type: new Abstract: Quantum low-density parity-check (QLDPC) codes with good parameters are promising candidates for low-overhead fault-tolerant quantum computing, but thei"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25026v1 Announce Type: new Abstract: Quantum low-density parity-check (QLDPC) codes with good parameters are promising candidates for low-overhead fault-tolerant quantum computing, but their non-local stabilizers require long-range connectivity and frequent qubit movement, introducing practical challenges. Prior work has studied the networked implementation of topological codes, where each node only holds one or a few qubits of the entire code, and demonstrated competitive performance under practical constraints such as the quality of network-provided entanglement. However, since these codes are already geometrically local, such a networked setting might not be essential. In this work, we propose and study the networked implementation of better QLDPC codes, specifically bivariate bicycle codes due to their similarity to surface codes and the controlled amount of long-range connections in their stabilizers. We begin by recreating networked surface codes in Stim, with one code qubit per node, and provide additional insights into their circuit-level noise performance. We then extend this approach to bipartitions of bivariate bicycle codes, using balanced min-cut partitioning on their combined X-Z Tanner graph to identify optimal qubit splits. For stabilizers spanning nodes, we implement teleported CNOTs and vary the Bell pair fidelity enabling these gates. Through circuit-level noise simulations with BP-OSD decoding, we provide the first insights into networked realizations of these codes and compare their performance with monolithic implementations. We conclude by outlining advantages, limitations, and future directions.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25026) | 2026-04-29
