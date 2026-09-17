---
title: "Square Root of All Evil: The Dangers of Falcon's Superfluous Square Roots"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2046"
summary: "Falcon is one of the 3 post-quantum signature schemes already selected by NIST for standardization (as FN-DSA). It is very compact and efficient, but also infamously difficult to implement correctly a"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Falcon is one of the 3 post-quantum signature schemes already selected by NIST for standardization (as FN-DSA). It is very compact and efficient, but also infamously difficult to implement correctly and securely. This is due in particular to its reliance of various floating point operations, the most complex and costly of which are square root computations. In this paper, we first point out that those square root computations are in fact wholly unnecessary: the algorithm can be rewritten without them, resulting in a somewhat simpler implementation that is equally fast or even slightly faster. We then observe that they also present security risks, in particular as a singularly sensitive target for physical attacks. We demonstrate this with a fault attack, supported by concrete experiments against an ARM Cortex-M4 microcontroller target. We show that injecting a single glitch in one square root computation, and then generating around a million signatures with the unperturbed signing algorithm, leads to full key recovery with 100% success rate and, moreover, faulty signatures are not easy to distinguish from validly generated ones. This makes this fault attack the most devastating against Falcon to date, in contrast with earlier attacks requiring hundreds of millions of signature samples, many injected faults, or resulting in signatures that are straightforward to distinguish from regular ones. In addition, we mention potential risks of the square root computations from the standpoint of dependency management and supply chain security.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2046) | 2026-09-15
