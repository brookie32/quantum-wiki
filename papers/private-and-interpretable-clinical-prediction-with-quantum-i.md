---
title: "Private and interpretable clinical prediction with quantum-inspired tensor train models"
date: "2026-08-28"
updated: "2026-08-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2602.06110"
summary: "arXiv:2602.06110v2 Announce Type: replace-cross Abstract: Publicly available clinical machine learning models pose an underappreciated privacy risk: their parameters or outputs can be exploited to rec"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

arXiv:2602.06110v2 Announce Type: replace-cross Abstract: Publicly available clinical machine learning models pose an underappreciated privacy risk: their parameters or outputs can be exploited to recover information from patients whose data were used during training. Moreover, this risk is exacerbated by models such as logistic regression (LR), which are typically preferred in clinical settings for their transparency. To assess this empirically, we attack LORIS, a publicly available LR model for immunotherapy response prediction hosted on a U.S. government website. From evaluations through its public interface, we recover the model parameters and identify the training cohort with high confidence. More broadly, we design cohort-level membership inference attacks under three levels of adversarial access---binary black-box, continuous black-box, and white-box---and apply them to both LR models and shallow neural networks (NNs) trained on the same task. Our results reveal that even a cohort of 35 patients can be reliably identified within training sets of hundreds to thousands, and that common practices such as cross-validation amplify rather than mitigate this risk. To address these vulnerabilities, we propose a quantum-inspired defense based on tensorizing discretized models into tensor trains (TTs). This representation obfuscates model parameters and preserves accuracy, while offering black-box protection comparable to practical Differential Privacy baselines. Additionally, the TT representations retain LR interpretability and extend it through efficient computation of marginal and conditional distributions, enabling this richer analysis also for black-box models such as NNs. Our results establish tensorization as a practical, post-hoc tool for private, interpretable, and effective clinical prediction.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2602.06110) | 2026-08-28
