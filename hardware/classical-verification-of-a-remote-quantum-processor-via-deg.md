---
title: "Classical Verification of a Remote Quantum Processor via Degenerate Concordant Computations: An Application to Randomness Generation"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.08185"
summary: "arXiv:2610.08185v1 Announce Type: new Abstract: A client who rents a cloud quantum processor cannot easily tell whether the bitstrings it receives came from a quantum device. Certification by random c"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2610.08185v1 Announce Type: new Abstract: A client who rents a cloud quantum processor cannot easily tell whether the bitstrings it receives came from a quantum device. Certification by random circuit sampling runs on present hardware, but scoring each returned sample costs the client time O(2^n). We give a protocol in which the client scores each round in time O(n), built on degenerate concordant ensembles. When a concordant state has a degenerate spectrum, every concordance-preserving gate factorizes as G_t=U_tP_tB_tU_{t-1}^agger, and the block factor B_t, which commutes with the state, cancels from the ensemble while entangling each pure component. The client holds a secret parity whose cosets are the degenerate sectors of every layer, so that it builds the circuit and predicts the ensemble with one inner product per layer. The secret never leaves the client. Inputs are sent uniformly at random, and the client attaches to each round, in its own bookkeeping, the eigenvalue of that input in the hidden state; both verification statistics, an input--output agreement test and a weighted collision test, then compare the server's samples with the non-flat output distribution of the concordant computation. We prove completeness, client efficiency, and soundness in an ideal model in which the compiled circuit reveals nothing about the secret, and we show that the secret must stay hidden: a classical server that holds it passes. For the explicit construction we prove that the single-qubit symmetry test used in efficient simulations of concordant computation fails on non-product inputs with unbiased marginals, and we measure that the local-basis finder of Cable and Browne halts on every layer we tested, that the transmitted component saturates the maximal Schmidt rank, that the circuit is not Clifford, and that matrix-product spoofers are rejected. Soundness of the explicit construction is stated as a conjecture.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.08185) | 2026-10-07
