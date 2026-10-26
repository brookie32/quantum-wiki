---
title: "Hardware-Friendly Estimation of LCU-Based Expectation Values via Quantum-to-Classical Workload Shifting"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.32841"
summary: "arXiv:2610.32841v1 Announce Type: new Abstract: Estimating the expectation value of an observable O for a quantum state evolved under a general, possibly non-unitary, operator A is a fundamental task "
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2610.32841v1 Announce Type: new Abstract: Estimating the expectation value of an observable O for a quantum state evolved under a general, possibly non-unitary, operator A is a fundamental task in quantum simulation, chemistry, and variational algorithms. Existing linear-combination-of-unitaries (LCU) approaches implement A on hardware, requiring ancilla qubits, controlled unitaries and, in randomized variants, fresh circuit executions for every Monte Carlo sample. These costs are prohibitive on NISQ and early fault-tolerant devices. We propose HERMES (Hardware-Efficient Reusable Measurements for Estimating LCU-based expectation valueS), which moves the processing of A entirely to the classical domain. Expanding A and O in the Pauli basis and sampling pairs of Pauli terms classically, HERMES rewrites mu = Tr(OArho A^{agger})/Tr(Arho A^{agger}) as a ratio of weighted sums of Pauli expectation values on the unmodified state rho, with no ancillas, controlled unitaries, or quantum implementation of A. A two-level measurement reduction scheme (Pauli deduplication and commuting-group partitioning) bounds the number of distinct measurement settings independently of the sample count, unlike randomized LCU methods whose circuit executions grow linearly with it. On ground-state energy estimation of H_2 and LiH via imaginary-time evolution, HERMES matches or beats Pauli single-ancilla LCU baseline using shallow circuits with no two-qubit gates beyond state preparation under qubit-wise commuting grouping. It is also more robust to noise and completes a noisy LiH simulation infeasible for the baseline, at the cost of classical overhead growing with the number of Pauli terms in A.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.32841) | 2026-10-26
