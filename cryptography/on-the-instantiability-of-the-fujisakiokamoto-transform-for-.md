---
title: "On the Instantiability of the Fujisaki–Okamoto Transform for Trapdoor Functions"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2365"
summary: "The Fujisaki--Okamoto (FO) transform (Journal of Cryptology, 2013) is the standard route from weakly secure public-key encryption to chosen-ciphertext security, and it underlies many practical post-qu"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

The Fujisaki--Okamoto (FO) transform (Journal of Cryptology, 2013) is the standard route from weakly secure public-key encryption to chosen-ciphertext security, and it underlies many practical post-quantum key-encapsulation schemes, including ML-KEM. Security proofs for FO are set in the (quantum) random oracle models. FO uses two hash functions: the derandomization hash~H, which turns the base scheme into a deterministic trapdoor function (TDF) by Encrypt-with-Hash, and the key-derivation hash~G. We ask whether it is possible to instantiate the hash functions in the FO transform while retaining its security guarantees. While prior work mainly focused on the H step, our focus is the G step, and we take an underlying injective TDF as given. We first show that the message-only implicit-rejection variant smash{UmIR}, a key-encapsulation mechanism formulation of FO that follows ML-KEM's choices of rejection and key derivation, is uninstantiable in general. Namely, assuming standard LWE and subexponentially secure indistinguishability obfuscation and puncturable PRFs, for every efficient hash function family~G with superlogarithmic output length there is a one-way, perfectly correct injective trapdoor function for which the resulting KEM is not IND-CCA2 secure. We next give sufficient conditions on~G to instantiate the TDF-based hybrid-encryption formulation of FO, rather than the KEM version. To this end, we introduce distributional injective extractability (DINJEXT{}), a new hash function property defined relative to a partially injective ``wrapping function.'' Under this assumption relative to the FO-derived wrapping function, combined with an achievable form of universal computational extractor security (Bellare, Hoang, and Keelveedhi, CRYPTO 2013) on G and suitable assumptions on the base schemes, we obtain standard-model IND-CCA2 security. As evidence that DINJEXT{} is achievable, we show that a random oracle satisfies it for every partially injective wrapping function, and that a quantum random oracle satisfies a formulation of it for the FO wrapping function, in both cases even relative to an oblivious sampling oracle. We leave a standard-model construction open.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2365) | 2026-10-05
