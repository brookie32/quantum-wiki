---
title: "SoK: The Landscape of Post-Quantum Multi-Party Signature Aggregation"
date: "2026-09-26"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2222"
summary: "Post-quantum signature schemes such as ML-DSA, FN-DSA (Falcon), and SLH-DSA have significantly larger keys and signatures than their classical counterparts, making compact multiparty signing an increa"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Post-quantum signature schemes such as ML-DSA, FN-DSA (Falcon), and SLH-DSA have significantly larger keys and signatures than their classical counterparts, making compact multiparty signing an increasingly important research problem. We survey more than 30 schemes published between 2021 and 2026, covering threshold and dis tributed signing, proof-based aggregation, and algebraic half-aggregation. Our survey shows that most existing work is designed around blockchain and validator-consensus applications, where large numbers of mostly ho mogeneous signers sign a common message and accountability is typically represented by a compact signer set. We found that a different and practically important setting has received little attention: institutional multiparty document signing, where tens to hundreds of signers may use different post-quantum schemes or parame ter sets during a gradual migration, while requiring non-interactive sign ing and exact per-signer accountability. To study this gap, we develop an eight-dimensional taxonomy based on deployment requirements and sys tematically classify existing approaches. We also formulate three testable hypotheses and propose a common benchmark methodology for evalu ating communication, computation, verification cost, scalability, signer heterogeneity, and accountability. Our analysis finds no published study that quantitatively evaluates the institutional workload across the ag gregation paradigms covered in our survey. We therefore identify the key experimental and architectural requirements for assessing whether ex isting post-quantum aggregation techniques can support heterogeneous, accountable, and non-interactive institutional signing.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2222) | 2026-09-26
