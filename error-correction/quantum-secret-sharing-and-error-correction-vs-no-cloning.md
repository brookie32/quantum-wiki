---
title: "Quantum Secret Sharing and Error Correction vs No-Cloning"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.00441"
summary: "arXiv:2610.00441v1 Announce Type: new Abstract: Secret sharing is ubiquitous throughout cryptography. All possible access structures are classically feasible, and in the case of threshold access struc"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.00441v1 Announce Type: new Abstract: Secret sharing is ubiquitous throughout cryptography. All possible access structures are classically feasible, and in the case of threshold access structures, the protocols are even very efficient. However, when moving to the quantum setting, the no-cloning theorem shows that many access structures are impossible. In fact, no-cloning exactly characterizes feasibility: for thresholds, quantum secret sharing is possible if and only if the threshold t is strictly more than n/2. In this work, we propose a variant of quantum secret sharing (QSS) where two or more identical copies of the input state are provided, but the output is only required to recover one copy. This notion circumvents the simple one-copy no-cloning obstruction, though the natural k-copy generalization still gives much milder obstructions. For thresholds using k copies, no-cloning implies that QSS is impossible whenever tleq n/(k+1). It is tempting to hypothesize that no-cloning continues to exactly characterize the many-copy case. However, we show that this is not the case. We give positive results showing that multiple copies allow for going slightly beyond the single-copy obstruction: for thresholds, we construct QSS whenever t>(n-k+1)/2. On the other hand, we give a novel obstruction we call the Clique Path obstruction, which applies to arbitrary access structures. For thresholds, it shows that QSS is impossible whenever tleq (n-1)/k. Our upper and lower bounds exactly match for k=2. Both our results leverage connections to the k-colorability of certain graphs derived from the access structure. We leave closing the gap for kgeq 3 copies as a fascinating direction for future work. Secret sharing is closely related to error correction, which can also be considered in the many-copy setting. Our results imply similar obstructions for quantum error correction for erasure channels.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.00441) | 2026-10-02
