---
title: "Representation-Aware Kleptographic Attacks on Post-Quantum Cryptography"
date: "2026-11-23"
updated: "2026-11-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3001"
summary: "Kleptographic subversions of cryptographic implementations, through Algorithm Substitution Attacks (ASAs), threaten the trust assumptions of black-box cryptosystems. This work studies such subversions"
last_verified: "2026-11-25"
review_by: "2027-02-23"
stale: false
---

Kleptographic subversions of cryptographic implementations, through Algorithm Substitution Attacks (ASAs), threaten the trust assumptions of black-box cryptosystems. This work studies such subversions in Post-Quantum Cryptography (PQC) through the lens of public-key representation. We formalize key-generation subversion with explicit public-key representations, distinguishing seed-compressed interfaces from expanded-key interfaces. This distinction captures a security-relevant role of seed compression beyond bandwidth and storage efficiency: public components regenerated from seeds can be checked against the specification, creating a regeneration barrier against certain expanded-component substitutions. We further present the first kleptographic key-generation backdoor targeting HQC. Our construction instantiates the model in the expanded-key setting by building a BIKE-form in-band carrier that exploits structural similarities between HQC public-key formation and BIKE decoding instances. A subverter holding the BIKE decoding trapdoor can recover the randomness used to derive the victim's HQC secret state. We implement a dimension-aligned proof of concept and evaluate functional correctness, runtime overhead, and coarse black-box statistical tests. We further provide a conditional indistinguishability proof for subverted keys. Moreover, we contrast this behaviour with ML-DSA, where recomputability from public seeds and secret-key material constrains analogous perturbation-style subversions. We also analyze a generic seed-level SETUP pattern as a remaining attack surface, showing that seed compression blocks certain expanded-component carriers but does not by itself eliminate seed-generation subversion. Overall, our results support the view that public-key representation should be treated as part of the kleptographic assurance boundary for PQC implementations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3001) | 2026-11-23
