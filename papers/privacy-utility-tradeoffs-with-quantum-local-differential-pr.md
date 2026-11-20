---
title: "Privacy-Utility Tradeoffs with Quantum Local Differential Privacy"
date: "2026-11-20"
updated: "2026-11-20"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.10510"
summary: "arXiv:2602.10510v2 Announce Type: replace Abstract: When sensitive information is encoded in data, it is important to ensure the privacy of information when attempting to learn useful information from"
last_verified: "2026-11-20"
review_by: "2027-02-18"
stale: false
---

arXiv:2602.10510v2 Announce Type: replace Abstract: When sensitive information is encoded in data, it is important to ensure the privacy of information when attempting to learn useful information from the data. There is a natural tradeoff whereby increasing privacy requirements may decrease the utility of a learning protocol. In the quantum setting of differential privacy, such tradeoffs between privacy and utility have so far remained largely unexplored. In this work, we study optimal privacy-utility tradeoffs for both generic and application-specific utility metrics when privacy is quantified by (arepsilon,elta)-quantum local differential privacy. In the generic setting, we focus on optimizing fidelity and trace distance between the original state and the privatized state. We show that the depolarizing mechanism achieves the optimal utility for given privacy requirements. We then study the specific application of learning the expectation of an observable with respect to an input state when only given access to privatized states. We derive a lower bound on the number of samples of privatized data required to achieve a fixed accuracy guarantee with high probability. To prove this result, we employ existing lower bounds on private quantum hypothesis testing, thus showcasing the first operational use of them. We also devise private mechanisms that achieve optimal sample complexity with respect to the privacy parameters and accuracy parameters, demonstrating that utility can be significantly improved for specific tasks in contrast to the generic setting. In addition, we show that the number of samples required to privately learn observable expectation values scales as Theta((arepsilon eta)^{-2}), where arepsilon in (0,1) is the privacy parameter and eta is the accuracy tolerance. We conclude by initiating the study of private classical shadows, which promise useful applications for private learning tasks.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.10510) | 2026-11-20
