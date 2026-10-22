---
title: "CoDecoder: Make Quantum Decoders Up to 100x Faster and Even More Accurate"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.28748"
summary: "arXiv:2610.28748v1 Announce Type: new Abstract: Fault-tolerant quantum computers need fast and accurate error decoding. We present CoDecoder, a small neural frontend that composes with an existing dec"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2610.28748v1 Announce Type: new Abstract: Fault-tolerant quantum computers need fast and accurate error decoding. We present CoDecoder, a small neural frontend that composes with an existing decoder to improve accuracy and reduce mean decoding time. It predicts each shot's logical outcome, retains confident predictions and routes the remaining shots to the unchanged fallback. A logical-operator-aware output head scores shifted logical operators, combining equivalent logical lines on surface codes and deciding logical qubits jointly on bivariate-bicycle (BB) codes. Fused GPU inference and efficient routing reduce the overhead paid on every shot. In registered tests under circuit-level noise, composition reduces failures by 6.4-31.4% relative to correlated matching on surface codes of distance 7-17 and by 22-50% relative to full-DEM Relay-BP on two BB codes, with 2.3-124-fold speed-ups across these comparisons. With our re-implementations of the neural decoder Cascade, composition reduces decoding time in all four settings. A joint decision of both decoders on the routed shots keeps this speed and makes the composition more accurate than Cascade in all four, with 14-18% fewer failures on the [[72,12,6]] code. On the [[72,12,6]] BB code, a conventional head with independent logical outputs fails 3.8-5.0 times as often as our joint class score under matched training conditions. Per-shot analysis shows how composition gains accuracy. On retained shots, the frontend corrects more fallback errors than it introduces, even when it is less accurate overall.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.28748) | 2026-10-22
