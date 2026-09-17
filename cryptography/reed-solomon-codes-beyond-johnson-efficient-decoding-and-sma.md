---
title: "Reed-Solomon Codes Beyond Johnson: Efficient Decoding and Smaller Cryptographic Proofs"
date: "2026-09-16"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2056"
summary: "List decoding Reed–Solomon codes is a central problem in coding theory and, together with mutual correlated agreement (MCA), underpins the soundness of many succinct cryptographic proofs. In this work"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

List decoding Reed–Solomon codes is a central problem in coding theory and, together with mutual correlated agreement (MCA), underpins the soundness of many succinct cryptographic proofs. In this work, we give precise quantitative bounds on Reed–Solomon list decoding and MCA up to capacity, provide deterministic decoding algorithms that remain efficient over cryptographically large fields, and specialize our bounds to reduce proof sizes in implemented proof systems. Our bounds apply to arbitrary prescribed evaluation domains; beyond Johnson, they require sufficiently large field characteristic. Refining the hidden-derivative method of Brakensiek, Chen, Putterman, Zhang, and Zheng, we obtain an explicit agreement threshold a_1(rho) strictly below the Johnson bound sqrt{rho}, using only the first derivative, without requiring its evaluations in the received word. At agreement a_1(rho)+eta_1, where eta_1>0, our sharper interpolation and candidate counts give list size O_rho(n/eta_1^2) and MCA error O_rho(n^2/(qeta_1^4)) for codes of length n over F_q. Higher derivatives give explicit quantitative bounds up to capacity, uniformly over all rates, sharpening prior MCA results in Zheng's unpublished manuscript and Jeronimo's work, concurrent with ours. At fixed rate, for agreement gap eta_0>0 above Johnson, we improve the MCA error bound of Ben-Sasson et al. (BCHKS) from O_rho(n/(qeta_0^5)) to O_rho(n/(qeta_0^3)), in every characteristic. Our decoders use agreement constraints to recover close messages without enumerating initial field values. With fast explicit field arithmetic, at fixed rate and a fixed positive agreement margin above the respective threshold, deterministic decoding takes widetilde O(nlog q) bit operations above Johnson in every characteristic and widetilde O(n^2log q) above our first-order curve in sufficiently large characteristic. Decoding remains polynomial in n and log q at every fixed positive gap from capacity, under the same requirement of sufficiently large characteristic. Our first-derivative bounds give the first proof-size reductions in existing proof-system implementations from provable Reed–Solomon proximity-gap bounds beyond the Johnson radius. At unchanged security targets, we save 79.4 KB (11.1%) for ProveKit passport proofs, 13.2 KB (4.63%) for ZisK compressed final proofs, and 59.8 KB (4.85%) for LambdaVM CPU subproofs. We have formally verified the list-decoding and MCA bounds and concrete parameter certificates in ArkLib, a Lean library for verified cryptographic proofs, and proved correctness of a simplified version of our list-decoder.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2056) | 2026-09-16
