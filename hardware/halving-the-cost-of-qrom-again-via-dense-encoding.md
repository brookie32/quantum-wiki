---
title: "Halving the cost of QROM again via dense encoding"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.02321"
summary: "arXiv:2610.02321v1 Announce Type: new Abstract: Quantum read only memory (QROM) is a substantial source of non-Clifford cost in fault-tolerant quantum algorithms. Borrowing dirty qubits can reduce thi"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.02321v1 Announce Type: new Abstract: Quantum read only memory (QROM) is a substantial source of non-Clifford cost in fault-tolerant quantum algorithms. Borrowing dirty qubits can reduce this cost, provided their unknown initial states are restored. We consider the practically relevant qubit-constrained regime, where limited workspace restricts the table-block size and table loading dominates the cost. For N entries of b bits and approximately blambda dirty qubits, SelectSwap has leading Toffoli count 2N/lambda. Recent work using sequential bit packets reduces this to (1+1/b)N/lambda. In this work we introduce a dense encoding construction of QROM, where two bits of classical information are stored in each dirty qubit instead of one by utilizing both the Z and X bases. On its own, dense encoding provides a 2imes improvement over SelectSwap by reducing the leading Toffoli count to N/lambda. Combining it with sequential bit packets gives frac12(1+1/b)N/lambda, a further halving of the sequential construction's leading cost, and an approximately 4imes improvement over SelectSwap in the large-N limit for practical values of b.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.02321) | 2026-10-05
