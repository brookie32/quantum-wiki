---
title: "Molecular Ground State Simulation by Subspace Restriction and Hund's Rule"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2404.03268"
summary: "arXiv:2404.03268v4 Announce Type: replace Abstract: The Subspace Restriction Scheme (SRS) is presented to address the qubit and resource constraints of molecular simulation on near-term quantum hardwa"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2404.03268v4 Announce Type: replace Abstract: The Subspace Restriction Scheme (SRS) is presented to address the qubit and resource constraints of molecular simulation on near-term quantum hardware. SRS restricts a molecular Hamiltonian to a selected determinant subspace before qubit encoding, so a D-dimensional subspace requires only q=lceillog_2Drceil qubits. We apply SRS to the established seniority-resolved Multi-Hund Subspaces MHS(Omega) and develop compact encodings for these sectors. At fixed seniority and filling fraction, MHS asymptotically uses about half as many qubits as a compact particle-conserving encoding. For the H_{22} chain, the register shrinks from 44 to 20 qubits. Compression can nevertheless increase Pauli-operator density and does not always reduce measurement cost. In noiseless VQE benchmarks, shallow circuits reach within 1.6~mHa of the exact subspace minima using only 4--30 CNOT gates. However, the corresponding subspace minima for LiH, HF, OH, and CH remain 4.39--9.73~mHa above FCI. Full-space UCCSD reaches chemical accuracy but requires hundreds to thousands of CNOT gates. SRS therefore provides a controlled resource--accuracy trade-off when register width is the binding constraint and the target state is well represented within a selected seniority sector.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2404.03268) | 2026-10-19
