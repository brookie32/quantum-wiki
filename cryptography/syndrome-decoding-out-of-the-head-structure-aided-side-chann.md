---
title: "Syndrome Decoding out of the Head: Structure-Aided Side-Channel Witness Recovery on SDitH"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2760"
summary: "Regular syndrome decoding (RSD) underlies several code-based signature schemes, including SD-in-the-Head (SDitH). Its secret witness has exactly one nonzero coordinate per block, and the selected posi"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Regular syndrome decoding (RSD) underlies several code-based signature schemes, including SD-in-the-Head (SDitH). Its secret witness has exactly one nonzero coordinate per block, and the selected positions must satisfy a public syndrome equation. In this work, we show how these structural constraints can be exploited to recover the complete witness from imperfect side-channel information. We present a profiled power analysis of the witness-embedding operation in the SDitH Round-3 reference implementation. We train convolutional neural networks (CNNs) to classify the mux digits encoding each regular block and use their outputs to rank candidate positions. To correct errors in these predictions, we combine the resulting rankings with the public syndrome and the regularity constraints. We formulate this recovery problem as an affine correction system with block-validity constraints and analyze its rank, consistency, and uniqueness for the systematic parity-check matrix used in SDitH. Based on this analysis, we develop a quotient-syndrome decoder that identifies blocks whose true positions fall outside the initial candidate lists, avoiding exhaustive enumeration of block subsets. We evaluate our attack on an ARM Cortex-M4 using measured power traces. With a single target trace per key, our approach recovers all 100 test witnesses under -Os using 4,000 profiling traces, and 91 out of 100 under -O3 using 16,000 profiling traces. Each successful recovery matches all 616 serialized witness bits. These results demonstrate how the regular structure of RSD and the public syndrome can compensate for imperfect side-channel predictions, thereby enabling full-witness recovery.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2760) | 2026-11-04
