---
title: "Post-Quantum Cryptography from Quantum Stabilizer Decoding"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.19110"
summary: "arXiv:2603.19110v2 Announce Type: replace Abstract: Post-quantum cryptography currently rests on a small number of hardness assumptions, posing significant risks should any one of them be compromised."
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2603.19110v2 Announce Type: replace Abstract: Post-quantum cryptography currently rests on a small number of hardness assumptions, posing significant risks should any one of them be compromised. This vulnerability motivates the search for new and cryptographically versatile assumptions that make a convincing case for quantum hardness. In this work, we argue that decoding random quantum stabilizer codes---a quantum analog of the well-studied LPN problem---is an excellent candidate. This task occupies a unique middle ground: it is inherently native to quantum computation, yet admits an equivalent formulation with purely classical input and output, as recently shown by Khesin et al. (STOC '26). We prove that the average-case hardness of quantum stabilizer decoding implies the core primitives of classical Cryptomania, including public-key encryption (PKE) and oblivious transfer (OT), as well as one-way functions. Our constructions are moreover practically efficient: our PKE scheme achieves essentially the same efficiency as state-of-the-art LPN-based PKE. We also provide substantial evidence that stabilizer decoding does not reduce to LPN, suggesting that the former problem constitutes a genuinely new post-quantum assumption. Our primary technical contributions are twofold. First, we give a reduction from random quantum stabilizer decoding to an average-case problem closely resembling LPN, but which is equipped with additional symplectic algebraic structure. While this structure is essential to the quantum nature of the problem, it raises significant barriers to cryptographic security reductions. Second, we develop a new suite of scrambling techniques for such structured linear spaces, and use them to produce rigorous security proofs for all of our constructions.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.19110) | 2026-10-08
