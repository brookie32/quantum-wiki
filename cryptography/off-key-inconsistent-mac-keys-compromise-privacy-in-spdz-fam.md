---
title: "Off-Key: Inconsistent MAC Keys Compromise Privacy in SPDZ-Family MPC"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2533"
summary: "SPDZ-family protocols for maliciously secure multi-party computation protect secret-shared values with message authentication codes (MACs) under a secret-shared global key. Their security requires tha"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

SPDZ-family protocols for maliciously secure multi-party computation protect secret-shared values with message authentication codes (MACs) under a secret-shared global key. Their security requires that all values and preprocessing used together be authenticated under the same key. We present Off-Key, a privacy attack that exploits violations of this requirement. Depending on which specific MAC check protocol is used, a corrupted party can either recover the value of a shared secret from a single authentication check or test a guess through selective failure by modifying a MAC share and observing whether a masked check succeeds. While this attack does not compromise the theoretical security guarantees of the protocols, we demonstrate this key-consistency vulnerability in evaluated versions of MP-SPDZ, SCALE-MAMBA, and FANNG-MPC, which allow a corrupted party to use different keys across batches, threads, or process runs. To help implementations avoid this class of attacks, we identify the state that enforces key consistency in representative preprocessing protocols and show how preserving and reusing it prevents the attack.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2533) | 2026-10-19
