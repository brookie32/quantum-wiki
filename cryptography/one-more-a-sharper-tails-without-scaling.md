---
title: "One More A: Sharper Tails Without Scaling"
date: "2026-09-12"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1996"
summary: "Repeat--accumulate--accumulate (RAA) codes have minimum distance linear in the block length with probability tending to one, both with and without random coordinate scaling. Sharp results, however, re"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Repeat--accumulate--accumulate (RAA) codes have minimum distance linear in the block length with probability tending to one, both with and without random coordinate scaling. Sharp results, however, reveal a tradeoff between the two constructions. For block length (N=rn) and fixed repetition factor (rge4), the probability that the minimum distance is at most (elta N) is (Theta(N^{2-r})) for unscaled RAA and (Theta(N^{1-r})) for scaled RAA, on their common proved range (0<eltale1/10). Thus scaling reduces the failure probability by a factor of order (N). This improvement comes at a cost: the scaled result requires (q=Omega(N)) over (F_q), and the encoder uses two length-(N) layers of coordinatewise field multiplications. In contrast, unscaled RAA works over a fixed field of characteristic greater than (r), and its accumulator stages use only field additions. In this work, we show that adding a third accumulator provides a substantially larger reliability gain without random scaling. For the unscaled repeat--accumulate--accumulate--accumulate ensemble [ G_3=RPi_1APi_2APi_3A, ] where (R) is (r)-fold repetition, (A) is the accumulator, and the (Pi_i) are independent uniform interleavers, we prove that [ Prb[d_{min}(G_3)leelta N] =Theta_{r,elta}!left(N^{,2-r-eil{r/2}}right) ] for every fixed (rge4) and (0<eltale1/10), uniformly over all finite fields of characteristic greater than (r). Hence the field size need not grow with (N), and the encoder requires three accumulator passes but no coordinatewise field multiplications. On the common threshold range, its failure probability is smaller by a factor of order (N^{eil{r/2}}) than that of unscaled RAA and by a factor of order (N^{eil{r/2}-1}) than that of scaled RAA. For example, when (r=4), the respective failure probabilities have orders (N^{-2}), (N^{-3}), and (N^{-4}).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1996) | 2026-09-12
