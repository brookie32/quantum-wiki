---
title: "Finite-Batch q-ary OT Extension for High-Arity Private Lookup: Certified Radix--Code Co-Design"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2734"
summary: "High-arity oblivious transfer is a natural abstraction for private lookup: a elta-bit table address selects one entry out of 2^elta candidates. This paper characterizes the finite-batch design space o"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

High-arity oblivious transfer is a natural abstraction for private lookup: a elta-bit table address selects one entry out of 2^elta candidates. This paper characterizes the finite-batch design space of the CCG q-ary OT-extension family and derives certified radix-selection rules. For q=2^r, we formulate radix-code selection as a security-constrained discrete optimization problem that accounts for subfield-check padding, code dimension, required distance, base-OT count, and q-ary symbol width. We derive exact communication thresholds showing when reduced base OTs can compensate for larger q-ary encoding cost. Then we convert the Griesmer bound into communication lower bounds, yielding certificates for regions where non-binary radices cannot improve communication, are provably beneficial, or remain dependent on better code constructions. Finally, we instantiate the framework with simplex and BCH constructions and CodeTables entries, and verify the selected elta=12 codes with Magma.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2734) | 2026-11-03
