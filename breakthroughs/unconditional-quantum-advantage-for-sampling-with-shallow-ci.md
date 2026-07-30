---
title: "Unconditional Quantum Advantage for Sampling with Shallow Circuits"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2301.00995"
summary: "arXiv:2301.00995v5 Announce Type: replace Abstract: Recent work by Bravyi, Gosset, and Koenig showed that there exists a search problem that a constant-depth quantum circuit can solve, but that any co"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2301.00995v5 Announce Type: replace Abstract: Recent work by Bravyi, Gosset, and Koenig showed that there exists a search problem that a constant-depth quantum circuit can solve, but that any constant-depth classical circuit with bounded fan-in cannot. They also pose the question: Can we achieve a similar proof of separation for an input-independent sampling task? In this paper, we show that the answer to this question is yes when the number of random input bits given to the classical circuit is bounded. We introduce a distribution D_{n} over {0,1}^n and construct a constant-depth uniform quantum circuit family {C_n}_n such that C_n samples from a distribution close to D_{n} in total variation distance. For any elta < 1 we also prove, unconditionally, that any classical circuit with bounded fan-in gates that takes as input kn + n^elta i.i.d. Bernouli random variables with entropy 1/k and produces output close to D_{n} in total variation distance has depth Omega(log log n). This gives an unconditional proof that constant-depth quantum circuits can sample from distributions that can't be reproduced by constant-depth bounded fan-in classical circuits, even up to additive error. We also show a similar separation between constant-depth quantum circuits with advice and classical circuits with bounded fan-in and fan-out, but access to an unbounded number of i.i.d random inputs. The distribution D_n and classical circuit lower bounds are inspired by work of Viola, in which he shows a different (but related) distribution cannot be sampled from approximately by constant-depth bounded fan-in classical circuits.



## Related
- [[the-impact-of-qubit-connectivity-on-quantum-advantage-in-noi|The Impact of Qubit Connectivity on Quantum Advantage in Noisy IQP Circuits]]
- [[hardness-and-complexity-transition-of-noisy-random-circuit-s|Hardness and Complexity Transition of Noisy Random Circuit Sampling]]
- [[matrix-product-state-approach-to-lossy-boson-sampling-and-no|Matrix product state approach to lossy boson sampling and noisy IQP sampling]]
- [[pilot-wave-simulator-exact-classical-sampling-from-ideal-and|Pilot-Wave Simulator: Exact Classical Sampling from Ideal and Noisy Quantum Circuits up to Hundreds of Qubits]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2301.00995) | 2026-07-27
