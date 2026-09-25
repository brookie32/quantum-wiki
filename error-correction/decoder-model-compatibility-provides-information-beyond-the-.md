---
title: "Decoder Model Compatibility Provides Information beyond the Logical Gap under Drifting and Correlated Quantum Noise"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.29018"
summary: "arXiv:2609.29018v1 Announce Type: new Abstract: Quantum error-correcting decoders provide both corrections and confidence estimates for the logical-error risk of individual measurement records. Such c"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.29018v1 Announce Type: new Abstract: Quantum error-correcting decoders provide both corrections and confidence estimates for the logical-error risk of individual measurement records. Such confidence can guide postselection, but it depends on the accuracy of the decoder noise model. When the physical device drifts away from that model, confidence measures such as the logical gap can become miscalibrated. We show that this mismatch can itself provide useful information. On IBM quantum hardware, syndrome statistics drift across consecutive acquisition windows, and the resulting detector histories differ substantially from those predicted by the stationary detector error model used for decoding. We observe a similar hardware-model mismatch in independent Google surface-code memory data. We exploit this effect by assigning additional rejection weight to detector histories that are unlikely under the assumed model. For minimum-weight perfect matching (MWPM), the minimum weight W provides an inexpensive proxy for syndrome surprisal. On held-out IBM repetition-code memories, likelihood-aware postselection reduces the retained logical-error probability (LEP) by 10.6% at d=7 and 28.8% at d=9, both at 15% rejection. On Google ten-round d=5 XZZX surface-code memory data, it reduces retained LEP by 75.4% at 90% rejection. Applied to Google's magic-state cultivation experiment with the Tesseract decoder, it reduces tomography infidelity by 34.7% with 30% additional grafting-stage rejection, or increases accepted yield by 30.4% at a target fidelity of 97.0%. Burst-noise simulations show that the advantage persists as code distance and syndrome-extraction volume increase. The method reuses quantities already produced during logical-gap decoding and requires only an additional fitting step.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.29018) | 2026-09-25
