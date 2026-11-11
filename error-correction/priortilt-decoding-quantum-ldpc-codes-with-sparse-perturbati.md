---
title: "PriorTilt: Decoding quantum LDPC codes with sparse perturbations of belief propagation priors"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.13373"
summary: "arXiv:2611.13373v1 Announce Type: new Abstract: Although belief propagation (BP) is a widely adopted decoder for classical low-density parity-check (LDPC) codes, its accuracy is limited in the quantum"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13373v1 Announce Type: new Abstract: Although belief propagation (BP) is a widely adopted decoder for classical low-density parity-check (LDPC) codes, its accuracy is limited in the quantum setting. We introduce PriorTilt{}, a variant of BP obtained by selectively perturbing a small fraction of its prior log-likelihood ratios using offsets determined by recent posterior and outgoing-message statistics, while preserving the same message-passing rules. We compare PriorTilt{} with Relay-BP and beam search decoders for circuit-level decoding of three benchmark codes. PriorTilt{} achieves a lower logical error rate (LER) than both baselines at every tested data point. For the [[144,12,12]] Gross code BB144 at noise rate p=10^{-3}, the LER reductions reach 4.3imes relative to Relay-BP and 3.1imes relative to the beam search decoder. At p=10^{-3}, PriorTilt{} has lower mean decoding times than Relay-BP on all three codes and achieves mean decoding speedups of approximately 2.6imes--3.0imes over the beam search decoder. For BB144 at p=10^{-3}, PriorTilt{} achieves an LER approximately 610imes lower than the standard min-sum BP decoder with the same iteration budget, while perturbing fewer than 0.5% of its priors per round on average.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.13373) | 2026-11-11
