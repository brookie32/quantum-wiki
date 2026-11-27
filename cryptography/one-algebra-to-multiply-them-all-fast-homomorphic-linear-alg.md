---
title: "One Algebra to Multiply Them All: Fast Homomorphic Linear Algebra in Every Encoding"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3066"
summary: "Linear algebra is a core primitive of many applications of fully homomorphic encryption, including privacy-preserving machine learning, statistical analysis, and encrypted search. Efficient homomorphi"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Linear algebra is a core primitive of many applications of fully homomorphic encryption, including privacy-preserving machine learning, statistical analysis, and encrypted search. Efficient homomorphic matrix-vector and matrix-matrix multiplications are therefore an essential tool, and have been intensely studied over the last fifteen years. Recent work, notably by Bae et al. and Park reduces homomorphic matrix multiplication in large dimension to the multiplication of plaintext matrices, plus a number of key switchings only linear in the dimension, enabling the use of highly efficient linear algebra primitives, such as those of the BLAS library, while limiting the homomorphic cost. These results have been extended by Cheon et al. to batches of matrix multiplications in smaller dimension. In CKKS, the corresponding algorithms rely on dedicated encodings (coefficient, SinC). Using these encodings constrains integration of these algorithms into a larger computation; in practice, one has either to perform an expensive conversion or to schedule the linear algebra within bootstrapping. Alternatively, Gentry and Lee obtain reductions in the slot encoding through a different ciphertext ring. We obtain reductions to plaintext matrix multiplication directly in the slot encoding, over the standard power-of-two CKKS ring, showing that the change of ring of Gentry and Lee is not required for this functionality. Our approach uses the cyclic algebra of the field extension mathbb Q(zeta_{2N})/mathbb Q(i) to describe endomorphisms independently of the choice of coordinates. We show that choosing a basis (which identifies endomorphisms with matrices) is exactly choosing an encoding. Algorithms written once in this language cover the functionalities of the classical encodings, for single matrices and, over subfields, for batches of smaller ones. This language also makes explicit the commutation of the secret key with the matrix, which is the key step in the product of two encrypted matrices. The resulting algorithms admit elementary descriptions, corresponding to a precise scheduling of the key switchings, which allows them to be grouped, while the algebraic framework explains their common structure across various packings. Our framework extends to products of an encrypted d imes d matrix by an encrypted d imes c matrix, where it allows a baby-step giant-step strategy even though both factors are encrypted. For ring degree N, with c mid d mid N/2, we evaluate a batch of N/(2d) such products with O(sqrt{dc}) key switchings in total, without any preprocessing of the encrypted inputs. In particular, an encrypted matrix-vector product requires only O(sqrt{d}) key switchings.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3066) | 2026-11-26
