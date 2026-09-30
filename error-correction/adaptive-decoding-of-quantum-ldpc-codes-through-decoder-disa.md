---
title: "Adaptive decoding of quantum LDPC codes through decoder disagreement"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.37629"
summary: "arXiv:2609.37629v1 Announce Type: new Abstract: Accurate decoding of quantum low-density parity-check (qLDPC) codes often relies on expensive post-processing search, although decoding difficulty varie"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2609.37629v1 Announce Type: new Abstract: Accurate decoding of quantum low-density parity-check (qLDPC) codes often relies on expensive post-processing search, although decoding difficulty varies strongly between syndromes. We find that the benefit of deeper post-processing search is highly concentrated in a small subset of decoding instances, and that these instances can be identified directly from the decoder itself. To this end, we introduce an adaptive decoder based on belief propagation (BP) and ordered-statistics decoding (OSD), using the disagreement between the BP hard decision and the syndrome-consistent order-zero OSD solution as an internal risk signal to determine where deeper search is required. On a [[144,12,12]] bivariate bicycle code under circuit-level depolarising noise, encoding 12 logical qubits in 144 data qubits with distance 12, escalating only the highest-risk 20% of instances recovers 85% to 92% of the improvement in logical error rate available from a full one-free-variable sweep, while reducing the mean serial decoding cost by a factor of 3.6 relative to applying the same truncated search to every instance. At matched budget, disagreement-guided routing also outperforms routing based on the BP syndrome residual, syndrome weight and random selection. The same behaviour reappears on a structurally distinct radial qLDPC code obtained from a lifted-product construction, where escalating 20% of instances recovers 87% to 94% of the available gain. A Z-memory experiment on the Quantinuum H2 trapped-ion processor, implementing both X-type and Z-type checks, further shows that the signal remains predictive under device noise. These results show that decoder-internal disagreement can expose where additional decoding effort is valuable, allowing classical computation to be concentrated on the instances most likely to benefit from it.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.37629) | 2026-09-30
