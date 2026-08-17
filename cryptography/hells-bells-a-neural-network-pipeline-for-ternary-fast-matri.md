---
title: "Hell’s Bells: A Neural Network Pipeline for Ternary Fast Matrix Multiplication Algorithms"
date: "2026-08-14"
updated: "2026-08-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1688"
summary: "We present a neural network-based pipeline for efficiently generating fast matrix multiplication (FMM) algorithms of small but arbitrary dimensions (n,m,k). Our neural network is general and tunable t"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

We present a neural network-based pipeline for efficiently generating fast matrix multiplication (FMM) algorithms of small but arbitrary dimensions (n,m,k). Our neural network is general and tunable to output FMM schemes with specific properties, and in this paper we specifically target aspects that are useful and important in practical implementation, such as ternarity (coefficients in {-1, 0, 1}), sparseness and a low number of additions after optimization (addition reduction carried out separately). We generate and optimize thousands of FMM algorithms and show that our generation method is beneficial in terms of performance across the entire FMM pipeline (both the FMM generation itself and optimization of additions). We discuss performance metrics and utilize heatmaps to visualize and understand this performance. We achieve record-low arithmetic (additive) complexity for various combinations of dimensions. For (n,m,k) = (2,2,k), our method performs particularly well. Our improvement compared to previous results increases with k. We show that the (addition) optimization process can behave very differently depending on the dimensions considered, indicating how further improvements (beyond our results) can be targeted. In particular, in the (n,m,k) = (2,2,k) setting, we show evidence of structural FMM properties coming into play, concretely showing that FMM generation with a minimal number of additions is sometimes suboptimal with respect to the entire FMM pipeline. Finally, we make our neural network implementation, our generated FMM schemes, heatmap utilities and datasets publicly available.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1688) | 2026-08-14
