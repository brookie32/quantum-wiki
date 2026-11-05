---
title: "Discovering correlated error mechanisms: data-driven augmentation of detector error models improving decoding"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.06605"
summary: "arXiv:2611.06605v1 Announce Type: new Abstract: Accurate decoder priors are essential for high-performance quantum error correction. Theoretical noise models inevitably omit physically relevant error "
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.06605v1 Announce Type: new Abstract: Accurate decoder priors are essential for high-performance quantum error correction. Theoretical noise models inevitably omit physically relevant error mechanisms, most notably correlated errors, which appear consistently in experimental error budgets yet are absent from standard models. We introduce a data-driven method for augmenting detector error models (DEMs) by discovering entirely new error mechanisms directly from experimental detector-firing statistics, going beyond most existing approaches that merely refine the probabilities of already-known mechanisms. Our method generates candidates by combining pairs of existing mechanisms as building blocks, then filters and validates them using pairwise and higher-order detector correlations. Crucially, this construction provides each newly discovered mechanism with a well-defined logical effect derived from the constituent error mechanisms, enabling its direct use in decoding. Furthermore, each mechanism is accompanied by a natural decomposition into lower-order components, preserving compatibility with the original decoder. This is particularly valuable in settings that rely on correlated graph-based decoders such as correlated matching. We evaluate the method on surface-code simulations with correlated noise and correlated-matching decoding, demonstrating that, in a realistic near-term noise scenario, DEM augmentation increases the Lambda parameter by 20% across code distances 7-15 and reduces the logical error rate by 75% at code distance 15 relative to the unaugmented DEM. On experimental data from Google's superconducting device, the augmented DEM increases the Lambda parameter by 9% across code distances 5-7 and yields a reduction of 14% in logical error rate over the baseline for distance 7. To our knowledge, this is the first data-driven DEM augmentation method that produces decomposed hyperedges with assigned logical effects.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.06605) | 2026-11-05
