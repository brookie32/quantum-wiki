---
title: "Ties, Splits and Neighborhoods: New Area Records for Low-Latency Linear Layers"
date: "2026-11-22"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2980"
summary: "For the 23 linear layers of the benchmark of Shi, Feng and Xu (SFX23, ToSC 2023), we search for minimum-depth circuits with the fewest 2-input XOR (XOR2) gates, and for minimum-area circuits at the sa"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

For the 23 linear layers of the benchmark of Shi, Feng and Xu (SFX23, ToSC 2023), we search for minimum-depth circuits with the fewest 2-input XOR (XOR2) gates, and for minimum-area circuits at the same depth using both XOR2 and 3-input XOR (XOR3) gates, as in HILL by Li et al. (ToSC 2026). We combine three known techniques for the shortest linear program under a depth bound: (i) a beam search over the near-ties of the depth-bounded Boyar-Peralta heuristic; (ii) backward splitting; and (iii) a large neighborhood search. We set new records for the XOR2 count at the minimum depth for 14 of the 20 distinct problems represented by the 23 matrices up to row and column permutations, by 1 to 4 gates. After merging gates into XOR3 gates, our circuits are smaller than both the published XOR2/XOR3 circuits of HILL and the circuits of SFX23 merged in the same way for 19 of the 20 problems (UMC 180nm unit areas). We release the code, the logs, all the circuits recorded during our runs, and the verification scripts.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2980) | 2026-11-22
