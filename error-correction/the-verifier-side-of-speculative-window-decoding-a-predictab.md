---
title: "The verifier side of speculative window decoding: a predictability bracket, a machine-checked blast-radius bound, and a decoder-agnostic recover loop"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.13062"
summary: "arXiv:2607.13062v2 Announce Type: replace Abstract: Speculative window decoders hide quantum error-correction decoder latency by guessing the cross-boundary decisions that link adjacent decoding windo"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2607.13062v2 Announce Type: replace Abstract: Speculative window decoders hide quantum error-correction decoder latency by guessing the cross-boundary decisions that link adjacent decoding windows, running downstream work on the guess, and verifying lazily. SWIPER and ARTERY each build one predictor, about 90% accurate; neither built the verifier side. We build it on a reconstructed SWIPER harness (Stim rotated surface code, minimum-weight matching). A predictor-only bracket shows the cross-boundary decision is local, the achievable accuracy reaching about 0.999 within three rounds, with small, diffuse headroom over SWIPER. We establish a worst-case temporal blast-radius bound, its probability core machine-checked in Lean4 and conditional on a modeling reduction we then test: a misprediction's effect decays exponentially in the commit width, so the radius is one and speculation adds no error floor. We falsify that reduction shot by shot and find the real mechanism, clearest at near-threshold noise, is a global minimum-weight re-pairing. A compiler pass derives SWIPER's restart policy from these numbers; a runtime executor confirms on the harness that the loop recovers exactly and removes the serial commit-chain stall up to a small penalty. A second decoder (union-find) settles which results are decoder-agnostic: the predict-verify-recover wrapper and the structural phenomenology, while the absolute magnitudes and the min-weight mechanism are matching-specific.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.13062) | 2026-07-27
