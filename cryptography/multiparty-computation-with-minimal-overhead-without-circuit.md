---
title: "Multiparty Computation with Minimal Overhead without Circuit Transformation"
date: "2026-11-13"
updated: "2026-11-16"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2891"
summary: "A central goal in secure multiparty computation (MPC) is to minimize the gap between the total computation performed by all parties and the cost of insecure circuit evaluation. In the honest majority "
last_verified: "2026-11-16"
review_by: "2027-02-14"
stale: false
---

A central goal in secure multiparty computation (MPC) is to minimize the gap between the total computation performed by all parties and the cost of insecure circuit evaluation. In the honest majority setting, the ideal overhead of widetilde{O}(1) is known to be achievable. However, all prior protocols over prime fields attaining this goal for general circuits relied on the so-called share packing techniques and, as a consequence, required prohibitively expensive circuit transformation steps to impose repetitive structure on the circuit. The only exception is the recent work of Garg, Jain, Mukherjee, and Wang (CRYPTO’24), which introduced a share unpacking technique and obtained the first such protocol without circuit transformation. However, their protocol only applies when the underlying field size is extraordinarily large, in particular, exponential in the *square* of the number of parties. In this work, we present the first MPC protocol with widetilde{O}(1) overhead for any prime field F_p (more generally, any integer ring Z_p) whose size is only required to be n^{Omega(n)}, where n is the number of parties (as opposed to n^{Omega(n^2)}). Technically, we extend the unpacking approach of Garg et al. by developing a new approach to linear randomness extraction over integers, a tool that may be of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2891) | 2026-11-13
