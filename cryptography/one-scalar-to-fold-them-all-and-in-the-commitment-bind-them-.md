---
title: "One Scalar to Fold Them All, and in the Commitment Bind Them: Reduced Logarithmic ElGamal Shuffle Proofs"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2052"
summary: "Xue, Lu, and Au design a logarithmic-size verifiable shuffle for rerandomized ElGamal ciphertexts by combining a KZG permutation argument with a tagged inner-product argument, with cost (2log N+11) G_"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Xue, Lu, and Au design a logarithmic-size verifiable shuffle for rerandomized ElGamal ciphertexts by combining a KZG permutation argument with a tagged inner-product argument, with cost (2log N+11) G_1 + 8 F. We reduce the communication and computation of their construction by observing that the rerandomization vector oldsymbol{rho} in F^N, despite being utilized as a full witness vector, only enters the consistency equations through the scalar rho^* =langleoldsymbol{a}, oldsymbol{rho} rangle. We bind this scalar into an existing KZG commitment and replace XLA's two-vector consistency argument with a one-sided folding proof, while preserving the original relation, polynomial degrees, and powers-of-au setup. We show that the the naive scalarization is unsound. Applied correctly, the committed scalar indeed permits extraction of the full rerandomization vector. We present two variants: Variant A has proof size (2log_2 N+8) G_1 + 5 F, while Variant B adds one group element but removes one interactive round. Under XLA's grouped base-scalar-pair accounting, the prover's exponentiation count decreases from approximately 18N to 13N (or 14N, for Variant B), and the verifier's drops from approximately 7N to 6N. Each proof is a constant 240 B smaller than XLA's; in a 4-server mix-net election protocol with N = 2^{10} ballots, our Variant A mixing proof costs 5.88 KiB in total, about 14% smaller than XLA.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2052) | 2026-09-15
