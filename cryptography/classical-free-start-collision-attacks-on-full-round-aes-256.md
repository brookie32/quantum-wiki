---
title: "Classical Free-Start Collision Attacks on Full-Round AES-256-DM and AES-256-MMO"
date: "2026-11-20"
updated: "2026-11-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2959"
summary: "Despite extensive cryptanalysis of hash modes based on the Advanced Encryption Standard (AES), no classical free-start collision attack has previously been reported for full-round AES-256-DM or AES-25"
last_verified: "2026-11-22"
review_by: "2027-02-20"
stale: false
---

Despite extensive cryptanalysis of hash modes based on the Advanced Encryption Standard (AES), no classical free-start collision attack has previously been reported for full-round AES-256-DM or AES-256-MMO. In this work, we address this problem by extending the guess-and-determine (GD) rebound methodology. Our main technical contribution is a precomputation-based method for handling conflicts involving guessed variables in the GD procedure. By precomputing solutions to the corresponding systems of byte equations, such conflicts can be resolved in O(1) online time. We further exploit triangular dependencies among controllable guessed variables to reduce the memory required for precomputation. Using this method, we construct classical free-start collision attacks applicable to both AES-256-DM and AES-256-MMO. For the full 14-round AES-256, the attacks require 2^{60} time and 2^{24} memory, providing the first classical free-start collision attacks on these full-round constructions. The same approach improves the time complexity of the full-round free-start differential q-multicollision attack from qdot2^{67} to qdot2^{60}, with memory complexity 2^{24}. We also obtain free-start collision attacks on the 12-round variants with time complexity 2^{54} and memory complexity 2^{24}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2959) | 2026-11-20
