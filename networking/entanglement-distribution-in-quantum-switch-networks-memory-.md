---
title: "Entanglement Distribution in Quantum Switch Networks: Memory Limits and Achievability"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.28596"
summary: "arXiv:2610.28596v1 Announce Type: cross Abstract: We study the minimum persistent memory required to distribute a graph state through a quantum switch. Specifically, consider a central switch that ass"
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2610.28596v1 Announce Type: cross Abstract: We study the minimum persistent memory required to distribute a graph state through a quantum switch. Specifically, consider a central switch that assists n remote users in distributing a graph state, using independently generated user-switch Bell pairs. Since Bell-pair generation is probabilistic, different links generally succeed at different times. When a Bell-pair is generated, the qubits may need to be stored in memory while waiting for other links to succeed. Recently, new protocols have been proposed to reduce this storage overhead by processing and releasing some switch qubits before all Bell links are available. However, these protocols do not characterize the minimum persistent switch memory required at each stage. Moreover, the local-cover method in the state-of-the-art Piecemaker protocol is computationally expensive for general target graphs. In this work, we characterize the minimum persistent switch memory required after any subset of users' Bell links are generated and processed. We then develop an online stabilizer-transition protocol that attains this limit, which can be implemented in polynomial time in the number of qubits n. Remarkably, this optimal protocol can provide substantial memory reductions over existing heuristic approaches. In particular, for the path graph P_n over n users, Piecemaker protocol requires at least lfloor n/2rfloor qubits of peak persistent memory for extit{every Bell-links generation order}, whereas under the order (1,2,ldots,n), our protocol requires only one persistent switch qubit. Finally, the same stabilizer-transition framework also provides a direct forward construction for sequential graph-state generation using the minimum number of quantum emitters, equal to the maximum of the height function.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.28596) | 2026-10-21
