---
title: "Decoder-Prior Poisoning in Quantum Error Correction: Attacks and PriorGuard Defense"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.27805"
summary: "arXiv:2609.27805v1 Announce Type: new Abstract: Quantum error correction (QEC) protects quantum computations by repeatedly measuring stabilizer syndromes and using a classical decoder to infer correct"
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

arXiv:2609.27805v1 Announce Type: new Abstract: Quantum error correction (QEC) protects quantum computations by repeatedly measuring stabilizer syndromes and using a classical decoder to infer corrections. Modern surface-code decoders are increasingly calibration-aware: they use recent device behavior to set priors such as matching-graph edge probabilities, and these priors directly shape the selected correction. We identify the prior-update path as an overlooked integrity-critical attack surface: a poisoned prior can change decoding decisions even when the syndrome stream, logical labels, and decoder implementation are unchanged. This makes prior poisoning different from ordinary syndrome anomalies and difficult for raw syndrome-anomaly tests to detect. We introduce PriorGuard, a lightweight semantic guard that checks proposed prior changes on high-influence detector-graph entries against private syndrome-derived evidence, accepts updates only when their log-odds movement is evidence-supported, and otherwise falls back to the last evidence-supported prior. We evaluate on Stim-generated rotated surface-code memory circuits decoded with PyMatching. Prior influence is highly concentrated, with the top 10 percent of entries carrying over 60 percent of positive logical-error influence; poisoning only 6.4 percent of decoder-prior entries can raise logical error rate (LER) by 3.35x. PriorGuard recovers most attack-induced loss with a low false-positive rate and modest update-boundary overhead of about 1.7--1.8 ms and less than 0.31 MB auxiliary memory per update.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.27805) | 2026-09-24
