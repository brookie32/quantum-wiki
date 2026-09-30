---
title: "Improved Differential-Linear Cryptanalysis of Orthros, Gleeok, ZIP-AES, and ZIP-GIFT"
date: "2026-09-29"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2255"
summary: "We improve differential-linear distinguishers and derive key-recovery attacks on reduced-round versions of the PRFs Orthros, Gleeok, ZIP-AES, ZIP-GIFT-64, and ZIP-GIFT-128. Relative to previous differ"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

We improve differential-linear distinguishers and derive key-recovery attacks on reduced-round versions of the PRFs Orthros, Gleeok, ZIP-AES, ZIP-GIFT-64, and ZIP-GIFT-128. Relative to previous differential-linear analyses, we extend the reported coverage for Orthros from 7 to 9 rounds and for Gleeok-128 from 4 to 5 rounds. For Orthros and Gleeok-128, we obtain estimated correlation magnitudes (2^{-61.40}) and (2^{-31.71}), respectively. We also obtain distinguishers for 6-round Gleeok-256, ((3,3))-round ZIP-AES, ((7,7))-round ZIP-GIFT-64, and ((10,10))-round ZIP-GIFT-128. For key recovery, we give a ((3,3))-round differential-linear attack on ZIP-AES requiring approximately (2^{122.42}) chosen plaintexts and (2^{122.88}) ZIP-AES evaluations. Our ((10,10))-round ZIP-GIFT-128 attack has estimated data, time, and memory complexities of (2^{93}) chosen plaintexts, (2^{117}) full PRF evaluations, and (2^{25.01}) bits. We further obtain weak-key attacks on 9-round Orthros, 5-round Gleeok-128, and 6-round Gleeok-256, with key-space coverages of (2^{-2.87}), (2^{-3}), and (2^{-1}), respectively. The Orthros key-recovery result reaches one round beyond the previous DL key-recovery coverage. These results use automated differential and linear trail search together with existing round-based correlation estimation. We enforce the compatibility constraints between branches and select input-side extensions that make their prescribed differences jointly reachable.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2255) | 2026-09-29
