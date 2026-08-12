---
title: "When Does Quantum Differential Privacy Compose?"
date: "2026-08-12"
updated: "2026-08-12"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.00337"
summary: "arXiv:2601.00337v2 Announce Type: replace Abstract: Composition is a cornerstone of classical differential privacy, enabling strong end-to-end guarantees for complex algorithms through composition the"
last_verified: "2026-08-12"
review_by: "2026-11-10"
stale: false
---

arXiv:2601.00337v2 Announce Type: replace Abstract: Composition is a cornerstone of classical differential privacy, enabling strong end-to-end guarantees for complex algorithms through composition theorems (e.g., basic and advanced). In the quantum setting, however, privacy is defined operationally against arbitrary measurements, and classical composition arguments based on scalar privacy-loss random variables no longer apply. As a result, it has remained unclear when meaningful composition guarantees can be obtained for quantum differential privacy (QDP). In this work, we clarify both the limitations and possibilities of composition in the quantum setting. We first show that classical-style composition fails in full generality for POVM-based approximate QDP: even quantum channels that are individually perfectly private can completely lose privacy when combined through correlated joint implementations. We then identify a setting in which clean composition guarantees can be restored. For tensor-product channels acting on product neighboring inputs, we introduce a quantum moments accountant based on an operator-valued notion of privacy loss and a matrix moment-generating function. Although the resulting Renyi-type divergence does not satisfy a data-processing inequality, we prove that controlling its moments suffices to bound measured Renyi divergence, yielding operational privacy guarantees against arbitrary measurements. This leads to advanced-composition-style bounds with the same leading-order behavior as in the classical theory. Our results demonstrate that meaningful composition theorems for quantum differential privacy require carefully articulated structural assumptions on channels, inputs, and adversarial measurements, and provide a principled framework for understanding which classical ideas do and do not extend to the quantum setting.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.00337) | 2026-08-12
