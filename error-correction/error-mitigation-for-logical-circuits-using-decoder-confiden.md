---
title: "Error mitigation for logical circuits using decoder confidence"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.15689"
summary: "arXiv:2512.15689v4 Announce Type: replace Abstract: Fault-tolerant quantum computers use decoders to monitor for errors and find a plausible correction. A decoder may provide a decoder confidence scor"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2512.15689v4 Announce Type: replace Abstract: Fault-tolerant quantum computers use decoders to monitor for errors and find a plausible correction. A decoder may provide a decoder confidence score (DCS) to gauge its success. We adopt a swim distance DCS, computed from the shortest path between syndrome clusters. By contracting tensor networks, we compare its performance under phenomenological noise to the well-known complementary gap and find that both reliably estimate the logical error probability (LEP) in a decoding window. We explore ways to use this to mitigate the LEP in entire logical circuits. For shallow circuits, we just abort if any decoding window produces an exceptionally low DCS: for one window of a distance-13 surface code under circuit-level noise, rejecting a mere 0.1% of possible DCS values improves the window's mean LEP by more than 5 orders of magnitude. For larger algorithms comprising up to billions of windows, DCS-based rejection remains effective for enhancing observable estimation. Moreover, one can use the DCS to assign each circuit's output a unique LEP, and use it as a basis for maximum likelihood estimation. This can reduce the effects of noise by an order of magnitude at no quantum cost; we explore the combination of these methods.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.15689) | 2026-10-01
