---
title: "Fast Fault-Tolerant Decoders for Hypergraph Product and Lifted-Product Codes"
date: "2026-09-01"
updated: "2026-09-01"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.31040"
summary: "arXiv:2608.31040v1 Announce Type: cross Abstract: We design low-complexity, fault-tolerant decoders for quantum low-density parity-check (QLDPC) codes with the goal of reducing decoding latency. We ta"
last_verified: "2026-09-01"
review_by: "2026-11-30"
stale: false
---

arXiv:2608.31040v1 Announce Type: cross Abstract: We design low-complexity, fault-tolerant decoders for quantum low-density parity-check (QLDPC) codes with the goal of reducing decoding latency. We target two major bottlenecks of decoding under the circuit-level noise model: (i) post-processing via order-statistics decoding (OSD), and (ii) the large number of auxiliary variable nodes commonly introduced to represent CNOT-induced correlations during syndrome extraction. Our key observation is that propagating CNOT faults (hook errors) create stabilizer-induced trapping sets (TSs) that are intrinsic to hypergraph-product (HGP) and lifted-product (LP) constructions. Therefore, instead of modeling each such fault with an explicit correlation node and relying on OSD to clean up the resulting failures, we design message-passing decoders that resolve the corresponding stabilizer-induced TSs directly. We obtain these decoders by deriving QLDPC decoders from decoders for the parent classical LDPC codes and using them collectively to correct broad families of stabilizer-induced TSs. For CNOT faults that manifest primarily as syndrome errors, we show that their effect is equivalent to a data error together with syndrome-bit measurement errors. Consequently, given repeated measurements and a decoding graph that already includes nodes representing syndrome-bit errors, no distinct variable node is needed for each CNOT fault. Using a phenomenological Tanner graph with nodes representing only data errors and syndrome-bit errors, simulations on the LP codes show a reduction in, or comparable, logical error rates relative to BP+OSD, at substantially lower decoding complexity.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.31040) | 2026-09-01
