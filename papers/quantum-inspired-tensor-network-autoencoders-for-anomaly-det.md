---
title: "Quantum-Inspired Tensor Network Autoencoders for Anomaly Detection: A MERA-Based Approach"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.06541"
summary: "arXiv:2604.06541v2 Announce Type: replace-cross Abstract: We investigate whether a multiscale tensor-network architecture provides a useful inductive bias for reconstruction-based anomaly detection in"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2604.06541v2 Announce Type: replace-cross Abstract: We investigate whether a multiscale tensor-network architecture provides a useful inductive bias for reconstruction-based anomaly detection in collider jets. Jets are produced by a branching cascade, so their internal structure is naturally organised across angular and momentum scales. This motivates an autoencoder that compresses information hierarchically and can reorganise short-range correlations before coarse-graining. Guided by this picture, we formulate a Multiscale Entanglement Renormalization Ansatz (MERA)-inspired autoencoder acting on ordered jet constituents. To our knowledge, a MERA-inspired autoencoder has not previously been proposed, and this architecture has not been explored in collider anomaly detection. We compare this architecture to a dense autoencoder, the corresponding tree-tensor-network limit, and classical baselines within a background-only reconstruction framework. The paper is organised around two main questions: whether locality-aware hierarchical compression is genuinely supported by the data, and whether the disentangling layers of MERA contribute beyond a simpler tree hierarchy. To address these questions, we combine benchmark comparisons with a training-free local-compressibility diagnostic and a direct identity-disentangler ablation. In the nominal benchmark, the MERA-inspired model attains a higher mean AUC than the dense autoencoder at all three latent dimensions while using roughly one-third of its trainable parameters. The locality-preserving multiscale structure is well matched to jet data, and, at the strongest compression bottleneck, the trained disentanglers move substantially away from the identity and are accompanied by a positive mean performance shift. Overall, the study supports locality-aware hierarchical compression as a useful and parameter-efficient inductive bias for reconstruction-based jet anomaly detection in this benchmark setting.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.06541) | 2026-11-05
