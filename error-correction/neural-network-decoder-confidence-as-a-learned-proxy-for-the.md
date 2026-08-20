---
title: "Neural network decoder confidence as a learned proxy for the logical gap"
date: "2026-08-20"
updated: "2026-08-20"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.08758"
summary: "arXiv:2606.08758v3 Announce Type: replace Abstract: To utilize quantum error-correcting codes, a decoder must infer the logical sector from the measured syndrome. Beyond a hard logical decision, some "
last_verified: "2026-08-20"
review_by: "2026-11-18"
stale: false
---

arXiv:2606.08758v3 Announce Type: replace Abstract: To utilize quantum error-correcting codes, a decoder must infer the logical sector from the measured syndrome. Beyond a hard logical decision, some decoders provide soft information estimating its reliability. For minimum-weight perfect matching (MWPM), a common confidence measure is the complementary, or logical, gap. Neural-network decoders trained with binary cross entropy naturally output a different score, the logit, whose relation to the matching gap remains unclear. Here, we test whether the logit of a graph neural network (GNN) decoder behaves as a learned proxy for the logical gap. Using a pretrained GNN for the rotated surface code under uniform circuit-level noise [PRR, 7(2):023181, 2025], we compare its logit with the MWPM gap shot by shot on identical syndromes. The native GNN decoder-logit pair yields a lower post-selected logical error rate than the native MWPM decoder-gap pair over the operationally relevant range of acceptance rates. Exchanging the scores between decoders isolates score discrimination from hard-decision accuracy and shows that both contribute to the advantage. At larger distances each score best ranks failures of its own decoder, whereas at small distance, where the bounded matching gap saturates, the learned confidence better discriminates MWPM failures than the gap itself. Finally, GNN confidence is substantially better described by the posterior logistic form implied by an ideal log-likelihood ratio, while the MWPM gap shows systematic departures. Thus, a neural-network decoder trained only on syndromes and logical labels learns a gap-like confidence proxy whose native scale more closely follows the expected posterior calibration form, supporting learned soft output when MWPM gap estimates are unavailable, costly, or insufficiently expressive.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.08758) | 2026-08-20
