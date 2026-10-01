---
title: "Computational Bounds for f-Routing"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40278"
summary: "arXiv:2609.40278v1 Announce Type: new Abstract: The f-routing protocol is a leading candidate for quantum position verification (Kent, Munro, and Spiller, 2011), but security guarantees for explicit f"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40278v1 Announce Type: new Abstract: The f-routing protocol is a leading candidate for quantum position verification (Kent, Munro, and Spiller, 2011), but security guarantees for explicit functions remain limited. We prove unconditional resource lower bounds for uniform attackers; our new techniques bypass communication-complexity bounds central to previous works, which are inherently at most linear in the input length. We show that, for input length n and sufficiently small constant epsilon>0, a uniformly generated strategy using q qubits and having description length poly(q), with success probability at least 1-epsilon on every input, implies the following computational bounds on f: 1. If the strategies are arbitrary quantum channels, then finQSZK(poly(nq)), where QSZK(T) is the class of languages having quantum statistical zero knowledge proofs in which the verifier runs in time T (and the simulator in time poly(T)). 2. If the strategies are explicit Pauli-sparse unitaries on q qubits that have at most s nonzero Pauli coefficients, then finDTIME(poly(nqs)). 3. If the strategies are Clifford+T circuits using at most t magic gates, then finDTIME(poly(nq2^t)). Time and space hierarchies then yield explicit functions secure against polynomial and even quasipolynomial qubits q under our computational restrictions. These bounds exceed the qlelog n bound of Bluhm, Christandl, and Speelman (2022) for inner product function f=IP, at the cost of restricting adversarial computation and increasing honest evaluation complexity.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40278) | 2026-10-01
