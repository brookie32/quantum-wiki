---
title: "Topology-Driven Symbolic Verification of Post-Quantum Migration Paths Using Tamarin Prover"
date: "2026-04-26"
updated: "2026-04-29"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/819"
summary: "The transition from classical public-key cryptography to post-quantum cryptography introduces protocol-level risks that are not fully addressed by configuration review, performance benchmarking, or en"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

The transition from classical public-key cryptography to post-quantum cryptography introduces protocol-level risks that are not fully addressed by configuration review, performance benchmarking, or endpoint reachability testing. Under the current abstraction, deployments may appear operationally correct while still permitting secrecy, authentication, or forward-secrecy violations at the protocol level. This paper presents a topology-driven symbolic verification workflow that translates distributed-system communication graphs into Tamarin models for analysis under the Dolev--Yao adversary model. The workflow derives protocol roles, communication constraints, and migration policies from a graph-based deployment representation, producing .spthy models and associated lemmas for executability, secrecy, authentication, and forward secrecy. A canonical topology representation is used to ensure deterministic model generation from semantically equivalent graph inputs. Experimental evaluation across five scenarios indicates that the framework produces discriminative symbolic outcomes rather than uniform failure reports. A registration-only control scenario verifies all reported lemmas, while the remaining scenarios exhibit two distinct falsification patterns: secrecy and forward-secrecy failures in three scenarios, and authentication failure in one scenario. These results indicate that symbolic verification provides a complementary assurance layer for post-quantum migration analysis and can reveal protocol-level risks that are not observable through operational testing alone.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/819) | 2026-04-26
