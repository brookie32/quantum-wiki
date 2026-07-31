---
title: "Auditing Question-Order Effects in Large Language Models with the QQ Equality: Mechanism Characterization and a Saturation Caveat"
date: "2026-07-31"
updated: "2026-07-31"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.17219"
summary: "arXiv:2607.17219v2 Announce Type: replace-cross Abstract: Question-order effects in human survey data have been reported to approximately satisfy the QQ (quantum question) equality, a parameter-free p"
last_verified: "2026-07-31"
review_by: "2026-10-29"
stale: false
---

arXiv:2607.17219v2 Announce Type: replace-cross Abstract: Question-order effects in human survey data have been reported to approximately satisfy the QQ (quantum question) equality, a parameter-free prediction of the standard projective quantum question-order model. We develop this equality into an audit framework for sequential binary judgments of autoregressive large language models (LLMs). Theoretically, we characterize mechanism families that satisfy QQ robustly, show that classical repetition can reproduce the equality exactly, and combine QQ with the rank-2 Contextuality-by-Default criterion through |q_{QQ}| le OSS. This separates order sensitivity, QQ imbalance, and residual contextuality rather than treating them as interchangeable signatures. Methodologically, we introduce a committed multi-turn forced-branch protocol that reconstructs order-conditioned joint distributions from next-token log-probabilities under counterbalanced label mappings and pre-specified health gates. A first-signal pilot on an open-weight instruction-tuned model reveals the central measurement problem. Although all pre-specified health gates passed, the binary-conditioned distributions were near-deterministic for 17 of 18 item pairs under the direct-evaluation framing and 7 of 8 under the persona framing. Label assignment materially changed several mapping-specific QQ verdicts, and no item was certified as residually contextual. Thus, under the tested conditions, the observed QQ outcomes did not uniquely identify a response mechanism in the presence of a saturated and label-sensitive measurement interface. The main implication is methodological: next-token probabilities should not be interpreted as survey-response distributions without first establishing adequate dispersion. We therefore argue that saturation screening and label counterbalancing should precede structural interpretation in distribution-level audits of LLM judgments.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.17219) | 2026-07-31
