---
title: "Enabling Memory Encryption Using Ascon Derivatives"
date: "2026-11-09"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2842"
summary: "Keeping data stored in memory confidential is a tough challenge when assuming an adversary with physical access to it. First, we have fine-grained access to typically 256 to 512 bits at once, so nonce"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

Keeping data stored in memory confidential is a tough challenge when assuming an adversary with physical access to it. First, we have fine-grained access to typically 256 to 512 bits at once, so nonces or tags of the typical sizes used for authenticated encryption would lead to a sizeable overhead. Second, we have stringent performance requirements, including low latency that directly impacts CPU performance and, more generally, strict area and energy constraints, especially for the high bandwidth of memory interfaces. Currently, memory encryption solutions typically rely on the AES block cipher. In this paper, we explore ways of using Ascon as a building block for memory encryption. Our analysis shows that Ascon-based constructions achieve better performance than AES-based HCTR2 and can also compete with XTS-AES while providing larger block sizes.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2842) | 2026-11-09
