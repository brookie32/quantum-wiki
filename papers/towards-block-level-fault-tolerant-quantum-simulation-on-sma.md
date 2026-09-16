---
title: "Towards Block-Level Fault-Tolerant Quantum Simulation on Small High-Rate Non-CSS Codes"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.16159"
summary: "arXiv:2609.16159v1 Announce Type: new Abstract: Small high-rate non-CSS stabilizer codes provide compact platforms for encoded quantum computation, but mixed-Pauli checks and limited native transversa"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2609.16159v1 Announce Type: new Abstract: Small high-rate non-CSS stabilizer codes provide compact platforms for encoded quantum computation, but mixed-Pauli checks and limited native transversal logical gates complicate fault-tolerant dynamics. Block-level constructions offer an alternative by mapping an entire logical block to a physical circuit rather than compiling separately protected logical gates. We investigate this approach using the high-rate [[8,3,3]] non-CSS code and logical Trotter circuits as a testbed. We construct flagged syndrome-extraction circuits and establish a circuit-level memory pseudo-threshold near (1.5imes10^{-3}). We then apply our symplectic-transvection construction, which maps a logical Trotter circuit to a physical circuit with the same block pattern for any stabilizer code. Although this mapping preserves the intended unitary algebraically, encoded Trotter circuits exhibit asymmetry between logical-(X) and logical-(Z) failure channels. Single-fault analysis identifies the mechanism: a fault on the shared parity ancilla can propagate through the uncomputation network into an undetectable logical operator, reducing the effective circuit distance in the affected sector. We evaluate flag-conditioned recovery, biased-noise decoding, CliNR resource verification, flag postselection, and asymmetric gate-noise models. These methods suppress propagated faults but do not simultaneously suppress both logical sectors in the realistic configurations studied. A diagnostic protected limit removing the identified malignant first-order locations restores pseudo-threshold behavior in both sectors, approaching memory performance. These results demonstrate the potential of block-level logical constructions for non-CSS codes without rich native transversal gate sets and the joint protection of the parity network, analog rotation, and recovery required to preserve fault-tolerant distance.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.16159) | 2026-09-16
