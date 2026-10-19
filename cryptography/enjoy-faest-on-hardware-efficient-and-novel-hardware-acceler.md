---
title: "Enjoy FAEST on Hardware: Efficient and Novel Hardware Acceleration of Emerging Post-Quantum Digital Signature Scheme FAEST"
date: "2026-10-18"
updated: "2026-10-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2525"
summary: "The National Institute of Standards and Technology (NIST) Post-Quantum Cryptography (PQC) standardization process has drawn significant attention from the research community recently, especially regar"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

The National Institute of Standards and Technology (NIST) Post-Quantum Cryptography (PQC) standardization process has drawn significant attention from the research community recently, especially regarding these PQC schemes' hardware acceleration. Nevertheless, related research on the emerging schemes, e.g., those currently under consideration by the NIST additional digital signature scheme standardization, still needs further exploration. With this background, this paper presents an efficient and novel hardware acceleration for FAEST, one of the promising signatures in the NIST Round 3 additional scheme competition. Overall, we have presented several layers of innovative efforts to obtain the proposed acceleration. First of all, we have conducted detailed algorithmic analysis on the major computationally intensive operations within FAEST and proposed novel design strategies and algorithms for their efficient hardware implementation. Next, we have proposed novel design efforts to construct these major operations into efficient building blocks to finalize the overall accelerator, along with the help of optimized operational phase workflow. The dedicated extension to build the L1-EM-fast accelerator is also given. Finally, we have provided a detailed and thorough evaluation process to showcase the superior performance of the proposed design over the existing complete, Sign part, and single security level MPC-in-the-head signature acceleration works. For instance, at the same security level, the proposed fast variant has at least 98% less equivalent Area-Delay Product (eADP) than the recent complete SDitH design. To the authors' best knowledge, this is the first hardware acceleration work for FAEST, and we hope the outcome of this research will facilitate the ongoing PQC standardization process.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2525) | 2026-10-18
