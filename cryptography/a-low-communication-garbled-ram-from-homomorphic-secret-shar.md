---
title: "A Low-Communication Garbled RAM from Homomorphic Secret Sharing"
date: "2026-09-12"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1998"
summary: "Garbled circuits are fundamental in modern cryptography and secure two- or multi-party computation. For real-world programs that are naturally expressed in the Random-Access Machine (RAM) model, garbl"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Garbled circuits are fundamental in modern cryptography and secure two- or multi-party computation. For real-world programs that are naturally expressed in the Random-Access Machine (RAM) model, garbled RAM is the RAM counterpart of garbled circuits: they avoid the cost of compiling the entire program into a circuit, with communication complexity serving as the primary efficiency metric. We study the setting in which the RAM program is public, while the input data and memory contents remain secret except for the prescribed output. We construct a garbled RAM for programs running in time T over memory consisting of N words of W bits each, the scheme achieves [ O(T dot (W + lambda) dot log N) + poly (lambda) ] bits in communication, where lambda is the security parameter. For sufficiently large word size Wge lambda and running time Tgepoly(lambda), the communication becomes O(T W log N), asymptotically matching the bandwidth of an optimal oblivious RAM. Since any secure garbled RAM must hide memory accesses as in oblivious RAMs, our construction can be viewed as compiling an oblivious RAM into a non-interactive analogue, without incurring additional asymptotic communication cost. Technically, our garbled RAM builds on the recent succinct garbled circuits of Ishai, Li, and Lin (Crypto'25) and Li, Lin, and Lu (Eurocrypt'26), which are in turn based on homomorphic secret sharing. Accordingly, we inherit their circular-power variants of the Decisional Diffie-Hellman or Ring Learning-With-Errors assumptions. We also use techniques from the recent work on garbled arithmetic RAM, called Zebra, by Gu, Ghoshal, and Shi (Eurocrypt'26). Compared to Zebra, which achieves the same O(TWlog N) communication for *arithmetic* RAM programs that only perform arithmetic over large and bounded integers, our work focuses on the standard *boolean* RAM model. Compared to the best garbled RAM in the random oracle model, due to Liu, Liu, Luo, and Heath (ACM CCS'26), we remove a multiplicative factor lambda in communication.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1998) | 2026-09-12
