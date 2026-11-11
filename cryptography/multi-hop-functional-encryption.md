---
title: "Multi-Hop Functional Encryption"
date: "2026-11-08"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2835"
summary: "In this paper, we initiate the study of multi-hop functional encryption (mathsf{MHFE}), a new primitive for computing over encrypted data in recursive and multi-stage workflows while enabling controll"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

In this paper, we initiate the study of multi-hop functional encryption (mathsf{MHFE}), a new primitive for computing over encrypted data in recursive and multi-stage workflows while enabling controlled release of intermediate outputs. mathsf{MHFE} supports dynamic directed-acyclic computation graphs in which each node is labeled by a function and is equipped with a restricted secret key that reveals only that node's output, yet the computation can continue downstream on a forwardable encrypted state. In doing so, mathsf{MHFE} simultaneously overcomes (i) multi-hop fully homomorphic encryption's need for a globally trusted, always-online decryption key to reveal intermediate values, (ii) standard FE's lack of a native mechanism for forwarding reusable encrypted state across stages and handling evolving datasets without a fresh recomputation, and (iii) Multi Party Computation's deployment friction stemming from interaction and liveness/coordination requirements (at the cost of a central key-issuing authority). We formalize mathsf{MHFE} security via the simulation paradigm extending standard FE collusion resistance to the multi-hop setting; this simulation-based notion captures the intended information flow in recursive computations most accurately by characterizing an adversary's entire view as simulatable given only the authorized intermediate outputs. Our security games impose a natural topological-order on queries: a hop key for a node may be requested only after the ciphertexts/keys on all incoming edges to that node have been fixed. We then give the first generic simulation-secure construction of public-key mathsf{MHFE} for all polynomial-size circuits from any IND-secure standard FE for circuits.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2835) | 2026-11-08
