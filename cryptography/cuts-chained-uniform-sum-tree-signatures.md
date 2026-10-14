---
title: "CUTS: Chained Uniform-sum Tree Signatures"
date: "2026-10-12"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2455"
summary: "Stateful hash-based signatures fail badly when a one-time key signs twice, as happens when the signer's state is lost or rolled back. We study what a second signature reveals in a broad class of hash-"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Stateful hash-based signatures fail badly when a one-time key signs twice, as happens when the signer's state is lost or rolled back. We study what a second signature reveals in a broad class of hash-based schemes whose key is a tree of hash chains. In this class, a message selects a set of tree nodes that covers every leaf exactly once, together with a position on the chain of each selected node, and the signature reveals the chain values at those positions. For the whole class, we prove that the values derivable from several signatures are exactly the union of those derivable from each signature alone, and we bound forgery after b signatures in the classical random-oracle model by a combinatorial coverage exponent lambda_b, also when the signer grinds a counter. We then present CUTS (Chained Uniform-sum Tree Signatures), a member of the class built on one binary tree, in which both the selected nodes and their chain positions depend on the message, with the positions summing to a fixed value S. Signature length and verification cost are fixed by the parameters and do not depend on the tree height. For CUTS, we compute the two-use coverage exactly as one coefficient of a polynomial and derive deterministic lower bounds on lambda_2; one parameter set with 1 424-byte signatures has lambda_2ge128.6. A counter variant, CUTS+C, trades a short counter and extra signing work for a proven grinding gain of g bits in the coverage term.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2455) | 2026-10-12
