---
title: "ProtocolMatch: Protocol-Dependent Model Selection for Scientific Dynamics Forecasting"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.10239"
summary: "arXiv:2610.10239v1 Announce Type: cross Abstract: Scientific dynamics forecasting is often framed as an architecture choice, although deployment is also determined by observed history, rollout feedbac"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.10239v1 Announce Type: cross Abstract: Scientific dynamics forecasting is often framed as an architecture choice, although deployment is also determined by observed history, rollout feedback, compute budget, physical objective, and test distribution. We formulate protocol-dependent model selection and introduce ProtocolMatch, a compute-matched, validation-selected, and failure-preserving evaluation framework. On driven quantum-spin dynamics, we compare recurrent, patched-attention, causal-attention, and low-rank linear predictors across three independently generated datasets. The causal-attention--recurrence ordering reverses as the training set grows within a fixed two-spin task, while a linear predictor has the lowest mean error in the six-spin local-observable comparison. Restricting observed history worsens every refreshed-history view but improves every closed-loop view in the four-spin study. A latest-state MLP has lower error than persistence on every dataset under state refresh across all five cells, yet its closed-loop rank varies by system and includes finite explosive errors. Physical penalties improve targeted consistency without reliably improving prediction error, and in-distribution intervals lose most coverage after a driving-frequency shift. Thus scientific model selection should return a predictor with its protocol and report accuracy, physical validity, and shifted-distribution reliability separately.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.10239) | 2026-10-08
