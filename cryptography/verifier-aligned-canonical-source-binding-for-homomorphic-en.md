---
title: "Verifier-Aligned Canonical Source Binding for Homomorphic Encryption Computations"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2348"
summary: "q0 preprocessing verification and native HE computation verification can each succeed without establishing that their results refer to the same canonical source. To address this source mismatch across"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

q0 preprocessing verification and native HE computation verification can each succeed without establishing that their results refer to the same canonical source. To address this source mismatch across verification paths, we propose a verifier-aligned public-input transfer procedure that links heterogeneous authenticated artifacts to a single canonical-source relation. The public verifier reconstructs challenges and targets from the actual statements, roots, approved verification keys, and authenticated positions. The chunk circuits then verify the source and mask commitments together with the canonical range, sign, and partial-sum relations. The full-input implementation processes 524,288 coefficients across 128 blocks and 4,096 native-bridge chunks. Public reconstruction and verification without stored challenge caches take 184.77 seconds, with 27,345,153 B of explicit public data. In a representative-block comparison for the same relation, sharing duplicate hash, range, and sign computations reduces the number of constraints by 33.53% and proving time by 31.10%, while preserving the proof-body size. In contrast, three upstream proof artifacts account for 88.44% of the total public data. These results show that eliminating redundant circuit computations is effective for reducing prover-side cost, whereas the dominant public-data cost originates from separate upstream proof artifacts. Prover computation and public-data size should therefore be treated as distinct optimization targets in source-binding verification. This work specifies the common-source relation between heterogeneous HE verification results and evaluates its implementation at full input scale.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2348) | 2026-10-05
