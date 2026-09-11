---
title: "Generative Replay Mitigates Sample Starvation in Quantum Architecture Search"
date: "2026-09-11"
updated: "2026-09-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.11248"
summary: "arXiv:2609.11248v1 Announce Type: new Abstract: Reinforcement learning (RL) can automate quantum architecture search, but its scalability is limited when useful circuit trajectories become rare in the"
last_verified: "2026-09-11"
review_by: "2026-12-10"
stale: false
---

arXiv:2609.11248v1 Announce Type: new Abstract: Reinforcement learning (RL) can automate quantum architecture search, but its scalability is limited when useful circuit trajectories become rare in the rapidly expanding search space. Existing replay mechanisms reuse observed transitions; the proposed learned model produces additional predicted one step transitions from real state-action seeds. Here we introduce GenQAS, a tensor network-guided RL framework that combines a fixed matrix product state warm-start with prioritized generative replay. A learned local transition model generates synthetic circuit transitions on demand and mixes them with real experience during Double Deep Q-Network updates. Under a random exploration analysis, near ground state circuits occupy a rapidly shrinking region of the accessible state space. We investigate whether real data anchored synthetic replay can improve the effective training signal in this regime. Across chemical Hamiltonian benchmarks from 6 to 12 qubits, GenQAS improves fixed-budget success probability and identifies compact circuits at competitive energy error. At 12 qubits, it improves final success probability by up to 7.0imes over passive replay. On a 15-qubit transverse field Ising model, GenQAS increases success probability from 12% to 21%. In a noisy 6-qubit BeH_2 transfer experiment, generative replay reduces the steps to chemical accuracy by 92.7%. These results show that generative replay can mitigate sample starvation in quantum architecture search and support more resource efficient circuit discovery.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.11248) | 2026-09-11
