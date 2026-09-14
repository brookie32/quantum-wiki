---
title: "Angular Watermarking: Sharp Leakage Bounds and Public Subspace Validation"
date: "2026-09-12"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1989"
summary: "Does refreshing payload bits hide a fixed geometric watermark carrier when covariance is uninformative? For a Gaussian latent model with independently refreshed fair angular bits, we derive an exact f"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Does refreshing payload bits hide a fixed geometric watermark carrier when covariance is uninformative? For a Gaussian latent model with independently refreshed fair angular bits, we derive an exact fourth-order signature and a sharp relation between uniform decoding margin and distributional hiding. A fixed-probe operator bound has leading sufficient count O(p^3 log(p)/c(a)^2) at fixed rank, accuracy and confidence, where c(a)=sin(2*pi*a)/(2*pi*a). We then prove a dimension-independent centered fourth-tensor covariance bound whose constant (1+|c(a)|)^2 is attained when there are at least two carrier blocks. This yields a public finite-sample overlap certificate for any candidate subspace frozen before independent validation. The statistic needs no secret key and is computed by streaming projected fourth moments. For all eight archived outputs at p=240, 65,536 new directions per output give positive known- and unknown-scale lower bounds, with at least 95% simultaneous coverage for sixteen statements under the exact model. An exact working-subspace signal criterion and rank-dependent noise formula explain limits of subspace feedback. The main eight-seed training panel attains mean overlap 0.5999 against 0.3282 with a frozen initial frame at equal feature count. A noise-reducing variant improves feature-matched pilots but loses a near-compute-budget comparison; this negative result is retained. A complementary radial model provides directed population witnesses and a conditional certificate for a linear PNG carrier. The results identify and validate latent carrier subspaces; they do not establish adaptive training convergence, bit recovery or a neural watermark attack.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1989) | 2026-09-12
