---
title: "PairSwitch: Efficient Galois-Paired Key Switching for Gentry–Lee Matrix FHE"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2373"
summary: "Matrix-native fully homomorphic encryption, introduced by Gentry and Lee, multiplies encrypted matrices with a Trace product and returns its four-component output to an ordinary ciphertext with a BigS"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

Matrix-native fully homomorphic encryption, introduced by Gentry and Lee, multiplies encrypted matrices with a Trace product and returns its four-component output to an ordinary ciphertext with a BigSwitch, whose keys over an extended ring dominate the key material of the scheme. Existing BigSwitches follow two routes: they either store one key per source, as in the original construction, or factor the secret through the trace and relinearize at run time, as in the Trace-Factored BigSwitch (TFB) of Park et al., which halves the keys at the price of 50% more key switches and a whole switching error multiplied by the secret. Meanwhile, the Galois splitting of Park (Eurocrypt'25) decomposes such switches into base-ring diagonals, but it has not been used to reduce their keys. However, whether a BigSwitch can publish only the keys of TFB and still run at the speed of the original one has remained open. In this work, we first propose the pair-merge BigSwitch, which observes that the diagonals of a split BigSwitch are indexed by an inversion-closed coset kappa H and rewrites the target of a diagonal as x,g(s)+y,s,g(s)=gig(g^{-1}(x),s+g^{-1}(y),s,g^{-1}(s)ig), so that it borrows the product key of its inverse at the cost of one Galois step; it makes the 2n key switches of the original BigSwitch with n/2+1 instead of n product keys, and we prove that no per-diagonal BigSwitch with 2n key switches holds fewer than 3n/2+1 keys. Building on it, we propose public key rebasing, which turns Galois keys into product keys with one relinearization key placed one small modulus layer above the chain, so that the client publishes only the keys of TFB and a 10.6 MiB layer key, at the price of 1.5imes the resident keys of TFB on the server. Consequently, together with a Hermitian hop that finishes a partner diagonal of a Gram product with one Galois step, PairSwitch makes 2n key switches on general inputs and 3n/2+1 on Gram products. On the parameters of Park et al. (n=256, p=17, log_2 PQ=200), our implementation runs a BigSwitch 1.89--1.99imes faster than TFB and 1.28--1.38imes faster than the original BigSwitch, with 2.4 bits less noise than TFB and 4.3 bits more than the original, at a 128.3-bit layer key; it is 2.45imes faster than TFB on Gram inputs. Our implementation and the raw logs are available at https://github.com/acprk/pairswitch-gl.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2373) | 2026-10-06
