---
title: "'Train classical, deploy quantum' requires rethinking generalization"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.31117"
summary: "arXiv:2608.31117v1 Announce Type: new Abstract: Generative models have become central across science and industry, from image and text synthesis to the design of molecules and materials. Quantum gener"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.31117v1 Announce Type: new Abstract: Generative models have become central across science and industry, from image and text synthesis to the design of molecules and materials. Quantum generative models are considered one of the most promising applications for quantum computers, since a quantum circuit naturally produces samples from the distribution it encodes, and for suitable circuits that distribution is believed to be hard for any classical computer to reproduce. A leading strategy trains these models on a classical computer and reserves the quantum device for generating samples at deployment. This is possible when the training loss can be evaluated on a classical computer. A prime example is the maximum mean discrepancy (MMD^2), a moment-matching loss that compares the model and the data through their Pauli-Z correlations. Research so far has asked whether such models can be trained and whether their sampling is hard; whether minimizing such an objective yields a model that generalizes, rather than one that merely reproduces the training statistics, remains poorly understood. We benchmark a broad set of quantum and classical generative models by direct sampling and show that models trained with a moment-matching loss generally show worse generalization than the likelihood-trained models. We show this on two application-inspired datasets: first a cardinality-constrained dataset at up to 30 qubits and second a dataset of genomic single-nucleotide variants, whose valid set is the observed data. These results indicate that a converged moment-matching loss is not a reliable measure of generalization, and that train-classical, deploy-quantum workflows will need approaches that target generalization directly, leaving open whether better training objectives suffice or whether the model architectures themselves must change.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.31117) | 2026-09-01
