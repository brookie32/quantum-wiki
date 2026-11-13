---
title: "Affine Combiners for Reed-Solomon Proximity Gaps"
date: "2026-11-11"
updated: "2026-11-13"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2863"
summary: "Reed–Solomon proximity gaps establish soundness guarantees for protocols that test received words through random combinations. For length-n codes over F_q, classical scalar combiners achieve error O(n"
last_verified: "2026-11-13"
review_by: "2027-02-11"
stale: false
---

Reed–Solomon proximity gaps establish soundness guarantees for protocols that test received words through random combinations. For length-n codes over F_q, classical scalar combiners achieve error O(n/q) in the unique-decoding regime, with larger known bounds near the Johnson radius. We prove smaller error bounds using affine combiners, which combine two received words f,g as f(x)+(alpha+eta x)g(x), where alpha,eta are independent uniform elements of F_q. For output degree bound d=rho n, fixed rhoin(0,1) and 0<eta<1-sqrt{rho}, and sufficiently large block length n, we prove mutual correlated agreement (MCA) with one coordinate of agreement loss at threshold A=lceil(sqrt{rho}+eta)nrceil, with error O_{rho,eta}left(frac{1}{q}+frac{n^2}{q^2}right). The result holds over arbitrary evaluation domains in every finite field, including prime and binary extension fields. The agreement threshold can approach the Johnson threshold, beyond unique decoding. For qge n^2, our error is O_{rho,eta}(1/q), an asymptotic factor-n separation from scalar combiners: we prove that their worst-case MCA error is Omega_{rho,eta}(n/q) at the same agreement threshold and with the same one-coordinate loss. We also prove that affine combiners incur worst-case error Omega_{rho,eta}(n/q) when no agreement loss is allowed. Thus one coordinate of agreement loss is necessary for our guarantee; this relaxation of standard MCA reduces the guaranteed common agreement fraction by at most 1/n. We also extend the result to k-variate Reed–Muller codes on subfield grids, obtaining MCA error O_{rho,eta,k}(q^{-k}) for fixed rho,eta,k, sufficiently large n, and qge n^{k+1}, with agreement loss n^{1-1/k}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2863) | 2026-11-11
