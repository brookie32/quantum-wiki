---
title: "Shor's algorithm requires Fanout"
date: "2026-08-10"
updated: "2026-08-10"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.06703"
summary: "arXiv:2608.06703v1 Announce Type: new Abstract: Shor's algorithm is a canonical quantum supremacy target whose core operation relies on the Quantum Fourier Transform (QFT). We resolve an open question"
last_verified: "2026-08-10"
review_by: "2026-11-08"
stale: false
---

arXiv:2608.06703v1 Announce Type: new Abstract: Shor's algorithm is a canonical quantum supremacy target whose core operation relies on the Quantum Fourier Transform (QFT). We resolve an open question of Fang, Fenner, Green, Homer and Zhang from 2006 by showing that approximating QFT in constant depth, for any n-qubit modulus, necessarily requires the n-qubit Fanout operation. Formally, let mathsf{QFT}_q be the gate acting on n = lceil log q rceil qubits that computes the QFT under modulus q. It is known that any n-qubit mathsf{QFT}_q can be implemented in constant depth using mathsf{FANOUT}_n, i.e. mathsf{QFT}_q in mathsf{QAC}^0_f. We prove the converse by using a mathsf{QFT}_q gate to construct a state of ``non-negligible felinity". Consequently, mathsf{QFT}_q in mathsf{QAC}^0 iff mathsf{FANOUT}_n in mathsf{QAC^0}. In the case of q = 2^n, such as in Shor's, we approximate mathsf{FANOUT}_n using a single mathsf{QFT}_{2^n} gate and O(1) two-qubit local gates, thus tying the feasibility of realizing Shor's algorithm with NISQ circuits to that of Fanout.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.06703) | 2026-08-10
