---
title: "Beyond the Scope of This Paper: Practical Flash-Accelerator and Cache-Collision Timing Attacks on Microcontrollers"
date: "2026-10-29"
updated: "2026-10-31"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2673"
summary: "Cache and cache-collision attacks against AES are well-known since 2005, but their application to small (Cortex-M sized) microcontrollers has been limited in prior work, and in many cases the devices "
last_verified: "2026-10-31"
review_by: "2027-01-29"
stale: false
---

Cache and cache-collision attacks against AES are well-known since 2005, but their application to small (Cortex-M sized) microcontrollers has been limited in prior work, and in many cases the devices are assumed to be immune when they do not have a cache. However, the flash architecture of almost all microcontrollers introduces the same timing collision required for the well-known attacks and as a greatly underestimated channel. Recovery of AES keys using as little as 750 traces will be demonstrated on six popular cryptographic libraries across eight architectures and over twenty devices. Practical recovery on high-level applications is demonstrated against SPI bootloaders, Ethernet applications, CTAP2 over USB, and 802.15.4. wireless protocols. In addition, a new open-source tool called FlashWhisperer is introduced to assist with evaluation of microcontrollers, cryptographic libraries, and applications. Countermeasures already exist in the form of bitsliced implementations, and this work also discusses other countermeasures that existing libraries offer.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2673) | 2026-10-29
