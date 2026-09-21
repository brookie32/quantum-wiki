---
title: "Transcript-Bound Combiners for Downgrade-Resilient Hybrid Post-Quantum Key Establishment: Definition, Proof, and Embedded-Device Cost"
date: "2026-09-21"
updated: "2026-09-21"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.21273"
summary: "arXiv:2609.21273v1 Announce Type: cross Abstract: Hybrid key establishment runs a post-quantum key-encapsulation mechanism (KEM) alongside a classical Diffie-Hellman primitive, so that the session key"
last_verified: "2026-09-21"
review_by: "2026-12-20"
stale: false
---

arXiv:2609.21273v1 Announce Type: cross Abstract: Hybrid key establishment runs a post-quantum key-encapsulation mechanism (KEM) alongside a classical Diffie-Hellman primitive, so that the session key stays secure while either component resists attack. This design is now standardized in the Transport Layer Security protocol, Secure Shell, and the Internet Key Exchange, with the standardized module-lattice KEM (ML-KEM) as the post-quantum component. A hybrid KEM secures the derived key, but not the integrity of the negotiation that selects which primitives are used. Full protocols authenticate that negotiation through a handshake transcript; a hybrid KEM deployed as a standalone drop-in primitive, or inside a minimal handshake without transcript authentication, inherits no such guarantee, and an active attacker can strip the post-quantum option. We ask what the key schedule alone must contain to make downgrade resilience a local property of the combiner. We give a game-based definition at the combiner layer and prove a two-sided separation: a combiner that ignores the transcript is downgraded with certainty, whereas one that binds the session key and the confirmation tag to a hash of the transcript blocks every such attempt, up to a term negligible for a 256-bit transcript hash. We also give an explicit strongest-link security bound. Using a calibrated cost model composed from published Cortex-M4 measurements, transcript binding adds one hash per party - about 11.8% of handshake computation but only 1.5% of radio-inclusive energy - and adds no messages or bytes on the wire. Every reported number is produced by a released harness that passes a 30-check validation gate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.21273) | 2026-09-21
