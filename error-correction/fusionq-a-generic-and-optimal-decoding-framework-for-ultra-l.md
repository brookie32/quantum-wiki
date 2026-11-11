---
title: "FusionQ: A Generic and Optimal Decoding Framework for Ultra-Low-Latency Quantum Error Correction"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.13111"
summary: "arXiv:2611.13111v1 Announce Type: new Abstract: Quantum error correction (QEC) decoding has traditionally been organized around fixed decoding instances: a monolithic space-time detector error model ("
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.13111v1 Announce Type: new Abstract: Quantum error correction (QEC) decoding has traditionally been organized around fixed decoding instances: a monolithic space-time detector error model (DEM), or a predetermined temporal window, is handed to a backend decoder after enough syndrome data has arrived. This paper presents FusionQ, a fusion decoding framework that changes this paradigm by deriving local decoding tasks from the observed syndrome and then fusing their results into a single global correction. Instead of forcing every shot through the same global or windowed problem, FusionQ builds open-boundary local DEMs around fired detector clusters and expands the corresponding footprints only when a local optimum uses virtual boundary errors. FusionQ is generic in the decoder backend: the scheduler requires only a local solution and a boundary-use flag, so exact solvers, matching-style decoders on graphlike DEMs, and heuristic decoders can share the same runtime. We prove a compositional optimality theorem: with an exact minimum-weight local backend and boundary-free publication, fusing the published local decoding results yields a global most-likely error (MLE) solution of the original DEM. Our evaluation shows that, with an exact backend, FusionQ matches the monolithic MLE result on every shot. Across decoder backends, FusionQ substantially reduces decoding latency by overlapping local decoding with hardware syndrome acquisition.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.13111) | 2026-11-11
