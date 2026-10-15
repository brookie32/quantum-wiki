---
title: "Sequential vs. Synchronized Entanglement Swapping: QKD Secret-Key Rate under Optimized Link-Layer Control"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.04047"
summary: "arXiv:2605.04047v2 Announce Type: replace Abstract: Quantum repeater chains build long-distance entanglement for quantum key distribution (QKD) by creating pairs on short links and joining them throug"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2605.04047v2 Announce Type: replace Abstract: Quantum repeater chains build long-distance entanglement for quantum key distribution (QKD) by creating pairs on short links and joining them through entanglement swapping. Because stored pairs lose fidelity while they wait, swap timing can affect the secret-key rate. We study how network-layer swap scheduling affects six-state QKD on a simulated four-hop chain under an idealized Werner-state noise model. We compare a sequential (swap-and-wait) discipline, which builds and stores partial chains, with a synchronized (wait-and-swap) discipline, which waits until all links are ready before swapping. Both use the same reinforcement-learned link controllers, isolating the effect of the swapping discipline. When stored pairs cannot retain sufficient fidelity for one network time step, our sequential implementation produces no key, while synchronized retains a small key rate from simultaneous link deliveries. Once sequential becomes viable, it outperforms synchronized by up to 19.1% in the homogeneous chains studied, with the advantage decreasing as memory lifetime increases. We predict the synchronized short-memory pair-delivery rate from link-delivery statistics and derive a closed-form condition for when sequential can preserve progress across time steps. We also examine chains with one slower link, where partial chains can wait and decay at the bottleneck. In this setting, synchronized slightly outperforms sequential at longer memory lifetimes. Moving the slow link has little effect on key rate away from the transition region but strongly affects sequential link-buffer occupancy. Choosing a swapping discipline therefore depends not only on whether memories can preserve partial progress, but also on how the link configuration determines where that progress must wait and decay.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.04047) | 2026-10-15
