---
title: "Beskar: Efficient Threshold ML-DSA via Preprocessed Rejection Sampling"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3023"
summary: "Efficient threshold variants of ML-DSA are important for the transition to post-quantum cryptography, as they allow parties to jointly produce standard ML-DSA signatures without reconstructing the sig"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Efficient threshold variants of ML-DSA are important for the transition to post-quantum cryptography, as they allow parties to jointly produce standard ML-DSA signatures without reconstructing the signing key. The main obstacle is rejection sampling: before releasing a candidate signature, the parties must jointly evaluate several norm checks on secret-shared values and restart the computation if any check fails. In existing MPC-based protocols, these checks account for much of the cost of the online phase. We present Beskar, a threshold ML-DSA protocol secure against malicious adversaries in the honest-majority setting. Building on Quorus (Bienstock et al., USENIX 2026), we reduce online signing from sixteen rounds to three and reduce online communication by a factor of 10. Our main technical contribution is a method for moving most of the computation required by rejection sampling into preprocessing and combining the remaining checks with signature release. In contrast to Mithril (Celi et al., USENIX 2026), Beskar relies only on standard secret sharing, rather than short secret sharing, and its expected number of signing attempts does not grow with the number of parties. Our implementation demonstrates practicality with a 5 party threshold signing attempt running in under 700ms in a high latency setting.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3023) | 2026-11-24
