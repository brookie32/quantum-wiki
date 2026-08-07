---
title: "Classical Noise Inversion for Error-Propagatable Circuits with Minimal Overhead under General Gate-Dependent Noise"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2510.20686"
summary: "arXiv:2510.20686v2 Announce Type: replace Abstract: Quantum error mitigation (QEM) is critical for extracting reliable computations from noisy quantum processors, proving itself essential not only in "
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2510.20686v2 Announce Type: replace Abstract: Quantum error mitigation (QEM) is critical for extracting reliable computations from noisy quantum processors, proving itself essential not only in the near term but also as a valuable supplement to fully fault-tolerant systems in the future. Despite the necessity, practical QEM deployment still confronts challenges, including the excessive cost of sampling quantum circuits and reliance on unrealistic assumptions such as gate-independent noise. In this paper, we propose Classical Noise Inversion (CNI), which shifts the QEM from sampling diverse quantum circuits to repeated single-circuit measurement, a drastic cost reduction given that the former incurs far heavier time overhead than the latter on realistic quantum hardware. We target general noise models and establish critical conditions for their classical tractability, under which CNI remains effective. For noise models that violate the condition, we propose partial CNI, which mitigates the classically tractable factor of noise via CNI and mitigates the other part via probabilistic error cancellation tailored to gate-dependent noise. To minimize the sampling overhead, we introduce noise compression, which groups noise components with equivalent effects on measurement outcomes, thereby attaining theoretically optimal error-mitigation overhead. The proposed protocols are particularly efficient for error-propagatable circuits, including adaptive universal quantum computing represented by Clifford+T fault-tolerant circuits, and generalized measurement represented by classical shadows. To demonstrate the practical merits of CNI, we integrate it with thrifty classical shadow, and use analysis and numerical simulations to show its advantages in both efficiency and accuracy over existing approaches.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2510.20686) | 2026-08-07
