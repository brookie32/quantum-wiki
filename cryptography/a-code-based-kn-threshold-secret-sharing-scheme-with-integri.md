---
title: "A Code-Based (k,n)-Threshold Secret Sharing Scheme with Integrity Verification"
date: "2026-09-01"
updated: "2026-09-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1850"
summary: "Threshold secret sharing schemes (TSSS) enable a dealer to distribute a secret among multiple participants such that only authorized subsets can reconstruct the secret while unauthorized subsets obtai"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

Threshold secret sharing schemes (TSSS) enable a dealer to distribute a secret among multiple participants such that only authorized subsets can reconstruct the secret while unauthorized subsets obtain no information. Existing secret sharing schemes (SSS) are often constrained by limited secret size, non-threshold access structures, or the absence of mechanisms for verifying the authenticity of shares and the integrity of the reconstructed secret. In this paper, we propose a novel (k,n)-threshold secret sharing scheme based on linear Maximum Distance Separable (MDS) codes. The proposed construction supports the sharing of comparatively larger secrets by representing the secret as a matrix over a finite field and exploits the linearity of MDS codes to achieve efficient share generation and reconstruction. To strengthen reliability, the scheme incorporates cryptographic hash functions for share authentication and integrity verification of the reconstructed secret. We prove that the proposed scheme satisfies correctness and perfect secrecy, thereby providing unconditional security against unauthorized coalitions. Experimental evaluation demonstrates that the proposed construction achieves efficient share generation and reconstruction while outperforming existing code-based secret sharing schemes in terms of supported secret size, scalability, and practical runtime.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1850) | 2026-09-01
