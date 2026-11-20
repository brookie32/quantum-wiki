---
title: "Detailed assessment of calculating drag force with quantum computers: Explicit time-evolution precludes exponential advantage for nonlinear differential equations"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2406.06323"
summary: "arXiv:2406.06323v4 Announce Type: replace Abstract: This study examines the potential for fault-tolerant quantum computers to provide utility in fluid dynamics simulations, with a focus on drag force "
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2406.06323v4 Announce Type: replace Abstract: This study examines the potential for fault-tolerant quantum computers to provide utility in fluid dynamics simulations, with a focus on drag force calculations for ship hull design. We assess whether quantum algorithms can surpass classical computational limits by generating detailed quantum resource estimates (QREs) in terms of logical qubits and T-gate counts. Our analysis is based on a quantum algorithm leveraging Carleman linearization of the lattice Boltzmann method (LBM), which has been suggested to offer exponential speedup. We develop efficient block encodings for LBM matrices and a method for amplitude-encoding drag force. We apply the method to the simple case of fluid flow past a sphere across a range of Reynolds numbers (Re). We estimate the required (logical qubits)imes(T-gates), finding them to be prohibitively large, ranging from 10^{21} to 10^{39}. While classical simulations scale as O(Re^3), our QREs exhibit a modest polynomial scaling of O(Re^{2.69}), indicating no exponential quantum advantage. We attribute this limitation to an intrinsic power-law relationship between spatial grid resolution and time-stepping requirements that is a fundamental characteristic of explicit methods for evolving nonlinear differential equations. Thus, quantum computers are unlikely to provide utility in applications that require time-evolving fluids and other systems of nonlinear differential equations.



## Related
- [[an-efficient-explicit-implementation-of-a-quantum-algorithm-|An Efficient Explicit Implementation of a Quantum Algorithm with Quantum Advantage for Nonlinear Scalar Conservation Laws]]
- [[quantum-algorithms-for-general-nonlinear-dynamics-based-on-t|Quantum algorithms for general nonlinear dynamics based on the Carleman embedding]]
- [[an-end-to-end-quantum-algorithm-for-nonlinear-fluid-dynamics|An end-to-end quantum algorithm for nonlinear fluid dynamics with bounded quantum advantage]]
- [[quantum-algorithms-for-computational-fluid-dynamics|Quantum Algorithms for Computational Fluid Dynamics]]
- [[efficient-treatment-of-non-linearity-in-quantum-computationa|Efficient Treatment of Non-Linearity in Quantum Computational Fluid Dynamics Using Hybrid Tensor Networks]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2406.06323) | 2026-11-19
