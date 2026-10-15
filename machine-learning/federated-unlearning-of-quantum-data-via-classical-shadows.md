---
title: "Federated Unlearning of Quantum Data via Classical Shadows"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.19077"
summary: "arXiv:2610.19077v1 Announce Type: new Abstract: Quantum federated learning trains a quantum neural network (QNN) across nodes that hold quantum data, such as the states of quantum sensors. To forget d"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

arXiv:2610.19077v1 Announce Type: new Abstract: Quantum federated learning trains a quantum neural network (QNN) across nodes that hold quantum data, such as the states of quantum sensors. To forget data, unlearning methods for quantum models replay them, and federated unlearning from stored updates removes whole nodes only. Quantum data cannot be replayed, since a state is consumed when measured and cannot be cloned. We propose Shadow-based Data Erasure (SHADE), in which each node records a classical shadow of every training state, a few randomized single-qubit measurements taken at training time. The gradient and curvature of a QNN on a state are expectations of observables, so SHADE estimates them for the forget data from the shadows at any later parameters and removes their effect by a federated Newton correction. Only classical estimates cross the network. We prove that the shadow size needed for a target unlearning error grows exponentially in the size of the backward light cone of the measured observable and not in the number of qubits. In simulation with 50 nodes and on edge boards, SHADE matches the forget accuracy of retraining within 0.5 points, without replay and in under 0.2 s.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.19077) | 2026-10-15
