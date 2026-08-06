---
title: "DuetORAM: Two-Server Distributed ORAM with Constant Rounds and O(log N) Communication"
date: "2026-08-05"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1613"
summary: "Distributed Oblivious RAM (DORAM) is a promising building block for privacy-preserving cloud databases and outsourced storage systems. However, existing two-server designs often rely on slow linear sc"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Distributed Oblivious RAM (DORAM) is a promising building block for privacy-preserving cloud databases and outsourced storage systems. However, existing two-server designs often rely on slow linear scans or heavy cryptographic primitives, making them struggle to balance efficiency and bandwidth, and thus hindering their practical deployment. We present DuetORAM, a two-server DORAM that achieves constant-round access with O(log N) communication while avoiding these computational bottlenecks. Our key idea is a replicated-to-shared block encoding that allows servers to keep identical ciphertexts for efficient PIR-based retrieval, while locally interpreting them as secret shares to enable oblivious eviction via a lightweight shuffle. We further design a secret-shared shuffle with an offline-online decomposition that shifts most bandwidth-intensive work to a preprocessing phase, significantly reducing online communication. We implement a prototype of DuetORAM and evaluate it under diverse network conditions. Our results show that DuetORAM outperforms both the state-of-the-art two-server scheme DUORAM (reducing retrieval latency by up to 170imes in LAN settings), and three-server design S^3ORAM (reducing retrieval latency by 1.7imes in LAN and accelerating eviction by 7imes in LAN and 5imes in WAN, respectively).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1613) | 2026-08-05
