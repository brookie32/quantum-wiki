---
title: "Efficient Representation of multicategorical local Hilbert spaces: nonlinear Restricted Boltzmann Machines to Kolmogorov-Arnold Networks"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.06672"
summary: "arXiv:2609.06672v2 Announce Type: replace Abstract: Neural network quantum states (NQS) for representing spin-frac{1}{2} systems are typically built from Multi-Layer Perceptrons (MLPs) with binary vis"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2609.06672v2 Announce Type: replace Abstract: Neural network quantum states (NQS) for representing spin-frac{1}{2} systems are typically built from Multi-Layer Perceptrons (MLPs) with binary visible variables, in which the input spins are first combined through linear affine maps before more expressive nonlinear transformations are applied. The standard way for representing multi-categorical systems, namely spin-1 and spin-2, or the q-state quantum Potts systems with more than two local degrees of freedom, is a unary or one-hot encoded MLP architecture. Following a few similar studies, I observe that while the one-hot construction is the mathematically faithful encoding for systems with more than two local states such as spin-S models with S > 1/2 or q-state Potts models, its parameter count grows with the number of local states, and the resulting optimization landscape can hinder convergence. I find numerically that allowing log Psi to be a nonlinear function of the raw multi-valued spin variable is a natural categorical generalization: it preserves the labelling freedom of the local basis and reproduces the one-hot model with strictly fewer parameters, often with improved trainability. I first benchmark this idea on shallow Restricted Boltzmann Machines (RBMs), equipping them with several distinct nonlinear connections, for spin-1, 2, and 3 Heisenberg chains. I then turn to Kolmogorov-Arnold Networks (KANs), where each edge carries a learnable univariate nonlinearity, and show that they provide a strictly more expressive realization of the same principle. Finally, I demonstrate that this framework captures the critical behaviour of the quantum Potts Hamiltonian, recovering its phase transition.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.06672) | 2026-09-14
