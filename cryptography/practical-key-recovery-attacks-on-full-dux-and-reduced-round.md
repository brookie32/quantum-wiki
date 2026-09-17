---
title: "Practical Key Recovery Attacks on Full DuX and Reduced-Round YuX"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2045"
summary: "Dux{} and Yux{} are recent block-cipher families designed for efficient evaluation under fully homomorphic encryption. Both keep sixteen words of a large finite field in four blocks, with a low-degree"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Dux{} and Yux{} are recent block-cipher families designed for efficient evaluation under fully homomorphic encryption. Both keep sixteen words of a large finite field in four blocks, with a low-degree block-wise S-box and a circulant linear layer. We show that, in the chosen-ciphertext model, the algebraic degree of their decryption functions grows far more slowly than the designers' encryption-side evaluation suggests, and we turn this into practical key-recovery attacks. Our starting point is a sufficient criterion for zero sums. It treats affine subspaces in characteristic~2, full prime fields, and multiplicative cosets uniformly, then over prime fields it is tight on every cell we could compute exactly. To turn it into attacks, we add full-block structures, cheap-coordinate elimination, and weighted moments. The first makes the initial S-box layer free, the second extracts equations from states that are only partially balanced, and the third yields thousands of equations from a single structure. We recover the master key of the full twelve-round Dux{} over F_{65537} from 2^{32} chosen ciphertexts in 45 core-hours, executed on random keys. On Yux{} we recover the key of eleven of the fourteen rounds of YupXp{} and of YuXbig{} from 2^{32} chosen ciphertexts, executed as well, against 2^{96} previously on YuXbig{}. Our distinguishers on Dux{} coincide with those of independent concurrent work by Liu and Sun. Furthermore, our key recovery attack lowers the data complexity of their full-round attack from 2^{67.58} to 2^{32}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2045) | 2026-09-15
