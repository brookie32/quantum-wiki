---
title: "Uniform Sharing in Multiple Stages: Towards Second-Order Security"
date: "2026-10-14"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2483"
summary: "Mitigating Side‑Channel Analysis (SCA) of cryptographic implementations relies heavily on masking schemes; however, achieving efficient and straightforward hardware realizations remains challenging. W"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

Mitigating Side‑Channel Analysis (SCA) of cryptographic implementations relies heavily on masking schemes; however, achieving efficient and straightforward hardware realizations remains challenging. While Threshold Implementation (TI) provides provable security against glitches in hardware, it incurs significant area overhead due to the large number of shares required to protect non‑linear functions. Successor schemes achieve the same security order with a minimal number of shares, but often rely on a high amount of per‑cycle randomness, especially at higher orders. Recent optimizations such as NullFresh and MultiStage attain minimal share counts without additional randomness; however, they lack a generalized methodology for higher‑order security. In particular, although MultiStage enables automated generation of low‑randomness masked designs, it is currently limited to first‑order protection. In this work, we bridge this gap by introducing an automated masking technique for arbitrary functions that guarantees second‑order security in the glitch‑extended probing model. Building upon the MultiStage approach, our method preserves the efficiency of NullFresh by minimizing requirements for fresh masks, while overcoming structural limitations of previous schemes. We demonstrate the feasibility of the approach on the lightweight block ciphers PRINCE, Midori, and SKINNY. The resulting designs are formally verified using SILVER and PROLEAD, and experimentally evaluated on FPGA using TVLA.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2483) | 2026-10-14
