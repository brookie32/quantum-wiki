---
title: "Shorter Few-Time Signatures from Hash Chains and Blockwise Forced Pruning"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2374"
summary: "SLH-DSA is a standardized stateless hash-based signature scheme based on SPHINCS^+, but its signatures remain large. PORS+FP uses forced pruning to reduce the size of the bottom few-time signature (FT"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

SLH-DSA is a standardized stateless hash-based signature scheme based on SPHINCS^+, but its signatures remain large. PORS+FP uses forced pruning to reduce the size of the bottom few-time signature (FTS) component, while BPORS+FP distributes repeated uses among independent PORS child keys. In BPORS+FP, each selected leaf reveals a fixed secret value, and a single pruning budget limits the total number of authentication nodes across all coordinates. We introduce BPORS-C+BFP, which replaces each secret at a child leaf with a short hash chain and assigns a separate authentication budget to each block of coordinates. The child Merkle tree authenticates each chain endpoint. Each selected chain still contributes one hash value to the signature, while its opening depth provides an additional encoding choice. For a fixed set of selected chains, a constant-sum constraint prevents forward hashing alone from converting one valid depth tuple into another. Under repeated use, signatures may disclose different positions on the same chain. We derive a generating-function upper bound on coverage and an exact counting method for individual pruning blocks that accounts for these disclosures and target acceptance. Separate block budgets confine pruning-induced dependencies, reducing the number of coordinates counted jointly and making exact calculation practical for small blocks. Replacing FORS in SPHINCS+ while keeping the hypertree and one-time signature parameters fixed, BPORS-C+BFP reduces complete-signature sizes by 8.3%--18.1% across six standard settings, compared with 3.7%--13.4% for BPORS+FP. Across three limited-use settings, the reductions relative to FORS are 32.5%--36.5% for BPORS-C+BFP and 22.0%--26.0% for BPORS+FP.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2374) | 2026-10-06
