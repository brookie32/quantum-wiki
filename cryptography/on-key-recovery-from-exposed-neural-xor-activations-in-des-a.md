---
title: "On Key Recovery from Exposed Neural XOR Activations in DES and TDES"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2763"
summary: "We study the security of natural ReLU realizations of the Data Encryption Standard (DES) and two-key Triple DES (TDES) when an adversary can submit non-binary inputs and observe selected intermediate "
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

We study the security of natural ReLU realizations of the Data Encryption Standard (DES) and two-key Triple DES (TDES) when an adversary can submit non-binary inputs and observe selected intermediate neural values. The attack exploits the piecewise-linear extension of XOR: paired inputs that differ in one expanded right-half bit reveal the corresponding round-key bit from the change in a natural XOR node. For DES, the resulting 48-bit first-round subkey leaves only the eight key-schedule bits omitted by PC-2; enumerating these bits and checking an intermediate value recovers the 56-bit effective master key. For two-key EDE TDES, the same technique recovers the first encryption subkey of K_1 and the last DES subkey used by the middle decryption under K_2; two independent 2^8 completions then recover the full 112-bit key pair. The exposed round subkey is recovered with a constant number of leakage observations per bit, giving query complexity linear in the targeted subkey length; the remaining searches are fixed-size for DES. Python experiments report exact recovery for 1,000 random DES keys and 1,000 random two-key TDES key pairs. These results concern a synthetic intermediate-oracle model for natural neural implementations and do not claim a physical attack on conventional DES/TDES hardware or software.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2763) | 2026-11-04
