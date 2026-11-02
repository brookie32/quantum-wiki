---
title: "Resource efficient Sample Based Quantum Simulation through Fragmentation and Virtual Partitioning of QPU"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41986"
summary: "arXiv:2610.41986v1 Announce Type: new Abstract: Present-day sample-based quantum algorithms within quantum-centric supercomputing workflows require substantial classical post-processing, large circuit"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41986v1 Announce Type: new Abstract: Present-day sample-based quantum algorithms within quantum-centric supercomputing workflows require substantial classical post-processing, large circuit depths to produce chemically relevant samples, and long QPU times to execute the many circuits needed for molecules of chemically relevant size. We introduce FMO-QVM-HCI-HSQD, a resource-efficient sample-based framework that breaks a large problem into fragments, runs the fragments in parallel on virtual regions of the QPU, and reduces circuit depth through a half-qubit ansatz whose samples seed an HCI expansion. We demonstrate the algorithm on ibm_marrakesh and ibm_boston for the water trimer and the carmofur_Mpro complex with up to 52 qubits, benchmarking against FMO-CCSD(T), FMO-CASCI and FMO-HCI. For the water trimer (14 spin orbitals for monomers, 28 for dimers), our method reduces the two-qubit depth by 39% compared to FMO-QVM-SQD and the QPU time by 82% compared to sequential FMO-SQD, and accesses 3% of the determinant subspace versus 40% for FMO-SQD, while achieving more accurate energies. For the carmofur_Mpro complex (16 and 32 spin orbitals), it reduces the two-qubit depth by 47% and the QPU time by 20% compared to FMO-QVM-SQD, and accesses 0.007% of the determinant subspace versus 40%, while remaining within chemical accuracy. Extending the carmofur_Mpro active space in the 6-31G basis to 52 and 104 spin orbitals, sampled on 26 and 52 qubits, the total energy deviates from FMO-HCI by only 1.22 mHa. These results show that combining fragmentation, virtual QPU partitioning and half-qubit sampling makes sample-based quantum simulation of chemically relevant systems feasible on current hardware.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41986) | 2026-11-02
