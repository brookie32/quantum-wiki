---
title: "Magic state cultivation with lattice-surgery escape on superconducting hardware"
date: "2026-11-18"
updated: "2026-11-18"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.22035"
summary: "arXiv:2611.22035v1 Announce Type: new Abstract: Magic state cultivation (MSC) is a low-overhead protocol for fault-tolerantly preparing logical magic states. In this work, we implement two MSC variant"
last_verified: "2026-11-18"
review_by: "2027-02-16"
stale: false
---

arXiv:2611.22035v1 Announce Type: new Abstract: Magic state cultivation (MSC) is a low-overhead protocol for fault-tolerantly preparing logical magic states. In this work, we implement two MSC variants to prepare a magic state in a distance-5 code on a publicly available IBM Nighthawk processor. The first is a lattice-surgery escape, recently proposed by Hirano et al. and experimentally studied here for the first time. The second is a grafting escape, previously demonstrated by Rosenfeld et al., and extended here by incorporating a switch into a matchable code. Both protocols begin with fault-tolerant cultivation of a T state on a color code, followed by an escape into a larger code. We decode the results using minimum-weight perfect matching or Tesseract on circuit-level error models calibrated to the hardware noise. Compared with the previous experiment, our cultivated T state achieves a logical error probability of 2e-5 at the T-state injection angle, nearly 10x lower with about 3x the retainment. Moreover, our execution of the grafting escape has a 2x lower logical error rate per stabilizer round at a higher retainment. When comparing the two protocols under identical execution conditions and complementary gap postselection based on decoder confidence, lattice-surgery escape into the surface code preserves a T-state fidelity above 0.99 ten rounds after escape at about 5% retainment. By contrast, matchable-switched grafting drops below 0.95 fidelity at comparable retainment. Furthermore, the lattice-surgery escape reaches a logical error rate per stabilizer round of about 0.14% with around 11% average shot retainment. These results establish lattice-surgery escape as a practical MSC protocol that benefits from a direct transition into a surface code, and demonstrate the lowest MSC error and the highest surface-code magic-state fidelity reported to date, advancing the experimental realization of fault-tolerant non-Clifford gadgets.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.22035) | 2026-11-18
