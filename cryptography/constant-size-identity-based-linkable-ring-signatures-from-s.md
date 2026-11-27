---
title: "Constant-Size Identity-Based Linkable Ring Signatures from Standard Assumptions"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3032"
summary: "In this work, we propose an identity-based linkable ring signature (IB-LRS) scheme that achieves constant-size signatures and is provably secure in the standard model under standard assumptions. All p"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

In this work, we propose an identity-based linkable ring signature (IB-LRS) scheme that achieves constant-size signatures and is provably secure in the standard model under standard assumptions. All previous IB-LRS schemes are only proven secure in the random oracle model (ROM), and those achieving constant-size signatures additionally rely on non-standard assumptions. In contrast, our scheme removes both limitations simultaneously. To do this, we build our IB-LRS scheme from a constant-size hierarchical identity-based encryption (HIBE) scheme. First, we adapt this HIBE to a matrix-based dual-system framework to replace its non-standard assumptions with standard assumptions. Then, we use the ``all-but-one'' technique to aggregate all ring identities and get constant-size ring signatures. Finally, to support linkability, we add a separate matrix to bind each user's tracking key to the ring signature. Moreover, our scheme provides unconditional anonymity, and we prove its unforgeability, linkability, and non-slanderability under the Matrix Decisional Diffie-Hellman (MDDH) assumption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3032) | 2026-11-25
