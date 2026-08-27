---
title: "HRFPRE: Fast Proxy Re-encryption for Multi-RSU Outsourcing and Hardware-assisted Revocation in the IoV."
date: "2026-08-24"
updated: "2026-08-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1789"
summary: "In the Internet of Vehicles (IoV), content-centric data sharing is essential for driving safety and user experience. However, the highly dynamic and distributed IoV network raises challenges such as u"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

In the Internet of Vehicles (IoV), content-centric data sharing is essential for driving safety and user experience. However, the highly dynamic and distributed IoV network raises challenges such as unauthorized data access and inefficient information dissemination. Although existing proxy re-encryption (PRE) schemes with revocation partially mitigate these concerns, they still have key shortcomings: (i) computational costs that grow linearly with the number of attributes; (ii) heavy cloud-side overhead from re-encryption and outsourced decryption, causing delays or decryption failures; and (iii) revocation mechanisms that are inefficient or insufficiently responsive in handling malicious users. Recent studies have addressed these issues, but many schemes still struggle to ensure reliable message recovery in dynamic IoV scenarios. To overcome these limitations, we propose HRFPRE, an efficient proxy re-encryption mechanism based on multi-RSU outsourcing and hardware-assisted revocation. Our scheme provides constant-size public parameters and lightweight user-side decryption over asymmetric pairing-friendly groups, while supporting an unbounded attribute space. Re-encryption requires only four pairing operations and supports a novel "encrypt-then-offline hosting" model for vehicles. Simultaneously, Roadside Units (RSUs) provide outsourced re-encryption, key generation assistance, and decryption services to resource-constrained onboard units, effectively shifting computational load away from the cloud. By integrating a key-decoupled Trusted Execution Environment (TEE), HRFPRE enables immediate revocation and keeps plaintext recovery dependent on the user-held key even under TEE-side side-channel leakage. Under the Decisional Linear (DLIN) assumption, HRFPRE achieves adaptive security while resisting replay and collusion attacks. Theoretical analysis and experiments show that HRFPRE reduces computational and communication overhead, making it suitable for secure data exchange in dynamic IoV environments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1789) | 2026-08-24
