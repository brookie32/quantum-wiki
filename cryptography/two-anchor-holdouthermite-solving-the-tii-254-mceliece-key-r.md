---
title: "Two-Anchor Holdout/Hermite: Solving the TII-254 McEliece Key Recovery Challenge"
date: "2026-09-11"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1986"
summary: "We report on the solution to the TII-254 McEliece key recovery challenge -- currently the hardest solved challenge under the original brute-force metric (2^{254}). The parameters of TII-254 are (m,t,n"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

We report on the solution to the TII-254 McEliece key recovery challenge -- currently the hardest solved challenge under the original brute-force metric (2^{254}). The parameters of TII-254 are (m,t,n) = (8,12,223), defining a binary [223,127] code specified by a full-rank (96 imes 223) parity-check matrix. We state the method as a thirteen-step process, separating heuristic and non-heuristic choices. At a high level, we computed two complete 121-dimensional relation kernels conditioned at distinct public coordinates, combined them to isolate a certified 80-dimensional pair core, removed a 64-dimensional common nuisance space, and identified the remaining 16 dimensions as an F_{2^8} projective-line geometry. This yielded all 87 visible locators, after which a deterministic completion search recovered the full support and polynomial. The two final Krylov sequences alone used 27.2 GPU-hours on NVIDIA GH200s, excluding GPU reconstruction and CPU processing. We provide a self-contained artifact with compact recovery inputs and code, an independent key verifier, and Lean proofs of the reusable linear-algebraic steps.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1986) | 2026-09-11
