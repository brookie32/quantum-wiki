---
title: "The Lattice Isomorphism Problem with Hints"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2381"
summary: "The Lattice Isomorphism Problem (LIP) is a relatively new problem that has gained increasing attention in the field of lattice-based cryptography. It is the underlying hard problem of the Hawk signatu"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

The Lattice Isomorphism Problem (LIP) is a relatively new problem that has gained increasing attention in the field of lattice-based cryptography. It is the underlying hard problem of the Hawk signature scheme, which has been submitted to the second NIST call for post-quantum signatures. In this paper, we propose to study the security of LIP in the presence of partial information on the secret solution, which can be obtained through side-channel attacks or by design. We propose a new cryptanalysis approach for LIP that embeds it into a shortest vector problem (SVP) based on a different lattice than the one considered in the specifications of Hawk, allowing to integrate hints. We also introduce conversion techniques that transform hints expressed on arbitrary linear combinations of the secret key coefficients into hints on the target lattice, enabling the integration of a broader class of linear leakages on sensitive values. We implement our attack and predictions using the LeakyLWEEstimator tool (Crypto 2020) and obtain concrete security estimates for Hawk in the key-recovery setting. We also observe that Hawk signatures carry intrinsic information about the secret key and show that this can be exploited as a source of hints, yielding a refined key-recovery complexity, thereby eroding the original security estimates. For example, we estimate a security loss of around 11 bits for Hawk-1024. Finally, we apply our framework to side-channel analysis results on Hawk, solving an open problem raised in a recent analysis (TCHES 2024) and discuss further attack paths enabled by fault-injection techniques. We believe that this new cryptanalysis approach for LIP and the integration of hints provide new insights towards a better understanding of its security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2381) | 2026-10-06
