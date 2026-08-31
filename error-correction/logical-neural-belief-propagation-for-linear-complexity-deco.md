---
title: "Logical Neural Belief Propagation for Linear-Complexity Decoding of Surface Codes"
date: "2026-08-31"
updated: "2026-08-31"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.27682"
summary: "arXiv:2608.27682v1 Announce Type: new Abstract: Quantum error correction (QEC) requires decoders that achieve high logical accuracy while scaling efficiently with the code length. Belief propagation ("
last_verified: "2026-08-31"
review_by: "2026-11-29"
stale: false
---

arXiv:2608.27682v1 Announce Type: new Abstract: Quantum error correction (QEC) requires decoders that achieve high logical accuracy while scaling efficiently with the code length. Belief propagation (BP) is attractive for its linear decoding complexity, but conventional BP decoders often fail to reach sufficient logical accuracy on surface codes. We propose Logical Neural Belief Propagation (L-NBP), a BP-based neural decoder that redirects the decoding objective from physical-level decoding to logical-level decoding. L-NBP first runs a neural BP (NBP) module that produces posterior beliefs, and a logical classifier then transforms these beliefs into a continuous-valued soft syndrome and predicts the logical operator. Because all components in L-NBP are trainable by backpropagation, L-NBP is trained end-to-end, so that the NBP module learns to extract soft syndromes that are favorable for logical classification. On surface codes, L-NBP matches or outperforms the BP with ordered-statistics decoding (BP-OSD) and minimum-weight perfect matching (MWPM) while retaining the linear complexity of BP, and achieves a threshold of 17.5% under depolarizing noise. Moreover, under circuit-level noise, L-NBP matches the accuracy of BP-OSD on the distance-9 surface code while requiring only 0.2% of its complexity. These results show that combining BP, neural weights, and logical-level decoding enables scalable and high-accuracy quantum decoding.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.27682) | 2026-08-31
