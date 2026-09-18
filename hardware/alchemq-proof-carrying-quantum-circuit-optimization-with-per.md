---
title: "AlchemQ: Proof-Carrying Quantum Circuit Optimization with Per-Result Equivalence Certificates"
date: "2026-09-18"
updated: "2026-09-18"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.19160"
summary: "arXiv:2609.19160v1 Announce Type: new Abstract: We present AlchemQ v0.5, a proof-of-concept system that couples an untrusted beam-search optimizer with a machine-checkable per-result certification lay"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

arXiv:2609.19160v1 Announce Type: new Abstract: We present AlchemQ v0.5, a proof-of-concept system that couples an untrusted beam-search optimizer with a machine-checkable per-result certification layer and a versioned certificate protocol (0.2.0), so that every optimized circuit ships with a verifiable artifact rather than a bare claim. The certifier proves equivalence up to global phase by ZX-calculus full reduction, with a numeric-tensor fallback based on the optimal Hilbert-Schmidt overlap. Certificates are self-contained and tamper-evident: canonical gate-canon-v1 hashes, measured residuals, tri-state verdicts (certified/rejected/inconclusive), and versioned phase-note schemas for cross-platform reproducibility. The agent aggregates three fuzzy t-norms, cannot return an uncertified circuit, and since v0.4 guarantees no componentwise regression against the original. On a benchmark of 100 circuits, all 400 optimizations terminate without error, every returned circuit is certified, every mutation is detected, and a 2998-test suite passes on two platforms. The PyZX baseline is strong (21.4% mean T-count reduction over 82 circuits) and the agent is strictly better on 9/100; the three t-norms return identical circuits on all 100 standard instances, diverging only on 4/38 of an adversarial suite. Two case studies are new: a false negative root-caused to a pivot-normalization bug in PyZX's compare_tensors (pivot 4.7e-9; the optimal-overlap residual is 7.4e-11), and eight certificates rejected on macOS due to BLAS-dependent floats in phase_note. Both were fixed; all artifact sets validate 400/400 on both platforms. A pilot run on IBM Heron r2 gives a certified circuit 78% shallower with 65% fewer two-qubit gates; output quality favors it on all three metrics but is not significant at 1024 shots. We release the certificate specification and a standalone reference verifier (Apache-2.0) with data and scripts; the engine is proprietary.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.19160) | 2026-09-18
