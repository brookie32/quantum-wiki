---
title: "Practical Attacks Against EALPN Using Belief Propagation"
date: "2026-09-25"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2213"
summary: "Weak and shallow pseudo random functions form a new class of symmetric primitives that is seeing a growing relevance, from their use in the initialization phase of some MPC protocols to the internals "
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Weak and shallow pseudo random functions form a new class of symmetric primitives that is seeing a growing relevance, from their use in the initialization phase of some MPC protocols to the internals of some FHE-based protocols. However, their security is hard to ensure: "weak" means that chosen plaintext attacks are irrelevant, and "shallow" means that their construction cannot be round-based: in this exotic setting, how can we define secure PRFs? In this paper, we investigate EALPN, a recent proposal of this type. We identify critical blind spots in the initial asymptotic analysis of the designers: the role of l, one of its parameters, turns out to be crucial. Indeed, we present a key recovery attack with a complexity that is polynomial in all other parameters, and whose complexity grows exponentially but still slowly with l. As a consequence, some parametrizations intended to provide 128 bits of security only offer 37 bits. Our attack is based on novel use of the belief propagation algorithm. Our analysis of its efficiency in our specific setting can be of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2213) | 2026-09-25
