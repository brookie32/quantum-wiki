---
title: "The Good, the Bad, and the Noisy: A Systematic Analysis of Ring-Oscillator-Based Noise Generators"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2597"
summary: "Hiding countermeasures, alongside masking, play an important role in modern hardware security for protecting against side-channel attacks. Additive noise generators are one such hiding countermeasure."
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Hiding countermeasures, alongside masking, play an important role in modern hardware security for protecting against side-channel attacks. Additive noise generators are one such hiding countermeasure. They increase the noise, thereby lowering the signal-to-noise ratio and, simultaneously, amplifying the effectiveness of masking countermeasures. Among the different design options for additive noise generators, ring-oscillator-based designs feature regularly in scientific publications. These existing works not only differ in their designs, but also in their evaluation methods; therefore, they do not permit fair comparisons or enable systematic evaluations. Thus, it is currently not possible to design ring-oscillators for noise generation in an informed and tailored way. In this paper, we address this lack of systematic comparisons of existing designs, and discuss the possibility of filtering out the generated noise and further limitations of ring-oscillator-based noise generators. We find that many existing designs do not consider the need to amplify the output signal or the risk of filtering. As a consequence, the existing designs do not sufficiently lower the signal-to-noise ratio in our experiments. However, using these results, we provide a guideline for tailoring and configuring ring-oscillators so that they efficiently add noise in the desired frequency spectrum. This includes deciding on the inverter chain length, the amplification of the output, and the randomization of the output frequency. Finally, we apply this methodology to build a tailored ring-oscillator-based noise generator for an exemplary AES implementation and find that it significantly outperforms existing ring-oscillator-based designs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2597) | 2026-10-22
