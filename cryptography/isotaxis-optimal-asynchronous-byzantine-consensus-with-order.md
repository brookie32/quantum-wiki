---
title: "Isotaxis: Optimal Asynchronous Byzantine Consensus with Ordering Linearizability"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2645"
summary: "Despite ensuring both consistency and liveness, state machine replication (SMR) protocols remain vulnerable to adversaries that manipulate transaction order, causing, e.g., MEV attacks. To mitigate th"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

Despite ensuring both consistency and liveness, state machine replication (SMR) protocols remain vulnerable to adversaries that manipulate transaction order, causing, e.g., MEV attacks. To mitigate this, researchers have proposed new variants augmented with order-fairness. However, existing protocols that employ dependency graphs, such as Aequitas (Crypto 2020), Themis (CCS 2023), and SpeedyFair (NDSS 2024), often suffer from suboptimal performance, limited resilience, or weakened security guarantees. Pompē (OSDI 2020) introduced a novel ordering notion called ordering linearizability (OL) that may circumvent those drawbacks. However, its guarantee holds only under favorable network conditions, making the protocol vulnerable to order fairness violations during network delays and susceptible to performance degradation in the presence of Byzantine faults. Also, implementing SMR under OL remains an open challenge in asynchronous settings, as no known protocol achieves this without sacrificing liveness of SMR. In this paper, we present mathsf{Isotaxis}, a state machine replication with ordering linearizability; moreover, our protocol has communication complexity O(nell+lambda n^2), where n is the number of processes, ell is the input (transaction) size, and lambda is the security parameter. This is optimal when ellgeq lambda n, while previous works have cubic communication. To the best of our knowledge, mathsf{Isotaxis} is the first protocol to achieve ordering linearizability in the asynchronous setting, especially one with optimal communication complexity and optimal Byzantine resilience. We implemented mathsf{Isotaxis} and conducted extensive experiments using up to 100 EC2 c6a.2xlarge instances. The experimental results show that our protocol robustly outperforms Pompē across all system scales, ranging from 4 to 100 nodes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2645) | 2026-10-26
