---
title: "An (almost) efficient classical algorithm for sampling from typical Gibbs states"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40250"
summary: "arXiv:2609.40250v1 Announce Type: new Abstract: Gibbs state preparation has emerged as a potential avenue for quantum advantage in the study of physical systems. Although there is known advantage for "
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40250v1 Announce Type: new Abstract: Gibbs state preparation has emerged as a potential avenue for quantum advantage in the study of physical systems. Although there is known advantage for computing local properties of worst-case Gibbs states, recent results suggest a different picture for average-case local systems: at temperatures where their Gibbs states can be efficiently prepared quantumly, quasi-polynomial time classical algorithms can also compute local expectation values. Yet this leaves open the possibility of an advantage under a stronger notion of simulation: sampling. Gibbs sampling underlies Boltzmann machine-based quantum learning algorithms and quantum supremacy proposals, but its classical average-case complexity for physically relevant models remains unresolved. Here, we give strong evidence against an exponential quantum advantage in Gibbs sampling for an ensemble of local systems known as the quantum p-spin model. We describe a classical algorithm for sampling from the Gibbs state to any polynomially small error in total variation distance. Our algorithm is based on a meta-algorithm known as algorithmic stochastic localization (ASL). Our main technical result is a generalized convergence theorem for ASL which reduces approximate sampling from any distribution on the hypercube to estimating the mean of a related "tilted distribution" to sufficiently low additive error. We then extend known quasi-polynomial time algorithms for computing local expectation values of a related disordered model to compute these "tilted means" for the quantum p-spin model. Finally, we give a non-rigorous physics argument that this mean-estimation algorithm works down to the spin glass transition temperature. As efficient quantum algorithms also fail at this transition, this suggests they cannot Gibbs sample the quantum p-spin model at temperatures below that for which classical algorithms are also (almost) efficient.



## Related
- [[unconditional-quantum-advantage-for-sampling-with-shallow-ci|Unconditional Quantum Advantage for Sampling with Shallow Circuits]]
- [[verifiable-quantum-advantage-in-extremely-low-depth|Verifiable quantum advantage in extremely low depth]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40250) | 2026-10-01
