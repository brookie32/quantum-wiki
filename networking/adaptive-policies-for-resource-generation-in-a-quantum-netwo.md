---
title: "Adaptive Policies for Resource Generation in a Quantum Network"
date: "2026-09-21"
updated: "2026-09-21"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.17576"
summary: "arXiv:2509.17576v2 Announce Type: replace Abstract: Protocols for distributed quantum systems commonly require the simultaneous availability of n entangled states, each with a fidelity above some fixe"
last_verified: "2026-09-21"
review_by: "2026-12-20"
stale: false
---

arXiv:2509.17576v2 Announce Type: replace Abstract: Protocols for distributed quantum systems commonly require the simultaneous availability of n entangled states, each with a fidelity above some fixed minimum F_{app} relative to the target maximally-entangled state. However, the fidelity of entangled states degrades over time while in memory. Entangled states are therefore rendered useless when their fidelity falls below F_{app}. This is problematic when entanglement generation is probabilistic and attempted in a sequential manner, because the expected completion time until n entangled states are available can be large. Motivated by existing entanglement generation schemes, we consider a system where the entanglement generation parameters (the success probability p and fidelity F of the generated entangled state) may be adjusted at each time step. We model the system as a Markov decision process, where the policy dictates which generation parameters (p,F) to use for each attempt. We use dynamic programming to derive optimal policies that minimise the expected time until n entangled states are available with fidelity greater than F_{app}. We observe that the advantage of our optimal policies over the selected baselines increases significantly with n. In the parameter regimes explored, which are based closely on current experiments, we find that the optimal policy can provide a speed-up of as much as a factor of twenty over a constant-action policy. In addition, we propose a computationally inexpensive heuristic method to compute policies that perform either optimally or near-optimally in the parameter regimes explored. Our heuristic method can be used to find high-performing policies in parameter regimes where finding an optimal policy is intractable.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.17576) | 2026-09-21
