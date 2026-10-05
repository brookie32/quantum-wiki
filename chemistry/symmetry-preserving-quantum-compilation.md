---
title: "Symmetry-preserving quantum compilation"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03624"
summary: "arXiv:2610.03624v1 Announce Type: new Abstract: Fault-tolerant quantum simulation requires compiling symmetry-preserving time evolutions into discrete gate sets. Standard Clifford+T synthesis can brea"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03624v1 Announce Type: new Abstract: Fault-tolerant quantum simulation requires compiling symmetry-preserving time evolutions into discrete gate sets. Standard Clifford+T synthesis can break continuous symmetries even when the target evolution preserves them, causing compiled simulations to lose essential features of the original system. We develop a fault-tolerant compilation framework that preserves SU(2) symmetry exactly. We characterize the number-theoretic obstruction preventing symmetry-preserving unitary Clifford+T circuits from approximating arbitrary SU(2)-symmetric evolutions and circumvent it using measurement and feed-forward. The resulting synthesis confines compilation errors to the symmetry-preserving operator algebra rather than introducing symmetry-breaking perturbations. We demonstrate the algorithm by simulating transport in the one-dimensional Heisenberg model. At a lower matched T-count, for instance, 54 T gates per two-site Trotter step, standard synthesis yields an incorrect transport exponent, whereas our symmetry-preserving compilation reproduces the expected exponent for the same expected T-count. If instead each approach is allocated whatever resources are necessary to estimate this exponent to the same accuracy, our construction reduces the T-count by approximately a factor of five. We further extend the framework to gauge symmetries in lattice gauge theories and to particle-number and spin symmetries in fermionic models relevant to quantum chemistry and the Fermi-Hubbard model. These results show that symmetry-preserving fault-tolerant compilation can qualitatively change the effects of synthesis error while substantially reducing the resources required for quantum simulation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03624) | 2026-10-05
