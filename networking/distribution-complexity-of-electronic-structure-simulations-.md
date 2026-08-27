---
title: "Distribution Complexity of Electronic Structure Simulations on Quantum Supercomputers"
date: "2026-08-27"
updated: "2026-08-27"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.20805"
summary: "arXiv:2606.20805v2 Announce Type: replace Abstract: Efficient simulation of strongly-interacting fermionic systems on quantum processing units (QPUs) is a challenging task due to nonlocal mode entangl"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

arXiv:2606.20805v2 Announce Type: replace Abstract: Efficient simulation of strongly-interacting fermionic systems on quantum processing units (QPUs) is a challenging task due to nonlocal mode entanglement generation. However, it is not yet well understood how the structure of entanglement governs the hardness of large-scale quantum chemistry simulations or the scaling of distributing such workloads. Here, we introduce an algorithm for estimating the distribution complexity of hybrid quantum-classical simulation for electronic structure Hamiltonians over heterogeneous high-performance architectures. Our algorithm relies on efficient analytical evaluation of the low entanglement boundaries for the orbital rotations and dephasing-induced localization within tensor fragments, in a double-factorized representation. Our entanglement estimation scales as O(N^3) for each fragment, where N is the number of orbitals. When QPUs are communicating via a quantum network, the cost of distribution per fragment is reduced quadratically from O(N^2) to O(N). Similarly, for hybrid quantum-classical approaches, with access to only conventional HPC interconnects, the worst-case cost is reduced from O(exp(N^2)) to O(exp(N)). We show that emergent entanglement patterns are induced by the interplay between coherent Gaussian orbital rotations and disordered Coulomb interactions. We discuss the underlying physical mechanisms that govern distribution complexity and introduce model systems that are tunable based on the localizability of fragments and the overlap of interfragment rotations. We characterize three different regimes of hardness for distribution complexity and classical simulability. The framework introduced here enables novel and more efficient quantum-classical application workflows towards utility-scale quantum computing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.20805) | 2026-08-27
