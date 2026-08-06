---
title: "DYNAFIX: Dynamic Fixed‑Point Encoding for Arbitrary‑Range MPC"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1612"
summary: "Privacy-preserving computation over real numbers typically employs either floating-point or fixed-point arithmetic. While fixed-point methods are highly efficient, they struggle to handle wide dynamic"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Privacy-preserving computation over real numbers typically employs either floating-point or fixed-point arithmetic. While fixed-point methods are highly efficient, they struggle to handle wide dynamic ranges. Conversely, floating-point methods support a much larger numerical scope but incur overheads more than a hundred times higher than their fixed-point counterparts. In this paper, we propose DYNAFIX, a dynamic fixed-point computation scheme that strikes a balance between floating-point and fixed-point arithmetic. Compared to traditional fixed-point approaches, our scheme supports an arbitrary numerical range; compared to floating-point computation, it maintains performance comparable to fixed-point execution. Experimental results demonstrate that our method achieves a 24.1imes speedup over the state-of-the-art when evaluating high-precision functions, such as the exponential function.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1612) | 2026-08-05
