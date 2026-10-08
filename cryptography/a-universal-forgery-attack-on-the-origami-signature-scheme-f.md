---
title: "A Universal Forgery Attack on the Origami Signature Scheme from the Public Key Alone"
date: "2026-10-07"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2390"
summary: "Origami is a multivariate signature scheme submitted to the NGCC round-1 public-key call. We show that the submitted bilinear construction is a Rainbow-type scheme whose central map is exposed. The ve"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

Origami is a multivariate signature scheme submitted to the NGCC round-1 public-key call. We show that the submitted bilinear construction is a Rainbow-type scheme whose central map is exposed. The verification map is the layered signing map in a public coordinate order. The public key therefore gives an equivalent secret key, allowing signature forgery at about the cost of one verification (about 0.01s at Origami-128). Our attack exploits this public layered structure and succeeds against the unmodified reference implementation on all four parameter sets and the official test vectors. We also refute the security proof's inversion assumption in a bilinear independent-coefficient model. The hidden local algebras introduced by Origami do not prevent the attack. They raise a separate problem: the specification treats constrained matrix coordinates as independent, and honest signatures lie in a proper subspace.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2390) | 2026-10-07
