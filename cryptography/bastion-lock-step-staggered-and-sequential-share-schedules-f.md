---
title: "BASTION: Lock-Step, Staggered and Sequential Share Schedules for a First-Order Masked ML-KEM NTT on FPGA"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2765"
summary: "The Number Theoretic Transform (NTT) is the arithmetic core of ML-KEM (FIPS 203) and a prominent side-channel target in hardware. Because the transform is linear, first-order arithmetic masking applie"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

The Number Theoretic Transform (NTT) is the arithmetic core of ML-KEM (FIPS 203) and a prominent side-channel target in hardware. Because the transform is linear, first-order arithmetic masking applies share-wise without fresh randomness, which leaves one design decision open: when each share is processed. Published designs process the shares in sequence on one datapath, or on one datapath per share started a configurable delay apart and in random order; running both datapaths in lock-step is the third option. We implement the three schedules on one first-order masked NTT core for ML-KEM on Artix-7 and measure their cost and pre-silicon leakage under one synthesis flow. An iso-architectural unmasked control separates the cost of masking from that of parallelisation: the delivered lock-step core costs 1.56x the LUTs, 2.33x the slices and twice the DSPs of the control at an unchanged cycle count and 196.1 instead of 227.3 MHz, while the sequential core needs 9 LUTs more than the control at twice the cycles. We state when a set of samples combines both shares of a secret, measure the criterion on the RTL and use it as a cycle-accurate oracle. On a whole-design toggle model that sums both share domains, calibrated with injected flaws detected within 750 traces, no schedule leaks at first order in five pairs of runs of 10^5 traces. At second order the schedules form a scale: the lock-step core leaks in single samples, the sequential core only at the pair of samples that its public offset relates, and the staggered core in both ways at every delay we tested short of one transform. Every detected sample lies in the support view of the oracle, which flags up to 80% of the samples of a window for the univariate test, and some lie outside its form view, so lazy reduction matters. A check on the routed netlist finds no cell shared by the domains of the lock-step and staggered cores, and finds the cells that synthesis shares once the preservation attributes are removed. Silicon validation is left to future work.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2765) | 2026-11-04
