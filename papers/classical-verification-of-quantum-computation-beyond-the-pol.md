---
title: "Classical Verification of Quantum Computation Beyond the Polynomial Hierarchy"
date: "2026-10-28"
updated: "2026-10-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.37635"
summary: "arXiv:2610.37635v1 Announce Type: new Abstract: It is not known whether a classical polynomial-time verifier can verify arbitrary polynomial-time quantum computations with an efficient quantum honest "
last_verified: "2026-10-28"
review_by: "2027-01-26"
stale: false
---

arXiv:2610.37635v1 Announce Type: new Abstract: It is not known whether a classical polynomial-time verifier can verify arbitrary polynomial-time quantum computations with an efficient quantum honest prover without computational assumptions. We show that, relative to a classical oracle, such verification is possible for a language beyond the polynomial hierarchy that is decided exactly in quantum polynomial time. The protocol is public-coin, with perfect completeness and soundness error at most 1/4. To our knowledge, no language with such a proof system was previously proved to lie outside AM relative to an oracle. For every unbounded polynomial-time computable function, the oracle can be chosen so that the message count and the oracle query counts of the quantum algorithm, verifier, and honest prover are bounded by this function of the input length. The message count is optimal up to a constant factor, since for a suitable oracle every interactive proof system for the language uses at least a constant fraction of the messages of our protocol on infinitely many lengths, with a constant depending on its verifier. The language is a variant of recursive Fourier sampling in which code tables encode secrets that address data tables. The tables are evaluated recursively, and the oracle stores only the leaves. The quantum algorithm recovers every secret exactly, and the verifier checks the prover's secrets recursively against random code entries. The recursion restricts the input in a correlated way, as the same secret fixes the code bits and chooses the free coordinate, so H{aa}stad's switching lemma does not apply. We prove a switching theorem for these restrictions, which may be of independent interest. For instances of sufficient height, no constant-depth circuit of size 2^{poly(n)} changes its output with probability above 2^{-Omega(n)} when the answer of a random instance is flipped by changing a single leaf.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.37635) | 2026-10-28
