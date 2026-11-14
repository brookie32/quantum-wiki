---
title: "Toward Eﬃcient Post-Quantum Bitcoin Bridges"
date: "2026-11-12"
updated: "2026-11-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2877"
summary: "BitVM-style protocols verify succinct proofs on Bitcoin by garbling a proof veriﬁer oﬀ-chain. What reaches the chain in a dispute is the proof itself: its bits under one-time keys, the scripts that au"
last_verified: "2026-11-14"
review_by: "2027-02-12"
stale: false
---

BitVM-style protocols verify succinct proofs on Bitcoin by garbling a proof veriﬁer oﬀ-chain. What reaches the chain in a dispute is the proof itself: its bits under one-time keys, the scripts that authenticate them and the signatures that bind them to transactions. Existing designs garble elliptic-curve SNARK veriﬁers, which a quantum adversary breaks. Our goal is a post-quantum alternative: a hash-based STARK veriﬁer, garbled and fed with hash-based one-time keys, with no number-theoretic assumption anywhere in the veriﬁer; its price is a far larger proof, and this paper measures and reduces that on-chain data. We compile the complete veriﬁer for WHIR-based STARK proofs from Ziren into a Boolean circuit using free-XOR gadgets for binary-tower arithmetic and Blake3. Our implementation uses Ziren’s binary-ﬁeld proof stage and narrow recursion. For the ﬁnal recursive WHIR-proof veriﬁer, our circuit-cost analysis gives 218.0M non-free gates and 564,552 input bits, corresponding to 3.49 GB of garbled tables. The transactions publishing that input with translated Winternitz keys have a total virtual size of 4.26 million virtual bytes (MvB) for one key set.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2877) | 2026-11-12
