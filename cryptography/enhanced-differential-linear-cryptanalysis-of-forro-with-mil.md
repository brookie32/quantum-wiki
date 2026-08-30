---
title: "Enhanced Differential-linear Cryptanalysis of Forro with MILP"
date: "2026-08-28"
updated: "2026-08-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1825"
summary: "ARX-based design is a major building block of modern cryptographic ciphers due to its efficiency in software. Forro is an ARX-based stream cipher proposed by Coutinho et al. at ASIACRYPT 2022, which w"
last_verified: "2026-08-30"
review_by: "2026-11-28"
stale: false
---

ARX-based design is a major building block of modern cryptographic ciphers due to its efficiency in software. Forro is an ARX-based stream cipher proposed by Coutinho et al. at ASIACRYPT 2022, which was designed to provide higher security margin than the ChaCha stream cipher. In this paper, we propose a full automated MILP model called extit{MinForro}, to derive linear approximations for the Forro stream cipher. For the differential part, a two-stage strategy to search for single-bit differential trails with high differential correlations is presented, which helps us to find the first-ever 3-round differential trails for Forro. By combining the linear approximations obtained by extit{MinForro} and 3-round differential trail for Forro, we propose improved differential-linear distinguishers for 4-, 5-, 5.25-, 5.5-, 5.75-, 6-, 6.25- and 6.5-round Forro with complexities {2^{32.44}}, {2^{46}}, {2^{50}}, {2^{64.32}}, {2^{87.12}}, {2^{117.92}}, {2^{174.92}} and {2^{226.88}}, respectively. The proposed differential-linear distinguishers for 4-, 5-, 5.25- and 5.5-round Forro significantly improve the existing distinguishers by factors of {2^{4.11}}, {2^{83.68}}, {2^{127.64}} and {2^{178.20}}, respectively. To the best of our knowledge, this is the first differential-linear distinguisher for Forro that reaches 6.5 rounds, which is a significant advancement over the existing record of 5.5 rounds. We have implemented the differential-linear distinguishers for 4- and 5-round Forro on a common PC, and the experimental results confirm the correctness of these distinguishers. Furthermore, when combined with the extit{Probabilistic Neutral Bits} (PNB) technique, we obtain key recovery attacks on 5.5-, 6-, 6.5- and 6.75-round Forro with time complexities {2^{149.20}}, {2^{151.84}}, {2^{213.49}} and {2^{251.97}}, respectively. The proposed key recovery attack on 5.5-round Forro significantly improves the time complexity of the existing attack by a factor of {2^{75.84}}. To the best of our knowledge, this is the first key recovery attack on Forro that reaches 6.75 rounds, which is a significant advancement over the existing record of 5.5 rounds.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1825) | 2026-08-28
