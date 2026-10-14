---
title: "DPF-SGD: Byzantine-Robust Differentially Private Federated SGD with Exact Optimality Guarantees"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2467"
summary: "Federated optimization enables collaborative learning over decentralized data but is accompanied by significant privacy risks due to the exchange of model updates. While differential privacy (DP) prov"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Federated optimization enables collaborative learning over decentralized data but is accompanied by significant privacy risks due to the exchange of model updates. While differential privacy (DP) provides formal protection, optimization accuracy is often degraded, and robustness becomes particularly limited in the presence of Byzantine agents. A Byzantine-robust, differentially private federated SGD algorithm, DPF-SGD, is proposed, in which private step sizes are integrated with a DP noise–decay schedule to regulate gradient updates. To further enhance robustness, a privacy-preserving comparative elimination (PPCE) filter is developed to suppress Byzantine contributions during aggregation while preserving privacy guarantees. Almost sure convergence to the global optimum under ϵ-differential privacy is established, despite persistent noise and adversarial behavior. Experiments on synthetic and MNIST datasets demonstrate oneto two-order-of-magnitude reductions in final optimization error relative to DP baselines.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2467) | 2026-10-14
