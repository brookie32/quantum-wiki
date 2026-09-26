---
title: "SafeCast: End-to-End Security for Ultra-High-Bitrate Broadcast Media"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2189"
summary: "To address the scalability and flexibility limitations of dedicated point-to-point cabling in broadcast production, the broadcasting community created a suite of standards for carrying media over IP m"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

To address the scalability and flexibility limitations of dedicated point-to-point cabling in broadcast production, the broadcasting community created a suite of standards for carrying media over IP multicast. This shift removes the inherent physical protection that dedicated cabling provides, exposing streams to tampering and eavesdropping. Such threats have been widely reported and pose major risks to broadcasters and their audiences. Despite almost a decade of deployment, the security of IP-based broadcast has received little academic attention. We collaborate with the European Broadcasting Union (EBU) to establish the security and deployment requirements of this environment. We introduce SafeCast, a system to secure the transmission of ultra-high-bitrate multicast media. SafeCast builds on established and standardized protocols (the MLS group key agreement protocol and the SRTP media-protection protocol), while extending and adapting them to the demanding setting of broadcast media. SafeCast provides strong confidentiality and integrity guarantees, and exploits the precise clock synchronization of broadcast networks to achieve cheap per-sender authentication. We evaluate SafeCast against the stringent deployment requirements of production facilities (throughput, latency, large dynamic groups) and find that it can sustain the most common media formats with ample headroom.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2189) | 2026-09-23
