---
title: "Learning to Rank for Selected Configuration Interaction"
date: "2026-07-27"
updated: "2026-07-27"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2605.10348"
summary: "arXiv:2605.10348v2 Announce Type: replace Abstract: The accurate description of electron correlation is a central challenge in computational chemistry, with selected configuration interaction (SCI) em"
last_verified: "2026-07-27"
review_by: "2026-10-25"
stale: false
---

arXiv:2605.10348v2 Announce Type: replace Abstract: The accurate description of electron correlation is a central challenge in computational chemistry, with selected configuration interaction (SCI) emerging as a powerful tool to approach the full CI limit. While recent machine learning (ML) integrations have accelerated determinant selection, existing regression and classification approaches suffer from a fundamental objective-loss mismatch: they evaluate the importance of determinants in isolation without explicitly accounting for their relative importance ranking. Here, we introduce ranking configuration interaction (RCI), a novel ML-supported SCI framework that reframes determinant selection as a pairwise ranking problem. Building upon a Transformer-based architecture to capture complex, non-local orbital dependencies, RCI progressively optimizes the partial ordering of determinants. By doing so, RCI aligns the training objective more closely with the intrinsic ranking nature of SCI. Extensive benchmarks across both plane-wave and Gaussian basis sets, including the molecules N_2, CO, H_2O, NH_3, and C_2, demonstrate the efficiency of RCI. Compared to previously reported classification baselines, RCI consistently accelerates convergence-reducing overall computational time by 23% to over 50% depending on the system, and requiring only 55% of the determinant count in representative cases such as N_2 and CO. Furthermore, RCI exhibits robust performance and reaches chemical accuracy on the highly challenging iron-sulfur cluster using only 12% of the full CI space. Notably, RCI outperforms recent regression-based SCI methods by delivering a more than 15% improvement in accuracy at comparable determinant counts. RCI also demonstrates higher efficiency than heat-bath CI on the strongly correlated chromium dimer, yielding a compact and accurate wavefunction.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2605.10348) | 2026-07-27
