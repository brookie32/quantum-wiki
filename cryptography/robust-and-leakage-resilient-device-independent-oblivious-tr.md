---
title: "Robust and leakage-resilient device-independent oblivious transfer in MiniQCryp"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01421"
summary: "arXiv:2610.01421v1 Announce Type: new Abstract: Assuming post-quantum one-way functions, we construct device-independent (DI) oblivious transfer (OT) and bit commitment: honest parties use only truste"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01421v1 Announce Type: new Abstract: Assuming post-quantum one-way functions, we construct device-independent (DI) oblivious transfer (OT) and bit commitment: honest parties use only trusted classical computation to operate untrusted quantum devices, which may share arbitrary entanglement and behave non-IID. Security is simulation-based against quantum polynomial-time adversaries and composes sequentially with efficient simulators. One protocol skeleton serves both, in two regimes. With isolated laboratories and coordinate-local measurements in the honest receiver's device, it tolerates a constant rate of honest-device faults. With polylogarithmically many qubits of adaptive leakage between the laboratories and arbitrary joint measurements, it tolerates an inverse-polylogarithmic rate. Each elementary DI call uses a fresh, isolated batch of polylogarithmically many device coordinates, and total device use in the compiled OT protocol is polynomial. The commitment has efficient simulators against both parties and yields DI coin tossing with abort. Because OT is complete for secure computation, the construction yields a DI protocol, with abort, for every efficiently computable classical functionality on a fixed number of parties, secure against static corruption of any proper subset of them. The commitment's extractor changes a public parity relation through classical equivocation and leaves the device execution, hence its leakage, unchanged. A commit-and-prove functionality, disjoint audits, and an affine consistency check link the certified correlations to ideal OT. Sender security rests on a selector-aware parallel-repetition bound for the Magic Square game, which we derive from the two-round threshold theorem of Kundu and Tan.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01421) | 2026-10-02
