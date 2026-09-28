---
title: "Practical Null-Branch Witness Attacks on In-the-Head Signatures"
date: "2026-09-27"
updated: "2026-09-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2235"
summary: "In-the-head signatures provide a route to post-quantum authentication based on symmetric primitives. Their algebraic instantiations rely on constraint relations that faithfully encode the underlying o"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

In-the-head signatures provide a route to post-quantum authentication based on symmetric primitives. Their algebraic instantiations rely on constraint relations that faithfully encode the underlying one-way function (OWF). We give a classical, public-key-only forgery attack on AIM2-based AIMer v2.0; AIMer was selected in Korea's KpqC competition. For every honestly generated public key of every v2.0 parameter set, the attack forges signatures on arbitrary messages with probability one, without signing queries. We introduce a null-branch witness attack exploiting zero factors that leave intermediate values unconstrained. We complete these local assignments into witnesses satisfying the full relation, including public-output binding, using only public data and without solving an OWF inversion problem. Prover completeness ensures that the original message-bound prover can use these witnesses to generate signatures accepted by the unmodified verifier. Proof-system soundness applies to the encoded relation, which the constructed witnesses satisfy. Tests with reference implementations confirm accepted forgeries from satisfying witnesses whose decoded values are not valid OWF preimages. The median AIMer-256f forgery API time is approximately 11.6 ms in our reference benchmark. We identify a gap in AIMer's security reduction: a satisfying relation witness need not decode to an OWF preimage. A complementary application to vulnerable Lynxer variants extends the analysis to VOLE-in-the-Head. We give quadratic encodings that are sound and complete for the full AIM2 and Lynx computations, including zero inputs. These results highlight relation encoding as a distinct security obligation between OWF hardness and proof-system soundness.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2235) | 2026-09-27
