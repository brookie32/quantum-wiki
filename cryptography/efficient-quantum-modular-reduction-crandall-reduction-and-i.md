---
title: "Efficient Quantum Modular Reduction: Crandall reduction and its Fault-tolerant resource analysis"
date: "2026-08-13"
updated: "2026-08-13"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.11563"
summary: "arXiv:2608.11563v1 Announce Type: new Abstract: Modular arithmetic is central to quantum algorithms for cryptographic problems, including Shor's algorithm and Grover-based cryptanalysis, with modular "
last_verified: "2026-08-13"
review_by: "2026-11-11"
stale: false
---

arXiv:2608.11563v1 Announce Type: new Abstract: Modular arithmetic is central to quantum algorithms for cryptographic problems, including Shor's algorithm and Grover-based cryptanalysis, with modular reduction contributing substantially to circuit cost. Pseudo-Mersenne moduli q=2^n-c allow classical Crandall reduction to replace division with folding and constant arithmetic, providing a structural opportunity for more efficient quantum modular reduction than Barrett reduction. We translate this advantage into a reversible quantum setting by deriving explicit folding and normalization conditions for 2n-bit inputs. To the best of our knowledge, this constitutes the first exact reversible quantum circuit formulation of Crandall reduction. Based on this formulation, we develop two variants: Crandall reduction-1 is designed to minimize execution cost through one-step normalization, whereas Crandall reduction-2 uses two-step normalization to support a wider range of c with limited overhead. Logical resource estimates show that both variants require fewer qubits and lower T-count and T-depth than optimized folding Barrett reduction. At n=10, Crandall reduction-1 reduces both T-count and T-depth by approximately 46.9% relative to optimized folding Barrett reduction. Surface-code analysis further shows that, at n=20 under the Sparse Blossom decoder, the estimated runtimes of the two variants are 30.05 ms and 35.39 ms, respectively, compared with 53.77 ms for optimized folding Barrett reduction. These results demonstrate the practical value of exploiting modulus-specific arithmetic structure in fault-tolerant quantum circuit design.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.11563) | 2026-08-13
