---
title: "Bounding the security of the FALCON signature scheme in the quantum random oracle model"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3034"
summary: "In 2016, the National Institute of Standards and Technology (NIST) announced their invitation for proposals of public key encryption and signature schemes that are resistant to attacks by quantum comp"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

In 2016, the National Institute of Standards and Technology (NIST) announced their invitation for proposals of public key encryption and signature schemes that are resistant to attacks by quantum computers. Since then, several rounds of proposals and revisions have occurred resulting in the 2022 announcement that three signature schemes - CRYSTALS-Dilithium, FALCON, and SPHINCS+ - would be standardized. However, in 2024, work by Fouque et al. noted an oversight in the published security for FALCON, which they were only able to remedy in a classical computing setting, namely the random oracle model (ROM). In this paper, we provide the first complete security proof for FALCON in the quantum random oracle model (QROM). Specifically, we will prove a reduction to the security of FALCON from the ring inhomogeneous short integer solution (RISIS) problem and the NTRU learning problem utilizing known quantum reprogramming results. We then provide parameter sets which meet the security levels required by NIST under our reduction.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3034) | 2026-11-25
