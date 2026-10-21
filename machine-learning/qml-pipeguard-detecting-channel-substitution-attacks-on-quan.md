---
title: "QML-PipeGuard: Detecting Channel-Substitution Attacks on Quantum Machine Learning Pipelines in Untrusted Clouds"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.25066"
summary: "arXiv:2605.25066v2 Announce Type: replace Abstract: As machine-learning workloads move onto quantum hardware they inherit a trust problem classical AI deployments have largely solved and quantum ones "
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2605.25066v2 Announce Type: replace Abstract: As machine-learning workloads move onto quantum hardware they inherit a trust problem classical AI deployments have largely solved and quantum ones have not: quantum machine learning (QML) is already sold as a cloud service, and a customer cannot check that the circuit they paid for is actually the circuit that ran. We show the gap is exploitable. A malicious or cost-cutting provider can substitute the declared quantum channel with one that reproduces every accuracy test the customer performs, passes the single-observable checks used in practice, and still differs from the declared computation at the channel level. We call this a channel-substitution attack and instantiate it in three deployments: audit evasion, service downgrade, and result forgery in reproducibility review. QML-PipeGuard detects the attack at runtime from measurement statistics the customer already collects. Its guarantee is two-sided, stated in the distance a local verifier measures: any substitution shifting a single-qubit output marginal by elta in trace norm forces a contract deviation of at least elta/sqrt{3}, the constant tight and independent of qubit count; the guarantee is relative to the chosen observable family and reference-input set. For local-unitary substitutions the adversary's blind set is characterised exactly, as a commutation condition, which gives the defender a rule for choosing challenge inputs that shrinks it. A finite-shot budget rule bounds false accepts and false alarms at once, one tolerance separates attack from the benign drift observed here, and every decision enters a hash-anchored audit trail. On an IBM Heron r2 processor a substituted quantum-kernel intrusion-detection pipeline evades the weak contract and our verifier halts it, while the honest channel stays within tolerance.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.25066) | 2026-10-21
