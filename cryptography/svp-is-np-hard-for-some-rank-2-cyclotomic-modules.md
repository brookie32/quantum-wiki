---
title: "SVP Is NP-Hard for Some Rank-2 Cyclotomic Modules"
date: "2026-09-01"
updated: "2026-09-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1856"
summary: "Let q range over primes congruent to 3 modulo 4. Let zeta_q be a primitive qth root of unity, and put K=Q(zeta_q), with ring of integers O_K=Z[zeta_q]. We prove that the decision version of the Shorte"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

Let q range over primes congruent to 3 modulo 4. Let zeta_q be a primitive qth root of unity, and put K=Q(zeta_q), with ring of integers O_K=Z[zeta_q]. We prove that the decision version of the Shortest Vector Problem (SVP) in the ell_2-norm is NP-complete on full-rank free submodules of O_K^2 by a deterministic polynomial-time many-one reduction from Exact Cover by 3-Sets (X3C). The module rank is fixed at two. As a Z-lattice, the module has rank 2(q-1), which grows with q. The main obstacle is closure under the action of O_K. A module containing a nonzero vector also contains every scalar multiple of that vector by a nonzero element of O_K, and some of these multiples may be shorter. Three ideas overcome this obstacle. First, we map the Bennett--Peikert Reed--Solomon lattice to a principal cyclotomic ideal and use Wan's point-count estimates to prove that a coset of this ideal contains many binary coefficient representatives. Second, a checker based on a quadratic Gauss sum turns the X3C equations into a canonical squared norm. Third, the checker and a second module coordinate combine with a separation bound for ideal cosets to rule out every unintended vector created by the O_K-action. Each constructed instance consists of a prime qequiv3pmod4, two integral generators whose 2imes2 generator matrix has nonzero determinant, and an integer squared threshold. The construction also gives NP-hardness of search-SVP under polynomial-time Turing reductions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1856) | 2026-09-01
