---
title: "Learning and interpreting policies for simultaneous entanglement requests in quantum networks"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "sensing"
tags: [sensing, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.30157"
summary: "arXiv:2609.30157v1 Announce Type: new Abstract: Future quantum networks will make use of entanglement to perform numerous tasks, such as sending quantum information over long distances, distributed qu"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.30157v1 Announce Type: new Abstract: Future quantum networks will make use of entanglement to perform numerous tasks, such as sending quantum information over long distances, distributed quantum computing, and quantum sensing. In general, these tasks will need to be performed simultaneously in various regions of a network, while minimizing resources and latency. We will thus require policies for scheduling link-level entanglement resources, and using the link-level entanglement to create various forms of multipartite entanglement required for every task. In this work, we address this problem using reinforcement learning. We formulate a Markov Decision Process for the problem and use double deep Q-networks (DQN) with Message Passing Neural Networks (MPNNs), experience replay buffers, and curriculum training to obtain policies. The key physical parameter is the probability of link-level entanglement generation, i.e., the link activation probability. We show that our policies maintain 100% success for up to 71% lower link activation probability than the baseline heuristics for a set of physically relevant network topologies. We then examine an additional constraint where experiment (task) placements are restricted to specific hardware types and demonstrate a similar advantage in performance over heuristics, with our policy maintaining at least an 80% success rate for up to a 59% lower link activation probability. Finally, we explore methods to interpret the learned policy by defining metrics enabling conclusions to be drawn about the model's behavior and by tasking a large language model (LLM) to derive a novel heuristic given example actions taken by the DQN-trained policy. We find that the LLM heuristic performs similarly to the DQN-trained policy in performance, indicating a promising method for interpretable policy extraction for large quantum networks, where direct training becomes computationally expensive.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.30157) | 2026-09-25
