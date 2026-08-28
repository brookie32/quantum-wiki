---
title: "Practical Differential Fault Attacks on the GPRS Standard Ciphers"
date: "2026-08-26"
updated: "2026-08-28"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1806"
summary: "GEA-1 and GEA-2 are two standard stream ciphers used in GPRS (General Packet Radio Service) to protect against eavesdropping GPRS between the base station and the phone. Now, a range of current phones"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

GEA-1 and GEA-2 are two standard stream ciphers used in GPRS (General Packet Radio Service) to protect against eavesdropping GPRS between the base station and the phone. Now, a range of current phones still support them. In this paper, a differential fault attack on the GEA-like stream ciphers under the random fault model is proposed for the first time. In this attack, an efficient dedicated algorithm for identifying the exact fault location is proposed. By using this dedicated algorithm, the attacker can succeed in determining the exact fault location. As applications, practical differential fault attacks on the GPRS standard ciphers (i.e., GEA-1 and GEA-2) are presented, which recover the 64-bit secret keys of GEA-1 and GEA-2 with time complexities of {2^{{rm{33}}{rm{.807}}}} and {2^{{rm{33}}{rm{.858}}}}, respectively. We validate the cryptanalytic results by simulating the whole attacks on the platform ChipWhisperer Lite. The experimental results show that both GEA-1 and GEA-2 can be broken within sixteen minutes on a common laptop. Finally, the possible countermeasures are presented to protect the processed data of massive GPRS devices.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1806) | 2026-08-26
