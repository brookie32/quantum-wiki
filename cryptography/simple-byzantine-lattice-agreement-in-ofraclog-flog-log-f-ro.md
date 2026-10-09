---
title: "Simple Byzantine Lattice Agreement in O(frac{log f}{log log f}) Rounds"
date: "2026-10-07"
updated: "2026-10-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2400"
summary: "Lattice agreement is a relaxed version of the standard consensus problem: correct processes need not decide the same value, but their decisions must be ``comparable''. Namely, every process proposes a"
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

Lattice agreement is a relaxed version of the standard consensus problem: correct processes need not decide the same value, but their decisions must be ``comparable''. Namely, every process proposes a value from a join semi-lattice, and correct processes decide values that (1) lie on a single chain, (2) include their own proposals, and (3) include nothing beyond what was proposed. Lattice agreement has important practical applications, as it underpins atomic snapshot objects and replicated state machines with commutative operations. Yet, the best known protocols decide in O(log f) rounds, where f is an upper bound on the number of faulty processes. In this paper, we break the logarithmic barrier. Namely, we present Join-IT, a synchronous Byzantine lattice agreement protocol that tolerates f < n/3 Byzantine processes and decides in Oig( frac{log f}{log log f} ig) rounds. Join-IT uses no cryptography whatsoever, and its guarantees thus hold against a computationally unbounded adversary. Perhaps surprisingly, Join-IT is also remarkably simple. It sequentially composes two classical primitives: gradecast, which takes three rounds, and approximate agreement, which, at the precision Join-IT requires, takes Oig( frac{log f}{log log f} ig) rounds. A single local step finally turns the output of approximate agreement into comparable decisions, at no additional cost in rounds.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2400) | 2026-10-07
