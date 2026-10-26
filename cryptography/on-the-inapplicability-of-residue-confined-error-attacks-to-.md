---
title: "On the Inapplicability of Residue-Confined Error Attacks to CRT-FHE with Non-Degenerate Error Distributions"
date: "2026-10-24"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2633"
summary: "This paper responds to the cryptanalysis presented in “Key Recovery from Residue- Confined Errors in the Pradhan CRT-RLWE Construction” (Olejnik and Naskrecki, 2026), which claims key recovery and pla"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

This paper responds to the cryptanalysis presented in “Key Recovery from Residue- Confined Errors in the Pradhan CRT-RLWE Construction” (Olejnik and Naskrecki, 2026), which claims key recovery and plaintext recovery against the CRT-FHE scheme introduced in “A New CRT-based Fully Homomorphic Encryption” (Pradhan et al., 2026). We demonstrate that the reported recovery attacks rely entirely on a deliberately con- structed error distribution whose support lies in the kernel of the CRT encoding function. Consequently, the effective encryption error is identically zero, reducing the attacked con- struction to a noiseless RLWE instance. The subsequent key-recovery and plaintext-recovery results therefore follow from the deliberate elimination of the encryption noise, rather than from any cryptanalytic method capable of recovering secrets from properly noise-bearing CRT-FHE ciphertexts. Crucially, the proposed attack neither removes nor estimates errors from normally generated CRT-FHE ciphertexts. Instead, it assumes an artificial error distribution specifically chosen to guarantee their annihilation during encoding. This condition does not hold for the intended centered-binomial error distribution, under which the probability that an entire error polynomial belongs to the encoder’s kernel is negligible at the reported parameters. Thus, the presented recovery procedures do not constitute attacks against the concrete CRT-FHE instantiation with its intended non-degenerate error distribution. We conclude that the reported key-recovery and plaintext-recovery results concern a deliberately degenerate, effectively zero-error instantiation and do not demonstrate a practical security compromise of CRT-FHE under its intended error sampling.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2633) | 2026-10-24
