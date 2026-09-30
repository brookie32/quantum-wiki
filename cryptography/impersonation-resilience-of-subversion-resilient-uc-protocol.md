---
title: "Impersonation Resilience of Subversion-Resilient UC Protocols"
date: "2026-09-29"
updated: "2026-09-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2267"
summary: "Subversion attacks where the attacker aims to replace parts of a cryptographic system by manipulated parts in an undetectable manner have been shown to model both theoretical and practical attacks suc"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

Subversion attacks where the attacker aims to replace parts of a cryptographic system by manipulated parts in an undetectable manner have been shown to model both theoretical and practical attacks such as supply chain attacks. Originally proposed by Young and Yung (CRYPTO 1996), interest in them has increased dramatically after the revelations about the inner workings of intelligence agencies due to Snowden and the following paper by Bellare, Paterson, and Rogaway (CRYPTO 2014). One of the most promising countermeasures against such attacks are cryptographic reverse firewalls, proposed by Mironov and Stephens-Davidowitz (EUROCRYPT 2015), which are small devices used by the parties with the aim to rerandomize the protocol message to remove possible leakage. A wide range of protocols and corresponding firewalls have been developed based on this notion. The usage of such firewalls, however, also introduces another attack surface as an attacker might also corrupt these firewalls. In most works, this problem is either not addressed or treated as if in this case, the complete party using the firewall is compromised. However, as firewalls typically only perform rerandomization without knowledge of secret key material, this is a very coarse over-approximation, as an honest party Alice is now treated as maliciously corrupted. Instead, the main security problem comes from the fact that the firewall can impersonate Alice. In this paper, we introduce the notion of impersonation resilience, which allows us to develop protocols that are also secure against such a corrupted firewall and thus result in an honest complete party. We show a generic compiler that transforms subversion-resilient protocols for commitment or coin toss into protocols that are also impersonation resilient. Following a recent research line, our protocols and security analysis are built on the Universal Composability (UC) framework of Canetti. Of independent interest, we show that existing UC subversion models are either too strong and do not allow secure string commitments, or too weak and allow trivially secure protocols. We addressed this by developing a new, intermediate UC subversion model.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2267) | 2026-09-29
