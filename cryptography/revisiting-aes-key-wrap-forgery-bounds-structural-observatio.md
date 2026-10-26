---
title: "Revisiting AES Key Wrap: Forgery Bounds, Structural Observations, and Recommendations for the Revision of NIST SP 800-38F"
date: "2026-10-25"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2636"
summary: "NIST is revising SP~800-38F, which specifies the AES Key Wrap modes KW and KWP. This paper is an updated and expanded version of our technical comments to NIST. We show that the forgery probabilities "
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

NIST is revising SP~800-38F, which specifies the AES Key Wrap modes KW and KWP. This paper is an updated and expanded version of our technical comments to NIST. We show that the forgery probabilities stated in SP~800-38F do not account for adaptive attacks, give the resulting forgery probabilities for KW, KWP, and TKW, and show that checking the expected plaintext length can raise the security level of KWP considerably. Revisiting Kelsey's long-message observation, we correct the collision conditions, show that a successful forgery leaks a plaintext prefix, derive an encryption-only distinguisher, and conclude that KW does not have beyond-birthday-bound security. We explain the role of the step counter, analyse the single-semiblock path of KWP and the trade-off between the number of passes and the length limit, and give recommendations for the revision, for implementations, and for future key-wrap designs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2636) | 2026-10-25
