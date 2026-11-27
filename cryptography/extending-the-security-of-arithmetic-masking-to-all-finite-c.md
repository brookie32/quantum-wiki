---
title: "Extending the Security of Arithmetic Masking to All Finite Cyclic Groups via Fourier Analysis"
date: "2026-11-27"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3073"
summary: "Let Ngeq 2 and let G=Z/NZ. A secret sin G is shared by choosing a tuple (X_1,ldots,X_k) uniformly subject to X_1+dots+X_k=s in G. Represent each share by the unique integer in {0,ldots,N-1} in its res"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Let Ngeq 2 and let G=Z/NZ. A secret sin G is shared by choosing a tuple (X_1,ldots,X_k) uniformly subject to X_1+dots+X_k=s in G. Represent each share by the unique integer in {0,ldots,N-1} in its residue class. Let D_s denote the joint distribution of the Hamming weights of the k shares, and let D_U denote the corresponding distribution when the secret is uniform on G. The problem is to bound the total variation distance between these distributions uniformly in s. Biswas et al. established an upper bound for this distance when the modulus is close to a power of two. In this paper we prove that for every integer Ngeq 2 and every fixed kgeq 3, putting n=lceillog_2 Nrceil, we have $max_{sin G}operatorname{TV}(D_s,D_U)=O_kigl(n^{-k/2+5/4}igr). We obtain this bound using Fourier analysis on the Boolean cube and a decomposition of {0,ldots,N-1}$ into intervals whose lengths are powers of two. This removes the restriction on the modulus without weakening the exponent in the general bound of Biswas et al.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3073) | 2026-11-27
