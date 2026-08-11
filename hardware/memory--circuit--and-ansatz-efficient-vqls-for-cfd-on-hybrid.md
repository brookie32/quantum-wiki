---
title: "Memory-, Circuit-, and Ansatz-Efficient VQLS for CFD on Hybrid Quantum-HPC Systems"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.09661"
summary: "arXiv:2608.09661v1 Announce Type: new Abstract: Fluid dynamics workloads are dominated by repeated solves of large, structured linear systems, motivating the search for quantum acceleration. The Varia"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.09661v1 Announce Type: new Abstract: Fluid dynamics workloads are dominated by repeated solves of large, structured linear systems, motivating the search for quantum acceleration. The Variational Quantum Linear Solver (VQLS) is a leading near-term candidate, but practical deployment on hybrid quantum--high--performance computing (HPC) systems faces three persistent challenges: (i) the linear-combination-of-unitaries (LCU) encoding of the system matrix explodes in memory and runtime as the problem size grows, (ii) ansatz selection is largely empirical, with no clear link between standard circuit metrics and solver convergence, and (iii) end-to-end VQLS pipelines have rarely been exercised on production HPC hardware at non-trivial qubit counts. This work addresses these challenges through three contributions. First, we benchmark four matrix-encoding strategies---naive LCU, PennyLane-integrated, Fast Walsh--Hadamard Transform (FWHT)-based parallel Pauli decomposition, and an singular value decomposition (SVD)-based two-term LCU---and show that the FWHT approach reduces peak memory by up to 1298imes on an 11imes 11 Hele--Shaw grid, while the SVD-based coherent VQLS delivers over 10{,}000imes per-iteration speedup over standard Pauli-based VQLS at 8 qubits. Second, we evaluate 11 ansatz families with gradient-free and gradient-based optimizers on canonical Hele--Shaw flow, and find that expressibility and entanglement metrics correlate only weakly with VQLS convergence, motivating problem-aware ansatz design. Third, we deploy the full workflow on the OLCF Frontier supercomputer and successfully simulate a 15-qubit tridiagonal Toeplitz system on a single node. Together, these results establish a practical baseline for VQLS in hybrid quantum--HPC computation fluid dynamic (CFD) workflows and identify the remaining bottlenecks for larger problems.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.09661) | 2026-08-11
