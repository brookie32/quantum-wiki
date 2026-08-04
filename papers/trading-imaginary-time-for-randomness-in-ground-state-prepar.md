---
title: "Trading Imaginary Time for Randomness in Ground State Preparation"
date: "2026-08-04"
updated: "2026-08-04"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.00443"
summary: "arXiv:2608.00443v1 Announce Type: new Abstract: Imaginary-time evolution (ITE) is a foundational method for ground state preparation on quantum computers. However, because ITE is non-unitary, existing"
last_verified: "2026-08-04"
review_by: "2026-11-02"
stale: false
---

arXiv:2608.00443v1 Announce Type: new Abstract: Imaginary-time evolution (ITE) is a foundational method for ground state preparation on quantum computers. However, because ITE is non-unitary, existing implementations incur a sample complexity and/or classical cost that scales exponentially with the target imaginary time eta. Moreover, the state itself converges slower than the energy, making accurate estimation of arbitrary ground state observables even more expensive. In this work, we improve upon standard ITE by introducing twirled imaginary-time evolution (TITE), which pairs ITE with real-time evolution applied for a random duration drawn from a carefully designed distribution. We prove that this randomization quadratically suppresses the trace distance to the ground state, and thus also the error of arbitrary observables, which allows roughly half of the imaginary time to be replaced with real-time evolution (eta mapsto eta/2) while maintaining the same level of accuracy. Because real-time evolution is unitary and does not incur an overhead in sample complexity or classical computation, this affords a quadratic reduction in the cost of any black-box ITE implementation, including Trotterization and quantum imaginary-time evolution. We demonstrate the efficiency of our algorithm in noisy circuit-level simulations of a non-integrable Ising chain, showing substantial improvements over standard ITE.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.00443) | 2026-08-04
