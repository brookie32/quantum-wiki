---
title: "On the Mismatch between Neural-Discovered Differential-Linear Features and Long-Round Distinguisher Construction"
date: "2026-09-02"
updated: "2026-09-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1858"
summary: "To the best of our knowledge, existing differential-neural cryptanalysis have not yet shown a clear round advantage over the strongest comparable classical analyses. Recent Fourier-based interpretabil"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

To the best of our knowledge, existing differential-neural cryptanalysis have not yet shown a clear round advantage over the strongest comparable classical analyses. Recent Fourier-based interpretability results show that, under a difference-only representation, features extracted from differential-neural distinguishers can be interpreted as classical differential-linear masks. This suggests a possible route toward longer-round classical cryptanalysis and motivates our question: can such neural-discovered masks serve as useful candidates in the search for long-round differential-linear distinguishers of ARX ciphers? As a prerequisite to the long-round study, we first characterize the short-round differential-linear candidates exposed by difference-only differential-neural distinguishers. We introduce Conv1DFully to facilitate mask-level analysis by removing the residual tower and reorganizing the first convolution along the ciphertext-difference bit dimension. On Speck32/64, the dominant differential-linear feature remains preserved after these modifications. On SipHash, we compare Fourier masks extracted from trained distinguishers with an exhaustive evaluation of a low-Hamming-weight output-mask space. The neural-extracted masks are concentrated among high-correlation differential-linear approximations, including several of the strongest candidates examined. These experiments provide a controlled basis for treating neural-extracted masks as candidates in the subsequent long-round analysis. We then examine their utility in the known 18-round Speck128/128 distinguisher with a 5+8+5 decomposition. Under the same middle input difference, an 8-round difference-only differential-neural distinguisher recurrently exposes several masks with substantially stronger local middle correlations than the classically selected mask. However, after 5-round single XOR-linear extensions, these masks yield considerably weaker overall 18-round correlations. We further impose sparsity guidance on the first convolutional layer to promote low-Hamming-weight candidates. Under this guidance, the intermediate mask used in the classical 18-round distinguisher is recovered in the first-layer candidate set in 9 of 30 independent runs, showing that the neural model can reproduce a long-round-useful classical candidate. Nevertheless, this recovery is not stable, and the final neural decision rule still favors locally stronger features rather than the classically selected mask. These results indicate that differential-neural distinguishers can assist long-round candidate generation, while reliable recovery and long-round-aware prioritization remain unresolved.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1858) | 2026-09-02
