---
title: "Extremely Low-Cost Magic State Preparation toward Fault-Tolerant Quantum Computing"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.12698"
summary: "arXiv:2609.12698v1 Announce Type: new Abstract: Fault-tolerant preparation of non-Clifford resource states is a major contributor to the overhead of quantum computation, motivating protocols that achi"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2609.12698v1 Announce Type: new Abstract: Fault-tolerant preparation of non-Clifford resource states is a major contributor to the overhead of quantum computation, motivating protocols that achieve high output fidelity with minimal qubit and circuit costs. We introduce a low-cost magic-state preparation protocol in which the choice of stabilizer generators is co-designed with the flag gadgets, allowing the syndrome-extraction circuit itself to filter correlated faults across a non-Clifford layer. The protocol prepares a logical plus state in the 15-qubit quantum Reed-Muller code, applies a transversal T gate, and gauge-fixes the same register into the seven-qubit Steane code. By reorganizing equivalent Z-type stabilizer generators into jointly flagged measurement groups, the protocol eliminates all accepted logical-error contributions arising from one or two circuit faults under destructive error detection. Under a uniform circuit-level depolarizing noise model, the postselected infidelity is 210.2p^3+O(p^4). At p=10^{-3}, exact low-order enumeration combined with stratified sampling bounds the infidelity by 2.2imes10^{-7} at 99.9% joint confidence, while retaining an acceptance probability of 86.9%. The complete circuit requires only 19 qubits and 82 CNOT gates. These results demonstrate that stabilizer-generator design can substantially reduce the cost of postselected magic-state preparation, although corrected operation and the fidelity of an unmeasured output block require separate analysis.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.12698) | 2026-09-14
