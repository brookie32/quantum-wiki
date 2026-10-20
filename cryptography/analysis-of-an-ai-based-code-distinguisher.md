---
title: "Analysis of an AI based code distinguisher"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2556"
summary: "Recently, DeepDistinguisher demonstrated the capability of transformer-like architectures to accurately distinguish Goppa codes from linear codes randomly generated, outperforming traditional distingu"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Recently, DeepDistinguisher demonstrated the capability of transformer-like architectures to accurately distinguish Goppa codes from linear codes randomly generated, outperforming traditional distinguishers in certain settings. The purpose of our research is to examine the working mechanism of the mentioned machine learning algorithm. In particular, we explore the performance of the distinguisher using saliency maps and attention visualization techniques. We first identify a low-weight-row artifact present in the random instances used during training and show that the model partially relies on this feature. After removing this artifact, the distinguisher still achieves significant accuracy, suggesting the use of more structural properties. Inspired by the constraints induced by the minimum distance of Goppa codes, we proposed a rule based on pairwise XOR operation between the rows of the generator matrix. Our experiments have shown that the predictions made by DeepDistinguisher and XOR-based rule are highly correlated especially for high-rate codes. Furthermore, when evaluated on random matrices satisfying both the minimum distance and XOR constraints, the neural distinguisher loses most of its predictive power. This suggests that transformer-based architectures exploit general combinatorial properties of a code rather than some hidden underlying algebraic structure.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2556) | 2026-10-19
