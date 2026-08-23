---
title: "Parity Floors in Quantum Denoisers: A Closed-Form Benchmark for Fixed-Map Denoising Networks"
date: "2026-08-14"
updated: "2026-08-14"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.12712"
summary: "arXiv:2608.12712v1 Announce Type: new Abstract: Fixed quantum feature maps are increasingly inserted into diffusion denoisers, but standard image benchmarks do not reveal which structural constraint l"
last_verified: "2026-08-14"
review_by: "2026-11-12"
stale: false
---

arXiv:2608.12712v1 Announce Type: new Abstract: Fixed quantum feature maps are increasingly inserted into diffusion denoisers, but standard image benchmarks do not reveal which structural constraint limits them. We introduce CoupledPhaseTexture, a torus-diffusion benchmark with analytic heat-kernel noising that separates parity, within-sector approximation, and sample-complexity limitations. For the depth-1 RY+CNOT+Pauli-Z family we prove a containment-free parity floor: all reachable features are even functions of the encoded angles while the sine components of the Bayes denoiser are odd, so the excess risk splits exactly into an inaccessible odd part and a within-sector residual. The first term is an irreducible, noise-scale-resolved lower bound holding for every even feature class, with no containment, linearity, or closedness assumption on the feature class. The obstruction is a property of the noise-conditioned denoising target rather than static representability: the floor is re-derived at each noise scale because the target's parity content changes with noise. The measured excess is dominated by the parity proxy on two distinct priors. Higher-order Z readouts improve the even sector, but entanglement does not lower the floor and re-uploading does not reliably close it. Classical controls confirm the deficit is parity rather than quantumness: a cosine-only bank is floored similarly, while adding the sine sector matches the reference. Among tested constructions, odd readouts and a noise-coupled encoder do not match the sine-carrying classical bank. These results motivate nonclassical data access or feature classes without efficient classical surrogates; they do not establish either as sufficient for quantum advantage.



## Related
- [[separating-quantum-circuits-from-classical-llms|Separating quantum circuits from classical LLMs]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.12712) | 2026-08-14
