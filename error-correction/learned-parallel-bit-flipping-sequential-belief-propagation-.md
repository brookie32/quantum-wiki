---
title: "Learned Parallel Bit-Flipping Sequential Belief Propagation Decoding of Quantum LDPC Codes"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.01068"
summary: "arXiv:2610.01068v1 Announce Type: new Abstract: Quantum low-density parity-check (QLDPC) codes are promising candidates for low-overhead fault-tolerant quantum computation, but their practical use req"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.01068v1 Announce Type: new Abstract: Quantum low-density parity-check (QLDPC) codes are promising candidates for low-overhead fault-tolerant quantum computation, but their practical use requires fast, low-complexity, and reliable decoders. Belief propagation (BP) is attractive because of its local message-passing structure, yet standard flooding BP often suffers from convergence failures on QLDPC codes due to short cycles, degeneracy, and symmetric decoding trajectories. Learned sequential BP improves convergence by using a reinforcement-learning policy to choose variable-node update orders, but a single learned trajectory can still be sensitive to unfavorable local Pauli decisions. We propose a learned parallel bit-flipping sequential BP decoder with a new quaternary score combining syndrome gain, a quantized Pauli log-likelihood penalty, and Q-table lookahead at hypothetical post-flip states. Our decoder first runs learned sequential BP for a fixed number of iterations. If the syndrome is not satisfied, it constructs quaternary bit-flipping candidates, each corresponding to changing the current Pauli decision of one qubit. The selected candidates initialize independent learned sequential BP continuations from the same decoder state. Since these continuations are independent, they can be executed in parallel, so testing several candidates mainly increases parallel hardware resources rather than sequential decoding latency. Simulations on representative QLDPC codes over the depolarizing channel show that the proposed decoder improves the reliability of learned sequential BP while having a parallel low-latency structure.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.01068) | 2026-10-02
