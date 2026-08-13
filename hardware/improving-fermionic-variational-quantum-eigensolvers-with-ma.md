---
title: "Improving fermionic variational quantum eigensolvers with Majorana swap networks"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.07855"
summary: "arXiv:2509.07855v2 Announce Type: replace Abstract: Simulating computationally hard fermionic systems is a promising application of quantum computing. However, mapping nonlocal fermionic operators to "
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2509.07855v2 Announce Type: replace Abstract: Simulating computationally hard fermionic systems is a promising application of quantum computing. However, mapping nonlocal fermionic operators to qubits often produces deep circuits, rendering such simulations impractical on near-term hardware. We introduce two Majorana swap network compilation strategies for variational quantum eigensolvers that reduce circuit depth and two-qubit gate count. First, we develop a cyclic compilation algorithm that localizes all two-particle interaction terms in a general fermionic Hamiltonian containing up to O(M^4) such terms using only O(M^3) auxiliary Majorana-swap transpositions, where M is the number of fermionic modes. Here, the cubic scaling refers to auxiliary routing; a complete UCCGSD ansatz still contains O(M^4) double-excitation rotations. Second, we design a Majorana swap network for the k-UpCCGSD variational ansatz, which is already more compact than UCCGSD. In this setting, our network yields constant-factor reductions of approximately 50 % in circuit depth and 20 % in two-qubit gate count under all-to-all connectivity. For the more restricted 2imes N connectivity, the reductions are larger --- about 55 % in circuit depth an 40 % in gate count. These structural improvements are accompanied by improved robustness in numerical noise simulations on the small molecular instances tested.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.07855) | 2026-08-13
