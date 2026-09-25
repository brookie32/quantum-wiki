---
title: "Efficient Record-and-Replay Arithmetic for Quantum Elliptic-Curve Point Addition"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.28882"
summary: "arXiv:2609.28882v1 Announce Type: new Abstract: We study reversible secp256k1 point-addition circuits developed through ECDSA.Fail for Shor's elliptic-curve discrete-logarithm algorithm. Two complemen"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.28882v1 Announce Type: new Abstract: We study reversible secp256k1 point-addition circuits developed through ECDSA.Fail for Shor's elliptic-curve discrete-logarithm algorithm. Two complementary constructions improve record-and-replay GCD arithmetic: Jump-2 groups binary-GCD steps and compresses their decisions using base-5 encoding, while ping-pong uses fixed register alternation and one-bit decisions to avoid full-width comparisons and data-dependent swaps. Fused replay combines doubling and signed addition into one modular correction. Both constructions support quantum-addressed window selection with measurement-based lookup cleanup. We compare three circuits on 100,000 fresh inputs across nine lookup-table configurations. A separately tested repair uses 1,419 qubits and 1.356 million mean executed Toffolis, with no detected failures on another 100,000 inputs. Structured supported-input counterexamples remain, so these tests do not establish all-input correctness. We also provide conditional coherent-error analysis and reversible safegcd comparisons. Under the stated window allowance, repaired-circuit resources lie below Google's low-gate caps and Schrottenloher's low-gate estimates, but differing accounting and correctness evidence preclude formal dominance. The results concern individual window-selected additions, not complete Shor computations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.28882) | 2026-09-25
