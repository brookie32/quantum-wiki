---
title: "A Recursive Module-Coupling Algorithm for Computing Low-Energy Eigenstates"
date: "2026-09-03"
updated: "2026-09-03"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.02394"
summary: "arXiv:2609.02394v1 Announce Type: new Abstract: Finding the eigenstates of a many-body Hamiltonian is a fundamental challenge in physics and computational science. Since the search space grows exponen"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

arXiv:2609.02394v1 Announce Type: new Abstract: Finding the eigenstates of a many-body Hamiltonian is a fundamental challenge in physics and computational science. Since the search space grows exponentially with system size, numerous classical and quantum algorithms have been developed to address this problem. A practical strategy is to identify a physics-informed low-dimensional subspace that effectively accommodates the low-lying eigenstates, thereby reducing the computational complexity. In this paper, we propose a recursive module-coupling algorithm, which iteratively treats a system as a composition of locally-coupled smaller modules, with low-energy subspace estimated successively according to the same recursive structure. Unlike the density matrix renormalization group (DMRG) approach that optimizes a global matrix product state through repeated local sweeps and obtains excited states sequentially, our algorithm constructs a physically tailored variational basis from module eigenstates and obtains several low-energy states on an equal footing, leading to substantial speedups if targeting moderate accuracy. Our proposed method further leads naturally to a recursive quantum variational algorithm, providing a systematic and modular circuit-construction framework compatible with contemporary gate-based quantum architectures. At each recursive level, block encoders are trained to map logical basis states onto the retained physical subspace, within which a variational circuit is subsequently optimized.Such a quantum-circuit implementation provides not only a quantum multistate eigensolver, but also a systematic prescription for hierarchically constructing quantum state-preparation circuits. Classical simulations demonstrate the accuracy and efficiency of the proposed method, whereas experiments on IBM quantum processors show that eigenstate preparation with reasonable fidelities is achievable even in the current NISQ era.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.02394) | 2026-09-03
