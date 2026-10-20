---
title: "Quantum State Search with Classical Interactive Advice"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "hardware"
tags: [hardware, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2535"
summary: "We study whether a quantum verifier can find a hidden quantum state by exchanging classical messages with an unbounded prover who knows the state. The verifier has access to a reflection oracle about "
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

We study whether a quantum verifier can find a hidden quantum state by exchanging classical messages with an unbounded prover who knows the state. The verifier has access to a reflection oracle about the target. For a Haar-random n-qubit target, we prove that achieving constant average fidelity with the target requires (q+1)^2(B+1)=Omega(2^n), where q is the number of verifier queries and B is the total prover-to-verifier communication. The bound allows arbitrary classical interaction and unrestricted computation between queries. Our proof extends the lower bound of Aaronson and Kuperberg from a single classical proof to an arbitrary classical interaction. As a result, we obtain a quantum-oracle separation of UniqueQMA from QCIP with polynomially many classical messages. In particular, we give a unitary oracle U such that there exists a language LinUniqueQMA^{U} but LnotinQCIP^{U}. We further give an oracle construction for a notion known as QMA-QCIP[2] gap problem. This gives average case hardness for a QMA language under classical access to a QCIP[2] decision oracle and is used in establishing negative results on witness encryption and quantum indistinguishability obfuscation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2535) | 2026-10-19
