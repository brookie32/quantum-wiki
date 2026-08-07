---
title: "Scalable Circuit Cutting: A Framework for Combined Gate and Wire Cuts Using Gate Groups"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.05287"
summary: "arXiv:2608.05287v1 Announce Type: new Abstract: Quantum circuit cutting enables the execution of large circuits on devices with a limited number of qubits by partitioning circuits into independent sub"
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2608.05287v1 Announce Type: new Abstract: Quantum circuit cutting enables the execution of large circuits on devices with a limited number of qubits by partitioning circuits into independent subcircuits. However, this introduces a sampling overhead, which grows exponentially with the number of cuts, rendering the choice of cut placements critical for practical circuit cutting. Determining optimal cut placements remains computationally challenging, particularly as circuits grow in size. Additionally, existing circuit cutting approaches typically treat gate and wire cuts independently. Those combining both cutting approaches, however, do not take advantage of joint cutting, i.e., identifying common gate groups and cutting them jointly for a reduced overhead. This work presents a unified framework that combines gate and wire cutting within a single partitioning strategy, enabling more efficient circuit decompositions. Moreover, our approach incorporates joint cutting via a novel gate grouping technique, further reducing sampling overhead. By formulating the cut placement problem as a scalable graph partitioning task, our method efficiently identifies near-optimal cut placements for large circuits, also providing diagnostic feedback on whether circuits are suitable for cutting.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.05287) | 2026-08-07
