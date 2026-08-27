---
title: "On Removing Interaction from Quantum Proofs"
date: "2026-08-25"
updated: "2026-08-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1795"
summary: "An important open question in quantum cryptography is the construction of publicly-verifiable NIZKs for QMA. Classically, one can construct NIZKs for NP in the random oracle model (and sometimes in th"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

An important open question in quantum cryptography is the construction of publicly-verifiable NIZKs for QMA. Classically, one can construct NIZKs for NP in the random oracle model (and sometimes in the standard model) by compiling an honest-verifier ZK (HVZK) Sigma-protocol for NP using the Fiat–Shamir transformation. Broadbent and Grilo introduced a quantum analog of a Sigma-protocol (which they call a Xi-protocol) in which the prover's first message is quantum, and show that HVZK Xi-protocols exist for QMA. However, it is not clear how to compile such protocols into NIZKs in the (Q)ROM, because the Fiat–Shamir transformation seems to be incompatible with quantum messages. In this work we give formal evidence that this is indeed the case: we show that if generic "Fiat–Shamir-like" compilers for quantum protocols exist in the QROM (with small completeness and soundness error) then QMA = BQP.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1795) | 2026-08-25
