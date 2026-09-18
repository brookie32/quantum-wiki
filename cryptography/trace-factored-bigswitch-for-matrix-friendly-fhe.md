---
title: "Trace-Factored BigSwitch for Matrix-Friendly FHE"
date: "2026-09-16"
updated: "2026-09-18"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2058"
summary: "Evaluation keys represent a primary memory and initialization bottleneck in matrix-native fully homomorphic encryption (FHE). In the Gentry–Lee (GL) framework, each Trace product yields a four compone"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

Evaluation keys represent a primary memory and initialization bottleneck in matrix-native fully homomorphic encryption (FHE). In the Gentry–Lee (GL) framework, each Trace product yields a four component ciphertext whose BigSwitch procedure requires two extended-ring keys, dominated by a massive product-secret key (sXsY → sX). We present Trace-Factored BigSwitch (TFB), which structurally eliminates this product-secret evaluation key by exploiting the rank one tensor structure of the Trace-generated key, (1, sX, sY , sXsY ) = (1, sY ) ⊗ (1, sX). By routing the product secret through an sY → sX switch followed by standard base ring (s^2)X → sX relinearization, TFB achieves an exact evaluation-key memory saving of (n − 1)/(2n) (≈ 50%) without ever generating or storing evk_XY →X. To amortize TFB’s recurring base-ring relinearization cost in blocked matrix multiplication, we introduce FRee-L (Fused Relinearization with noise reduction). FRee-L accumulates K Trace products componentwise in the four-component domain and invokes BigSwitch only once per output tile, reducing post-processing noise injections from K to one and amortizing the latency overhead as O(1/K). In our OpenFHE-linked prototype (n = 256), TFB reduces the coefficient-domain BigSwitch key footprint from 768.0 to 385.5 MiB (49.80%), peak RSS by 15.31%, and cold key preparation by 51–63%. On real GPT-2 attention kernels (K = 4), FRee-L lowers TFB’s paired overhead to 5.90%, which further diminishes to 0.1933% (K = 160) and 0.0618% (K = 512) in deep accumulation workloads, confirming that substantial key savings are achieved with negligible workload-level compute penalty.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2058) | 2026-09-16
