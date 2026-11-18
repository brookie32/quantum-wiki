---
title: "Quantum Advantage in Storage and Retrieval of Isometry Channels"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2507.10784"
summary: "arXiv:2507.10784v5 Announce Type: replace Abstract: Storage and retrieval refer to the task of encoding an unknown quantum channel Lambda into a quantum state, known as the program state, such that th"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2507.10784v5 Announce Type: replace Abstract: Storage and retrieval refer to the task of encoding an unknown quantum channel Lambda into a quantum state, known as the program state, such that the channel can later be retrieved. There are two strategies for this task: classical and quantum strategies. The classical strategy uses multiple queries to Lambda to estimate Lambda and retrieves the channel based on the estimate represented in classical bits. The classical strategy turns out to offer the optimal performance for the storage and retrieval of unitary channels. In this work, we analyze the asymptotic performance of the classical and quantum strategies for the storage and retrieval of isometry channels. We show that the optimal fidelity for isometry estimation is given by F = 1-{d(D-d)over n} + O(n^{-4/3}), where d and D denote the input and output dimensions of the isometry, and n is the number of queries. This result indicates that, unlike in the case of unitary channels, the classical strategy is suboptimal for the storage and retrieval of isometry channels, which requires n = Theta(epsilon^{-1}) to achieve the diamond-norm error epsilon. We propose a more efficient quantum strategy based on port-based teleportation, which stores the isometry channel in a program state using only n = Theta(1/sqrt{epsilon}) queries, achieving a quadratic improvement over the classical strategy. As an application, we extend our approach to general quantum channels, achieving improved program cost compared to prior results by Gschwendtner, Bluhm, and Winter [Quantum extbf{5}, 488 (2021)].

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2507.10784) | 2026-11-18
