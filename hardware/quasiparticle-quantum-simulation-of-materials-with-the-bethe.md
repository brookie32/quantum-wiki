---
title: "Quasiparticle quantum simulation of materials with the Bethe-Salpeter equation"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.02916"
summary: "arXiv:2610.02916v1 Announce Type: new Abstract: The first-principles quantum simulation of the full electronic Hamiltonian of a material model of realistic size appears daunting even in a future era o"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.02916v1 Announce Type: new Abstract: The first-principles quantum simulation of the full electronic Hamiltonian of a material model of realistic size appears daunting even in a future era of fully fault-tolerant quantum computers. In contrast, classical simulations of material excited states rely on heuristic quasiparticle frameworks, such as the GW approximation and Bethe-Salpeter equation, where only a few quasiparticles are explicitly considered. Here we give a detailed description of quasiparticle quantum simulation for multi-excitonic states within the BSE. We develop an explicit first-quantized, orbital-based block encoding of the multi-exciton BSE Hamiltonian for qubitization, and reduce its cost using integral factorization and crystal symmetries. For a materials model of size N, and a fixed number of quasiparticles, the resulting algorithms require widetilde{O}(N) Toffoli gates and O(log N) logical qubits, or, using space-time tradeoffs, widetilde{O}(sqrt{N}) Toffoli gates and widetilde{O}(sqrt{N}) logical qubits, achieving up to a sixth power reduction in Toffoli count, or up to exponential reduction in qubit count, versus standard full Hamiltonian simulation techniques that have been explored in materials simulation. Resource estimates for the classically challenging problem of triexcitonic eigenvalue estimation across a range of semiconductor models of a realistic physical size of O(10^3) atoms, show that our Toffoli-optimized implementation reduces the Toffoli count by 10^6-10^7 relative to full Hamiltonian simulation estimates, while a qubit-optimized implementation requires only a few hundred logical qubits. More broadly, these results show that classical heuristic frameworks will be essential in the design of future fault-tolerant quantum algorithms for materials.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.02916) | 2026-10-05
