---
title: "Dynamic Entanglement-Weighted Pruning for Quantum Federated Unlearning in Supply-Chain Risk Prediction"
date: "2026-08-19"
updated: "2026-08-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.17069"
summary: "arXiv:2608.17069v1 Announce Type: new Abstract: Federated deployments of variational quantum classifiers are attractive for cross-organisation risk prediction in supply chains, because raw data never "
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

arXiv:2608.17069v1 Announce Type: new Abstract: Federated deployments of variational quantum classifiers are attractive for cross-organisation risk prediction in supply chains, because raw data never leaves the client, yet data-protection regulations such as the GDPR grant clients a right to request that their contribution be removed from a trained model after the fact. Retraining a federated model from scratch to honour such a request is correct but wasteful, and it is not obvious which quantum circuit parameters actually carry a given client's influence. We introduce Entanglement-Weighted Pruning (EWP), an unlearning procedure for quantum federated learning that scores every trainable circuit parameter with the product of two signals: the diagonal entry of the quantum Fisher information matrix estimated on the target client's data via the parameter-shift rule, and a structural entanglement weight associated with the parameter's gate. Parameters with the lowest scores are pruned, optionally followed by a short fine-tuning pass on the retained clients. We implement the full pipeline in Qiskit for a four-qubit data-re-uploading ansatz trained with FedAvg across five simulated supply-chain-risk clients, and benchmark EWP against full retraining, fine-tuning alone, random pruning, Fisher-only pruning, and entanglement-only pruning, over three random seeds. EWP attains a mean post-unlearning accuracy statistically indistinguishable from the full-retraining oracle, while producing a lower forgetting score and requiring roughly 16 times less wall-clock time. Ablations over pruning threshold, client count, and non-IID strength show that combining the two signals is necessary, as entanglement-only and Fisher-only pruning each substantially degrade accuracy relative to EWP.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.17069) | 2026-08-19
