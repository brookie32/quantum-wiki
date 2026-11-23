---
title: "Differential Collision Resistance of Feed-Forward Sponge Variants"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2998"
summary: "Feed-forward sponge variants have recently been proposed in independent lines of work to overcome the capacity bound limitation of the sponge construction and to strengthen provable (second-)preimage "
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Feed-forward sponge variants have recently been proposed in independent lines of work to overcome the capacity bound limitation of the sponge construction and to strengthen provable (second-)preimage security. Representative examples include Sponge-DM, Sponge-DM^{c}, Sponge-EDM^{c}, and Sponge-F^{P,pd}. While these designs improve generic security guarantees, their behavior under dedicated cryptanalysis remains largely unexplored. Focusing on differential collision attacks, we review the inner and outer collision frameworks for sponge hashes and analyze how the feed-forward operation, the rate-capacity ratio, and the squeezing phase affect collision cryptanalysis. Our analysis shows that feed-forward sponge variants do not necessarily offer stronger collision resistance than the standard sponge, and that the modified collision conditions and the enlarged rate can even facilitate attacks. We substantiate this analysis on feed-forward sponge instantiations with Keccak-p that are configured to match the generic collision security levels of SHA3-224, SHA3-256, SHA3-384, and SHA3-512. For these instantiations, we develop classical and quantum collision attacks. Compared with the best known attacks on the corresponding SHA-3 instances, our attacks reach more rounds or lower complexity in several cases. These results demonstrate that, for the reduced-round instantiations considered in this work, the structural changes introduced by feed-forward sponges do not carry over to collision resistance against dedicated classical and quantum attacks. They also indicate that strong collision resistance still relies on a careful choice of the feed-forward sponge configuration and on the differential propagation of the underlying permutation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2998) | 2026-11-23
