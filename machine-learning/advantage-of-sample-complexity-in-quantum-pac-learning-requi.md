---
title: "Advantage of Sample Complexity in Quantum PAC Learning Requires Inverse Access to State-Preparation Unitaries"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "machine-learning"
tags: [machine-learning, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.38403"
summary: "arXiv:2609.38403v1 Announce Type: new Abstract: Whether quantum computation can reduce the amount of data sampled from an unknown probability distribution required to learn a prediction rule is a fund"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.38403v1 Announce Type: new Abstract: Whether quantum computation can reduce the amount of data sampled from an unknown probability distribution required to learn a prediction rule is a fundamental question in quantum machine learning. Quantum PAC learning studies this question using quantum data as a quantum state whose squared amplitudes encode the unknown distribution from which classical learning data are sampled. With only copies of such quantum data, the optimal worst-case sample complexity asymptotically matches that of classical PAC learning. In contrast, access to both a state-preparation unitary for this state and its inverse can improve the query-complexity dependence on the accuracy parameter in realizable learning. However, it has remained unclear whether forward-only access allows such an improvement. In this work, taking the worst case over compatible state-preparation unitaries and their finite ambient dimensions, we show that the optimal forward-only query complexities of realizable and agnostic learning are, respectively, Theta((d+log(1/elta))/arepsilon) and Theta((d+log(1/elta))/arepsilon^2), where d is the VC dimension of the concept class, arepsilon the accuracy parameter, and elta the failure probability. These bounds match the optimal sample complexities with classical data or quantum data copies. To prove them, we establish a reduction using q copies of the prepared state to approximate the Haar-averaged output of any q-query forward-only algorithm. These results show that forward-only access cannot provide an asymptotic query-complexity advantage over learning from classical data or quantum data copies in this worst-case setting, and establish the essential role of inverse access in the known realizable-setting improvement. Our reduction also provides a new framework for analyzing limitations of forward state-preparation access via state-copy lower bounds.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.38403) | 2026-10-01
