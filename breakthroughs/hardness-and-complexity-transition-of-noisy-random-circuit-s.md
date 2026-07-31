---
title: "Hardness and Complexity Transition of Noisy Random Circuit Sampling"
date: "2026-07-24"
updated: "2026-07-24"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.20804"
summary: "arXiv:2607.20804v1 Announce Type: new Abstract: Random circuit sampling (RCS) is a leading candidate for demonstrating quantum advantage, supported by strong complexity-theoretic evidence of hardness "
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

arXiv:2607.20804v1 Announce Type: new Abstract: Random circuit sampling (RCS) is a leading candidate for demonstrating quantum advantage, supported by strong complexity-theoretic evidence of hardness in the ideal setting and by rapid experimental progress to date. In practice, however, noise is unavoidable, and a central problem is to identify the noise-strength boundary between classically simulable and classically hard regimes. In this work, we establish an architecture-general hardness bound for this boundary for the standard local depolarizing noise of strength gamma. Assuming the standard average-case #P-hardness conjecture for ideal RCS, we show that, for any circuit architecture satisfying this conjecture, noisy RCS on the same architecture remains hard to simulate classically within any inverse-polynomial total variation distance whenever gamma=O(log n/(nd)) for n-qubit circuits of depth d, unless the polynomial hierarchy collapses. Crucially, noisy-RCS hardness follows without any additional conjectural or architecture-specific assumption beyond those already entering the ideal-RCS hardness framework. Our proof combines a low-degree polynomial extrapolation with a monotonicity reduction showing that efficient classical simulation at one depolarizing noise strength implies efficient simulation at every larger strength. Together, these ingredients transfer the standard ideal-RCS hardness conjecture to sampling hardness at a prespecified noise strength. Finally, combining the convergence-to-uniformity result of Dalzell et al. [Commun. Math. Phys. 405, 78 (2024)] with our monotonicity reduction yields efficient classical simulation for gamma=omega(log n/(nd)) on layered, regularly connected architectures. Thus, wherever the two architectural settings overlap, this identifies gamma=Theta(log n/(nd)) as the asymptotic complexity-transition scale.



## Related
- [[the-impact-of-qubit-connectivity-on-quantum-advantage-in-noi|The Impact of Qubit Connectivity on Quantum Advantage in Noisy IQP Circuits]]
- [[matrix-product-state-approach-to-lossy-boson-sampling-and-no|Matrix product state approach to lossy boson sampling and noisy IQP sampling]]
- [[approximate-sampling-from-decoded-quantum-interferometry-via|Approximate sampling from decoded quantum interferometry via Markov chain Monte Carlo methods]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.20804) | 2026-07-24
