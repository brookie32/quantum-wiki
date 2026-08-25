---
title: "How Far Can You Do Nothing On a Quantum Computer?"
date: "2026-08-25"
updated: "2026-08-25"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.21904"
summary: "arXiv:2608.21904v1 Announce Type: new Abstract: We present a route-resolved comparative assessment of Rigetti's Cepheus-1-108Q and IBM Heron-r2 processors using the established 'do-nothing' state-tran"
last_verified: "2026-08-25"
review_by: "2026-11-23"
stale: false
---

arXiv:2608.21904v1 Announce Type: new Abstract: We present a route-resolved comparative assessment of Rigetti's Cepheus-1-108Q and IBM Heron-r2 processors using the established 'do-nothing' state-transfer protocol. Rather than proposing a new protocol, we use this deterministic, low-complexity task as a high-resolution spatial probe. For each evaluated initial qubit, we report two complementary quantities: the largest tested radius within which every evaluated shortest route satisfies the operational success rule, and the longest successful route identified within the evaluated route family. To achieve this, we address a deceptively simple yet foundational question: ``How far can you do-nothing on a quantum computer?'' Operationally, this do-nothing protocol serves as a fundamental state transfer protocol: we prepare an initial quantum state, route it across the physical qubits using SWAP gates, and measure the final state fidelity against the well-established classical fidelity limit for single-qubit state transfer. While this trivial state-transfer protocol serves as the most intuitive baseline, actively preserving a quantum state across a physical lattice proves to be a non-trivial task that exposes the information to cumulative relaxation, dephasing, and environmental cross-talk. In the highlighted IBM QPU case, we identify an isotropic radius of 10 and a successful path of swap distance 27, whereas the highlighted Rigetti Cepheus case exhibits an isotropic radius of 1 but selected above-threshold routes reaching swap distance 8. These results reveal a sharp distinction between uniform spatial reliability and best-route performance. The presented quantities are empirical and conditional on the evaluated route families, finite-shot decision rule, calibration state, and execution time; they are not architecture-wide constants.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.21904) | 2026-08-25
