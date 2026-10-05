---
title: "Learning Noise-Robust Stabilizer Structure via Bell Sampling"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.03307"
summary: "arXiv:2610.03307v1 Announce Type: new Abstract: Bell sampling efficiently learns the stabilizer group, and hence the stabilizer nullity, of pure states with little magic, a primitive underlying tomogr"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.03307v1 Announce Type: new Abstract: Bell sampling efficiently learns the stabilizer group, and hence the stabilizer nullity, of pure states with little magic, a primitive underlying tomography and certification of low-magic states. Real devices, however, only prepare noisy images of the target, which we model as a Pauli channel acting on the ideal state; the resulting noisy state generically has no exact Pauli stabilizers. Existing structure learners for mixed states rely on such exact stabilizers. Agnostic tomography does not, but its guarantees scale exponentially in the nullity t. We show that the ideal stabilizer group remains encoded in the noisy state as the set of Pauli operators under which it is invariant. We give Bell-sampling algorithms that learn the group to accuracy arepsilon for states of nullity at most t. The difficulty is that noisy samples break the group structure pure-state learners rely on, so more samples can erase structure rather than reveal it. We resolve this with a finder-verifier scheme that extracts stabilizer structure from partially corrupted sample batches while certifying proposed updates. For sufficiently weak global depolarizing noise, both samples and runtime are poly(n,t,1/arepsilon) when the channel's total error probability is at most of order arepsilon n/t. Up to a constant total error probability (approx 0.16), samples remain polynomial while classical processing costs 2^t, and for any error probability below one a 4^t overhead suffices. Arbitrary Pauli channels exhibit the same three regimes, with more restrictive thresholds. For weak Pauli noise, this closes much of the gap between agnostic learners such as stabilizer bootstrapping and polynomial pure-state algorithms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.03307) | 2026-10-05
