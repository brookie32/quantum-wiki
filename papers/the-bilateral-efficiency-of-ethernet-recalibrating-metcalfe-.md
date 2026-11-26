---
title: "The Bilateral Efficiency of Ethernet: Recalibrating Metcalfe and Boggs After Fifty Years"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.19406"
summary: "arXiv:2603.19406v3 Announce Type: replace-cross Abstract: In July 1976, Metcalfe and Boggs published their foundational paper on Ethernet in Communications of the ACM. Their efficiency model -- E = (P"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2603.19406v3 Announce Type: replace-cross Abstract: In July 1976, Metcalfe and Boggs published their foundational paper on Ethernet in Communications of the ACM. Their efficiency model -- E = (P/C)/(P/C + W*T) -- measures the fraction of Ether time carrying good forward packets under contention. For fifty years this model has framed how the community thinks about Ethernet performance. We argue it is silent on the question that matters for modern intra-rack interconnect: bilateral transaction efficiency -- the fraction of link time that produces committed agreements between sender and receiver. Metcalfe and Boggs themselves planted the seed in their EFTP "end-dally" protocol (Section 7.2.2), and the deeper anchor is older still: Abramson's Alohanet carried positive acknowledgments at the link layer -- a bilateral mechanism Metcalfe consciously removed in 1973 to obtain Ethernet's simple, ACK-free packet format. The result is a fifty-year bilateral zigzag: Aloha (bilateral) to Ethernet (unilateral) to the EFTP end-dally (bilateral) to TCP (unilateral-with-bilateral-above). We formalize bilateral efficiency, connect it to the back-to-back Shannon channel with Perfect Information Feedback, and -- scoping the claim explicitly to intra-rack distances of one meter or less -- describe how the Open Aethernet link recovers mutual knowledge at the link layer. The correction to Table 1 is not a different set of numbers. It is a different question. A new appendix places the 2025-2026 return of link-level retry (UEC, OCP ESUN, UALink) in this history and shows that it restores half of the end-dally: the sender learns of delivery, the receiver never learns that the sender knows. It opens from Ron Crane's observation that produced Fast Ethernet: carried to 100 Gb/s, the same arithmetic makes the minimum frame about one meter long.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.19406) | 2026-11-26
