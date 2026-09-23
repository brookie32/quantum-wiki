---
title: "A Quantum Phase-based Comparator"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.25262"
summary: "arXiv:2609.25262v1 Announce Type: new Abstract: Quantum comparators decide the order of two operands. They rely on reversible logic acting on basis-encoded integers, so their width grows with the prec"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.25262v1 Announce Type: new Abstract: Quantum comparators decide the order of two operands. They rely on reversible logic acting on basis-encoded integers, so their width grows with the precision. We introduce the Quantum Phase-based Comparator (QPC), which compares two values carried in relative phases instead. The circuit places the two phases, entered with opposite signs, between a pair of Hadamard gates, and a fixed offset centers the interference, so that the probability of measuring zero falls below one half exactly when the first phase is the smaller. We give two implementations. With hard-coded values, the two values are written into the parameters of two phase gates, and the comparison costs one qubit and five gates. With the register-driven cascade, the values are drawn from two t-qubit registers through binary-weighted controlled-phase gates, at a cost of one qubit beyond the registers and depth linear in t; since the cascade induces each phase linearly from the register content, one circuit handles a superposition of operand pairs. The readout yields a biased coin rather than a definite bit, and we quantify the shots that a decision takes at a given phase separation. Scaling both phases by an integer widens the decision margin at no cost in width or depth, and an adaptive doubling schedule turns this amplification into a shot count logarithmic in the inverse separation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.25262) | 2026-09-23
