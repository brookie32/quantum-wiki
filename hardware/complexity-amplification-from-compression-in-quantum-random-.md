---
title: "Complexity Amplification from Compression in Quantum Random Access Optimization"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.07090"
summary: "arXiv:2609.07090v2 Announce Type: replace Abstract: Compressed quantum encodings aim to overcome hardware limitations towards tackling challenging problems at scale, with many classical variables mapp"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.07090v2 Announce Type: replace Abstract: Compressed quantum encodings aim to overcome hardware limitations towards tackling challenging problems at scale, with many classical variables mapped onto noncommuting observables of fewer qubits. Classically, relaxations such as the semidefinite program formulation of MaxCut trade solution quality for computational efficiency. By contrast, quantum relaxations based on compression can amplify the worst-case complexity of the problem being solved. We study quantum random access optimization (QRAO), a special case of the Pauli correlation encoding (PCE) framework that assigns up to three binary variables to the Pauli X, Y, and Z observables of each qubit, with the packing choices determining the compressed Hamiltonian to be optimized. We identify explicit QRAO optimal energy promise problems complete for NP, StoqMA, and QMA, with inverse-polynomial promise gaps for the latter two. Our problem reductions preserve inverse-polynomial promise gaps without requiring gadgets or ancillas. For any prescribed packing, we show that weighted MaxCut instances compress, up to a known shift and rescaling, to arbitrary nonnegative-weight pairwise Pauli couplings allowed by the packing. For QRAO, using one aligned axis gives an NP-complete energy problem. Using two or three positive aligned Pauli axes generally gives QMA-complete problems, with bipartite restrictions in BQP ap StoqMA. We show that this computational hardness survives compilation and is practically relevant. Notably, this result applies directly to the current QRAO compiler implementation in Qiskit Optimization 0.7.0, confirming our hardness results are not artifacts of artificial or contrived packing rules. Altogether our results identify worst-case complexity barriers arising from quantum compression, while making no broad claims about typical cases or the performance and trainability of algorithm pipelines that use it.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.07090) | 2026-10-01
