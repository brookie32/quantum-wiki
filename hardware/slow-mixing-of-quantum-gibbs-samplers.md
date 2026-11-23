---
title: "Slow Mixing of Quantum Gibbs Samplers"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2411.04300"
summary: "arXiv:2411.04300v3 Announce Type: replace Abstract: Preparing thermal (Gibbs) states is a common task in physics and computer science. Recent algorithms mimic cooling via system-bath coupling, where t"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2411.04300v3 Announce Type: replace Abstract: Preparing thermal (Gibbs) states is a common task in physics and computer science. Recent algorithms mimic cooling via system-bath coupling, where the cost is determined by mixing time, akin to classical Metropolis-like algorithms. However, few methods exist to demonstrate slow mixing in quantum systems, unlike the well-established classical tools for systems like the Ising model and constraint satisfaction problems. We present a quantum generalization of these tools through a generic bottleneck lemma that implies slow mixing in quantum systems. This lemma focuses on quantum measures of distance, analogous to the classical Hamming distance but rooted in uniquely quantum principles and quantified either through Bohr spectrum jumps or operator locality. Using our bottleneck lemma, we establish unconditional lower bounds on the mixing times of Gibbs samplers for several families of Hamiltonians at low temperatures. For classical Hamiltonians with mixing time lower bounds T_mix = exp[Omega(n^alpha)], we prove that quantum Gibbs samplers also have T_mix = exp[Omega(n^alpha)]. This applies to models like random K-SAT instances and spin glasses. For stabilizer Hamiltonians, we provide a concise proof of exponential lower bounds T_mix = exp[Omega(n)] on mixing times of good n-qubit stabilizer codes at low constant temperature. Finally, we consider constant-degree classical Hamiltonians and show how to lift classical slow mixing results in the presence of a transverse field using Poisson Feynman-Kac techniques. We show generic results for models with linear free energy barriers, and we demonstrate that our techniques extend to models with sublinear free energy barriers by proving T_mix = exp[n^{1/2-o(1)}] for the ferromagnetic 2D transverse field Ising model.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2411.04300) | 2026-11-23
