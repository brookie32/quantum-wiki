---
title: "AceFF: A State-of-the-Art Machine Learning Potential for Small Molecules"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2601.00581"
summary: "arXiv:2601.00581v3 Announce Type: replace Abstract: We introduce AceFF, a pre-trained machine learning interatomic potential (MLIP) optimized for small molecule drug discovery. While MLIPs have emerge"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2601.00581v3 Announce Type: replace Abstract: We introduce AceFF, a pre-trained machine learning interatomic potential (MLIP) optimized for small molecule drug discovery. While MLIPs have emerged as efficient alternatives to Density Functional Theory (DFT), generalizability across diverse chemical spaces remains difficult. AceFF addresses this by refining the TensorNet2 architecture and training it on a comprehensive dataset of drug-like compounds. This approach yields a force field that balances high-throughput inference speed with DFT-level accuracy. We introduce two models sharing the same architecture: mbox{AceFF-2}, trained on our own dataset of small molecules and supporting the essential medicinal chemistry elements (H, B, C, N, O, F, Si, P, S, Cl, Br, I); and mbox{AceFF-2-OMOL}, trained on a subset of OMol25 containing the AceFF-2 elements plus the common biomolecular ion elements Na and K. The models are explicitly trained to handle charged states. Validation against rigorous benchmarks, including complex torsional energy scans, molecular dynamics trajectories, batched minimizations, and tests of force and energy accuracy, demonstrates that AceFF is state-of-the-art for organic molecules in the accuracy and speed regime important for drug discovery. The AceFF-2 and AceFF-2-OMol model weights and inference code are available at https://huggingface.co/Acellera/AceFF-2.0 and https://huggingface.co/Acellera/AceFF-2-OMOL.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2601.00581) | 2026-10-19
