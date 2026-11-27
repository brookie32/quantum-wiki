---
title: "Adams Bridge is Falling Down: A New Chosen Ciphertext Side-Channel Attack on the PQC Accelerator"
date: "2026-11-24"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3027"
summary: "With ML-KEM and ML-DSA now standardized by NIST, post-quantum cryptography (PQC) is moving from research into real world. Adams Bridge is an industry-oriented hardware accelerator that implements both"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

With ML-KEM and ML-DSA now standardized by NIST, post-quantum cryptography (PQC) is moving from research into real world. Adams Bridge is an industry-oriented hardware accelerator that implements both ML-KEM and ML-DSA in a unified architecture. It is used as the post-quantum engine of Caliptra 2.1, a silicon root of trust designed to be integrated into data center chips from multiple vendors. This broad integration makes its security particularly important, as vulnerabilities could affect a wide range of deployed systems. In this paper, we reveal new vulnerabilities in the centered binomial sampling and ciphertext compression and comparison operations. We demonstrate the first practical key recovery attack on the released Adams Bridge v2.0.3 hardware implementation of ML-KEM with all countermeasures enabled. We further propose a new non-profiled chosen ciphertext attack method, achieving full secret key recovery for ML-KEM-1024 using 18 580 traces in 49.5 minutes. Compared to our profiled attack, the new method reduces the number of traces by at least 29.2%. More broadly, our findings highlight a gap between the countermeasures recommended by the research community and those adopted in industrial PQC hardware designs. As the transition to PQC accelerates, bridging this gap is crucial to ensuring the security of real-world deployments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3027) | 2026-11-24
