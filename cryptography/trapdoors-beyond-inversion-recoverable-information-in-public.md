---
title: "Trapdoors Beyond Inversion: Recoverable Information in Public-Key Cryptography"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2764"
summary: "Classical trapdoor functions recover complete preimages, whereas public-key decryption needs only designated information about an encryption input. We study this distinction through trapdoor hardcore "
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Classical trapdoor functions recover complete preimages, whereas public-key decryption needs only designated information about an encryption input. We study this distinction through trapdoor hardcore functions (TDHFs), whose trapdoor recovers a prescribed value h(x) from a public evaluation f (x), while h(x) remains pseudorandom given the public key and evaluation. For perfectly correct primitives, we show that adaptive TDHFs characterize IND-CCA2-secure public-key encryption. The constructive direction requires only a single recoverable bit and allows noninjective public evaluations. Extending the rejection-sampling approach, we show that adaptive pseudorandomness itself controls queries to unselected candidate evaluations, without requiring full inversion. We also prove that lossy TDHFs characterize lossy public-key encryption, identifying statistical hiding of the designated recovered value as the relevant lossiness requirement. Fiber samplability together with fiber hiding yields a parameter-preserving correspondence with lossy encryption and, through the known long-message transformation, almost-always lossy trapdoor functions when the recovered-value length exceeds the fiber-sampling randomness length. Ordinary TDHFs provide the corresponding characterization of IND-CPA encryption. Together, these results make explicit the roles of adaptive recovery, conditional sampling, and randomness costs in transformations between public-key encryption and full-inversion primitives.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2764) | 2026-11-04
