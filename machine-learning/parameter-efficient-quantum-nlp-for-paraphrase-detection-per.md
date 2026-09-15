---
title: "Parameter-Efficient Quantum NLP for Paraphrase Detection: Performance, Robustness, and Entanglement"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.14529"
summary: "arXiv:2609.14529v1 Announce Type: new Abstract: Rigorous empirical validation of quantum machine learning on natural language tasks remains scarce. We evaluate a 10-qubit hybrid quantum-classical vari"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.14529v1 Announce Type: new Abstract: Rigorous empirical validation of quantum machine learning on natural language tasks remains scarce. We evaluate a 10-qubit hybrid quantum-classical variational circuit (2,148 parameters) for paraphrase detection across three benchmarks: MRPC, Quora Question Pairs (QQP), and adversarial PAWS. On QQP (n = 10 seeds), the circuit achieves 75.53% +/- 0.75%. accuracy, statistically outperforming parameter-matched classical baselines (DeepMLP: p = 0.015, Cohen's d = 1.20; F1: p < 0.001, d = 2.32) and surpassing DistilBERT-4bit with 31,191 fewer parameters. On MRPC the optimal 2-layer variant reaches 92% of BERT-base accuracy at 54,000 lower parameter cost. Circuit depth analysis reveals a dataset-depth scaling effect; entanglement analysis via the Meyer-Wallach measure identifies multi-qubit entanglement as the primary performance driver (r = 0.85 across four variants). Adversarial evaluation on PAWS reveals emergent robustness: 98.2% recall versus 81.6% classical (+16.6 pp, d = 1.24, p < 0.001), without adversarial training. These results constitute the first systematic parameter-matched multi-benchmark empirical validation of hybrid variational circuits for NLP. All results are from classical simulation; hardware validation is future work.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.14529) | 2026-09-15
