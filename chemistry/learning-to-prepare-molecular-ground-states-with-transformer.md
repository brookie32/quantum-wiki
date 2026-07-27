---
title: "Learning to Prepare Molecular Ground States with Transformer Models"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.22468"
summary: "arXiv:2607.22468v1 Announce Type: new Abstract: Quantum state preparation is a key component of many quantum algorithms. Performing this step efficiently is essential for realizing practical quantum a"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2607.22468v1 Announce Type: new Abstract: Quantum state preparation is a key component of many quantum algorithms. Performing this step efficiently is essential for realizing practical quantum advantage in quantum chemistry applications. Iterative algorithms like ADAPT-VQE can produce shallow ground-state preparation circuits, but become computationally prohibitive for the larger molecules relevant to materials science and pharmaceutical development. Here, we introduce ADAPT-GQE, a generative AI framework that learns to synthesize ground-state preparation circuits for electronic structure calculations. We first use ADAPT-VQE to generate high-quality reference circuits, which are then used as targets for training models for circuit generation. Once trained, the model can efficiently propose and score circuits, enabling reinforcement learning (RL) to drive circuit generation accuracy beyond the accuracy of the ADAPT-VQE training data. This pipeline achieves order-of-magnitude reductions in circuit generation time relative to ADAPT-VQE while maintaining comparable or improved state-preparation accuracy. We demonstrate ADAPT-GQE on imipramine, a well-established tricyclic antidepressant that serves as a representative, challenging target for computational modelling in drug stability protocols. We execute generated circuits on Quantinuum Helios-1, representing a milestone for AI-generated quantum chemistry circuits on state-of-the-art quantum hardware. These results establish a pathway toward automated quantum circuit synthesis for utility-scale quantum computational chemistry.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.22468) | 2026-07-27
