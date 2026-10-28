---
title: "Tensor-network simulation of quantum phase estimation in the von Neumann measurement formulation with DMRG-prepared initial states"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2407.19348"
summary: "arXiv:2407.19348v3 Announce Type: replace Abstract: The von Neumann measurement formulation of quantum phase estimation [Phys. Rev. A extbf{66}, 032314 (2002); Quantum extbf{5}, 465 (2021)] estimates "
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2407.19348v3 Announce Type: replace Abstract: The von Neumann measurement formulation of quantum phase estimation [Phys. Rev. A extbf{66}, 032314 (2002); Quantum extbf{5}, 465 (2021)] estimates energies by coupling the system to a discretized pointer register through hat Hotimeshat p and reading out the pointer after an inverse quantum Fourier transform. Building on these works, we develop a tensor-network framework for simulating and benchmarking this protocol when the system is initialized in a matrix product state (MPS) pre-trained with the density matrix renormalization group (DMRG). The system and the pointer are represented as a composite MPS, the coupling hat Hotimeshat p as a matrix product operator, and the coupled dynamics is evolved with the time-dependent variational principle. This gives direct access to the time-resolved pointer distribution, the recovered energy, and the entanglement generated between system and pointer. We apply the framework to quantum many-body spin systems and to electronic-structure problems. For the systems studied, the pointer readout yields accurate ground-state energy estimates from DMRG-prepared approximate states, even when their variational energies are not fully converged. These states generally contain contributions from both ground and excited eigenstates, with their spectral weights determining the corresponding contributions to the pointer distribution. More accurate initial states also strongly suppress the entanglement generated between system and pointer. We also provide logical and compiled resource estimates for a Suzuki--Trotter realization of the protocol.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2407.19348) | 2026-10-28
