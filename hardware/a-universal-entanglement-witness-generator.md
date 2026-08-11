---
title: "A Universal Entanglement Witness Generator"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.07806"
summary: "arXiv:2608.07806v1 Announce Type: new Abstract: Entanglement witnesses are essential for certifying entanglement, yet constructing ones that are both noise-robust and economical in measurement setting"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.07806v1 Announce Type: new Abstract: Entanglement witnesses are essential for certifying entanglement, yet constructing ones that are both noise-robust and economical in measurement settings remains challenging - particularly beyond qubits and for non-stabilizer ("magic") states. We present a machine-learning method that, given a target state and a user-specified number of measurement settings, generates an entanglement witness optimized for noise tolerance in the neighborhood of that state, requiring only local measurements. The approach is fully general, applying to multipartite qubit and qudit systems alike, including non-stabilizer states. For N qudits of dimension d, we train on the fully-separable eigenstates of each qudit's SU(d) generators to find a prototype witness, then tune the witness's bias term via gradient descent to maximize noise tolerance. Adversarial training further strengthens the witnesses, delivering greater noise tolerance with even fewer settings; critically, under this scheme the required training-set size becomes independent of system size. We package the entire pipeline as an automated script that, in every case we tested, produces witnesses surpassing all existing methods in noise tolerance and/or number of measurement settings. We demonstrate the method on Bell, GHZ, W, and hypergraph states, along with a range of qudit states, spanning 2-6 qubits, bipartite qudits up to d=10, and tripartite qutrits. Our witnesses achieve perfect accuracy across both physical experimental test states and large numerical sets of separable mixed states-including 30 million test states for a 3-qubit W-state witness and 10 million for a 4-qubit hypergraph-state witness-and we experimentally confirm the noise tolerance of Bell- and hypergraph state witnesses on both photonic and superconducting platforms, respectively.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.07806) | 2026-08-11
