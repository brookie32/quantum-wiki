---
title: "LLM-Assisted Generation of Transparent, Open-Source Multiphysics Models of Electrochemical Devices"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2610.10320"
summary: "arXiv:2610.10320v1 Announce Type: new Abstract: Multiphysics continuum models are powerful tools for studying electrochemical devices, enabling in silico reactor design and resolution of local pH, pot"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.10320v1 Announce Type: new Abstract: Multiphysics continuum models are powerful tools for studying electrochemical devices, enabling in silico reactor design and resolution of local pH, potential, and concentration fields that govern device performance but are difficult to measure experimentally. However, constructing such models requires substantial numerical expertise or reliance on proprietary software. Here, we show that frontier large language model agents can remove this implementation burden while keeping the underlying physics under researcher control. Using one-dimensional electrochemical CO2 reduction to CO in a porous gas diffusion electrode as a test case, we develop a machine-readable, human-specified modeling harness containing governing equations, parameters, numerical methods, logical build stages, and human-verifiable checkpoints. From this specification, the agent reproducibly constructs complete multiphysics models in open-source Julia. Independently built models, including fully autonomous agent-built models, agree with an equivalent COMSOL implementation to within 0.7% of the peak CO partial current density, and with one another to within 0.04%. Systematically planted errors demonstrate the importance of explicit specifications for reproducibility and reveal the agent's capabilities and limitations in debugging model physics. This framework establishes a more transparent approach to multiphysics modeling in which physical descriptions and governing equations, rather than specialized code, become the primary inputs for computational model development.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2610.10320) | 2026-10-08
